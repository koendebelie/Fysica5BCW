# -*- coding: utf-8 -*-
"""Genereer labocursus 6BCW uit één inhoudsbron.

    PYTHONPATH=work python3 work/build.py            # leerlingen
    PYTHONPATH=work python3 work/build.py --teacher  # leerkrachten

De PDF wordt gemaakt met de optionele `render_pdf.py` (HTML/weasyprint) of
LibreOffice indien op het systeem beschikbaar. Alle docx-elementen blijven
bewerkbaar en de formules zijn echte OfficeMath-objecten.
"""
import argparse
import os
import re
from pathlib import Path
from urllib.parse import quote

from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

import kit as K
from labs import LABOS, INSPIRATIE
from answers import ANSWERS
from rubric_data import RUBRIC
import deel1

ROOT = Path(__file__).resolve().parent.parent
FIGS = Path(__file__).resolve().parent / 'figs'
SRC = 'Labocursus 6BCW voorlopig.pdf'

THEORY_FILES = {
 '02':'02 Beweging en  kracht 6BCW deel 1.pdf',
 '03':'03 Beweging en  kracht 6BCW deel 2.pdf',
 '04':'04 Beweging en  kracht 6BCW deel 3 (zwaartekracht en valbeweging) 2627.pdf',
 '05':'05Derde wet van Newton 6BCW 2526 lkr (in 2627 lpd overlopen).pdf',
 '06':'06 Gravitatie versus zwaartekracht 6BCW 2526 (in 2627 lpd overlopen).pdf',
 '07':'07 Arbeid en Energie Deel 1 6BCW 2526 lkr.pdf',
 '08':'08 Arbeid en Energie Deel 2 6BCW 2526 lkr.pdf',
 '09':'09 De eenparig cirkelvormige beweging 6BCW 2526 lkr.pdf',
 '10':'10 Harmonische trillingen 2526 6BCW lkr.pdf',
 '11':'11 De slinger 2526 6BCW lkr.pdf',
 '12':'12 Resonantie 6BCW 2526.pdf',
 '13':'13 LOPENDE GOLVEN 6BCW 2526 lkr.pdf',
 '13A':'13A Verschijnselen bij lopende golven 6BCW 2425 lkr.pdf',
 '14':'14 Staande golven 2526 6BCW lkr.pdf',
 '15':'15 Geluidsgolven 6BCW 2526 lkr .pdf',
 '16':'16 Elektromagnetische golven 2526 6BCW lkr.pdf',
}
THEORY_LABS={1:['02','03'],2:['03','04'],3:['04','06'],4:['04'],
             5:['04','05'],6:['07','08'],7:['09'],8:['09'],9:['10'],
             10:['10','11'],11:['10','12'],12:['13','13A','14'],13:['15'],
             14:['13A','16'],15:['16'],16:[]}

EXTRA_FIGS = {
 (1,2):[('sch_tijdtikker_wagentje.png','Eigen elektrisch wagentje met 50 Hz-tijdtikker, papierbandje en 6 V~-voeding (schema naar bron blz. 68–72).')],
 (2,2):[('bron_p086_2.png','Wagentje op stijgende helling (bron: voorlopige cursus blz. 86).')],
 (3,2):[('sch_verticale_worp_tweecamera.png','Twee camera’s: één filmt de loslaathoogte, één het hoogste punt; hetzelfde meetlatvlak (eigen schema naar bron blz. 16–18).')],
 (4,1):[('sch_worp.png','Horizontale worp: leg zelf x- en y-assen en schaal vast (eigen schema naar bron blz. 56–57).')],
 (5,3):[('bron_p104_1.png','Krachtenparallellogram met twee dynamometers (bron: voorlopige cursus blz. 104).')],
 (7,1):[('bron_p109_1.png','Krachtarm bij een draaibaar statiefje (bron: voorlopige cursus blz. 109).')],
 (7,2):[('bron_p116_1.png','Tussenstandige last (bron: voorlopige cursus blz. 116).'),
         ('bron_p117_1.png','Tussenstandige macht (bron: voorlopige cursus blz. 117).')],
 (14,2):[('sch_cd_sporen.png','CD-sporen als rooster (nieuw, veilig schema; de vraag komt uit de voorlopige cursus blz. 5–6 en 62).')],
}

FIG_BEST = {
 1:('sch_luchtbel_twee_standen.png','Dezelfde luchtbel bij 90° en 45°; volg steeds dezelfde voorkant (schema naar bron blz. 63–67).'),
 2:('bron_p079_1.png','Tijdtikker en hellend vlak (bron: voorlopige 6BCW-cursus, blz. 79).'),
 3:('bron_p026_1.png','Voorbeeld van een v(t)-grafiek bij valbeweging (bron: voorlopige cursus, blz. 26).'),
 4:('bron_p093_1.png','Geverfd kogelspoor op een schuine plank (bron: voorlopige cursus, blz. 93).'),
 5:('bron_p097_1.png','Wagentje, tijdtikker en katrol (bron: voorlopige cursus, blz. 97).'),
 6:('bron_p106_1.png','Wagentje op hellend vlak, dynamometer en hoogte h (bron: voorlopige cursus, blz. 106).'),
 7:('bron_p113_1.png','Hefboom met tussenstandig steunpunt (bron: voorlopige cursus, blz. 113).'),
 8:('bron_p033_1.png','Draaiende massa en hangmassa (bron: voorlopige cursus, blz. 33).'),
 9:('sch_massa_veer.png','Massa-veersysteem (schematische tekening).'),
 10:('sch_slinger.png','Slinger, lengte tot massamiddelpunt (schematische tekening).'),
 11:('bron_p051_1.png','Gedempte veer met aandrijving (bron: voorlopige cursus, blz. 51).'),
 12:('sch_golfbak.png','Golfbak als onderzoeksmiddel (schematische tekening).'),
 13:('sch_geluid.png','Twee tonen in tegenfase en hun som (schematische tekening).'),
 14:('bron_p002_1.png','Laserlicht achter een rooster (bron: voorlopige cursus, blz. 2).'),
 15:('bron_p012_1.png','Twee kijkrichtingen bij de speldeprikproef (bron: voorlopige cursus, blz. 12).'),
 16:('sch_slinger.png','Voorbeeld: slinger met vast te houden variabelen (schematische tekening).'),
}


