# -*- coding: utf-8 -*-
"""Zelfstandig afdrukbare OVUR-werkbladen, één per oorspronkelijke 6BCW-proef.

Uit dezelfde labs.py/answers.py als de cursus: GEEN parallelle kopie van het protocol.
Deze bijbundel houdt de originele proeven gescheiden waar de algemene leerlijn
meerdere in één genummerd thema behandelt (bv. val tegenover verticale worp).
"""
from pathlib import Path
from urllib.parse import quote
import kit as K
from labs import LABOS
from answers import ANSWERS

ROOT=Path(__file__).resolve().parent.parent

# (hoofdstuk uit labs.py, deelselectie (1-based), oorspronkelijke proefnaam)
SHEETS=[
 (1,(1,),'De luchtbel bij 90° en 45°'),
 (1,(2,),'ERB met elektrisch wagentje en tijdtikker'),
 (2,(1,),'EVRB met beginsnelheid op een helling'),
 (2,(2,),'Open practicum: vertraagde beweging omhoog'),
 (3,(1,),'De valbeweging met triller en bandje'),
 (3,(2,3),'De verticale worp: handmatig en met Tracker'),
 (4,(1,),'Open practicum: horizontale worp met Tracker'),
 (4,(2,),'Paraboolbaan met geverfde kogel'),
 (5,(1,),'Tweede wet van Newton: a als functie van F'),
 (5,(2,),'Tweede wet van Newton: a als functie van m'),
 (5,(3,),'Samenstellen van krachten met twee dynamometers'),
 (6,(1,),'Arbeid van een wagentje op een helling'),
 (7,(1,),'Moment van een kracht met een statiefje'),
 (7,(2,),'Drie soorten hefboom'),
 (8,(1,),'ECB met speelgoedtrein en platenspeler'),
 (8,(2,),'Centripetale kracht met rubberstop'),
 (9,(1,),'Periode van een massa aan twee veren'),
 (9,(2,),'Onbekende massa zonder balans'),
 (9,(3,),'Een halve harmonische trilling met triller'),
 (10,(1,2,3),'Slinger: amplitude, massa en lengte'),
 (11,(1,2),'Resonantie bij een gedempte veer'),
 (12,(1,),'Golfbak: applet en fysieke projectie'),
 (12,(2,),'Staande golven op een touw'),
 (13,(1,2,3),'The Soundry: geluid, Doppler en harmonischen'),
 (14,(1,2,3),'Rooster: laser, CD en lichtspectrum'),
 (15,(1,2),'Lichtbreking met drie spelden'),
]


def rows(headers, source):
    if isinstance(source,int): return [['']*len(headers) for _ in range(source)]
    return [[str(v) if v is not None else '' for v in r] if isinstance(r,(list,tuple))
            else [str(r)]+['']*(len(headers)-1) for r in source]


