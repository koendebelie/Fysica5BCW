# -*- coding: utf-8 -*-
"""PDF-leesversie vanuit dezelfde gegenereerde DOCX (zonder LibreOffice).

Mammoth zet de bewerkbare Word-inhoud om in HTML; xhtml2pdf zet die om in PDF.
Rubric (Bijlage C) wordt apart op liggende A4-pagina's gezet en daarna ingevoegd.
De Word-bestanden behouden echte OMML-formules; voor de PDF plaatsen we dezelfde
formules als tekst op dezelfde plaats omdat Mammoth OfficeMath niet omzet.
"""
import argparse
import io
import re
import html
import os
import base64
import hashlib
import tempfile
from pathlib import Path

import mammoth
from xhtml2pdf import pisa
from xhtml2pdf.xhtml2pdf_reportlab import PmlImageReader
import pymupdf

# xhtml2pdf 0.2.23 geeft PmlImageReader-objecten een naam via het huidige
# BytesIO-leespunt en id(self). Na een eerste decode staat de stream op EOF;
# object-id's kunnen vervolgens worden hergebruikt. ReportLab verwart dan
# verschillende afbeeldingen en herhaalt de eerste figuur op alle pagina's.
# Een op pixelinhoud gebaseerde sleutel houdt ieder bronbeeld bij zijn bijschrift.
def _stable_image_name(self):
    return 'PmlImageObject_' + hashlib.sha256(self.getRGBData()).hexdigest()
PmlImageReader.__str__ = _stable_image_name

from course_guidance import FORMULA_DISPLAY

ROOT=Path(__file__).resolve().parent.parent

CSS = '''
@font-face {font-family: Dejavu; src: url("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf");}
@font-face {font-family: Dejavu; src: url("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"); font-weight:bold;}
@page {size: a4; margin: 1.8cm 2cm;}
body {font-family: Dejavu, sans-serif; font-size: 9.6pt; color:#222; line-height: 1.18;}
h1 {font-size:17pt; color:#1F4E79; margin: 12pt 0 6pt 0; page-break-before: always;}
h2 {font-size:13pt; color:#1F4E79; margin: 10pt 0 4pt 0;}
h3 {font-size:11pt; color:#2E7D32; margin: 8pt 0 3pt 0;}
p {margin: 2.2pt 0 4pt 0;}
ul, ol {margin:3pt 0 5pt 0;padding-left:15pt;}
li {margin:1.5pt 0;}
table {border: .45pt solid #999; border-collapse:collapse; width:100%; margin:3pt 0 7pt 0; font-size:8.4pt;}
td, th {border:.45pt solid #999; padding:3pt 4pt; vertical-align:top;}
th {background:#D9E2F3; font-weight:bold;}
table.box tr:first-child td {background:inherit;font-weight:normal;}
table.box td {border:.5pt solid #9DB6CF;}
table.doel td {background:#E8F5E9;}
table.lp td {background:#FFF8E1;}
table.voor td {background:#F3E5F5;}
table.veilig td {background:#FDECEA;}
table.stem td {background:#E0F2F1;}
table.uitleg td {background:#E8F1FA;}
table.eval td {background:#EEEEEE;}
table.box.lkr tr:first-child td,table.box.antw tr:first-child td {background:#FFF3F3;color:#B71C1C;}
table.fill {border:1pt solid #888;height:1.2cm;}
table.fill td {height:1.2cm;}
table.fill tr:first-child td {background:white;}
table.individual td {height:1.2cm;}
p.formula {font-size:11pt;text-align:center;color:#1F4E79;margin:7pt 0;}
img {max-width:12cm;max-height:7cm;display:block;margin:4pt auto;}
a {color:#1F4E79;}
'''


