# -*- coding: utf-8 -*-
"""Technische regressiecontrole; geen vervanging van bron-/vakinhoudelijke review."""
from pathlib import Path
from zipfile import ZipFile
import sys
from lxml import etree
from docx import Document
import pymupdf
from labs import LABOS
from answers import ANSWERS
from build import THEORY_LABS

ROOT=Path(__file__).resolve().parent.parent
W={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
   'm':'http://schemas.openxmlformats.org/officeDocument/2006/math',
   'r':'http://schemas.openxmlformats.org/package/2006/relationships'}


def check_original_protocols():
    """Regressies voor de letterlijk bedoelde tijdtikkerkolommen en eigen proefgang."""
    ticker_parts=[(1,2),(2,1),(2,2),(3,1),(9,3)]
    for labno,partno in ticker_parts:
        p=LABOS[labno-1]['delen'][partno-1]
        heads=p['kop']
        tprime=heads.index('t′ (s)')
        assert tprime == len(heads)-2 or tprime == len(heads)-3,heads
        assert 'v' in heads[tprime+1] or '⟨v⟩' in heads[tprime+1],heads
        assert all('Δv' not in h and 'Δt' not in h for h in heads),heads
        assert isinstance(p['rijen'][0],list) and p['rijen'][0][4] in ('0,010','0,020'),p['rijen'][0]
    for p in LABOS[4]['delen'][:2]:
        h=p['extra_tabellen'][0]['kop']
        assert h[h.index('t′ (s)')+1].startswith('v'),h
    assert len(LABOS[2]['delen'])==3  # val, handmatige worp, volledige Tracker-worp
    assert LABOS[1]['delen'][1]['open_opdracht'] and 'OPEN' in LABOS[1]['delen'][1]['titel']
    assert LABOS[3]['delen'][0]['open_opdracht']
    assert LABOS[0]['delen'][0]['rijen'][0][0]=='0,100' and len(LABOS[0]['delen'][0]['rijen'])==10
    assert '90°' in LABOS[0]['delen'][0]['kop'][1] and '45°' in LABOS[0]['delen'][0]['kop'][3]
    assert LABOS[5]['delen'][0]['rijen']==['30','45','60'] and 'l sin α' in LABOS[5]['onderzoek']
    assert LABOS[9]['delen'][2]['rijen']==10
    assert len(LABOS[12]['delen'])==3 and '443' in str(LABOS[12]['delen'][0]['rijen'])


def check_source_booklet(label):
    """Elke oude bronproef heeft ook een zelfstandig afdrukbaar OVUR-werkblad."""
    from source_sheets import SHEETS
    path=ROOT/f'Bronpractica_6BCW_{label}.docx'
    doc=Document(path)
    titles=[p.text for p in doc.paragraphs if p.style.name.startswith('Heading 1') and p.text.startswith('PRACTICUM ')]
    assert len(titles)==len(SHEETS)==26,titles
    assert 'EVRB met beginsnelheid' in titles[2]
    assert 'vertraagde beweging' in titles[3]
    assert 'De valbeweging' in titles[4]
    assert 'De verticale worp' in titles[5]
    assert 'horizontale worp' in titles[6]
    for table in doc.tables:
        if not table.rows:continue
        header=[c.text for c in table.rows[0].cells]
        if 't′ (s)' in header:
            pos=header.index('t′ (s)')
            assert pos+1<len(header) and ('v' in header[pos+1] or '⟨v⟩' in header[pos+1]),header
    text=' '.join(c.text for t in doc.tables for r in t.rows for c in r.cells)
    if label=='LEERLING':assert 'modelantwoord' not in text.lower()
    else:assert text.lower().count('modelantwoord')>20
    pdf=pymupdf.open(ROOT/f'Bronpractica_6BCW_{label}.pdf')
    assert len(pdf)>50
    assert len({img[0] for page in pdf for img in page.get_images()})>=20
    assert all(len(page.get_text())>100 for page in pdf)
    print('BRONWERKBLADEN',label,len(titles),'zelfstandige proeven, PDF',len(pdf),'blz.')


