# -*- coding: utf-8 -*-
"""De 6BCW-cursus: vertrouwde schoolopstellingen als afzonderlijke OVUR-labo's.

De inhoud van de proeven komt uit labs.py; alleen bruikbare instructies worden
zichtbaar voor leerlingen. Bronverantwoording staat apart in work/ en niet op
leerlingen- of leerkrachtenwerkbladen.
"""
import re
from pathlib import Path
import kit as K
from labs import LABOS
from answers import ANSWERS

ROOT=Path(__file__).resolve().parent.parent
# (data uit labs.py, onderdelen 1-based, titel voor de leerlingen)
SHEETS=[
 (1,(1,),'Eenparige beweging van een luchtbel'),
 (1,(2,),'ERB met elektrisch wagentje en tijdtikker'),
 (2,(1,),'EVRB met beginsnelheid op een helling'),
 (2,(2,),'Open onderzoek: vertraagde beweging omhoog'),
 (3,(1,),'Vrije val met triller en papierband'),
 (3,(2,3),'Verticale worp: handmatige meting en Tracker'),
 (4,(1,),'Open onderzoek: horizontale worp'),
 (4,(2,),'Paraboolbaan met geverfde kogel'),
 (5,(1,2),'Tweede wet van Newton: kracht en massa'),
 (5,(3,),'Krachten samenstellen: vectoren'),
 (8,(1,),'Inleiding op de eenparige cirkelbeweging'),
 (8,(2,),'Centripetale kracht met rubberstop'),
 (9,(1,),'Periode van een massa aan twee veren'),
 (9,(3,),'Een halve harmonische trilling met tijdtikker'),
 (9,(2,),'Onderzoek: onbekende massa zonder balans'),
 (10,(1,2,3),'Slinger: amplitude, massa en lengte'),
 (11,(1,2),'Resonantie bij een gedempte veer'),
 (12,(1,),'Golven in de golfbak'),
 (12,(2,),'Staande golven op een touw'),
 (13,(1,2,3),'Geluid: tonen, zwevingen en klankkleur'),
 (14,(1,),'Laser en interferentie aan een rooster'),
 (14,(2,),'De sporenafstand van een CD'),
 (14,(3,),'Wit licht en lijnenspectra'),
 (15,(1,2),'Lichtbreking met drie spelden'),
 (16,(1,2),'Open onderzoek en wetenschappelijke poster'),
]

THEORY={1:'Beweging en kracht: eenparige beweging',2:'Beweging en kracht: versnelling en beweging op een helling',
 3:'Valbeweging en verticale worp',4:'Beweging in twee dimensies',5:'De wetten van Newton en krachten als vectoren',
 8:'Eenparige cirkelbeweging',9:'Harmonische trillingen',10:'De slinger',11:'Resonantie',
 12:'Lopende golven en staande golven',13:'Geluidsgolven',14:'Elektromagnetische golven: interferentie en spectra',
 15:'Elektromagnetische golven: lichtbreking',16:'Kies het theoriehoofdstuk dat bij je eigen onderzoek hoort'}


def clean(text):
    """Verwijder alleen redactionele herkomstverwijzingen; laat proefwaarden intact."""
    text=str(text)
    text=re.sub(r'\s*\((?:bron[^)]*|p\.\s*\d+[^)]*|blz\.\s*\d+[^)]*)\)', '',text,flags=re.I)
    text=re.sub(r'\b(?:[Oo]orspronkelijk(?:e)?|[Bb]ronpracticum|[Bb]ronopstelling|[Bb]ronreeks)\b',
                lambda m:{'bronopstelling':'opstelling','bronreeks':'meetreeks'}.get(m.group().lower(),''),text)
    text=re.sub(r'\b(?:bron|bronbladen)\s+blz\.?\s*[\d–-]+', '',text,flags=re.I)
    text=re.sub(r'\([^)]*(?:bron:|schema naar bron|blz\.)[^)]*\)','',text,flags=re.I)
    text=re.sub(r'\s{2,}',' ',text).strip()
    return text


def rows(headers, source):
    if isinstance(source,int):return [['']*len(headers) for _ in range(source)]
    return [[str(v) if v is not None else '' for v in r] if isinstance(r,(list,tuple))
            else [str(r)]+['']*(len(headers)-1) for r in source]