def _teacher(doc, teacher, text, label='Modelantwoord'):
    if teacher:
        K.modelantwoord(doc, text, label=label)


def _lines(doc, count, teacher=False):
    # Leerlingen- en leerkrachtenversie hebben identieke invulvakken;
    # de rode modelantwoorden komen er in de leerkrachtenversie direct onder.
    K.invul(doc, regels=count)


def _docid(lab, typ, nr):
    return f'L{lab["nr"]}:{typ}:{nr}'


def _formula(doc, src):
    K.formule(doc, src.replace('\\\\', '\\'))


def cover(doc, teacher):
    for _ in range(3):
        K.p(doc, '')
    K.p(doc, 'LABOCURSUS TOEGEPASTE FYSICA', size=26, bold=True, color='1F4E79', align='c', space_after=14)
    K.p(doc, 'Beweging • krachten • arbeid en energie • trillingen • golven • licht',
        size=16, color='2E7D32', align='c', space_after=20)
    K.p(doc, 'Toegepaste fysica • 6BCW', size=14, align='c', space_after=18)
    K.p(doc, 'Werkbladen volgens de OVUR-methode – Oriënteren – Voorbereiden – Uitvoeren – Reflecteren',
        size=11, italic=True, align='c', space_after=25)
    if teacher:
        K.p(doc, 'LEERKRACHTENVERSIE – met modelantwoorden, verwachte resultaten en didactische tips (rood gemarkeerd)',
            size=12, bold=True, color='B71C1C', align='c', space_after=20)
    for label in ('Naam', 'Klas / nummer', 'Leerkracht', 'Labogroep / partner(s)'):
        K.p(doc, f'{label}:  …………………………………………………………………………………………', size=12, space_after=10)
    for _ in range(4):
        K.p(doc, '')
    K.p(doc, 'Afgestemd op leerplan III-BCSW-d (Katholiek Onderwijs Vlaanderen, versie januari 2024): '
             'STEM-doelen LPD 1–6 S en fysica LPD 12–23 F.', size=9, align='c', color='555555')
    K.pagebreak(doc)


def contents(doc):
    K.h1(doc, 'Inhoud')
    K.p(doc, "Automatische inhoudsopgave op basis van Word-koppen (niveau 1–2). "
             "Bijwerken: klik in de inhoudsopgave → F9 → 'Veld bijwerken' → 'In zijn geheel bijwerken'.",
        size=9, italic=True, color='555555')
    fallback=[(0,'Deel 1 – Algemene inleiding')]
    for lab in LABOS:
        fallback.append((0,f'LABO {lab["nr"]} – {lab["titel"]}'))
        fallback.extend([(1,'O – ORIËNTEREN'),(1,'V – VOORBEREIDEN'),
                         (1,'U – UITVOEREN'),(1,'R – REFLECTEREN')])
    fallback += [(0,f'Bijlage {x} – {t}') for x,t in [
        ('A','Het Excel-verslagsjabloon'),('B','Productevaluatie'),('C','Proces- en attituderubric'),
        ('D','Zelfreflectie en peer-evaluatie'),('E','Naslag'),('F','Tracker en tijdtikker gebruiken')]]
    # TOC-veld met statische fallback alleen op het niveau van de hoofddelen om de inhoud compact te houden
    K.toc(doc,[x for x in fallback if x[0]==0])
    K.pagebreak(doc)


def smart(doc, lab, teacher):
    n=lab['nr']
    if n == 1:
        K.h3(doc,'Onderzoeksvraag (leerlijn SMART – stap 2: jij kiest)')
        K.p(doc,'Stap 2 van de leerlijn: vier voorstellen, maar slechts één is een goede SMART-onderzoeksvraag '
                 'voor dit volledige labo. Omcirkel ze. De drie afleiders zien er geloofwaardig uit.')
        for i,s in enumerate(lab['mc']): K.p(doc,chr(65+i)+'. '+s)
        K.p(doc,'Verantwoord per letter waarom jouw keuze SMART is. Schrijf bij elk ander voorstel '
                 'in één zin welke letter ontbreekt of waarom het niet over ons onderzoek gaat.')
        K.tabel(doc,['Mijn keuze','S','M','A','R','T'],[['','','','','','']],
                widths=[1600,1600,1600,1600,1600,1638])
        _lines(doc,2,teacher)
        _teacher(doc,teacher,ANSWERS['L1:MC'])
    else:
        K.h3(doc,'Onderzoeksvraag (leerlijn SMART – stap 3: jij formuleert)')
        K.p(doc,'Stap 3 van de leerlijn: formuleer zelf een SMART-onderzoeksvraag voor het **hele** labo. '
                 'Gebruik de vorm “Hoe hangt … af van … bij …?” Geef aan wat je varieert, wat je meet '
                 'en wat constant blijft. Noem bereik en meetmethode. Eindig op “tijdens dit labo”.')
        K.tabel(doc,['Mijn onderzoeksvraag','S','M','A','R','T'],[['','','','','','']],
                widths=[1900,1550,1550,1550,1550,1538])
        _lines(doc,2,teacher)
        _teacher(doc,teacher,lab['onderzoek']+' '+lab['variabelen'],label='Voorbeeldvraag en variabelen')


