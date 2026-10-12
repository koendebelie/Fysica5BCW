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
    assert landscape and all(len(p.get_text())>450 for p in pdf)
    alltext=' '.join(p.get_text() for p in pdf)
    assert 'LABO 16' in alltext and 'Bijlage F' in alltext
    assert ('modelantwoord' not in alltext.lower()) if label=='LEERLING' else ('modelantwoord' in alltext.lower())
    print(label, 'DOCX:',len(headings),'H1,',len(d.tables),'tabellen,',omml,'OMML,',pictures,'afbeeldingen,',blanks,'invul-/leegtabellen; PDF:',len(pdf),'p., liggend',landscape)

if __name__=='__main__':
    assert len(LABOS)==16 and all(l['delen'] and l['stem'] for l in LABOS)
    assert len(ANSWERS)>=170
    assert all(l['nr'] in THEORY_LABS for l in LABOS)
    check_doc('LEERLING');check_doc('LEERKRACHT')
    f=pymupdf.open(ROOT/'Bestellijst_nieuw_materiaal_6BCW.pdf');assert len(f)>0
    print('OK — technische controles; geen inhoudelijke goedkeuring van alle 118 bronpagina’s')