def intro(doc, teacher):
    K.p(doc,'LABOCURSUS TOEGEPASTE FYSICA · 6BCW',bold=True,size=22,color='1F4E79',align='c',space_after=14)
    K.p(doc,'HAST · leerkracht De Belie K.',align='c',size=14)
    K.p(doc,'Leerlingenversie' if not teacher else 'Leerkrachtenversie met modelantwoorden',align='c',size=11)
    K.p(doc,'Naam: ………………………………………………  Klas: …………  Schooljaar: …………',size=11)
    K.h1(doc,'Inhoud')
    for idx,(_,_,title) in enumerate(SHEETS,1):K.p(doc,f'{idx:02d} · {title}',size=9)
    K.h1(doc,'Zo gebruik je deze cursus')
    K.p(doc,'Elke proef heeft een eigen werkblad met Oriënteren, Voorbereiden, Uitvoeren en Reflecteren. '
        'Voer de aangegeven proef uit met het beschikbare schoolmateriaal; vervang de opstelling niet door een andere meetmethode. '
        'Noteer de echte ruwe gegevens en bewaar het papierbandje of de video. Laat een open werkplan eerst controleren.')
    K.kader(doc,'ONDERZOEKSVRAGEN: SNEL ZELFSTANDIG',[
        'Labo 1: je krijgt een volledige onderzoeksvraag en onderzoekt waarom die SMART is.',
        'Labo 2: kies uit vier mogelijke onderzoeksvragen en verantwoord je keuze.',
        'Vanaf labo 3: formuleer vóór de proef zelf een SMART-onderzoeksvraag; vermeld onafhankelijke en afhankelijke grootheid, gecontroleerde omstandigheden, meetwijze en de beschikbare lestijd.'
    ],soort='uitleg',size=9.5)
    K.kader(doc,'TIJDTIKKER EN EXCEL',[
        'Bij 50 Hz is één tikinterval 0,020 s. Kies je om de twee stippen een meetpunt, dan is Δt = 0,040 s.',
        'Een uit Δx/Δt berekende snelheid hoort bij de tussentijd t′ = (t_begin + t_eind)/2. In elke tijdtikkertabel staat t′ DIRECT LINKS van v: kopieer deze aangrenzende kolommen naar Excel voor de XY-grafiek v(t′).',
        'Δt betekent tijdsduur. Δv betekent verandering in snelheid en is geen naam voor de kolom met tussentijdstippen.'
    ],soort='uitleg',size=9.5)
    K.p(doc,'Beoordeling: product 60 % en proces/attitude 40 %. De volledige, ongewijzigde procesrubric en het blanco verslagoverzicht staan achteraan. Raadpleeg je theoriedocumenten per onderwerp, niet op een vast dianummer.',size=9.5)
    K.pagebreak(doc)


def smart(doc, idx, lab, teacher):
    K.h3(doc,'Onderzoeksvraag – SMART')
    if idx==1:
        q='Hoe verschilt de snelheid van dezelfde luchtbel over 0,10–1,00 m bij een buisstand van 90° en 45°, gemeten met dezelfde chronometer tijdens dit labo?'
        K.p(doc,q,bold=True)
        K.tabel(doc,['S','M','A','R','T'],[
            ['twee buisstanden, dezelfde bel','tijd en afstand in s en m','veilig op statief','materiaal in dit lokaal','meting in dit labo']],size=8.5)
        K.p(doc,'Verklaar waarom iedere SMART-letter hier past:');K.invul(doc,regels=2)
    elif idx==2:
        opts=[
          'Wat gebeurt er met een wagen wanneer we de spanning zomaar sterk verhogen?',
          'Hoe hangt de plaats x van het elektrische wagentje af van de tijd t in het gelijkmatige middendeel van zijn baan, gemeten met 50 Hz-tijdtikker bij dezelfde ingestelde spanning tijdens dit labo?',
          'Hoe veranderen alle denkbare wagentjes in verschillende lokalen?',
          'Welk materiaal ligt er vandaag op tafel?'
        ]
        K.p(doc,'Omcirkel de geschikte SMART-vraag en leg bij elke andere keuze uit wat ontbreekt.')
        for letter,opt in zip('ABCD',opts):K.p(doc,letter+'. '+opt)
        K.invul(doc,regels=3)
        if teacher:K.modelantwoord(doc,'B: afgebakend tot één wagentje en één baanfase, x/t meetbaar, veilig met bekende 50 Hz-tijdtikker en spanning, uitvoerbaar en tijdsgebonden. A is onveilig en vaag; C is onhaalbaar; D onderzoekt geen fysisch verband.')
    else:
        K.p(doc,'Formuleer zelf één toetsbare vraag voor de proef die je nu gaat uitvoeren. '
                 'Schrijf O (wat verander je?), A (wat meet je?), C (wat blijft gelijk?) en hoe je meet. Eindig op “tijdens dit labo”.')
        K.tabel(doc,['Mijn onderzoeksvraag','S','M','A','R','T'],[['','','','','','']],size=8.5)
        K.invul(doc,regels=2)
        if teacher:K.modelantwoord(doc,lab['onderzoek'],label='Mogelijke vraag; pas aan per proef')