def build(doc,teacher):
    # Uitgestelde import: build.py blijft de ENIGE CLI en bepaalt bronfiguren,
    # formuleparser en theorie-PDF-links voor beide cursussen.
    from build import FIG_BEST,EXTRA_FIGS,THEORY_LABS,THEORY_FILES,SRC
    K.p(doc,'TOEGEPASTE FYSICA · 6BCW',bold=True,size=16,color='1F4E79',align='c')
    K.p(doc,'Mijn oorspronkelijke practica — zelfstandige OVUR-werkbladen',bold=True,size=15,align='c')
    K.p(doc,'HAST · leerkracht De Belie K. · '+('leerkrachtenversie' if teacher else 'leerlingenversie'),align='c')
    K.kader(doc,'WAT IS DEZE BUNDEL?',[
        'Elk oorspronkelijk practicum heeft een eigen werkblad: je kunt bijvoorbeeld vrije val, EVRB met beginsnelheid, het OPEN practicum vertraging, verticale worp en horizontale worp onafhankelijk plannen, uitvoeren en indienen.',
        'De bronopstellingen en originele meetgang zijn gemoderniseerd zonder ze te vervangen door sensoren of andere nieuwe proeven. De algemene 6BCW-cursus bevat de overkoepelende theorie, OVUR-leerlijn, product/procesrubric en Bijlagen A–F.',
        'Bij een tijdtikker staat het MIDDELTIJDSTIP t′ links van de berekende v; selecteer precies die twee kolommen voor Excel v(t′). Δt blijft de tijdsDUUR van het venster, Δv is een snelheidsverschil.'
    ],soort='uitleg',size=9.5)
    K.h1(doc,'Inhoud: originele practica')
    for idx,(_,_,title) in enumerate(SHEETS,1):
        K.p(doc,f'{idx:02d} · {title}',size=9.5)
    for idx,(n,parts,title) in enumerate(SHEETS,1):
        lab=LABOS[n-1]
        K.pagebreak(doc)
        K.h1(doc,f'PRACTICUM {idx:02d} – {title}')
        K.p(doc,'Naam: …………………………………………………   Klas: …………  Datum: ……/……/……  Groep: …………',size=9.5)
        bron='; '.join(str(lab['delen'][j-1]['bron']) for j in parts)
        K.kader(doc,'HERKOMST EN LEERPLANDOELEN',[f'Origineel: {SRC}, blz. {bron}.',lab['lp']],soort='lp',size=9.3)
        K.h2(doc,'O – ORIËNTEREN')
        K.p(doc,'De oorspronkelijke onderzoeksvraag: '+(' / '.join(lab['delen'][j-1]['vraag'] for j in parts)),bold=True,size=10)
        K.p(doc,'Wat wil je meten en waarom? Schrijf de vraag in eigen woorden en noteer een voorspelling vóór de eerste proef.')
        K.invul(doc,regels=3)
        if teacher:K.modelantwoord(doc,lab['onderzoek'],label='Mogelijke SMART-variant')
        K.h2(doc,'V – VOORBEREIDEN')
        material=[]
        for j in parts:
            p=lab['delen'][j-1]
            if p.get('materiaal_deel'):material.append(p['materiaal_deel'])
        if not material:material=lab['materiaal']
        K.h3(doc,'De oorspronkelijke materialen');K.bullets(doc,material,size=9.5)
        K.kader(doc,'VEILIGHEID – laat de opstelling controleren',lab['veiligheid'],soort='veilig',size=9)
        K.p(doc,'Voorbereiding: schema/foto van de echte opstelling, variabelen, gekozen nulpunt, aantal herhalingen en veilige grenzen:')
        K.invul(doc,regels=3)
        K.tabel(doc,['O – onafhankelijk','A – afhankelijk','C – constant','Meetwijze / eenheid'],[['','','','']],size=9)
        for chapter in THEORY_LABS[n]:
            fname=THEORY_FILES[chapter]
            url='https://github.com/koendebelie/Fysica5BCW/blob/main/leerstof%206BCW/'+quote(fname)
            K.hyperlink(doc,'Theorie-PDF '+chapter+' – '+fname,url)
        if teacher:
            K.modelantwoord(doc,'De oorspronkelijke meetopstelling en bronwaarden zijn leidend. Laat vooral bij een OPEN proef eerst de zelfgekozen stip 0 en de veilige opstelling controleren.',label='Leerkracht – voorbereiding')
        K.h2(doc,'U – UITVOEREN')
        for j in parts:
            p=lab['delen'][j-1]
            K.h3(doc,p['titel'])
            images=EXTRA_FIGS.get((n,j),[])
            if not images and j==parts[0]:images=[FIG_BEST[n]]
            for fname,caption in images[:2]:K.figuur(doc,fname,caption,breedte_cm=7.8)
            if p.get('open_opdracht'):
                K.kader(doc,'OPEN PRACTICUM – behoud de originele materialen, ontwerp zelf de werkwijze',p['open_opdracht'],soort='stem',size=9.3)
                K.p(doc,'Mijn EIGEN meetplan vóór goedkeuring door de leerkracht:')
                K.invul(doc,regels=4)
            K.h3(doc,'De oorspronkelijke uitvoeringsstappen, verduidelijkt')
            K.numbered(doc,p['stappen'],size=9.5)
            if p.get('tabel_uitleg'):K.p(doc,p['tabel_uitleg'],italic=True,color='1F4E79',size=9)
            K.h3(doc,'Meetwaarden: invulbare brontabel')
            K.tabel(doc,p['kop'],rows(p['kop'],p['rijen']),size=8.2)
            for extra in p.get('extra_tabellen',[]):
                K.p(doc,extra['titel'],bold=True,size=9)
                K.tabel(doc,extra['kop'],rows(extra['kop'],extra['rijen']),size=8.2)
            for graph in p.get('grafieken',[]):K.p(doc,'EXCEL / GRAFIEK: '+graph,size=9.2,color='1F4E79')
            K.p(doc,'Verwerking: '+p['verwerking'],size=9.2)
            K.p(doc,'Bij mijn echte meting horen dit originele papierbandje / deze foto’s / deze Tracker-file:')
            K.invul(doc,regels=2)
            K.h3(doc,'Bronvragen bij deze proef')
            for qnum,q in enumerate(p.get('vragen',[]),1):
                K.vraag(doc,qnum,q,size=9.5);K.invul(doc,regels=2)
                if teacher:K.modelantwoord(doc,ANSWERS[f'L{n}:deel{j}:vraag{qnum}'])
        K.h2(doc,'R – REFLECTEREN')
        K.p(doc,'Besluit: beantwoord de oorspronkelijke onderzoeksvraag met jouw eigen data; benoem het model en minstens één meetonzekerheid.')
        K.invul(doc,regels=4)
        K.p(doc,'Hoe zou je juist DEZE originele proef veiliger of betrouwbaarder maken, zonder een andere proef te vervangen?')
        K.invul(doc,regels=3)
        K.kader(doc,'PRODUCT EN PROCES',[
            'Product (60 %): origineel papierbandje / videobestand / spoor en volledige ruwe meettabel, eigen berekeningen, grafieken en besluit. Processcore (40 %): voorbereiding, veilig bouwen, zelfstandigheid, samenwerking en opruimen.',
            'Bij een open practicum hoort het vooraf goedgekeurde eigen werkplan. Zie de volledige beoordelingsrubric in Bijlage B–C van de centrale 6BCW-cursus.'
        ],soort='eval',size=9)
        if teacher:K.teacher_note(doc,ANSWERS[f'L{n}:docent'][:4],title='LEERKRACHTENINFO – uitvoering van deze bronproef')
    return doc


def write(teacher=False):
    doc=K.new_document('Originele practica 6BCW – HAST')
    build(doc,teacher)
    tag='LEERKRACHT' if teacher else 'LEERLING'
    path=ROOT/f'Bronpractica_6BCW_{tag}.docx'
    doc.save(path);print(path)
    return path