def check_doc(label):
    path=ROOT/f'Labocursus_6BCW_{label}.docx'
    d=Document(path)
    headings=[p.text for p in d.paragraphs if p.style.name.startswith('Heading 1')]
    assert len([s for s in headings if s.startswith('LABO ')]) == 16,headings
    assert headings.index('LABO 1 – EENPARIGE BEWEGING: LUCHTBEL EN WAGENTJE') < headings.index('LABO 16 – OPEN ONDERZOEK: EEN EIGEN VRAAG VAN BEGIN TOT POSTER')
    with ZipFile(path) as z:
        raw=z.read('word/document.xml'); x=etree.fromstring(raw)
        omml=len(x.xpath('//m:oMathPara',namespaces=W))
        pictures=len(x.xpath('//*[local-name()="drawing"]'))
        blanks=len(x.xpath('//w:tbl[w:tr/w:tc/w:p[not(.//w:t)]]',namespaces=W))
        text=' '.join(x.xpath('//w:t/text()',namespaces=W))
        rel=z.read('word/_rels/document.xml.rels').decode()
        assert 'theorie-PDF 02' in text and 'theorie-PDF 16' in text
        assert 'github.com/koendebelie/Fysica5BCW/blob/main/leerstof%206BCW' in rel
        assert omml>=16 and pictures>=16 and blanks>=80,(omml,pictures,blanks)
        assert 'LPD 6 S' in text and 'STEM-ONTWERPOPDRACHT' in text
        assert 'S – Specifiek' in text or 'S – Specifiek' in ' '.join(p.text for p in d.paragraphs)
        if label=='LEERLING':
            assert 'modelantwoord' not in text.lower()
            assert 'LEERKRACHTENINFO' not in text
            assert 'verwachte interpretatie' not in text.lower()
        else:
            assert text.lower().count('modelantwoord')>70
            assert len(x.xpath('//w:rPr/w:color[@w:val="B71C1C"]',namespaces=W))>100
    pdf=pymupdf.open(ROOT/f'Labocursus_6BCW_{label}.pdf')
    landscape=[i+1 for i,p in enumerate(pdf) if p.rect.width>p.rect.height]
    # Een pagina met grote bronfiguur of het einde van een apart bronpracticum
    # bevat soms weinig tekst; ze mag niet volledig leeg zijn.
    assert landscape and all(len(p.get_text())>100 for p in pdf)
    image_ids={pic[0] for page in pdf for pic in page.get_images()}
    # xhtml2pdf herhaalde voordien dezelfde (eerste) afbeelding onder ELK bijschrift.
    # Twee identieke slingerschema's mogen wél dezelfde PDF-image-ID delen.
    assert len(image_ids)>=20, f'{label}: slechts {len(image_ids)} verschillende PDF-beelden'
    alltext=' '.join(p.get_text() for p in pdf)
    assert 'LABO 16' in alltext and 'Bijlage F' in alltext
    assert ('modelantwoord' not in alltext.lower()) if label=='LEERLING' else ('modelantwoord' in alltext.lower())
    print(label, 'DOCX:',len(headings),'H1,',len(d.tables),'tabellen,',omml,'OMML,',pictures,'afbeeldingen,',blanks,'invul-/leegtabellen; PDF:',len(pdf),'p., liggend',landscape)

if __name__=='__main__':
    assert len(LABOS)==16 and all(l['delen'] and l['stem'] for l in LABOS)
    assert len(ANSWERS)>=170
    assert all(l['nr'] in THEORY_LABS for l in LABOS)
    check_original_protocols()
    check_doc('LEERLING');check_doc('LEERKRACHT')
    check_source_booklet('LEERLING');check_source_booklet('LEERKRACHT')
    f=pymupdf.open(ROOT/'Bestellijst_nieuw_materiaal_6BCW.pdf');assert len(f)>0
    print('OK — technische controles; geen inhoudelijke goedkeuring van alle 118 bronpagina’s')
