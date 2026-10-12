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
from course_guidance import G, FORMULAS, SMART_EXAMPLES
from learning_targets import T

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


# Benodigdheden en veiligheidsinstructies horen bij het EIGEN werkblad,
# niet bij andere deelproeven uit hetzelfde (vroegere) themalabo.
SHEET_MATERIAL={
 (1,(1,)):['luchtbelbuis op houten lat met schaal 0–100 cm, gradenboog, stopwatch, statief en klem'],
 (1,(2,)):['elektrisch wagentje en schakelaar, rechte baan, 50 Hz-tijdtikker, carbonlint, papierbandje ca. 1,1 m, kleefband, voltmeter en passende gecontroleerde laagspanningsvoeding, meetlat, Excel'],
 (5,(1,2)):['wagentje 50 g, 4 × 50 g ballast, baan, katrol, vijf hangschijfjes van 10 g, touw, 50 Hz-tijdtikker en passende voeding, carbonlint, papierbandjes, meetlat en Excel'],
 (5,(3,)):['twee dynamometers (3 N/0,1 N), veer, plank of bestaand krachtenbord, kort touwtje, blad, gradenboog; haakjes/klemmen of docentdemo met spijkers en hamer'],
 (8,(1,)):['speelgoedtrein met spoor én platenspeler met twee krijtstreepjes op verschillende stralen; stopwatch, meetlat en werkblad; fietswiel met reflector uitsluitend optioneel'],
 (8,(2,)):['afgerond dikwandig glazen buisje ca. 20 cm, nylondraad ca. 90 cm, rubberstop, hangmassa’s 60/80/100/120/140 g, bestaande balans voor de stop, meetlat, stopwatch en veiligheidsbril'],
 (9,(1,)):['statief met klem, soepele en minder soepele veer, gewichtjes 30–150 g voor veer 1 en 50–250 g voor veer 2, meetlat, chronometer en Excel'],
 (9,(3,)):['statief, veer, veilige voldoende zware massa, carbonlint, 50 Hz elektromagnetische triller/tijdtikker met passende gecontroleerde laagspanningsvoeding, meetlat en Excel'],
 (9,(2,)):['statief en klem, veer met onbekende massa die blijft hangen (bijvoorbeeld een ijzeren kern), vier bekende massa’s van 50,0 g, chronometer, meetlat en Excel; géén balans'],
 (12,(1,)):['fysieke golfbak op overheadprojector, water, punt- en staafbron, schermpjes met openingen, meetlat, camera; bestaande golfbak-app alleen indien beschikbaar'],
 (12,(2,)):['bestaande trillingsbron met touw en statief, passende voeding, rolmeter'],
 (14,(1,)):['goedgekeurde laag-vermogenlaser met bundelstop, vier aanwezige roosters (80/100/300/600 lijnen/mm indien beschikbaar), roosterhouder, scherm, meetlat en Excel'],
 (14,(2,)):['intacte CD, veilige laser met bundelstop, scherm, meetlat en geodriehoek; bestaande houders en Excel'],
 (14,(3,)):['witlichtbron met gleuf en scherm, aanwezige roosters, eventueel kwikdamplamp uitsluitend door leerkracht, meetlat en Excel'],
}
SHEET_SAFETY={
 (8,(1,)):['Houd vingers, haren en kleding uit treinspoor, platenspeler en optioneel fietswiel. Laat de trein alleen rijden met de bestaande schoolvoeding; vraag toestemming vóór het wisselen van opstelling.'],
 (8,(2,)):['Controleer draad en rubberstop; draag bril en maak een ruime vrije draaicirkel. Draai nooit binnen bereik van anderen.',
             'Gebruik alleen veilige hangmassa’s en een gaaf glazen buisje met afgeronde randen; leerkracht controleert opstelling vooraf. Stop de rotatie vóór elke verandering van massa of straal.'],
 (9,(1,)):['Klem beide veren stevig, belast ze niet voorbij de toegestane grens; gebruik een opvangbak en kies kleine, beheersbare amplitudes.'],
 (9,(3,)):['Klem statief en veer; leerkracht controleert triller en passende lage voeding. Kies een massa die vrij op en neer kan bewegen; blijf weg van triller en vallende massa.'],
 (9,(2,)):['Maak de onbekende massa NIET van de veer los; controleer klem, veilige veerbelasting en een opvangbak. Gebruik geen balans in deze onderzoeksopdracht.'],
 (5,(1,2)):['Bevestig katrol en statief; houd gezicht en handen buiten de baan van wagen en hangmassa.',
              'Laat tijdtikker en lage voeding controleren; schakel de voeding uit bij bandwissel. Stop de wagen vóór de tafelrand.'],
 (5,(3,)):['Laat spijkers/hamer alleen door de leerkracht gebruiken; werk anders met de bestaande haakjes/klemmen.',
             'Blijf met beide dynamometers onder het aangegeven meetbereik.'],
 (14,(1,)):['Richt de laser beneden ooghoogte op een vaste bundelstop; kijk nooit in de directe of gereflecteerde bundel. Alleen aanwezige roosters gebruiken.'],
 (14,(2,)):['Gebruik een intacte CD. Kras of verwijder geen reflectielaag en kijk niet in de laserbundel; vang de bundel op het scherm op.'],
 (14,(3,)):['De leerkracht bedient een eventuele hete/UV-emitterende kwikdamplamp. Volg de afscherming en kijk niet in de lichtbron.'],
}
SHEET_SAFETY.update({
 (1,(1,)):['Fixeer de glazen luchtbelbuis op het statief; laat haar niet vallen.',
             'Volg bij elke stand dezelfde kant van de bel; meet herhaaldelijk en noteer de afleesnauwkeurigheid.'],
 (1,(2,)):['Laat de leerkracht de tijdtikker en de bijbehorende lage wisselspanning controleren; geen netspanning op de tijdtikker.',
             'Plaats een stootblok achter de baan. Schakel voeding uit vóór je carbonlint of bandje verschuift.'],
 (3,(1,)):['Zet opvangmat en vrije valzone klaar; niemand staat onder de vallende massa.',
             'Laat 50 Hz-triller, laagspanningsvoeding, bandje en hoog statief vóór loslaten controleren.'],
 (3,(2,3)):['Gebruik een tennisbal en houd de ruimte tussen bal en lamp/plafond vrij.',
                'Zet camera’s stabiel opzij; film uitsluitend de proef en respecteer de privacy van leerlingen. Leg de meetlat in hetzelfde vlak als de bal.'],
 (4,(1,)):['Laat de bal vanaf een lage, veilige tafel in een zachte opvangbak landen; niemand staat in de baan.',
             'Film opzij met een vaste camera en meetlat in het bewegingsvlak; laat je meetplan vooraf goedkeuren.'],
 (4,(2,)):['Gebruik een opvangbak en laat de plank, blokken en valgeul vooraf controleren.',
             'Gebruik weinig afwasbare verf op beschermpapier en ruim gemorste verf direct op.'],
 (12,(1,)):['Zet de waterbak stabiel neer; houd alle snoeren en stekkers droog en schakel de voeding uit voor je water toevoegt of schermpjes wisselt.',
              'Leerkracht controleert triller en geschikte voedingsspanning.'],
 (12,(2,)):['Leerkracht controleert touw, statief en passende voeding; houd handen uit de buurt van het trillende touw.',
              'Zet de voeding uit vóór je de spanning of de opstelling wijzigt.'],
})
TEACHER_NOTES={
 (8,(1,)):['Laat de trein minstens twintig rondjes stabiliseren. Wissel werkelijk naar de platenspeler en meet twee verschillende stralen. Het fietswiel is facultatief.'],
 (8,(2,)):['Weeg m van de stop vóór montage en let op twee uitgelijnde merktekens bij het draaien; r kan pas na stop veilig worden nagemeten.'],
 (9,(3,)):['De proef gebruikt CARBONLINT onder de 50 Hz-triller. Markeer evenwicht als y=0; onder is negatief. Schakel triller in vóór loslaten en bewaar het lint.'],
 (10,(1,2,3)):['T² tegen l: rico=4π²/g en g=4π²/rico. Let op: 2π/√g is uitsluitend de rico van T tegen √l.'],
 (11,(1,2)):['Lees de aandrijffrequentie af uit getelde omwentelingen van het excenter. Wacht bij elke verandering tot de stationaire amplitude bereikt is.'],
}


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
    # De 5BCW-referentie is didactische basis, maar niet de oude 16-laboinleiding.
    from course_intro import build as build_intro
    build_intro(doc,teacher,SHEETS)