def _html(docx):
    with open(docx,'rb') as f:
        raw=mammoth.convert_to_html(f).value
    # Vakken/kleurkaders herkennen op hun unieke titel; lege invulvakken apart stylen.
    def mark(m):
        table=m.group(0)
        txt=re.sub(r'<[^>]+>','',table)
        first=txt[:135]
        cls=''
        if not txt.strip(): cls='fill'
        elif 'Mijn uitleg / verwijzing naar mijn gegevens' in first: cls='individual'
        elif any(x in first.lower() for x in ('modelantwoord','didactische aanwijzing',
                 'verwachte interpretatie','voorbeeldvraag en variabelen')):
            cls='box antw'
        else:
            for prefix,label in [('LESDOELEN','doel'),('LEERPLANDOELEN','lp'),('VOORKENNIS','voor'),
                                 ('VEILIGHEID //','veilig'),('VEILIGHEID –','veilig'),('STEM-ONTWERPOPDRACHT','stem'),('OPEN ONDERZOEK','stem'),
                                 ('UITLEG –','uitleg'),('BEGRIPPEN EN MODEL','uitleg'),('TIJDTIKKER →','uitleg'),('EVALUATIE EN INDIENEN','eval'),('MINICHECK','eval'),('WAT, HOE EN WANNEER','eval'),
                                 ('LEERKRACHTENINFO','lkr')]:
                if first.startswith(prefix): cls='box '+label;break
        if cls=='fill':
            # Lege Word-invulvakken hebben geen inhoud: xhtml2pdf laat de breedte
            # zonder expliciet HTML-attribuut instorten tot een smalle verticale strook.
            return table.replace('<table>','<table class="fill" width="100%">',1).replace('<td>','<td width="100%">&#160;',1)
        return table.replace('<table>','<table class="'+cls+'">',1) if cls else table
    raw=re.sub(r'<table>.*?</table>',mark,raw,flags=re.S)
    # De DOCX bevat OfficeMath, dat Mammoth overslaat. Plaats de correcte
    # tekstweergave NA het conceptenkader van het juiste zelfstandige werkblad;
    # de oude themanummers zouden hier inhoudelijk fout zijn.
    parts=re.split(r'(<h1>LABO \d+ – .*?</h1>)',raw)
    for i in range(1,len(parts)-1,2):
        n=int(re.search(r'LABO (\d+)',parts[i]).group(1))
        if n not in FORMULA_DISPLAY:continue
        match=re.search(r'<table[^>]*>.*?BEGRIPPEN EN MODEL.*?</table>',parts[i+1],flags=re.S)
        if not match:raise ValueError(f'Begrippenkader ontbreekt bij labo {n}')
        formula='<p class="formula">'+html.escape(FORMULA_DISPLAY[n])+'</p>'
        parts[i+1]=parts[i+1][:match.end()]+formula+parts[i+1][match.end():]
    raw=''.join(parts)
    # Mammoth negeert de Word-paginabreuk vlak voor de individuele 4 S-check;
    # zonder PDF-overgang valt de vraag op de vorige bladzijde en de invultabel erna.
    raw=raw.replace('<h3>INDIVIDUEEL DOELBEWIJS – STEM 4 S</h3>',
                    '<div style="page-break-before:always"></div><h3>INDIVIDUEEL DOELBEWIJS – STEM 4 S</h3>')
    # Bij de golfbak is de applet-tabel breed/lang: xhtml2pdf plaatste eerder
    # alleen de kop op de vorige pagina en alle 10 rijen pas op de volgende.
    # Een bewuste pagina-overgang houdt kop en data samen in de PDF-leesversie.
    bits=re.split(r'(<h1>LABO 18 – .*?</h1>)',raw)
    if len(bits)==3:
        bits[2]=bits[2].replace('<h3>Metingen</h3>', '<div style="page-break-before:always"></div><h3>Metingen</h3>',1)
        raw=''.join(bits)
    def expand_blank_row(m):
        tr=m.group(0)
        cells=re.findall(r'<td[^>]*>(.*?)</td>',tr,flags=re.S)
        if len(cells)>1 and all(not re.sub(r'<[^>]+>','',c).strip() for c in cells[1:]):
            return tr.replace('<td>','<td height="21">',1)
        return tr
    raw=re.sub(r'<tr>.*?</tr>',expand_blank_row,raw,flags=re.S)
    # Behoud het invullabel bij het lege vak wanneer een pagina-einde nadert.
    raw=re.sub(r'<p>((?:(?!</p>).)*?)</p>(?=<table class="fill")',
               lambda m:'<p style="page-break-after:avoid">'+m.group(1)+'</p>',raw,flags=re.S)
    return raw