def build(doc,teacher):
    # Dezelfde inhoudsdata voeden leerling- en leerkrachtversie.
    from build import FIG_BEST,EXTRA_FIGS
    intro(doc,teacher)
    for idx,(n,parts,title) in enumerate(SHEETS,1):
        lab=LABOS[n-1]
        K.pagebreak(doc)
        K.h1(doc,f'LABO {idx:02d} – {title}')
        K.p(doc,'Naam: …………………………………………………   Klas: …………  Datum: ……/……/……  Groep: …………',size=9.5)
        K.kader(doc,'LEERPLANDOELEN',[lab['lp']],soort='lp',size=9)
        K.h2(doc,'O – ORIËNTEREN')
        K.p(doc,'Doel: '+clean(' / '.join(lab['delen'][j-1]['titel'] for j in parts)).replace('Deel 1 –','').replace('Deel 2 –','').replace('Deel 3 –',''),size=9.5)
        smart(doc,idx,lab,teacher)
        K.h2(doc,'V – VOORBEREIDEN')
        material=[clean(s) for s in lab['materiaal']]
        material += [clean(lab['delen'][j-1]['materiaal_deel']) for j in parts if lab['delen'][j-1].get('materiaal_deel')]
        material=list(dict.fromkeys(material))
        K.h3(doc,'Benodigdheden');K.bullets(doc,material,size=9.5)
        K.p(doc,'Theorie: '+THEORY[n]+'. Gebruik het actuele theoriedocument; dianummers veranderen.',size=9)
        K.kader(doc,'VEILIGHEID – laat de opstelling controleren',[clean(s) for s in lab['veiligheid']],soort='veilig',size=9)
        K.p(doc,'Hypothese (vóór de meting) en een korte verklaring:');K.invul(doc,regels=2)
        K.p(doc,'Schets de opstelling; noteer je variabelen, meetinstrumenten, aantal herhalingen en veilige grenzen:')
        K.invul(doc,regels=3)
        K.tabel(doc,['O – onafhankelijk','A – afhankelijk','C – constant','Meetwijze / eenheid'],[['','','','']],size=9)
        K.h2(doc,'U – UITVOEREN')
        for j in parts:
            p=lab['delen'][j-1]
            heading=clean(p['titel'])
            heading=re.sub(r'^Deel \d+\s*[–-]\s*', '',heading).replace('practicum:','').replace('OPEN :','')
            K.h3(doc,heading.strip(' –:'))
            images=EXTRA_FIGS.get((n,j),[])
            if not images and j==parts[0]:images=[FIG_BEST[n]]
            for fname,caption in images[:2]:
                # Geen herkomstetiketten bij een figuur. Alleen nuttige labels behouden.
                K.figuur(doc,fname,clean(caption.split('(bron:')[0].split('(schema naar')[0].strip(' .'))+'.',breedte_cm=7.8)
            if p.get('open_opdracht'):
                K.kader(doc,'OPEN ONDERZOEK – maak eerst je eigen werkplan',[clean(s) for s in p['open_opdracht']],soort='stem',size=9)
                K.p(doc,'Mijn werkwijze vóór de goedkeuring door de leerkracht:');K.invul(doc,regels=4)
            K.h3(doc,'Uitvoering')
            K.numbered(doc,[clean(s) for s in p['stappen']],size=9.5)
            if p.get('tabel_uitleg'):K.p(doc,clean(p['tabel_uitleg']),italic=True,color='1F4E79',size=9)
            K.h3(doc,'Metingen')
            K.tabel(doc,p['kop'],rows(p['kop'],p['rijen']),size=8.2)
            for extra in p.get('extra_tabellen',[]):
                K.p(doc,clean(extra['titel']),bold=True,size=9)
                K.tabel(doc,extra['kop'],rows(extra['kop'],extra['rijen']),size=8.2)
            for graph in p.get('grafieken',[]):K.p(doc,'Excel/grafiek: '+clean(graph),size=9.2,color='1F4E79')
            K.p(doc,'Verwerking: '+clean(p['verwerking']),size=9.2)
            K.p(doc,'Bewaar de ruwe data, de opstellingsschets en het papierbandje of de video:');K.invul(doc,regels=2)
            K.h2(doc,'R – REFLECTEREN')
            for qnum,q in enumerate(p.get('vragen',[]),1):
                K.vraag(doc,qnum,clean(q),size=9.5);K.invul(doc,regels=2)
                if teacher:K.modelantwoord(doc,clean(ANSWERS[f'L{n}:deel{j}:vraag{qnum}']))
            # Bij iedere deelproef een echt besluit vóór de volgende proef start.
            K.p(doc,'Besluit bij deze proef: toets je hypothese met concrete meetwaarden, grafiek en onzekerheid.')
            K.invul(doc,regels=3)
        K.kader(doc,'WAT WORDT BEOORDEELD?',[
            'Product (60 %): volledige ruwe meettabel, berekeningen, grafieken en besluit. Proces/attitude (40 %): voorbereiding, veilig werken, zelfstandig meten, samenwerken en opruimen.',
            'Bij een open onderzoek hoort het vooraf goedgekeurde eigen werkplan. De volledige rubric en het blanco verslagoverzicht staan achteraan.'
        ],soort='eval',size=9)
        if teacher:
            K.teacher_note(doc,['Gebruik het aanwezige schoolmateriaal; vervang de beproefde opstelling niet zonder bespreking.',
                                'Vergelijk cijferwaarden met de echte opstelling en bewaar het bewijs van de ruwe meting.'],title='LEERKRACHTENINFO')
    return doc
