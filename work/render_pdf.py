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
from pathlib import Path

import mammoth
from xhtml2pdf import pisa
import pymupdf

from labs import LABOS

ROOT=Path(__file__).resolve().parent.parent
FORMULAS={
 1:'v = Δx/Δt     [v] = m/s',
 2:'a = Δv/Δt     [a] = m/s²',
 3:'y(t) = y₀ + v₀t − ½gt²     [g] = m/s²',
 4:'x = v₀t ; y = ½gt²     [x] = [y] = m',
 5:'Fᵣ = mₜₒₜ·a     [Fᵣ] = N',
 6:'W = F·s ; ΔE_z = mgh     [W] = J',
 7:'M = F·d     [M] = N·m',
 8:'F_cp = m·v²/r = m·ω²r     [F_cp] = N',
 9:'T = 2π√(m/k) ; k = F/Δy     [k] = N/m',
 10:'T = 2π√(l/g)     [T] = s',
 11:'A = (B−O)/2 ; f = N/t     [A] = cm ; [f] = Hz',
 12:'v = λf ; L = nλ/2     [v] = m/s',
 13:'f = 1/T     [f] = Hz',
 14:'a·sin θ = nλ ; θ = arctan(y/l)',
 15:'n = sin α/sin β',
 16:'x̄ = (x₁+x₂+x₃)/3',
}

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
tr:first-child td {background:#D9E2F3; font-weight:bold;}
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
p.formula {font-size:11pt;text-align:center;color:#1F4E79;margin:7pt 0;}
img {max-width:12cm;max-height:7cm;display:block;margin:4pt auto;}
a {color:#1F4E79;}
'''


def _html(docx):
    with open(docx,'rb') as f:
        raw=mammoth.convert_to_html(f).value
    # formele OMML ontbreekt in de HTML, maar is wel aanwezig in Word: toon dezelfde symbolische formule.
    parts=re.split(r'(<h1>LABO \d+ – .*?</h1>)',raw)
    for i in range(1,len(parts)-1,2):
        m=re.search(r'LABO (\d+)',parts[i]);
        if not m:continue
        n=int(m.group(1)); formula=FORMULAS.get(n,'')
        if formula:
            parts[i+1]=parts[i+1].replace('<h3>Hypothese</h3>',
                '<p class="formula">'+html.escape(formula)+'</p><h3>Hypothese</h3>',1)
    raw=''.join(parts)
    # Vakken/kleurkaders herkennen op hun unieke titel; lege invulvakken apart stylen.
    def mark(m):
        table=m.group(0)
        txt=re.sub(r'<[^>]+>','',table)
        first=txt[:135]
        cls=''
        if not txt.strip(): cls='fill'
        elif any(x in first.lower() for x in ('modelantwoord','didactische aanwijzing',
                 'verwachte interpretatie','voorbeeldvraag en variabelen')):
            cls='box antw'
        else:
            for prefix,label in [('LESDOELEN','doel'),('LEERPLANDOELEN','lp'),('VOORKENNIS','voor'),
                                 ('VEILIGHEID //','veilig'),('STEM-ONTWERPOPDRACHT','stem'),
                                 ('UITLEG –','uitleg'),('WAT, HOE EN WANNEER','eval'),
                                 ('LEERKRACHTENINFO','lkr')]:
                if first.startswith(prefix): cls='box '+label;break
        if cls=='fill':
            # Lege Word-invulvakken hebben geen inhoud: xhtml2pdf laat de breedte
            # zonder expliciet HTML-attribuut instorten tot een smalle verticale strook.
            return table.replace('<table>','<table class="fill" width="100%">',1).replace('<td>','<td width="100%">&#160;',1)
        return table.replace('<table>','<table class="'+cls+'">',1) if cls else table
    raw=re.sub(r'<table>.*?</table>',mark,raw,flags=re.S)
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


def _make(htmlpart,landscape=False):
    css=CSS.replace('@page {size: a4;','@page {size: a4 landscape;') if landscape else CSS
    css=css.replace('/usr/share/fonts/truetype/dejavu/',str(Path(__file__).resolve().parent/'fonts')+'/')
    if landscape:
        css=css.replace('font-size:8.4pt','font-size:6.5pt').replace('padding:3pt 4pt','padding:2pt 2pt')
    # De eerste h1 van een PDF-deel krijgt geen extra pagina vóór zich.
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
    raw=_html(docx)
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