def _image_files(raw, tempdir):
    """Geef elke Mammoth-data-URI een unieke lokale bestandsnaam.

    xhtml2pdf cachet anders alle base64-afbeeldingen onder dezelfde sleutel:
    in de PDF werd de eerste figuur ten onrechte bij ALLE bijschriften herhaald.
    """
    def replace(match):
        mime,data=match.group(1),match.group(2)
        blob=base64.b64decode(data)
        ext='.jpg' if mime in ('jpeg','jpg') else '.png'
        name=hashlib.sha256(blob).hexdigest()[:24]+ext
        target=tempdir/name
        if not target.exists():target.write_bytes(blob)
        return '<img src="'+str(target)+'"'
    return re.sub(r'<img src="data:image/([^;]+);base64,([^"]+)"',replace,raw)


def _make(htmlpart,landscape=False):
    css=CSS.replace('@page {size: a4;','@page {size: a4 landscape;') if landscape else CSS
    css=css.replace('/usr/share/fonts/truetype/dejavu/',str(Path(__file__).resolve().parent/'fonts')+'/')
    if landscape:
        css=css.replace('font-size:8.4pt','font-size:6.5pt').replace('padding:3pt 4pt','padding:2pt 2pt')
    # Enkel wanneer het PDF-DEEL met h1 begint, onderdrukken we een lege
    # voorafgaande pagina. Bij de titelpagina moet 'Inhoud' wél nieuw starten.
    if re.match(r'^\s*<h1>',htmlpart):
        htmlpart=re.sub(r'<h1>', '<h1 style="page-break-before:auto">',htmlpart,count=1)
    doc='<!doctype html><html><head><meta charset="utf-8"><style>'+css+'</style></head><body>'+htmlpart+'</body></html>'
    output=io.BytesIO()
    result=pisa.CreatePDF(io.BytesIO(doc.encode('utf-8')),dest=output,encoding='utf-8',
                          link_callback=lambda src,*args: src)
    if result.err:
        raise RuntimeError(f'HTML→PDF-fouten: {result.err}')
    output.seek(0)
    return pymupdf.open(stream=output.read(),filetype='pdf')


def render(docx,pdf):
    with tempfile.TemporaryDirectory(prefix='.pdf_fig_',dir=ROOT/'work') as tmp:
        raw=_image_files(_html(docx),Path(tmp))
        marker_c='<h1>Bijlage C – Proces- en attituderubric (40 %)</h1>'
        marker_d='<h1>Bijlage D – Zelfreflectie- en peer-evaluatiefiche</h1>'
        if marker_c in raw and marker_d in raw:
            part1,tail=raw.split(marker_c,1)
            mid,part3=tail.split(marker_d,1)
            docs=[_make(part1),_make(marker_c+mid,True),_make(marker_d+part3)]
        else: docs=[_make(raw)]
    out=pymupdf.open()
    for d in docs: out.insert_pdf(d)
    for i,page in enumerate(out,1):
        footer=f'Labocursus Fysica 6BCW – mechanica, trillingen en golven – pagina {i}'
        page.insert_text((page.rect.width/2-185,page.rect.height-28),footer,fontsize=7.5,fontname='helv',color=(.35,.35,.35))
    out.set_metadata({'title':'Labocursus toegepaste fysica 6BCW','author':'De Belie K. — HAST'})
    out.save(pdf,garbage=3,deflate=True)
    print(pdf,'pagina’s:',len(out))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('docx');ap.add_argument('--output')
    args=ap.parse_args()
    render(args.docx,args.output or str(Path(args.docx).with_suffix('.pdf')))