def worksheet(doc, lab, teacher):
    n=lab['nr']; title=f'LABO {n} – {lab["titel"]}'
    K.pagebreak(doc);K.h1(doc,title)
    K.p(doc,'Naam: ………………………………………………   Klas: …………   Nr.: …………   Datum: ……/……/……',size=10)
    K.p(doc,f'Richtduur: {lab["duur"]} lesuren     Type practicum: {lab["type"]}',size=10)
    K.p(doc,'Mate van sturing: '+lab['sturing'],italic=True,size=10)
    K.p(doc,'Veiligheidsverantwoordelijke (wisselt per labo): ………………………………………………',size=9)
    K.kader(doc,'LESDOELEN – na dit labo kan je …',lab['doelen'],soort='doel',size=9.7)
    bronregel = ('Nieuw ontworpen open werkblad; geen bronpagina.' if str(lab['bron']).lower() == 'nieuw'
                 else 'Bronbladen van de voorlopige labocursus 6BCW: blz. '+lab['bron']+'.')
    K.kader(doc,'LEERPLANDOELEN (III-BCSW-d)',
            [lab['lp'], bronregel+' Zie de theoriebron bij “Theorie-overzicht”.'],soort='lp',size=9.5)
    K.kader(doc,'VOORKENNIS – check vóór je begint',[q for q,a in lab['voor']],soort='voor',size=9.7)
    if teacher:
        for i,(q,a) in enumerate(lab['voor'],1): _teacher(doc,True,ANSWERS[_docid(lab,'voor',i)],label=f'Voorkennis {i} – modelantwoord')
        # vakgroepcontext uitsluitend in leerkrachtenversie
        tips=list(ANSWERS[f'L{n}:docent'])
        if n == 12:
            tips.append('Vakvergadering BCSW 15 september 2026: LPD 21 F stond op nul in de doelenrapportage; '
                        'registreer dit doel in planner en evaluatie wanneer buiging/interferentie werkelijk besproken en beoordeeld worden.')
        if n == 16:
            tips.append('Vakvergadering BCSW 15 september 2026: voor lange practica/projecten minstens één feedbackmoment voorzien; '
                        'koppel alleen werkelijk behandelde en geëvalueerde doelen.')
        K.teacher_note(doc,tips)

    K.h2(doc,'O – ORIËNTEREN')
    K.h3(doc,'Context');K.p(doc,lab['context'])
    smart(doc,lab,teacher)
    K.h3(doc,'Doel van het onderzoek');K.bullets(doc,lab['doelen'][:3],size=10)
    K.h3(doc,'Oriëntatievragen (beantwoord vóór het labo)')
    for i,(q,a) in enumerate(lab['orientatie'],1):
        K.vraag(doc,i,q);_lines(doc,2,teacher)
        _teacher(doc,teacher,ANSWERS[_docid(lab,'orientatie',i)])

    K.h2(doc,'V – VOORBEREIDEN')
    K.h3(doc,'Benodigdheden');K.bullets(doc,lab['materiaal'],size=10)
    K.h3(doc,'Theorie-overzicht')
    K.p(doc,lab['begrip'])
    K.p(doc,'Zie theoriecursus: **'+lab['theorie']+'**. Bij woorden die je nog niet kende: '
             'zie de begrippenlijst in Bijlage E.',size=9.5)
    for chapter in THEORY_LABS[n]:
        fname = THEORY_FILES[chapter]
        url = 'https://github.com/koendebelie/Fysica5BCW/blob/main/leerstof%206BCW/' + quote(fname)
        K.hyperlink(doc, f'Open theorie-PDF {chapter}: {fname}', url)
    _formula(doc,lab['formule'])
    K.kader(doc,'VEILIGHEID // NAUWKEURIGHEID',lab['veiligheid'],soort='veilig',size=9.6)
    if n == 16:
        K.kader(doc,'UITLEG – risicobeoordeling bij eigen opstelling',
                ['Er bestaat geen veilige standaardwaarde voor alle proeven. Noteer toestelgrenzen en '
                 'laat je materiaal en de maximale instellingen door de leerkracht controleren voordat je begint.'],
                soort='uitleg',size=9.6)
    K.h3(doc,'Hypothese')
    K.p(doc,'*Formuleer vóór de proef wat je verwacht, waarom, en welk resultaat je voorspelling zou tegenspreken.*')
    _lines(doc,3,teacher)
    _teacher(doc,teacher,'Een hypothese benoemt een concreet verband in '+lab['onderzoek']+
             ' en is geen achteraf overgenomen besluit.',label='Hypothese – didactische aanwijzing')
    K.h3(doc,'Werkplan')
    K.bullets(doc,['Verdeel de rollen (meten, noteren, veiligheid) en wissel ze per deel.',
                    'Noteer jouw gekozen bereiken, stappen en aantal herhalingen; één variabele tegelijk.',
                    'Maak een variabelentabel en schets je opstelling. Laat het plan en de opstelling vóór uitvoering goedkeuren.'],size=10)
    K.tabel(doc,['O – onafhankelijk','A – afhankelijk','C – constant','Bereik / meettoestel'],[['','','',''],['','','','']],
            widths=[2200,2200,2200,3038],size=9)

    K.h2(doc,'U – UITVOEREN')
    # minimaal één figuur per werkblad, bij voorkeur oorspronkelijk bronbeeld
    img,caption=FIG_BEST[n]
    K.figuur(doc,img,caption,breedte_cm=9.0)
    for j,part in enumerate(lab['delen'],1):
        if part.get('nieuw_blad'):
            # Deel 1 sluit aan op het overzicht en de bronfiguur. Volgende
            # afzonderlijke bronpractica krijgen een eigen afdrukblad.
            if j > 1: K.pagebreak(doc)
            K.p(doc, f'LABO {n} · bronpracticum {j} — naam: ……………………………… datum: ……/……/……',
                bold=True, color='1F4E79', size=9)
        K.h3(doc,part['titel'])
        if part.get('materiaal_deel'):
            K.p(doc,'Oorspronkelijk materiaal voor dit practicum: '+part['materiaal_deel'],size=9.4)
        if part.get('open_opdracht'):
            K.kader(doc,'OPEN PRACTICUM – jouw eigen meetplan, dezelfde oorspronkelijke proef',
                    part['open_opdracht'],soort='stem',size=9.5)
            K.tabel(doc,['Onderzoeksvraag / toetsbare hypothese','O: wat verander je?','A: wat meet je?',
                         'C: wat houd je gelijk?'],[['','','','']],size=8.5)
            K.p(doc,'Eigen werkplan, keuze van stip 0 en veilige schets (laat goedkeuren vóór je meet):',size=9.5)
            _lines(doc,4,teacher)
        for ef,cap in EXTRA_FIGS.get((n,j),[]):
            K.figuur(doc,ef,cap,breedte_cm=7.0)
        K.p(doc,'Onderzoeksvraag: '+part['vraag'],bold=True,size=10)
        K.p(doc,'Hypothese: schrijf je verwachting en één reden op vóór de meting.',italic=True,size=9.5)
        _lines(doc,1,teacher)
        K.p(doc,'Uitvoering:',bold=True,size=10)
        K.numbered(doc,part['stappen'],size=10)
        if part.get('tabel_uitleg'):
            K.p(doc,part['tabel_uitleg'],size=9.3,italic=True,color='1F4E79')
        # Bronkolommen met vooraf ingevulde stippen en midden-tijdstippen zijn echte
        # volledige rijen, niet enkel een label met daarachter lege cellen.
        def table_rows(headers, rr):
            if isinstance(rr,int): return [['']*len(headers) for _ in range(rr)]
            return [([str(v) if v is not None else '' for v in r] if isinstance(r,(list,tuple))
                     else [str(r)]+['']*(len(headers)-1)) for r in rr]
        rows=table_rows(part['kop'],part['rijen'])
        K.tabel(doc,part['kop'],rows,size=8.4)
        for extra in part.get('extra_tabellen',[]):
            K.p(doc,extra['titel'],bold=True,size=9.5)
            K.tabel(doc,extra['kop'],table_rows(extra['kop'],extra['rijen']),size=8.4)
        for instruction in part.get('grafieken',[]):
            K.p(doc,'GRAFIEK: '+instruction,size=9.5,color='1F4E79')
        K.p(doc,'Verwerking: '+part['verwerking'],size=9.6,italic=True)
        K.p(doc,'Foto / schets van de echte opstelling (benoem de onderdelen):',size=9.5)
        _lines(doc,2,teacher)
        K.p(doc,'Waarneming (verwijs naar tabel/grafiek):',size=9.5)
        _lines(doc,2,teacher)
        K.p(doc,'Verklaring met het fysisch model:',size=9.5)
        _lines(doc,2,teacher)
        _teacher(doc,teacher,'Verwacht: '+part['verwerking']+' Vergelijk met de metingen van de klas; '
                 'cijferwaarden hangen van de opstelling af.',label=f'Deel {j} – verwachte interpretatie')
        bron = ('Bron: nieuw ontworpen deel voor deze cursus (geen bronpagina).'
                if str(part['bron']).lower() == 'nieuw' else
                'Bron: '+SRC+', blz. '+part['bron']+'.')
        K.p(doc,bron,size=8.5,italic=True,color='777777')
        for qi,q in enumerate(part.get('vragen',[]),1):
            K.vraag(doc,qi,q,size=9.7)
            _lines(doc,2,teacher)
            _teacher(doc,teacher,ANSWERS[f'L{n}:deel{j}:vraag{qi}'])
    K.kader(doc,'STEM-ONTWERPOPDRACHT (LPD 4 S) – ontwerp, test en bewijs',
            [lab['stem'],'Noteer: SMART-deelvraag, O/A/C, werkwijze, grenzen en herhalingen, '
             'meetresultaat en besluit; maak een foto of schets van de gebouwde/testopstelling.'],
            soort='stem',size=9.7)
    if n == 16:
        K.kader(doc,'Inspiratie – onderzoeksvragen (kies er één of bedenk zelf)',INSPIRATIE,soort='uitleg',size=9)
    K.h2(doc,'R – REFLECTEREN')
    K.h3(doc,'Besluit')
    K.p(doc,'*Antwoord op de eigen onderzoeksvraag, onderbouwd met je metingen. Klopt je hypothese?*')
    _lines(doc,4,teacher)
    K.h3(doc,'Foutenanalyse en betrouwbaarheid')
    K.p(doc,'*Wat is de grootste meetonzekerheid? Hoe verbeter je de proef concreet?*')
    _lines(doc,3,teacher)
    K.h3(doc,'Reflectievragen')
    for i,(q,a) in enumerate(lab['reflectie'],1):
        K.vraag(doc,i,q,size=10)
        _lines(doc,2,teacher)
        _teacher(doc,teacher,ANSWERS[_docid(lab,'reflectie',i)])
    if lab['zelf']:
        K.p(doc,'ZELFREFLECTIE: vul ook Bijlage D.1 in voor dit labo.',bold=True,color='1F4E79',size=9.5)
    K.kader(doc,'WAT, HOE EN WANNEER WORDT GEËVALUEERD IN DIT LABO?',[
        'PRODUCT (60 %) – wat: '+('wetenschappelijke poster, Excel-ruwe data, grafiek, hypothese en eigen onderzoeksplan.' if n==16
                             else 'volledige tabellen, berekeningen/grafieken of schetsen en antwoorden op de vragen van alle delen.'),
        'PRODUCT – hoe en wanneer: puntenverdeling /10 (Bijlage B), groepspunt, feedback in het feedbackblok; '
        'deadline = één week na het labo, 23.59 u, Smartschool-uploadzone.',
        'PRODUCT – wat dien je in: '+lab['product']+'. Eén upload per groep.',
        'PROCES & ATTITUDE (40 %) – wat: veilig werken, meetplan vóór uitvoering, eigen rol, tijdige ruwe data en opruimen.',
        'PROCES & ATTITUDE – hoe: observatie door de leerkracht met de rubric van Bijlage C (10 thema’s × 5 niveaus), individueel punt.',
        ('PEER-EVALUATIE: ja – 300-puntenmethode, werkwijze Bijlage D.' if lab['peer'] else
         'PEER-EVALUATIE: niet voorzien bij dit labo (tenzij de leerkracht dit aankondigt).')
    ],soort='eval',size=9.1)