def smart(doc, idx, lab, parts, teacher):
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
        if teacher:K.modelantwoord(doc,SMART_EXAMPLES[idx-1],label='Mogelijke SMART-vraag; niet vooraf uitdelen')


def build(doc,teacher):
    # Dezelfde inhoudsdata voeden leerling- en leerkrachtversie.
    from build import FIG_BEST,FIG_SHEET,EXTRA_FIGS
    intro(doc,teacher)
    for idx,(n,parts,title) in enumerate(SHEETS,1):
        lab=LABOS[n-1]
        K.pagebreak(doc)
        K.h1(doc,f'LABO {idx:02d} – {title}')
        guide=G[idx-1]
        target=T[idx-1]
        K.p(doc,'Naam: …………………………………………………   Klas: …………  Datum: ……/……/……  Groep: …………',size=9.5)
        K.p(doc,'Mate van sturing: '+guide.steering+'  ·  Werkwijze: OVUR',size=9,color='1F4E79')
        K.p(doc,'Rollen (wissel tijdens de meetreeks): opstelling/veiligheid ……………  meter ……………  notulist/verwerker ……………',size=9)
        K.h2(doc,'O – ORIËNTEREN')
        K.h3(doc,'Context')
        K.p(doc,guide.context,size=9.7)
        K.kader(doc,'LESDOELEN – na dit labo kan je …',
                [f'{i}. '+clean(g)[0].lower()+clean(g)[1:] for i,g in enumerate((*guide.goals,*target.additions),1)],soort='doel',size=9)
        K.kader(doc,'LEERPLANDOELEN – wat oefen je hier?',
                ['Fysica '+target.physics+': '+target.physics_meaning,
                 'STEM '+', '.join(f'{k} S' for k in target.stem)+': zichtbaar bewijs via je plan, metingen en besluit. '
                 'Zie de doelenmatrix in Deel 1; een code is geen automatisch behaald doel.'],soort='lp',size=8.8)
        K.p(doc,'CONTROLEER ZELF – hoe toon je deze lesdoelen aan?',bold=True,size=9)
        K.bullets(doc,list(target.checks),size=9)
        K.h3(doc,'DOELCHECK – toon je vier lesdoelen aan (geen extra punten)')
        K.p(doc,'Vul dit tijdens of na het meten in. Verwijs per nummer naar een meetrij, grafiek, ontwerp of besluit. De leerkracht noteert '
                'nog niet / op weg / aangetoond met één volgende stap; gebruik Bijlage G voor de zes STEM-doelen.',size=8.9)
        K.tabel(doc,['Lesdoel hierboven','Mijn vindplaats / meetgegeven','Status + feedback leerkracht'],
                [[str(i),'',''] for i in range(1,5)],widths=[1550,4400,3688],size=8.3)
        K.h3(doc,'Oriëntatievragen (vóór je begint)')
        for number,(question,answer) in enumerate(guide.prior,1):
            K.vraag(doc,number,question,size=9.3);K.invul(doc,regels=1)
            if teacher:K.modelantwoord(doc,answer)
        smart(doc,idx,lab,parts,teacher)
        K.h2(doc,'V – VOORBEREIDEN')
        material=SHEET_MATERIAL.get((n,parts))
        if material is None:
            material=[lab['delen'][j-1]['materiaal_deel'] for j in parts if lab['delen'][j-1].get('materiaal_deel')]
            if not material:material=lab['materiaal']
        material=list(dict.fromkeys(clean(item) for item in material))
        K.h3(doc,'Benodigdheden');K.bullets(doc,material,size=9.5)
        K.p(doc,'Thema uit de theorie: '+THEORY[n]+'.',size=9)
        K.kader(doc,'BEGRIPPEN EN MODEL – gebruik dit bij je hypothese',[guide.concept],soort='uitleg',size=9.2)
        if idx in FORMULAS:K.formule(doc,FORMULAS[idx])
        K.kader(doc,'VEILIGHEID – laat de opstelling controleren',
                [clean(s) for s in SHEET_SAFETY.get((n,parts),lab['veiligheid'])],soort='veilig',size=9)
        K.p(doc,'Hypothese (vóór de meting) en een korte verklaring:');K.invul(doc,regels=2)
        K.p(doc,'Schets de opstelling; noteer je variabelen, meetinstrumenten, aantal herhalingen en veilige grenzen:')
        K.invul(doc,regels=3)
        K.tabel(doc,['O – onafhankelijk','A – afhankelijk','C – constant','Meetwijze / eenheid'],[['','','','']],size=9)
        if idx==7:
            K.kader(doc,'STEM 4 S – ontwerp vóór de worp een VEILIGE opvangoplossing',[
                'Behoud de bestaande horizontale-worp- en Trackeropstelling. Bereken de voorspelde landingsafstand x≈v₀√(2h/g) '
                'met de gemeten tafelhoogte h en een veilige bovengrens voor v₀ die de leerkracht vooraf opgeeft of goedkeurt; maak twee schetsen van een plaats/breedte voor de bestaande zachte opvangbak.',
                'Kies een veiligheidsmarge voor de onzekerheid in v₀ en h. Leg de twee voorstellen en het opvangplan vóór de eerste worp aan de leerkracht voor; '
                'niemand mag in de baan staan. Gebruik later de originele videometing als test. Geen extra worp zonder docentakkoord.'
            ],soort='stem',size=8.9)
            K.tabel(doc,['Variant opvangbak','voorspelde x (m)','marge (m)','keuze en veiligheidsreden'],
                    [['A','','',''],['B','','','']],size=8.3)
        if idx==20:
            K.kader(doc,'STEM 5 S – maatschappelijke vraag: veilig geluid zonder buitensluiten',[
                'Een school overweegt rustplekken met passieve demping of actieve ruisonderdrukking. '
                'Wat geven de gemodelleerde niveaus 60, 70 en 80 dB je wel en niet over geluidsintensiteit?',
                'Vergelijk na de geluidsproef minstens twee oplossingen voor leerlingen én begeleiders: '
                'fysisch principe, technologie, kost/toegang of batterijgebruik, veiligheid en een beperking. '
                'Werk uitsluitend met de gegeven dB-voorbeelden; het offline geluidlab is GEEN dB-meter.'
            ],soort='stem',size=8.9)
        K.h2(doc,'U – UITVOEREN')
        for j in parts:
            p=lab['delen'][j-1]
            heading=clean(p['titel'])
            heading=re.sub(r'^Deel \d+\s*[–-]\s*', '',heading).replace('practicum:','').replace('OPEN :','')
            K.h3(doc,heading.strip(' –:'))
            images=EXTRA_FIGS.get((n,j),[])
            if not images and j==parts[0]:images=[FIG_SHEET.get(idx,FIG_BEST[n])]
            for fname,caption in images[:2]:
                # Geen herkomstetiketten bij een figuur. Alleen nuttige labels behouden.
                useful_caption=re.sub(r'\([^)]*(?:bron|schema naar|blz\.)[^)]*\)', '',caption,flags=re.I)
                K.figuur(doc,fname,clean(useful_caption).strip(' .')+'.',breedte_cm=7.8)
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
            K.p(doc,'Bewaar ruwe data en meetbewijs (bandje, schets, foto of video waar van toepassing):');K.invul(doc,regels=2)
        K.h2(doc,'R – REFLECTEREN')
        # Alle deelproeven worden eerst uitgevoerd. Daarna volgt één duidelijke
        # reflectiefase met afzonderlijke vragen en een deelbesluit per proef.
        for j in parts:
            p=lab['delen'][j-1]
            if len(parts)>1:
                K.h3(doc,'Deel '+str(j)+' – reflectie op '+clean(p['titel']).split('–',1)[-1].strip())
            for qnum,q in enumerate(p.get('vragen',[]),1):
                K.vraag(doc,qnum,clean(q),size=9.5);K.invul(doc,regels=2)
                if teacher:K.modelantwoord(doc,clean(ANSWERS[f'L{n}:deel{j}:vraag{qnum}']))
            K.p(doc,'Deelbesluit: toets je hypothese met je meetwaarden en grafiek; bespreek onzekerheid en een mogelijke verbetering.')
            K.invul(doc,regels=3)
        if len(parts)>1:
            K.p(doc,'Synthese: wat leren de deelproeven samen over de onderzoeksvraag?')
            K.invul(doc,regels=2)
        if idx==7:
            K.h3(doc,'STEM 4 S – test en verbeter je opvangontwerp')
            K.p(doc,'Gebruik de echte videowaarde van x, de spreiding en de getekende veiligheidsmarge om A en B te toetsen. '
                    'Welke variant werkte volgens het bewijs? Teken één bijgestuurde opvangpositie of -breedte. '
                    'Toets deze nieuwe variant aan DEZELFDE originele videodata en onzekerheid; een extra echte worp '
                    'mag uitsluitend als de leerkracht die veilig vindt. Bespreek waarom het model niet exact is.',size=9)
            K.tabel(doc,['gemeten x ± onzekerheid (m)','test A/B aan video','wijziging + reden','hertoets aan video'],
                    [['','','','']],size=8.4)
            K.invul(doc,regels=2)
            if teacher:K.modelantwoord(doc,'S4: x≈v₀√(2h/g); de opvangbak moet het interval van geschatte landingsplaatsen plus veiligheidsmarge omvatten. '
                'Vergelijk beide varianten met de ORIGINELE video, kies of vergroot/verplaats de bak en toets opnieuw aan het gemeten interval. '
                'Geen gefingeerde tweede worp; bij een afwijkend model parallax, v₀- of h-fout onderzoeken.',label='Modelantwoord STEM 4 S')
        if idx==20:
            K.h3(doc,'STEM 5 S – besluit over de geluidsuitdaging')
            K.p(doc,'Reken ΔL=10 log₁₀(I₂/I₁) om: +10 dB = 10× de intensiteit en +20 dB = 100×. '
                    'Vergelijk gegeven 60, 70 en 80 dB (géén metingen met deze app). '
                    'Maak een beargumenteerde keuze tussen twee maatregelen; benoem fysica van fase/absorptie, '
                    'technologie, wiskundig verschil, ten minste twee betrokkenen en een sociaal/duurzaam nadeel.',size=9)
            K.tabel(doc,['maatregel','natuurkundig bewijs','technologie / kosten / toegang','keuze + beperking'],
                    [['passieve demping','','',''],['actieve ruisonderdrukking','','','']],size=8.2)
            K.invul(doc,regels=2)
            if teacher:K.modelantwoord(doc,'70 dB betekent t.o.v. 60 dB een factor 10 in intensiteit, 80 dB factor 100; '
                'dit is GEEN uitspraak dat de toon 10× luider wordt ervaren. Passieve demping verbruikt weinig energie '
                'maar werkt niet bij alle frequenties; actieve tegenfase vraagt energie/elektronica en kan duur zijn. '
                'Weeg leerling, docent, kosten/toegang en afval/batterij tegen elkaar af, met beperking van de simulatie.',label='Modelantwoord STEM 5 S')
        if idx==25:
            K.h3(doc,'STEM 6 S – bewijs van de volledige onderzoekscyclus')
            K.p(doc,'Vul voor ieder van de zeven fasen de vindplaats in het goedgekeurde plan, de ruwe data '
                    'of de poster in. Een lege fase is nog geen behaald onderzoeksdoel.',size=9)
            K.tabel(doc,['Fase','Vindplaats / concreet bewijs','Mijn verbetering na feedback'],
                    [[f,'',''] for f in ('Oriëntatie','Vraag + hypothese','Onderzoeksmethode','Gegevensverzameling',
                                      'Analyse','Conclusie + onzekerheid','Rapportering / poster')],size=8)
            if teacher:K.modelantwoord(doc,'LPD 6 S #: kijk of elke fase aantoonbaar is en samenhangt met een gekozen '
                'fysica-inhoud. De poster bevat de vraag, gekende grenzen, vijf O-waarden, drie ruwe herhalingen '
                'per waarde, analyse, conclusie en open bespreking van afwijkingen.',label='Modelantwoord STEM 6 S')
        K.h3(doc,'Toepassen: wat zeggen jouw gegevens buiten dit labo?')
        K.p(doc,guide.transfer[0],size=9.4,bold=True);K.invul(doc,regels=2)
        if teacher:K.modelantwoord(doc,guide.transfer[1],label='Mogelijke toepassing')
        from review_data import PRODUCTBEWIJS, WERKBLAD_PDF
        bestand=('poster (PDF) én originele ruwe meetgegevens (Excel .xlsx of ingevuld datablad als PDF)' if idx==25 else
                 'ingevuld werkblad met schetsen/foto’s als één PDF' if idx in WERKBLAD_PDF else
                 'groepsverslag als Excel-bestand (.xlsx); voeg meetbewijs als foto/bijlage toe')
        K.kader(doc,'EVALUATIE EN INDIENEN – WAT, HOE EN WANNEER',[
            'WAT? '+PRODUCTBEWIJS[idx-1]+' In te dienen: '+bestand+'.',
            'HOE? Product = één groepspunt /10 (Bijlage B: vraag/plan 2, metingen/grafieken 3, besluit 3, verzorging/indienen 2) × 60 %. '
            'Proces = individueel punt /10 (10 thema’s, Bijlage C) × 40 %. Eindpunt = 0,60 × product + 0,40 × proces.',
            'WANNEER? Lever als groep één bestand per gevraagd type in via de Smartschool-uploadzone uiterlijk één week na het labo om 23.59 u. '
            'De leerkracht bevestigt de concrete lesdatum, uploadzone en welke schooltemplate gebruikt wordt; het beschikbare Excel-bestand heet CONCEPT.',
            'FEEDBACK: groepsproduct schriftelijk in het feedbackblok (of bij de werkblad-PDF/poster); proces individueel na observatie tijdens het labo. '
            'Peerfactor uitsluitend indien vooraf aangekondigd. Beantwoord ook de reflectievragen.',
            ('SPECIFIEK DOELBEWIJS: '+('STEM 4 S: beide ontwerpen, berekening, videotoets en bijsturing.' if idx==7 else
                                      'STEM 5 S: dB-berekening en onderbouwde maatschappelijke keuze.' if idx==20 else
                                      'STEM 6 S: zeven fasen met bewijs in plan, data en poster.' if idx==25 else
                                      'Toon de twee controlepunten bovenaan aan met je ruwe data en besluit.')+
             ' Dit telt binnen de bestaande /10-criteria, niet als extra punten.')
        ],soort='eval',size=8.9)
        if teacher:
            K.teacher_note(doc,['Gebruik het aanwezige schoolmateriaal; vervang de beproefde opstelling niet zonder bespreking.',
                                'Vergelijk cijferwaarden met de echte opstelling en bewaar het bewijs van de ruwe meting.',
                                'Formatieve tussenstop: '+target.checkpoint+' Noteer feedback bij de betreffende doelbewijzen; beoordeel pas het ingediende werk en de geobserveerde individuele bijdrage.']
                               +TEACHER_NOTES.get((n,parts),[]),title='LEERKRACHTENINFO')
    return doc