def _start_appendix(doc, text):
    K.pagebreak(doc);K.h1(doc,text)


def appendices(doc, teacher):
    _start_appendix(doc,'Bijlage A – Het Excel-verslagsjabloon: opbouw en checklist')
    K.p(doc,"Gebruik het blanco 6BCW-Excel-sjabloon uit de Smartschool-map 'Toegepaste fysica – labo' en "
            "bekijk de bijbehorende screencast. Geen eigen Word/Google-document voor een Excel-labo.")
    checks=[
        ('Kopblok','Groepsleden, klas, uitvoeringsdatum, labonummer en titel; bestandsnaam bevat 6BCW.'),
        ('OMSCHRIJVING','Doel, materiaal en werkwijze in eigen woorden; door een ander herhaalbaar.'),
        ('ONDERZOEKSVRAAG','Eén eigen SMART-vraag die alle delen van het labo dekt.'),
        ('HYPOTHESE','Verwachting met redenering, genoteerd vóór de proef.'),
        ('SCHEMA / FOTO','Opstelling met onderdelen, meettoestellen en maatwaarden benoemd.'),
        ('TABEL','Ruwe data, symbool en eenheid per kolom; berekende kolommen met Excel-formule.'),
        ('BEREKENINGEN','Twee uitgewerkte voorbeelden per soort: formule → waarden met eenheid → resultaat.'),
        ('GRAFIEK','Spreidingsgrafiek met losse punten, assen + eenheid, titel, passende trendlijn/vergelijking.'),
        ('BESLUIT','Data beantwoorden vraag, theorieverbinding, hypothese, foutenanalyse, reflectievragen.'),
        ('FEEDBACKBLOK','Niet verwijderen; cursieve sjabloontekst op het einde wel verwijderen.'),
        ('GROEPSWERK','OneDrive gedeeld, ieders bijdrage, iedereen leest alles na.'),
        ('INDIENEN','Eén upload per groep in Smartschool uiterlijk één week na het labo, 23.59 u; juiste bestandssoort.')]
    K.tabel(doc,['Onderdeel (Excel)','Checklist','✔'],[[x,y,'☐'] for x,y in checks],widths=[2500,6538,600],size=9)

    _start_appendix(doc,'Bijlage B – Productevaluatie: het verslag (60 %)')
    K.p(doc,'Er is geen rubric voor het product: de punten volgen de verdeling van het Excel-sjabloon. '
            'Ook werkbladen-PDF en poster worden op dezelfde vier onderdelen (/10) beoordeeld.')
    K.tabel(doc,['Onderdeel','Max.','Wat wordt verwacht?','Typische feedbackcodes'],[
        ['1. Verkennen & onderzoeken','2','Eigen SMART-vraag, doel, materiaal, herhaalbare werkwijze, hypothese en schema/foto.','Doel/variabelen ontbreken • hypothese onduidelijk • schema zonder labels'],
        ['2. Onderzoek uitvoeren','3','Volledige ruwe data, eenheden, beduidende cijfers, voorbeelden van Excel-berekeningen, spreidingsgrafiek met juiste assen en trend.','Eenheden • berekening • punten niet verbinden • trendlijn toevoegen'],
        ['3. Concluderen','3','Beantwoord de vraag uit meetgegevens, koppel aan theorie, toets hypothese, bespreek meetfouten, reflectievragen.','Geen meetgegevens in besluit • hypothese niet getoetst • foutenanalyse te vaag'],
        ['4. Attitude en verzorging','2','Gevraagde bestandssoort, op tijd ingediend, feedbackblok bewaard, verzorgd en aantoonbaar als groep.','Verkeerd sjabloon • te laat • instructietekst niet verwijderd']
    ],widths=[2200,600,4438,2400],size=8.8)
    K.p(doc,'Bij labo 16 telt bij onderdeel 1 de eigen vraag en het plan; bij onderdeel 3 de kwaliteit '
            'van de wetenschappelijke poster. Het groepspunt kan bij labo 5, 10 en 14 met peerfactor '
            'worden aangepast; bij het open onderzoek is géén peerfeedback voorzien.',size=9.5)

    K.landscape_section(doc)
    K.h1(doc,'Bijlage C – Proces- en attituderubric (40 %)')
    K.p(doc,'Naam: ……………………………………………    Labo: ……    Datum: ……/……/……     Score: …… / 10    Opmerkingen: ………………………………',size=9)
    K.p(doc,'Per thema één niveau: uitstekend 1 · goed 0,8 · voldoende 0,6 · onvoldoende 0,4 · slecht 0,2. '
            'Tel de tien scores op; het resultaat is /10 en telt voor 40 %.',size=9)
    rows=[row[:] for row in RUBRIC]
    # Aanpassen van de contextvoorbeelden; niveaus en tien thema's letterlijk uit de 5BCW-referentie
    for row in rows[1:]:
        row[:] = [cell.replace('A-meter in serie, V-meter parallel, juiste bereiken, AC/DC juist',
                              'tijdtikker op juiste lage voeding, camera gekalibreerd, meetbereiken juist')
                      .replace('bron uit bij opbouwen, I_max, geen contact met blanke geleiders, magneten/warmte/water',
                               'opstelling gecontroleerd, valzone vrij, laser laag gericht, water bij voeding vermeden')
                      .replace('als .xlsx in het sjabloon', 'in de gevraagde bestandssoort')
                      .replace('als .xlsx', 'in de gevraagde bestandssoort')
                      for cell in row]
    K.tabel(doc,rows[0],rows[1:],widths=[1900]+[2650]*5,size=7.3)
    K.h3(doc,'Observatieblad leerkracht (per labo)')
    if teacher:
        K.tabel(doc,['Leerling']+[str(i) for i in range(1,11)]+['/10','Opmerking'],
                [['']*13 for _ in range(4)],widths=[2400]+[800]*10+[800,3900],size=7.5)
    else:
        K.p(doc,'De leerkracht vult het observatieblad bij het practicum in.',size=9,italic=True)
    K.portrait_section(doc)
    K.h1(doc,'Bijlage D – Zelfreflectie- en peer-evaluatiefiche')
    K.h3(doc,'D.1 Zelfreflectie (na labo 2, 6, 9 en 16)')
    K.tabel(doc,['Vraag','Mijn antwoord'],[
        ['Scoor jezelf op de 10 thema’s van Bijlage C (1 / 0,8 / 0,6 / 0,4 / 0,2) en motiveer één sterk punt en één werkpunt.',''],
        ['Welke vaardigheid beheers je nu beter dan bij het vorige reflectiemoment?',''],
        ['Wat ga je bij het volgende labo concreet anders doen?',''],
        ['Welke feedback op je verslagen heb je toegepast?','']
    ],widths=[5200,4438],size=9)
    K.h3(doc,'D.2 Peer-evaluatie (voorzien bij labo 5, 10 en 14)')
    K.p(doc,'Iedere leerling verdeelt per groep 100 punten per groepslid over zichzelf én de anderen: '
            'groep van 3 → 300; groep van 2 → 200. Iedereen evenveel gedaan? 100 per persoon. '
            'Motivatie moet gedrag en bijdrage benoemen, niet sympathie. Vul individueel en vertrouwelijk in.')
    K.p(doc,'Peerfactor = (gemiddeld ontvangen punten, jezelf inbegrepen) / 100. Individueel productpunt '
            '= groepspunt × peerfactor (maximum 10/10). Bijvoorbeeld: groepspunt 7,5; ontvangen '
            '105, 105, 90 → gemiddeld 100 → factor 1,00 → 7,5. Bij 80, 85, 90 → factor 0,85 → 6,4. '
            'De leerkracht kan bijsturen als de verdeling strijdig is met de observaties.',size=9.5)
    K.p(doc,'Labo nr.: ……   Groep: ………………………   Ingevuld door: …………………………    Totaal: 300 / 200',size=9)
    K.tabel(doc,['Groepslid (naam)','Punten','Korte motivatie (wat deed deze persoon concreet?)'],[
        ['Ikzelf:','',''],['2:','',''],['3 (indien van toepassing):','',''],['Totaal:','300 / 200','']
    ],widths=[2800,1400,5438],size=9)

    _start_appendix(doc,'Bijlage E – Naslag: begrippen en formuleoverzicht')
    gloss={
        'ERB':'Eenparige rechtlijnige beweging: gelijke afstanden in gelijke tijden.',
        'EVRB':'Eenparig versnelde rechtlijnige beweging: snelheid verandert per seconde evenveel.',
        'Tijdtikker':'Toestel dat op een papierband op vaste tijdsintervallen stippen zet.',
        'Ogenblikkelijke snelheid':'Snelheid op een bepaald tijdstip, benaderd over een heel kort tijdsvenster.',
        'Richtingscoëfficiënt':'Stijging gedeeld door horizontale verandering in een grafiek.',
        'Tracker':'Programma voor positie-tijdmetingen uit een video, beeld voor beeld.',
        'Parallax':'Schijnbare verschuiving doordat camera en meetlat niet in hetzelfde vlak staan.',
        'Nettokracht / resultante':'Vectoriële som van alle krachten op één voorwerp.',
        'Krachtarm':'Loodrechte afstand van draaipunt tot werklijn van kracht.',
        'Krachtmoment':'Draaieffect van kracht maal krachtarm.',
        'Hefboom':'Stijve staaf die rond een steunpunt kan draaien.',
        'Centripetale kracht':'Nettokracht naar het middelpunt van een cirkelbaan.',
        'Hoeksnelheid':'Afgelegde hoek per seconde (rad/s).',
        'Amplitude':'Grootste uitwijking vanuit de evenwichtsstand.',
        'Eigenfrequentie':'Frequentie van vrije trilling zonder voortdurende aandrijving.',
        'Demping':'Afname van amplitude door energieverlies.',
        'Resonantie':'Sterke respons bij aandrijving nabij de eigenfrequentie.',
        'Golflengte':'Afstand tussen opeenvolgende toppen (m).',
        'Knoop / buik':'Stil punt / punt met grootste uitwijking van een staande golf.',
        'Buiging':'Een golf waaiert uit achter een opening of hindernis.',
        'Interferentie':'Golven samen zorgen voor versterking of verzwakking.',
        'Superpositie':'Momentane optelling van de uitwijkingen van meerdere golven.',
        'Tegenfase':'Top van ene golf valt samen met dal van andere.',
        'Dopplereffect':'Waargenomen frequentie verandert bij relatieve beweging bron/waarnemer.',
        'Roosterconstante':'Afstand tussen opeenvolgende roosterlijnen (m).',
        'Brekingsindex':'Maat voor richtingsverandering van licht tussen twee middenstoffen.',
        'SMART':'Specifiek, Meetbaar, Aanvaardbaar, Realistisch, Tijdsgebonden.',
        'Peerfactor':'Gemiddeld ontvangen peerevaluatiepunten gedeeld door 100.'}
    K.tabel(doc,['Begrip','Betekenis in eenvoudige woorden'],[[k,v] for k,v in gloss.items()],widths=[3000,6638],size=9)
    K.h3(doc,'E.1 Constantes en nuttige formules')
    K.tabel(doc,['Grootheid','Formule / waarde / eenheid'],[
        ['Valversnelling nabij aardoppervlak','g ≈ 9,81 m/s²'],
        ['Snelheid en versnelling','v = Δx/Δt (m/s); a = Δv/Δt (m/s²)'],
        ['Tweede wet','Fᵣ = ma (N)'],
        ['Arbeid / zwaarte-energie','W = F·s·cos θ; E_z = mgh (J)'],
        ['Krachtmoment / hefboom','M = F·d (N·m); Fₗdₗ = Fₘdₘ'],
        ['ECB','v = 2πr/T, ω = 2π/T, F_cp = mv²/r'],
        ['Veer / slinger','T_veer = 2π√(m/k); T_slinger = 2π√(l/g) (kleine hoek)'],
        ['Golf / lichtrooster','v = λf; a sin θ = nλ; a = 1/(lijnen per m)'],
        ['Breking','n = sin α/sin β (lucht naar kunststof)'],
    ],widths=[3200,6438],size=9)
    K.h3(doc,'E.2 Bronwijzer')
    K.p(doc,'De voorlopige cursus bevat dubbele bronbladen voor verticale worp (15–20 en 58–61) '
            'en vrije val (20–26 en 73–78). Ze zijn in labo 3 samengebracht. De overige bronproeven '
            'zijn aan elk werkblad gekoppeld in het kader “Leerplandoelen” en bij de delen.')

    _start_appendix(doc,'Bijlage F – Tracker en tijdtikker: een startgids')
    K.h3(doc,'F.1 Tracker voor videoanalyse (eerste gebruik: labo 3)')
    K.numbered(doc,[
        'Film zijdelings met een vaste camera; houd een meetlat in het vlak van de beweging. Bewaar het fragment.',
        'Open Tracker op de schoollaptop. Importeer het videofragment (Bestand → Openen).',
        'Plaats kalibratiestok op de meetlat; geef de echte lengte in meter op.',
        'Zet de oorsprong (bij verticale worp: vloer of bal op vloer) en kies omhoog positief.',
        'Maak een spoor/point mass en markeer het midden van de bal op opeenvolgende frames.',
        'Controleer een paar punten op fout gekozen frames en pas ze aan; kopieer t en y naar Excel.',
        'Maak spreidingsgrafiek met losse punten, benoemde assen en gepaste trendlijn. Sla schermafbeelding met titel en uitleg op.'
    ],size=9.5)
    K.kader(doc,'PROBLEMEN OPLOSSEN',['Geen beeld? Gebruik een ander lokaal videobestand of schoollaptop.',
             'Vreemde snelheden? Controleer schaal, oorsprong en framefrequentie.',
             'Beeld springt? Markeer frames handmatig; meetlat in hetzelfde vlak.',
             'Bij ontbreken van Tracker: analyseer het filmpje frame voor frame met tijdstempels en meetlat.'],soort='uitleg',size=9.5)
    K.h3(doc,'F.2 Tijdtikker (eerste gebruik: labo 1)')
    K.numbered(doc,[
        'Lees de toegestane voedingsspanning en frequentie op het toestel; de leerkracht controleert de juiste lage voeding (bron noemt 6 V~).',
        'Bevestig carbonlint en papieren bandje; proef kort met het wagentje veilig in een vangbak.',
        'Bij 50 Hz ligt tussen twee opeenvolgende stippen 0,020 s. Twee intervallen = 0,040 s.',
        'Meet plaatsen vanaf één gekozen nulstip, bereken Δx tussen stippen, en koppel elke snelheid aan de middentijd.',
        'Plak het originele bandje of een duidelijke foto ervan bij je ruwe data; zet voeding uit na de meting.'
    ],size=9.5)
    K.kader(doc,'VEILIGHEID / CONTROLE',['Gebruik nooit netspanning direct op de tijdtikker.',
           'Houd vingers, haren en kleding weg van de bewegende band.',
           'Bij onleesbare stippen: carbonlint corrigeren met voeding UIT, niet de data achteraf verzinnen.'],soort='veilig',size=9.5)
    if teacher:
        K.teacher_note(doc,['De voorlopige 6BCW-bron gebruikt Tracker zonder een volledig uitgewerkte screenshot-handleiding. '
                  'Controleer de actuele schoolversie en voeg echte screenshots van het lokale menu toe vóór verspreiding.',
                  'De bron vermeldt 6 V~ voor de tijdtikker; de werkelijke typeplaat en schoolvoeding zijn leidend.'])


def order_list():
    doc=K.new_document('Bestellijst nieuw materiaal Toegepaste fysica 6BCW')
    K.h1(doc,'Bestellijst nieuw materiaal – 6BCW')
    K.p(doc,'Voorlopige checklist voor 8 groepen van 2–3. Alleen niet-vanzelfsprekend materiaal; '
            'controleer eerst de voorraad. Prijzen zijn **niet geverifieerd** en dienen enkel voor budgettering; '
            'geen bestelling plaatsen zonder offertes en veiligheidscontrole.',size=10)
    rows=[
      ['Glazen buisje met afgeronde randen + stevige nylondraad + rubberstop','8 sets','€10–25/set','schoolleverancier fysicalabo','☐'],
      ['Roosters 80, 100, 300, 600 lijnen/mm','8 sets van 4','€30–80/set','optical/educational supplier','☐'],
      ['Gekeurde lageklasse-laserpen met bundelstop','8','€15–40/stuk','schoolleverancier optica','☐'],
      ['Overhead-golfbak of gelijkwaardig camerasysteem','1–2','offerte','schoolleverancier fysicalabo','☐'],
      ['Laagtoerige regelbare motor met excenter (resonantie)','2','offerte','schoolleverancier STEM','☐'],
      ['Statieven + zachte valmat/opvangbak voor werpproeven','8 sets','€10–25/set','schoolvoorraad / sporthandel','☐'],
      ['Twee stabiele smartphonehouders + twee verticale meetlatten per groep (handmatige verticale worp)','8 sets','offerte / voorraad','schoolvoorraad / schoolleverancier','☐'],
      ['Plexiglazen balkjes + spelden (optica)','8 sets','€10–30/set','schoolleverancier optica','☐'],
      ['Papieren tijdtikkerbandjes + carbonlint','8 × verbruiksset','€10–20/set','schoolleverancier fysicalabo','☐'],
      ['Veiligheidsbrillen voor ECB-rotatie','24','€5–12/stuk','schoolleverancier PBM','☐'],
    ]
    K.tabel(doc,['Item','Aantal voor 8 groepen','Richtprijs (niet geverifieerd)','Waar te koop','Al aanwezig?'],rows,
            widths=[3100,1350,1550,2500,1138],size=9)
    K.p(doc,'Gewone fysica-uitrusting (meetlat, massa’s, statief, chronometer, dynamometer, balans, '
            'laptop) staat bewust niet op de bestellijst. Koppel de bestelling aan de werkelijke groepsgrootte.',size=9)
    out=ROOT/'Bestellijst_nieuw_materiaal_6BCW.docx';doc.save(out)
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--teacher',action='store_true')
    ap.add_argument('--list-only',action='store_true')
    ap.add_argument('--source-worksheets',action='store_true',
                    help='Maak elk oorspronkelijk practicum tot een zelfstandig OVUR-werkblad')
    args=ap.parse_args()
    if args.list_only:
        print(order_list());return
    if args.source_worksheets:
        from source_sheets import write
        write(args.teacher);return
    T=args.teacher
    doc=K.new_document()
    cover(doc,T); contents(doc); deel1.build(doc,T)
    for lab in LABOS: worksheet(doc,lab,T)
    appendices(doc,T)
    name=f'Labocursus_6BCW_{"LEERKRACHT" if T else "LEERLING"}.docx'
    path=ROOT/name;doc.save(path)
    print(path)
    if not T: print(order_list())

if __name__=='__main__': main()
