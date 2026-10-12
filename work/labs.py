# -*- coding: utf-8 -*-
"""Bewerkbare inhoudsbron voor de 6BCW-werkbladen.

De modelantwoorden en leerkrachtaanwijzingen staan uitsluitend in answers.py.
De tweede waarde in vraagparen is leeg om het vragenformaat voor build.py te bewaren.
Bron: Labocursus 6BCW voorlopig.pdf, blz. 1–118 (didactisch herwerkt).
"""

LABOS = [{'nr': 1,
  'titel': 'EENPARIGE BEWEGING: LUCHTBEL EN WAGENTJE',
  'bron': '63–72',
  'theorie': '02 Beweging en kracht deel 1, blz. 22–51; 03 Beweging en kracht deel 2, blz. 1–4',
  'lp': 'LPD 13 F; LPD 1 S, 2 S, 3 S',
  'duur': 2,
  'sturing': 'GESLOTEN → BEGELEID: eerste meettabel gegeven; tweede meetbereik kies je zelf.',
  'type': 'meetpracticum (groep 2–3)',
  'context': 'Een lift beweegt soms een tijdje met bijna constante snelheid. Met een luchtbel en een '
             'elektrisch wagentje ga je na hoe je dat in een plaats-tijdgrafiek herkent. Je herhaalt '
             'daarbij de afspraken over meetgrafieken van vorig jaar.',
  'doelen': ['de plaats x van een luchtbel en een wagentje op bekende tijdstippen meten',
             'uit een x(t)-grafiek de gemiddelde snelheid v bepalen en het verband uitleggen',
             'meetpunten als losse kruisjes en een best passende rechte weergeven',
             'de tijdtikker veilig gebruiken en ruwe data volledig noteren'],
  'voor': [('Wat is het verschil tussen afgelegde weg en verplaatsing?', ''),
           ('Wat betekent de richtingscoëfficiënt van x(t)?', '')],
  'materiaal': ['luchtbelbuis met gekende schaal, statief en klem, stopwatch (0,01 s), meetlint (mm)',
                'elektrisch wagentje op rechte baan van ca. 1 m, tijdtikker (50 Hz), carbonlint, '
                'papieren bandje (ca. 1,2 m), kleefband, 6 V~ voeding volgens toestelplaatje',
                'laptop met Excel; alternatief: gsm-filmpje en meetlat'],
  'begrip': '**ERB**: eenparige rechtlijnige beweging: in gelijke tijden legt het voorwerp gelijke '
            'afstanden af. **Tijdtikker**: markeert om de 0,020 s een punt op het bandje bij 50 Hz. '
            '**Richtingscoëfficiënt**: stijging gedeeld door horizontale verandering.',
  'formule': 'v = \\\\frac{\\\\Delta x}{\\\\Delta t} \\\\quad [v] = \\\\text{m/s}',
  'veiligheid': ['Fixeer de luchtbelbuis; laat de glazen buis niet vallen.',
                 'Gebruik de 6 V-wisselspanningsvoeding alleen als de leerkracht de typeplaat van de '
                 'tijdtikker heeft gecontroleerd; netspanning nooit aan de tijdtikker.',
                 'Leg een stootblok achter de baan en zet de voeding uit vóór je het lint verlegt.',
                 'Meet minstens driemaal en noteer de resolutie van de stopwatch en lat.'],
  'onderzoek': 'Hoe hangen de plaats x van de luchtbel en van het wagentje af van de tijd t (0–0,6 s), '
               'gemeten met stopwatch en tijdtikker bij dezelfde baaninstelling, tijdens dit labo?',
  'variabelen': 'O = t; A = x (m); C = dezelfde helling/spanning en dezelfde plaatsnul; meet met '
                'stopwatch en tijdtikker.',
  'orientatie': [('Wat verwacht je voor de afstand tussen opeenvolgende tijdtikkerstippen bij een ERB?',
                  ''),
                 ('Waarom meet je dezelfde proef meer dan één keer?', '')],
  'delen': [{'titel': 'Deel 1 – Een luchtbel in een vloeistofbuis',
             'bron': '63–67',
             'vraag': 'Is x(t) een rechte lijn bij vaste helling van de buis?',
             'stappen': ['Bevestig de buis stevig op een kleine helling. Kies de eerste zichtbare '
                         'markering als x = 0.',
                         'Start de klok bij die markering; noteer de tijden op minstens zes '
                         'merktekens.',
                         'Herhaal drie keer met dezelfde helling. Bereken de gemiddelde tijd per '
                         'merkteken.',
                         'Maak in Excel een spreidingsgrafiek x(t) en bepaal de helling van de '
                         'trendlijn.'],
             'kop': ['x (m)', 't₁ (s)', 't₂ (s)', 't₃ (s)', 't̄ (s)'],
             'rijen': 6,
             'verwerking': 'Noteer de richtingscoëfficiënt v en vergelijk de afzonderlijke tijden met '
                           'het gemiddelde.',
             'figuur': None},
            {'titel': 'Deel 2 – Elektrisch wagentje en tijdtikker',
             'bron': '68–72',
             'vraag': 'Zijn de stippen op het bandje ongeveer even ver van elkaar?',
             'stappen': ['Laat de leerkracht de voeding controleren. Bevestig carbonlint en een recht '
                         'papieren bandje aan het wagentje.',
                         'Laat de tijdtikker kort draaien terwijl het wagentje over de baan rijdt.',
                         'Kies een nulpunt en meet minstens tien opeenvolgende stipplaatsen; tijd per '
                         'stip = 0,020 s.',
                         'Zet x(t) uit in Excel. Bereken de snelheid uit de helling en uit één Δx/Δt.'],
             'kop': ['stip', 't (s)', 'x (m)', 'Δx (m)', 'v (m/s)'],
             'rijen': 10,
             'verwerking': 'Vergelijk beide snelheden en verklaar een verschil door wrijving, '
                           'startfase of afleesfout.',
             'figuur': 'sch_helling_sensor.png'}],
  'stem': 'Ontwerp een manier om met enkel het bandje te testen of het wagentje aan het eind '
          'vertraagt: kies drie vensters van vijf stippen, geef je beslisregel en bewijs met getallen.',
  'reflectie': [('Hoe herken je een ERB in een x(t)-grafiek en op het bandje?', ''),
                ('Een wagentje legt 0,24 m af in 0,60 s. Bereken v.', ''),
                ('Zoek zelf een toepassing waarbij het meten van een bijna constante snelheid zinvol '
                 'is. Geef je bron. [Internet toegelaten: gewone zoekmachine zoals Google, bron '
                 'vermelden – geen AI-tool.]',
                 ''),
                ('Waardoor kan een scheve x(t)-trendlijn ontstaan bij een niet-perfecte ERB?', ''),
                ('Waarom verbind je de meetpunten niet in volgorde met lijntjes?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': False,
  'zelf': False,
  'mc': ['Hoe verandert de snelheid van een elektrisch wagentje als we de spanning verhogen tot 230 V '
         'tijdens dit labo?',
         'Hoe hangt x (m), afgelezen op de luchtbelbuis, af van t (0–0,6 s) bij vaste helling, en hoe '
         'hangt x van het wagentje af van t (0–0,6 s) bij dezelfde baaninstelling en 50 Hz-tijdtikker, '
         'tijdens dit labo?',
         'Hoe hangt de plaats af van de tijd, gemeten met verschillende buizen en wagentjes, tijdens '
         'dit labo?',
         'Hoe hangt de versnelling af van de kracht op het wagentje tijdens dit labo?']},
 {'nr': 2,
  'titel': 'VERSNELDE EN VERTRAAGDE BEWEGING: TIJDSTIPPEN EN GRAFIEKEN',
  'bron': '79–92',
  'theorie': '04 Beweging en kracht deel 3, EVRB/versnelling; 03 Beweging en kracht deel 2, x(t) en '
             'v(t)',
  'lp': 'LPD 13 F; LPD 1 S, 2 S, 3 S, 4 S',
  'duur': 2,
  'sturing': 'BEGELEID: kies zelf nulstip, vensterlengte en veilige baanhelling.',
  'type': 'meetpracticum met tijdtikker (groep 2–3)',
  'context': 'Een fiets op een helling versnelt omlaag en vertraagt omhoog. Je meet beide bewegingen '
             'met een tijdtikker en onderzoekt waarom de versnelling positief of negatief kan zijn.',
  'doelen': ['uit bandjes x(t) en v(t) berekenen',
             'de versnelling bepalen uit de helling van v(t)',
             'de nulstip kiezen en uitleggen waarom een beginsnelheid geen nulsnelheid is',
             'de baan veilig opbouwen en twee proeven met herhalingen uitvoeren'],
  'voor': [('Wat is een versnelling met negatief teken?', ''),
           ('Wat zegt een steeds grotere afstand tussen stippen?', '')],
  'materiaal': ['hellend vlak/ rechte baan (ca. 1 m), wagentje 50 g + ballast tot 200 g',
                'tijdtikker 50 Hz met 6 V~ voeding, carbonlint, 2 × bandje ca. 1,1 m, meetlat, '
                'kleefband',
                'blokken om helling te verhogen, vangblok, Excel'],
  'begrip': '**EVRB**: eenparig versnelde rechtlijnige beweging, met constante versnelling. '
            '**Ogenblikkelijke snelheid**: benaderd door Δx/Δt rond een gekozen tijdstip; vorig jaar '
            'leerde je de spreidingsgrafiek.',
  'formule': 'a = \\\\frac{\\\\Delta v}{\\\\Delta t} \\\\quad [a] = \\\\text{m/s^{2}}',
  'veiligheid': ['Wagentje mag niet van de tafel rijden: leg een vangblok klaar.',
                 'Controle door leerkracht vóór aansluiten; tijdtikker alleen op passende 6 '
                 'V~-voeding.',
                 'Vermijd vingers nabij bewegend lint en wielen; voeding UIT bij lintwissel.',
                 'Markeer gekozen nulstip en tel telkens dezelfde 0,040 s (twee tikintervallen).'],
  'onderzoek': 'Hoe hangt de snelheid v af van de tijd t tijdens een rit omlaag en een rit omhoog op '
               'dezelfde helling, bepaald uit 0,040 s-vensters van de tijdtikker, tijdens dit labo?',
  'variabelen': 'O = t; A = v (m/s); C = helling, massa, tijdtikkerfrequentie; twee '
                'bewegingsrichtingen afzonderlijk.',
  'orientatie': [("Waarom hoeft v niet nul te zijn op de stip die je 't = 0' noemt?", ''),
                 ('Hoe verwacht je de v(t)-lijn bij een constante versnelling?', '')],
  'delen': [{'titel': 'Deel 1 – Omlaag: EVRB met beginsnelheid',
             'bron': '79–85',
             'vraag': 'Is de versnelling ongeveer constant als het wagentje de helling afrijdt?',
             'stappen': ['Verzwaar het wagentje zoals in de bron (bv. 200 g), laat de helling '
                         'controleren.',
                         'Maak het lint vast en laat het wagentje rijden met de tijdtikker aan.',
                         'Kies een duidelijk zichtbare nulstip NA de dicht opeen liggende '
                         'startstippen; tel om de twee stippen.',
                         'Meet x (m), bereken v in vensters van 0,040 s en maak x(t) en v(t).'],
             'kop': ['stip', 't (s)', 'x (m)', 'Δx in 0,040 s (m)', "t' (s)", 'v (m/s)'],
             'rijen': 12,
             'verwerking': 'Lees a af uit de rico van v(t) en schat v₀ uit het snijpunt met de v-as.',
             'figuur': 'sch_helling_sensor.png'},
            {'titel': 'Deel 2 – Omhoog: eenparig vertraagd',
             'bron': '86–92',
             'vraag': 'Is v(t) ongeveer lineair dalend na het loslaten?',
             'stappen': ['Zet het wagentje onderaan, geef het een korte duw omhoog en laat los.',
                         'Gebruik enkel stippen NÁ het loslaten en VÓÓR het keerpunt.',
                         'Herhaal en vergelijk de rico van v(t) met deel 1 bij dezelfde baanhelling.',
                         'Noteer hoe de gekozen positieve richting het teken van v en a bepaalt.'],
             'kop': ['stip', 't (s)', 'x (m)', 'Δx (m)', "t' (s)", 'v (m/s)'],
             'rijen': 10,
             'verwerking': 'Vergelijk de grootte van de versnellingen; verklaar verschil door '
                           'wrijving.',
             'figuur': None}],
  'stem': 'Ontwerp een controle of wrijving meetbaar is: vergelijk |a| omhoog en omlaag bij dezelfde '
          'helling. Formuleer vooraf welk resultaat wrijvingsloos zou zijn en noteer minstens 3 '
          'herhalingen.',
  'reflectie': [('Wat betekent de rico van v(t)?', ''),
                ('Een wagentje gaat van 0,8 naar 0,2 m/s in 0,30 s. Bereken a.', ''),
                ('Noem zelf een techniek die bewust vertraagt. Geef je bron. [Internet toegelaten: '
                 'gewone zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waarom zijn de versnellingen omhoog en omlaag niet precies tegengesteld?', ''),
                ('Is x(t) bij een EVRB een rechte of een kromme?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': False,
  'zelf': True,
  'mc': None},
 {'nr': 3,
  'titel': 'VRIJE VAL EN VERTICALE WORP: HOE GROOT IS g?',
  'bron': '20–26; 73–78; 15–20; 58–61 (dubbele versies)',
  'theorie': '04 Beweging en kracht deel 3 (valbeweging), blz. 1–81; 06 Gravitatie versus '
             'zwaartekracht, blz. 33–35',
  'lp': 'LPD 13 F, 16 F; LPD 1 S, 2 S, 3 S',
  'duur': 3,
  'sturing': 'BEGELEID: bronprocedures gecombineerd; kies zelf nulhoogte, camerastandpunt en '
             'meetvenster.',
  'type': 'meetlabo (tijdtikker + Tracker; groep 2–3)',
  'context': 'Een bal die omhoog wordt geworpen vertraagt eerst, staat heel even stil en valt dan '
             'terug. Een vallend gewicht en een bal leveren twee manieren om dezelfde valversnelling g '
             'te bepalen. We voegen de twee dubbele bronversies per proef samen.',
  'doelen': ['g uit de rico van v(t) bij vrije val bepalen',
             'de maximale hoogte en tijd van een verticale worp berekenen en met Tracker toetsen',
             'een coördinatenstelsel en referentiehoogte consequent gebruiken',
             'vallende voorwerpen opvangen en data veilig filmen'],
  'voor': [('Wat is het teken van a tijdens de hele verticale worp als omhoog positief is?', ''),
           ('Wat is v op het hoogste punt?', '')],
  'materiaal': ['elektromagnetische triller 50 Hz + passende voeding, papierbandje ca. 1,5 m, 50 g '
                'massa, statief, klemmen, meetlat, kleefband, zachte valmat',
                'tennisbal, 2 meetlatten verticaal, smartphone(s) op statief met hoge beeldfrequentie, '
                'laptop met Tracker, Excel'],
  'begrip': '**Valversnelling g**: de versnelling door zwaartekracht nabij het aardoppervlak is '
            'ongeveer 9,81 m/s². **Tracker**: gratis videoprogramma waarmee je de positie frame voor '
            'frame volgt; kalibreren met een meetlat in hetzelfde vlak.',
  'formule': 'y(t) = y_0 + v_0 t - \\\\frac{1}{2}g t^{2} \\\\quad [g] = \\\\text{m/s^{2}}',
  'veiligheid': ['Zet zachte mat neer, zorg voor vrije valzone, nooit onder het gewicht staan.',
                 'Laat triller, voeding en statief door leerkracht controleren vóór loslaten.',
                 'Film op statief opzij, niet van onder; vraag toestemming als leerlingen in beeld '
                 'komen; deel alleen het gemeten fragment.',
                 'Breng de bal nooit naar een lamp/plafond en kies een worphoogte die in het lokaal '
                 'past.'],
  'onderzoek': 'Hoe verandert v (m/s) met t (s) van een vrijvallende massa en van een omhoog geworpen '
               'tennisbal, bepaald met tijdtikker en Tracker bij dezelfde lokale g, tijdens dit labo?',
  'variabelen': 'O = t; A = v; C = plaats op aarde, valrichting/assenstelsel per deel; twee '
                'meetmethoden apart.',
  'orientatie': [('Waarom geeft de v(t)-helling van de worp een negatieve waarde als omhoog positief '
                  'is?',
                  ''),
                 ('Hoe bepaal je een schaal in Tracker?', '')],
  'delen': [{'titel': 'Deel 1 – Vrije val met een triller',
             'bron': '20–26 en 73–78',
             'vraag': 'Is a constant en in grootte gelijk aan g?',
             'stappen': ['Klem de triller aan het statief, bevestig ca. 50 g onder aan het '
                         'papierbandje en plaats een valmat.',
                         'Laat de triller eerst aanlopen; laat de massa zonder duw vallen en vang op.',
                         'Kies stip 0 op het bandje; noteer x bij minstens 8 stippen, elke stip 0,020 '
                         's.',
                         'Bereken v in de vensters van 0,020 s op de middentijden; teken x(t) en '
                         'v(t).'],
             'kop': ['stip', 't (s)', 'x (m)', 'Δx in 0,020 s (m)', "t' (s)", 'v (m/s)'],
             'rijen': 9,
             'verwerking': 'g = |rico v(t)|; vergelijk met 9,81 m/s² en bereken percentuele afwijking.',
             'figuur': 'sch_valproef.png'},
            {'titel': 'Deel 2 – Verticale worp met videoanalyse',
             'bron': '15–20 en 58–61',
             'vraag': "Wat zijn v₀ en de maximale hoogte y' bij een worp omhoog?",
             'stappen': ['Zet meetlat in hetzelfde vlak als de tennisbal, camera op statief en kies '
                         'vloer als y = 0.',
                         'Werp de bal recht omhoog, blijf met camera opzij, neem meerdere clips op.',
                         'Laad in Tracker; kalibreer, kies een oorsprong en markeer de bal per frame.',
                         "Exporteer de y(t)-tabel naar Excel; zet y(t) en v(t) uit en bepaal v₀ en y' "
                         'via berekening.'],
             'kop': ['frame', 't (s)', 'y (m)', 'vᵧ (m/s)'],
             'rijen': 10,
             'verwerking': "Bereken t' = v₀/g en y' = y₀ + v₀²/(2g); vergelijk met de top in de film.",
             'figuur': None}],
  'stem': 'Ontwerp een tweede meetmethode voor de worphoogte zonder Tracker '
          '(stopwatch/toppunt/meetlat). Leg uit welke methode nauwkeuriger is en vergelijk drie '
          'herhalingen.',
  'reflectie': [('Waarom is g niet nul in het hoogste punt?', ''),
                ('Een bal heeft v₀ = 3,0 m/s. Hoelang tot de top?', ''),
                ('Zoek een toepassing van videoanalyse buiten school. Geef je bron. [Internet '
                 'toegelaten: gewone zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waardoor zijn de twee waarden voor g verschillend?', ''),
                ('Welke topmeting hangt van een goede keuze van de referentiehoogte af?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': True,
  'zelf': False,
  'mc': None},
 {'nr': 4,
  'titel': 'TWEE DIMENSIES: HORIZONTALE WORP EN PARABOOLBAAN',
  'bron': '56–57; 93–97',
  'theorie': '04 Beweging en kracht deel 3 (horizontale worp); 09 Eenparig cirkelvormige beweging, '
             'verschil met kromme baan',
  'lp': 'LPD 14 F, 13 F; LPD 1 S, 2 S, 4 S',
  'duur': 2,
  'sturing': 'BEGELEID → OPEN: kies camerastandpunt, metingen en tabel zelf.',
  'type': 'onderzoekspracticum (video en spoor op hellende plaat)',
  'context': 'Een bal die horizontaal van een tafel vertrekt, valt terwijl hij vooruit beweegt. Op een '
             'schuine plank laat een metalen kogel een zichtbare parabool achter. Je onderzoekt of '
             'beide proeven hetzelfde model ondersteunen.',
  'doelen': ['x(t) en y(t) bij een horizontale worp scheiden',
             'de reikwijdte uit valtijd en v₀ berekenen',
             'uit het verfspoor het parabolische karakter herkennen',
             'een veilige eigen filmopstelling ontwerpen en goedkeuren'],
  'voor': [('Hoe verandert vₓ zonder merkbare luchtweerstand?', ''),
           ('Hoe verandert y als een voorwerp zonder beginsnelheid in y valt?', '')],
  'materiaal': ['tennisbal, smartphone met Tracker, statief, meetlat, lage tafel en zachte opvangbak',
                'tekenplank ca. 45 × 55 cm, blokken, valgeul, grote metalen kogel, groot papier, '
                'waterafwasbare verf, lat en geodriehoek, opvangbak'],
  'begrip': '**Onafhankelijkheidsbeginsel**: de beweging horizontaal en verticaal kun je apart '
            'bekijken. Horizontaal bij v₀ constant is x = v₀t; verticaal is de valafstand y = ½gt².',
  'formule': 'x = v_0 t \\\\quad ; \\\\quad y = \\\\frac{1}{2}g t^{2} \\\\quad [x]=[y]=\\\\text{m}',
  'veiligheid': ['Gebruik een lage tafel en een opvangbak; niemand in het schietvlak.',
                 'Verf alleen op beschermpapier; veeg gemorste verf direct op.',
                 'Filmcamera zijwaarts en waterpas; meetlat in het vlak van de baan.',
                 'Laat de kogelvalgeul en de helling eerst door de leerkracht controleren.'],
  'onderzoek': 'Hoe hangen x en de valafstand y van de tijd af bij een horizontale worp vanaf vaste '
               'hoogte, gemeten met Tracker en met een kogelspoor op een gelijkblijvend hellende '
               'plaat, tijdens dit labo?',
  'variabelen': 'O = t en/of x; A = y (en x); C = hoogte, startplaats, plaathelling; twee methoden '
                'onafhankelijk.',
  'orientatie': [('Een bal rolt horizontaal van de tafel: is zijn valtijd afhankelijk van v₀?', ''),
                 ('Welke relatie tussen y en x verwacht je?', '')],
  'delen': [{'titel': 'Deel 1 – Horizontale worp met Tracker',
             'bron': '56–57',
             'vraag': 'Is vₓ constant en aᵧ ≈ g?',
             'stappen': ['Ontwerp een opstelling en laat camerahoek en veilige opvang goedkeuren.',
                         'Film de worp met een meetlat in het bewegingsvlak; geef de bal geen '
                         'verticale duw.',
                         'Kalibreer in Tracker en meet minstens acht frames: t, x en y (richting '
                         'vooraf kiezen).',
                         'Maak x(t), y(t) en y(x); pas een passend model toe.'],
             'kop': ['frame', 't (s)', 'x (m)', 'y (m)', 'y/x² (1/m)'],
             'rijen': 8,
             'verwerking': 'Leid vₓ uit x(t) en g uit y(t); bespreek afwijking.',
             'figuur': 'sch_worp.png'},
            {'titel': 'Deel 2 – Parabool op een schuine plaat',
             'bron': '93–97',
             'vraag': 'Wordt het geverfde kogelspoor bij gelijke plankhelling parabolisch?',
             'stappen': ['Kleef het papier vlak op de plaat en zet de valgeul evenwijdig met de '
                         'bovenrand.',
                         'Laat de kogel met een kleine hoeveelheid verf vanuit dezelfde starthoogte '
                         'rollen.',
                         'Herhaal voor drie plankhellingen; houd de startsnelheid binnen elke reeks '
                         'gelijk.',
                         'Leg een x- en y-as door het startpunt; meet x, y voor minstens zes punten '
                         'per spoor.'],
             'kop': ['helling (°)', 'x (cm)', 'y (cm)', 'x² (cm²)'],
             'rijen': 6,
             'verwerking': 'Zet y uit tegen x²; lineair verloop duidt op een parabool. Vermeld '
                           'rolwrijving en variërende v₀.',
             'figuur': None}],
  'stem': 'Ontwerp een eenvoudige instelbare uitwerper met karton en een elastiek: minstens drie '
          'starthoogten, één vaste valhoogte, test de reikwijdte; bewijs met foto/schema en een tabel.',
  'reflectie': [('Waarom is de baan een parabool?', ''),
                ('Bereken de valtijd vanaf 0,80 m hoogte.', ''),
                ('Zoek zelf een toepassing van de horizontale worp in techniek of sport. [Internet '
                 'toegelaten: gewone zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Welke systematische fout veroorzaakt een scheve camera?', ''),
                ('Waarom mag je de twee experimenten niet zonder meer numeriek vergelijken?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': False,
  'zelf': True,
  'mc': None},
 {'nr': 5,
  'titel': 'KRACHTEN EN VERSNELLING: NEWTON TESTEN',
  'bron': '97–105',
  'theorie': '05 Derde wet van Newton, blz. 3–15; 04 Beweging en kracht deel 3; leerplan 12 F',
  'lp': 'LPD 12 F, 13 F; LPD 1 S, 2 S, 3 S, 4 S',
  'duur': 2,
  'sturing': 'BEGELEID: vaste opstelling, keuze van herhalingen en verwerking zelf.',
  'type': 'meetlabo plus krachtenconstructie',
  'context': 'De aandrijving van een voertuig hangt af van de resulterende kracht én van de totale '
             'massa. Naast een wagentje gebruik je twee dynamometers om te zien hoe krachten als '
             'pijlen worden samengevoegd.',
  'doelen': ['a(F) bij vaste totale massa en a(m) bij vaste kracht meten',
             'de tweede wet Fᵣ = ma toetsen met een grafiek',
             'de resultante van twee krachten construeren en meten',
             'de volledige bewegende massa correct tellen en veilig samenwerken'],
  'voor': [("Wat betekent 'resulterende kracht'?", ''),
           ('Waarom behoort de hangmassa ook tot de bewegende massa?', '')],
  'materiaal': ['wagentje 50 g + 4 × 50 g ballast, baan, katrol, 5 × 10 g hangschijfjes, touw',
                'tijdtikker 50 Hz, passende voeding, carbonlint, papierbandje en meetlat',
                'plank, 3 spijkers, hamer/tang (uitsluitend door leerkracht), veer, kort touwtje, twee '
                'dynamometers 3 N/0,1 N, blad papier, gradenboog',
                'Excel, veiligheidsbril bij eventuele spijkerdemonstratie'],
  'begrip': '**Tweede wet van Newton**: de versnelling wijst in de richting van de nettokracht. '
            '**Parallellogramregel**: krachten (pijlen) op hetzelfde voorwerp tel je vectorieel op, '
            'niet enkel als getallen.',
  'formule': 'F_{r} = m_{tot} a \\\\quad [F_r]=\\\\text{N}',
  'veiligheid': ['Katrol en statief vast; hand en gezicht buiten de baan van hangmassa en wagentje.',
                 'Laat leerkracht de tijdtikker en voeding controleren; passend lage spanning volgens '
                 'typeplaat.',
                 'Spijkers en hamer alleen onder toezicht; alternatief: bestaande haakjes/klemmen op '
                 'een krachtenbord.',
                 'Begin dynamometers op grootste bereik en blijf onder 3 N.'],
  'onderzoek': 'Hoe hangt de versnelling a van wagentje en hangmassa af van de aandrijfkracht F (2–5 '
               'schijfjes van 10 g) bij vaste totale massa, en van de totale massa m bij twee vaste '
               'schijfjes, gemeten met tijdtikker tijdens dit labo?',
  'variabelen': 'O = F dan m_tot; A = a uit v(t); C = m_tot bij a(F), F bij a(m), baanhelling en '
                'katrol.',
  'orientatie': [('Welke grafiek geeft bij de tweede wet een rechte door de oorsprong?', ''),
                 ('Welke twee grootheden hebben richting?', '')],
  'delen': [{'titel': 'Deel 1 – Versnelling bij veranderende kracht',
             'bron': '97–99',
             'vraag': 'Geldt a ∝ Fᵣ als m_tot gelijk blijft?',
             'stappen': ['Houd m_tot gelijk: verplaats schijfjes van het wagentje naar de hangzijde in '
                         'plaats van er massa bij te zetten.',
                         'Neem voor 2, 3, 4, 5 schijfjes een tijdtikkerbandje op en bereken a uit '
                         'v(t).',
                         'Meet elke situatie minstens twee keer, kies een constante versnelfase.',
                         'Maak a(F) en bepaal m_tot uit de rico als wrijving klein is.'],
             'kop': ['schijfjes n',
                     'F_aandrijf (N)',
                     'm_tot (kg)',
                     'a₁ (m/s²)',
                     'a₂ (m/s²)',
                     'ā (m/s²)'],
             'rijen': 4,
             'verwerking': 'Vergelijk 1/rico van a(F) met de gewogen totale massa.',
             'figuur': 'sch_kracht_wagentje.png'},
            {'titel': 'Deel 2 – Versnelling bij veranderende massa',
             'bron': '98–102',
             'vraag': 'Geldt a ∝ 1/m_tot bij vaste aandrijfkracht?',
             'stappen': ['Laat precies twee schijfjes aan de hangzijde.',
                         'Voeg achtereenvolgens 50, 100, 150 en 200 g ballast op het wagentje toe.',
                         'Neem per massa een bandje op; bereken a en zet a tegen 1/m_tot uit.',
                         'Bewaar één bandje met stip/t/x/Δx/v-tabel als rekenvoorbeeld.'],
             'kop': ['ballast (g)', 'm_tot (kg)', '1/m_tot (1/kg)', 'F (N)', 'a (m/s²)'],
             'rijen': 4,
             'verwerking': 'De rico van a(1/m_tot) benadert de resulterende kracht.',
             'figuur': None},
            {'titel': 'Deel 3 – Resultante van twee krachten',
             'bron': '102–105',
             'vraag': 'Is de gemeten resultante gelijk aan de diagonaal van het '
                      'krachtenparallellogram?',
             'stappen': ['Bevestig de veer aan een veilig krachtenbord of door leerkracht aangebrachte '
                         'haken.',
                         'Breng twee dynamometers onder verschillende hoeken aan; noteer grootte en '
                         'hoek van beide krachten.',
                         'Teken pijlen op schaal en construeer de diagonaal; meet daarna met één '
                         'dynamometer de kracht die dezelfde uitrekking geeft.',
                         'Vergelijk de constructie met de enkele gemeten kracht.'],
             'kop': ['F₁ (N)', 'F₂ (N)', 'hoek (°)', 'Fᵣ,tekening (N)', 'Fᵣ,gemeten (N)'],
             'rijen': 3,
             'verwerking': 'Grootte én richting vergelijken; krachten in een vector zijn niet altijd '
                           'optelbare getallen.',
             'figuur': None}],
  'stem': 'Ontwerp een wagentje dat bij een extra 50 g ballast toch dezelfde versnelling behoudt: kies '
          'de aangepaste hangmassa, test met tijdtikker en toon je voorspelling plus meetbewijs.',
  'reflectie': [('Waarom verandert de versnelling als F gelijk blijft en m stijgt?', ''),
                ('Een netto kracht van 0,40 N versnelt 0,20 kg. Bereken a.', ''),
                ('Zoek zelf een toepassing waarin massa en kracht beide van belang zijn. [Internet '
                 'toegelaten: gewone zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waarom klopt F = m·a niet exact met de hanggewichtskracht?', ''),
                ('Wanneer is Fᵣ numeriek gelijk aan F₁ + F₂?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': True,
  'zelf': False,
  'mc': None},
 {'nr': 6,
  'titel': 'ARBEID EN ENERGIE: DEZELFDE HOOGTE VIA TWEE WEGEN',
  'bron': '106–108',
  'theorie': '07 Arbeid en Energie deel 1, blz. 4–16; 08 Arbeid en Energie deel 2, blz. 4–23',
  'lp': 'LPD 17 F; LPD 1 S, 2 S, 4 S, 5 S',
  'duur': 2,
  'sturing': 'BEGELEID: vaste hoeken, eigen herhalingen en energiebalans.',
  'type': 'meetpracticum met dynamometer',
  'context': 'Met een hellend vlak kost het minder kracht om een wagentje op dezelfde hoogte te '
             'krijgen, maar je legt een langere afstand af. Onderzoek of de arbeid gelijk blijft en '
             'wat wrijving ermee doet.',
  'doelen': ['kracht en afgelegde weg bij drie hellingshoeken meten',
             'F·s en ΔE_z = mgh voor dezelfde hoogte vergelijken',
             'de invloed van wrijving uit een energiebalans schatten',
             'veilig en met constante snelheid aan de dynamometer trekken'],
  'voor': [('Wat is de eenheid van arbeid?', ''),
           ('Waarom neem je dezelfde eindhoogte voor alle routes?', '')],
  'materiaal': ['hellend vlak ca. 40 cm, statiefmateriaal, wagentje ca. 100 g, touw',
                'dynamometer 1 N/0,02 N (controleer bereik versus m·g), lat, gradenboog, blokken voor '
                '30°, 45°, 60°, balans',
                'Excel'],
  'begrip': '**Arbeid**: energieoverdracht door kracht over een verplaatsing, W = F·s bij kracht in '
            'bewegingsrichting. **Zwaarte-energie**: E_z = mgh t.o.v. gekozen referentiehoogte. '
            'Wrijving zet een deel om in warmte.',
  'formule': 'W = F s \\\\quad ; \\\\quad \\\\Delta E_z = mgh \\\\quad [W]=\\\\text{J}',
  'veiligheid': ['Stel hoeken enkel in met een vastgeklemde baan; laat controleren vóór wagentje '
                 'vertrekt.',
                 'Een dynamometer met 1 N-bereik is mogelijk te klein voor 100 g plus wrijving; '
                 'vergelijk met m·g en vervang zo nodig door 3 N-toestel.',
                 'Laat wagentje niet van baan rijden; vangstop bij het einde.',
                 'Trek langzaam met constante snelheid; herhaal elke meting drie keer.'],
  'onderzoek': 'Hoe hangen de benodigde kracht F en afgelegde afstand s af van de hellingshoek (30°, '
               '45°, 60°) bij dezelfde eindhoogte h, gemeten met dynamometer en lat tijdens dit labo?',
  'variabelen': 'O = hoek α; A = F, s en W = F·s; C = wagentje, eindhoogte, snelheid ongeveer '
                'constant.',
  'orientatie': [('Is de zwaarte-energie op dezelfde hoogte afhankelijk van de gekozen weg?', ''),
                 ('Wat doet wrijving met de benodigde arbeid?', '')],
  'delen': [{'titel': 'Deel 1 – Recht omhoog en langs de helling',
             'bron': '106–108',
             'vraag': 'Kan een kleinere kracht over een grotere afstand dezelfde stijging van E_z '
                      'geven?',
             'stappen': ['Weeg het wagentje en bepaal F_z = mg.',
                         'Kies één haalbare vaste eindhoogte h voor alle drie hoeken en meet de '
                         'verticale route.',
                         'Meet bij 30°, 45° en 60° de afstand langs de baan en de kracht bij traag '
                         'trekken.',
                         'Bereken W_vert = F_vert·h en W_hel = F_hel·s; vergelijk met mgh.'],
             'kop': ['α (°)',
                     'h (m)',
                     'F_vert (N)',
                     's_hel (m)',
                     'F_hel (N)',
                     'W_vert (J)',
                     'W_hel (J)'],
             'rijen': ['30', '45', '60'],
             'verwerking': 'Maak W(α) en F(α). Bespreek waarom W_hel niet exact gelijk aan W_vert is.',
             'figuur': 'sch_wrijving.png'}],
  'stem': 'Ontwerp een baan met karton en lat waarbij dezelfde hoogte met zo klein mogelijke maximale '
          'trekkracht wordt bereikt. Bouw hem, test drie keer en noteer een foto en W; grens: baan '
          'stevig en binnen tafel.',
  'reflectie': [('Waarom is de kracht langs een flauwe helling kleiner?', ''),
                ('Een wagentje van 0,10 kg stijgt 0,20 m. Bereken ΔE_z.', ''),
                ('Zoek zelf een toepassing van een hellend vlak. [Internet toegelaten: gewone '
                 'zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Welk meetverschil verwacht je als je sneller trekt?', ''),
                ('Waarom kun je F·s niet altijd gebruiken zonder hoek?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': False,
  'zelf': True,
  'mc': None},
 {'nr': 7,
  'titel': 'DRAAIEN MET KRACHTEN: MOMENT EN HEFBOMEN',
  'bron': '109–117',
  'theorie': '09 Eenparig cirkelvormige beweging (rotatie als voortraject); verrijking buiten '
             'expliciete kern-LPD 12–23 F',
  'lp': 'LPD 12 F (kwalitatieve dynamica, verrijking); LPD 1 S, 2 S, 4 S',
  'duur': 2,
  'sturing': 'BEGELEID: bronopstelling gegeven; ontwerp hefboomtoepassing zelf.',
  'type': 'verdiepingspracticum (groep 2–3)',
  'context': 'Een deurklink zit ver van het scharnier: dezelfde draaibeweging vraagt dan minder '
             'kracht. Deze twee bronproeven over moment en hefboom zijn opgenomen als **verdieping**: '
             'het leerplan noemt ze niet als afzonderlijk verplicht fysica-LPD voor 6BCW.',
  'doelen': ['een krachtarm loodrecht op de werklijn van een kracht bepalen',
             'F·d bij verschillende aangrijpingspunten vergelijken',
             'de hefboomvoorwaarde Fₗdₗ = Fₘdₘ met metingen testen',
             'een veilige hefboom bouwen en het nut kritisch beoordelen'],
  'voor': [('Wat is de krachtarm van een deurklink?', ''),
           ('Waarom moet een statief vrij kunnen draaien?', '')],
  'materiaal': ['licht statief met draaipunt, dynamometer 3 N/0,1 N, lat, papieren tape',
                'hefboomstang, steunpunt/klem, haakje, gewichtjes, meetlint, balans',
                "opvangbak voor vallende massa's, Excel"],
  'begrip': '**Krachtmoment**: draaieffect van een kracht rond een as. **Hefboom**: stijve staaf met '
            'draaipunt; in evenwicht zijn de tegengestelde momenten even groot.',
  'formule': 'M = F d \\\\quad [M]=\\\\text{N\\\\cdot m}',
  'veiligheid': ['Klem het steunpunt maar niet de draaibare stang; laat controleren.',
                 'Geen gezicht boven gewichtjes en vangstop plaatsen.',
                 'Dynamometer niet hoger belasten dan 3 N.',
                 'Gebruik geen hamer of spijkers voor deze proef; werk met bestaand statiefmateriaal.'],
  'onderzoek': 'Hoe hangen de benodigde trekkracht F en de arm d (0,15–0,50 m) samen om een statief in '
               'evenwicht te houden en hoe verdelen last en macht zich bij drie typen hefboom, gemeten '
               'met dynamometer en lat tijdens dit labo?',
  'variabelen': 'O = arm d en plaats steunpunt/last/macht; A = F; C = dezelfde last, hetzelfde '
                'draaipunt per reeks.',
  'orientatie': [('Is een langere arm gunstig als je kracht wilt besparen?', ''),
                 ('Is het draaipunt onderdeel van de krachtarm?', '')],
  'delen': [{'titel': 'Deel 1 – Moment met een statiefje',
             'bron': '109–112',
             'vraag': 'Blijft F·d ongeveer constant als het statief horizontaal blijft?',
             'stappen': ['Meet de afstand van het draaipunt tot minstens acht markeringen langs de '
                         'statiefarm.',
                         'Houd het statief horizontaal en trek met de dynamometer loodrecht op de arm.',
                         'Noteer F bij elk d (start op 0,50 m en verklein in stappen van 0,05 m).',
                         'Maak F(d) en F(1/d); vergelijk het product F·d.'],
             'kop': ['d (m)', '1/d (1/m)', 'F (N)', 'M = F·d (N·m)'],
             'rijen': ['0,50', '0,45', '0,40', '0,35', '0,30', '0,25', '0,20', '0,15'],
             'verwerking': 'F(1/d) is een rechte bij vast moment; verklaar afwijking door massa van de '
                           'stang.',
             'figuur': None},
            {'titel': 'Deel 2 – Drie soorten hefboom',
             'bron': '113–117',
             'vraag': 'Wanneer is de hefboom in evenwicht en wanneer bespaar je kracht?',
             'stappen': ['Bouw één opstelling met tussenstandig steunpunt; meet Fₗ, Fₘ, dₗ en dₘ voor '
                         'vijf posities.',
                         'Herhaal met tussenstandige last en daarna met tussenstandige macht (laatste '
                         'kwalitatief).',
                         'Duid in elk schema de vier grootheden aan en bepaal per geval welk type '
                         'gunstig is.',
                         'Vergelijk de producten Fₗdₗ en Fₘdₘ.'],
             'kop': ['type', 'Fₗ (N)', 'dₗ (m)', 'Fₘ (N)', 'dₘ (m)', 'Fₗdₗ (N·m)', 'Fₘdₘ (N·m)'],
             'rijen': 5,
             'verwerking': 'Maak een schema van elk type met krachtpijlen en draaipunt.',
             'figuur': None}],
  'stem': 'Ontwerp en bouw met een lat, steunpunt en last een hefboom die een 1 N-last met maximaal '
          '0,5 N optilt. Toon schema, gemeten armen/krachten, foto van test en besluit; laat '
          'veiligheidscontrole doen.',
  'reflectie': [('Waarom kun je met een langere arm de last optillen met een kleinere kracht?', ''),
                ('Voor F_l = 2 N en d_l = 0,10 m, hoeveel is F_m bij d_m = 0,40 m?', ''),
                ('Zoek zelf een beroepstoepassing van een hefboom. [Internet toegelaten: gewone '
                 'zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waarom wijken gemeten momenten soms af?', ''),
                ('Is tussenstandige macht handig om kracht te besparen?', '')],
  'docent': [],
  'product': 'ingevulde werkbladen als één PDF',
  'peer': False,
  'zelf': False,
  'mc': None},
 {'nr': 8,
  'titel': 'EENPARIG CIRKELVORMIGE BEWEGING EN CENTRIPETALE KRACHT',
  'bron': '29–36',
  'theorie': '09 De eenparig cirkelvormige beweging, blz. 4–42',
  'lp': 'LPD 15 F; LPD 1 S, 2 S, 3 S, 4 S',
  'duur': 2,
  'sturing': 'BEGELEID: twee meetstrategieën, eigen test van één variabele.',
  'type': 'onderzoekspracticum (groep 2–3)',
  'context': 'Een speelgoedtrein en een platenspeler draaien rond. Met een rubberstop aan een draad '
             "onderzoek je daarna welke kracht de stop in zijn baan houdt: niet 'naar buiten', maar "
             'naar het middelpunt.',
  'doelen': ['T, f, ω en v bij speelgoedtrein/platenspeler bepalen',
             'F_cp = m v²/r met een hangmassa vergelijken',
             'de richting van de centripetale kracht uitleggen',
             'draaiende massa veilig op afstand houden'],
  'voor': [('Is v bij een ECB constant als vector?', ''), ('Wat is de richting van F_cp?', '')],
  'materiaal': ['speelgoedtrein met spoor of platenspeler, krijtstreepjes op twee stralen, stopwatch, '
                'meetlat; optioneel fietswiel',
                'glazen buisje met afgeronde randen ca. 20 cm, nylondraad ca. 90 cm, rubberstop, '
                '60/80/100/120/140 g hangmassa, meetlat, stopwatch',
                'veiligheidsbril, vrije draai-cirkel en Excel'],
  'begrip': '**ECB**: de grootte van de baansnelheid blijft constant, de richting niet. **Centripetale '
            'kracht**: de netto kracht die een voorwerp voortdurend naar het middelpunt trekt. '
            '**Hoeksnelheid ω**: de hoekverandering per seconde.',
  'formule': 'F_{cp} = \\\\frac{m v^{2}}{r} = m\\\\omega^{2}r \\\\quad [F_{cp}] = \\\\text{N}',
  'veiligheid': ['Controleer draad en rubberstop op slijtage, bril op, houd een vrije kring van '
                 'minstens 2 m; draai NIET als iemand binnen de kring staat.',
                 'Gebruik uitsluitend massa’s en draaddiktes die bij de toestellen passen; 60–140 g '
                 'uit bron is een richtwaarde, leerkracht test maximale veilige draaiing eerst.',
                 'Het glazen buisje moet afgeronde randen hebben; bij breuk STOP en leerkracht '
                 'waarschuwen.',
                 'Stop draaiende proef vóór je straal of massa verandert.'],
  'onderzoek': 'Hoe hangen v en ω af van de straal r bij een draaiende platenspeler en hoe hangt F_cp '
               'af van r en omlooptijd T bij dezelfde rubberstop, gemeten met stopwatch en meetlat '
               'tijdens dit labo?',
  'variabelen': 'O = r (twee krijtstrepen) of hangmassa; A = v, ω, T, F_cp; C = dezelfde draaisnelheid '
                'of rubberstop per deel.',
  'orientatie': [('Voor twee stippen op één platenspeler: wat is gelijk, ω of v?', ''),
                 ('Wat doet de hangmassa in de rubberstopproef?', '')],
  'delen': [{'titel': 'Deel 1 – Trein en platenspeler',
             'bron': '29–31',
             'vraag': 'Hebben twee punten op één schijf dezelfde ω en verschillende v?',
             'stappen': ['Laat de trein minstens twintig rondjes lopen zodat hij stabiel rijdt.',
                         'Meet voor minstens twintig toeren de tijd; bepaal T, f en ω van trein en '
                         'schijf.',
                         'Markeer twee radii op de schijf en meet r en v = 2πr/T voor beide.',
                         'Wissel van opstelling; herhaal minstens drie keer. Optioneel: fietswiel, '
                         'alleen als er tijd is.'],
             'kop': ['opstelling',
                     'r (m)',
                     'N (toeren)',
                     't (s)',
                     'T (s)',
                     'f (Hz)',
                     'ω (rad/s)',
                     'v (m/s)'],
             'rijen': 5,
             'verwerking': 'Vergelijk v en ω van de twee schijfpunten.',
             'figuur': 'sch_conische_slinger.png'},
            {'titel': 'Deel 2 – Rubberstop en hangmassa',
             'bron': '31–36',
             'vraag': "Is F_cp ≈ m'hang·g bij een gekozen r?",
             'stappen': ['Laat de opstelling en vrije draai-cirkel controleren.',
                         'Draai de stop horizontaal; markeer r aan de draad en meet tijd voor minstens '
                         'twintig toeren.',
                         'Meet voor 60, 80, 100, 120 en 140 g als de leerkracht die waarden veilig '
                         'acht.',
                         'Bereken f, ω, F_cp en F_z van de hangmassa; bereken de percentuele '
                         'afwijking.'],
             'kop': ["m' (kg)",
                     'F_z (N)',
                     'N',
                     't (s)',
                     'f (Hz)',
                     'ω (rad/s)',
                     'r (m)',
                     'F_cp (N)',
                     'afwijking (%)'],
             'rijen': ['0,060', '0,080', '0,100', '0,120', '0,140'],
             'verwerking': 'Vergelijk F_z en F_cp; geef aan dat wrijving in buis en niet-horizontaal '
                           'draaien de gelijkheid verstoren.',
             'figuur': None}],
  'stem': 'Bedenk hoe je de relatie F_cp(v) meet bij vaste r met één rubberstop: plan 4 draaisnelheden '
          'en veilige grens, test en maak F_cp(v²)-grafiek.',
  'reflectie': [('Waarom valt de stop niet recht vooruit zolang hij draait?', ''),
                ('Bereken ω bij T = 2,0 s.', ''),
                ('Zoek zelf een toepassing waar centripetale kracht nodig is. [Internet toegelaten: '
                 'gewone zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waarom wijkt F_cp van het gewicht van de hangmassa af?', ''),
                ('Als v verdubbelt bij dezelfde massa en straal, wat gebeurt er met F_cp?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': True,
  'zelf': False,
  'mc': None},
 {'nr': 9,
  'titel': 'HARMONISCHE TRILLINGEN: VEER, PERIODE EN ONBEKENDE MASSA',
  'bron': '36–46',
  'theorie': '10 Harmonische trillingen, blz. 8–32 en 70–81',
  'lp': 'LPD 18 F; LPD 1 S, 2 S, 3 S, 4 S',
  'duur': 3,
  'sturing': 'BEGELEID → OPEN: twee veren volgens bron, daarna eigen ijkplan voor onbekende massa.',
  'type': 'meetpracticum met tijdtikker (groep 2–3)',
  'context': 'Een horloge en een trillende veer verraden informatie via hun periode. Je ijkt twee '
             'veren, toetst de formule voor T en bepaalt ten slotte een onbekende massa zonder balans.',
  'doelen': ['k uit kracht/uitrekking bepalen',
             'T_gemeten en T_berekend bij twee veren vergelijken',
             'een onbekende massa bepalen uit T² met een eigen meetplan',
             'tijddata voor een halve trilling grafisch verwerken en veilig met veren werken'],
  'voor': [('Wat is een periode?', ''), ('Waarom meet je liever 20 dan 1 trilling?', '')],
  'materiaal': ['statief, klemmen, soepele en stuggere veer, meetlat, stopwatch, gewichtjes 40–250 g, '
                'onbekende massa aan veer',
                'elektromagnetische triller/tijdtikker 50 Hz, papierbandje, passende voeding, computer '
                'Excel'],
  'begrip': '**Veerconstante k**: kracht per meter uitrekking. **Harmonische trilling**: een beweging '
            'rond een evenwicht met (bij benadering) sinusvormige uitwijking. De veer heeft ook een '
            'eigen massa: bij kleine hangmassa kan die invloed hebben.',
  'formule': 'T = 2\\\\pi\\\\sqrt{\\\\frac{m}{k}} \\\\quad ; \\\\quad k=\\\\frac{F}{\\\\Delta y} '
             '\\\\quad [k]=\\\\text{N/m}',
  'veiligheid': ['Veer nooit voorbij fabrikantgrens/staat van blijvende vervorming rekken; leerkracht '
                 'test veilige maximale massa van elk exemplaar.',
                 "Klem statief stevig en gebruik opvangbak onder massa's.",
                 'Een triller alleen op geschikte lage voeding na controle; geen 230 V aan los '
                 'apparaat.',
                 'Kies kleine amplitude (ca. 2–3 cm) zodat de massa niet tegen tafel of statief '
                 'slaat.'],
  'onderzoek': 'Hoe hangt de periode T van een trillende massa af van de aangehangen massa m (40–250 '
               'g) en de veerconstante k van twee veren, gemeten met chronometer en gecontroleerd met '
               'een tijdtikker tijdens dit labo?',
  'variabelen': 'O = m en type veer; A = T; C = amplitude klein, veer per reeks, telling 10–20 cycli.',
  'orientatie': [('Wat gebeurt er met T als m viermaal zo groot wordt bij vaste k?', ''),
                 ('Waarom kun je k uit statische uitrekking vinden?', '')],
  'delen': [{'titel': 'Deel 1 – k en T van twee veren',
             'bron': '36–39',
             'vraag': 'Komen T_gemeten en 2π√(m/k) voor twee veren overeen?',
             'stappen': ["Bepaal voor elke veer de uitrekking bij vijf massa's binnen de veilige "
                         'grens.',
                         'Bereken per meting k = mg/Δy en bepaal een gemiddelde per veer.',
                         'Meet per massa de tijd voor twintig kleine trillingen, herhaal drie keer en '
                         'bereken T.',
                         'Vergelijk met T_berekend en de percentuele afwijking; maak T²(m).'],
             'kop': ['veer',
                     'm (kg)',
                     'F_z (N)',
                     'Δy (m)',
                     'k (N/m)',
                     't₂₀ (s)',
                     'T_gem (s)',
                     'T_berek (s)',
                     'afwijking (%)'],
             'rijen': 10,
             'verwerking': 'Verklaar waarom bij de lichtste massa de afwijking vaak groter is.',
             'figuur': 'sch_massa_veer.png'},
            {'titel': 'Deel 2 – Onbekende massa zonder balans',
             'bron': '40–41',
             'vraag': 'Kun je m_onbekend uit de periode halen terwijl die aan de veer blijft hangen?',
             'stappen': ['Laat de onbekende massa aan de veer; voeg achtereenvolgens gekende extra '
                         "massa's toe.",
                         'Meet telkens T uit twintig trillingen en zet T² tegen toegevoegde massa uit.',
                         'Bereken de onbekende massa uit het negatieve snijpunt van de horizontale as.',
                         'Maak een eigen instructieblad met materiaal, methode, veiligheid, tabel en '
                         'besluit.'],
             'kop': ['m_toegevoegd (kg)', 't₂₀ (s)', 'T (s)', 'T² (s²)'],
             'rijen': 5,
             'verwerking': 'Voor T² = (4π²/k)(m_onbekend + m_toegevoegd) is snijpunt x = −m_onbekend.',
             'figuur': None},
            {'titel': 'Deel 3 – Halve trilling via elektromagnetische triller',
             'bron': '43–46',
             'vraag': 'Is y(t) over een halve periode niet lineair, en hoe verandert v(t)?',
             'stappen': ['Bevestig het bandje aan de trillende massa en laat een korte, veilige halve '
                         'trilling registreren.',
                         'Noteer per stip t en y; bepaal Δy/0,020 s op de middentijden.',
                         'Maak y(t) en v(t) als spreidingsgrafieken met enkel punten.',
                         'Duid evenwichtsstand, amplitude en grootst gemeten |v| aan.'],
             'kop': ['stip', 't (s)', 'y (m)', 'Δy (m)', "t' (s)", 'v (m/s)'],
             'rijen': 9,
             'verwerking': 'Leg uit waarom |v| in de evenwichtsstand het grootst is.',
             'figuur': None}],
  'stem': 'Ontwerp een onbekende-massameter die maximaal 10% van de verborgen massa afwijkt: maak je '
          'instructieblad, test met een controlemassa en toon metingen en besluit.',
  'reflectie': [('Waarom is T²(m) een rechte?', ''),
                ('Wat wordt T bij een viermaal stuggere veer en dezelfde m?', ''),
                ('Zoek zelf een toepassing van een massa-veersysteem. [Internet toegelaten: gewone '
                 'zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waarom kan de formule T = 2π√(m/k) bij heel kleine m afwijken?', ''),
                ('Waarom ligt |v| maximaal bij de evenwichtsstand?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': False,
  'zelf': True,
  'mc': None},
 {'nr': 10,
  'titel': 'DE SLINGER: WELKE FACTOREN BEPALEN DE PERIODE?',
  'bron': '47–50',
  'theorie': '11 De slinger, blz. 4–27; 10 Harmonische trillingen, blz. 29–32',
  'lp': 'LPD 18 F, 16 F; LPD 1 S, 2 S, 4 S',
  'duur': 2,
  'sturing': 'BEGELEID → OPEN: drie variabelen, per meetreeks één variabele veranderen.',
  'type': 'onderzoekspracticum (groep 2–3)',
  'context': 'Een metronoom en een schommel lijken hetzelfde te doen, maar hun periode is niet altijd '
             'gelijk. Je onderzoekt met een eenvoudige slinger hoe massa, lengte en beginhoek de '
             'periode beïnvloeden.',
  'doelen': ['de invloed van amplitude, massa en lengte op T afzonderlijk onderzoeken',
             'T tegen √l grafisch voorstellen en g uit de rico berekenen',
             "een vergelijking maken met de slingerwet in de theoriedia's",
             'de slinger binnen een afgebakende veilige zone laten bewegen'],
  'voor': [('Wat is de lengte van een slinger?', ''),
           ('Voor welke hoeken geldt de eenvoudige slingerformule goed?', '')],
  'materiaal': ['statief, dubbelnoot, klem, dun touw, bolletjes met verschillende massa, rolmeter, '
                'gradenboog, stopwatch',
                'rekenblad Excel, zachte opvangmat'],
  'begrip': '**Wiskundige slinger**: ideaal model: puntmassa aan massaloos draadje bij kleine '
            'uitwijking. **Amplitude**: maximale uitwijking vanaf de evenwichtsstand.',
  'formule': 'T = 2\\\\pi\\\\sqrt{\\\\frac{l}{g}} \\\\quad [T]=\\\\text{s}',
  'veiligheid': ['Klem statief zodat het niet kan omvallen; houd alle hoofden buiten de slingerbaan.',
                 'Gebruik klein gewicht dat veilig aan het touw hangt; controle vóór loslaten.',
                 'Nooit het bolletje duwen bij start; loslaten vanuit rust.',
                 'Meet lengte tot het massamiddelpunt; tel telkens 10 of 20 hele perioden.'],
  'onderzoek': 'Hoe hangt de periode T van een slinger af van amplitude (5–20°), massa van het '
               'bolletje en lengte l (0,20–0,80 m), gemeten met stopwatch bij dezelfde lokale g, '
               'tijdens dit labo?',
  'variabelen': 'O = amplitude/massa/l in drie deelonderzoeken; A = T; C = overige twee grootheden per '
                'reeks.',
  'orientatie': [('Welk verband tussen T en l verwacht je?', ''),
                 ('Waarom meet je 20 perioden in plaats van één?', '')],
  'delen': [{'titel': 'Deel 1 – Verander de amplitude',
             'bron': '47–48',
             'vraag': 'Verandert T bij kleine uitwijking merkbaar met de beginhoek?',
             'stappen': ['Houd l en massa vast. Start zonder duw op 5°, 10°, 15° en 20°.',
                         'Meet telkens drie keer de tijd voor twintig slingerbewegingen en bereken T.',
                         'Vergelijk met de spreiding; leg uit waar de kleinehoekbenadering ophoudt.'],
             'kop': ['hoek (°)', 't₂₀,1 (s)', 't₂₀,2 (s)', 't₂₀,3 (s)', 'T̄ (s)'],
             'rijen': ['5', '10', '15', '20'],
             'verwerking': "Noem verschil 'meetbaar' alleen als het groter is dan spreiding.",
             'figuur': 'sch_slinger.png'},
            {'titel': 'Deel 2 – Verander de massa',
             'bron': '48',
             'vraag': 'Is T onafhankelijk van massa bij dezelfde l en hoek?',
             'stappen': ['Houd l en kleine hoek vast, wissel veilig tussen drie bolletjes met '
                         'verschillende massa.',
                         'Meet twintig perioden per massa drie keer.',
                         'Vergelijk T met de meetonzekerheid.'],
             'kop': ['m (kg)', 't₂₀ (s)', 'T (s)'],
             'rijen': 3,
             'verwerking': 'Een gelijke T past bij de slingerformule zonder m.',
             'figuur': None},
            {'titel': 'Deel 3 – Verander de lengte',
             'bron': '49–50',
             'vraag': 'Is T recht evenredig met √l?',
             'stappen': ['Kies minstens vijf lengten tussen 0,20 en 0,80 m; houd bolletje en hoek '
                         'vast.',
                         'Meet per l drie keer twintig perioden, noteer T en √l.',
                         'Maak T(√l) en bepaal g uit de richtingscoëfficiënt.'],
             'kop': ['l (m)', '√l (√m)', 't₂₀ (s)', 'T (s)'],
             'rijen': 5,
             'verwerking': 'rico = 2π/√g; dus g = (2π/rico)²; vergelijk met 9,81 m/s².',
             'figuur': None}],
  'stem': 'Ontwerp een slingerklok die per trilling ongeveer 1,0 s duurt (per halve slinger ≈ 0,5 s): '
          'bereken l, bouw, test 20 perioden, stel bij en maak een foto.',
  'reflectie': [('Waarom is T onafhankelijk van m volgens het model?', ''),
                ('Wat wordt T als l verviervoudigt?', ''),
                ('Zoek zelf een toepassing van een slinger buiten een klok. [Internet toegelaten: '
                 'gewone zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waarom levert een startduw een slechtere meting op?', ''),
                ('Waarom is de amplitudeproef bij 20° minder goed door de kleinehoekformule te '
                 'beschrijven?',
                 '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': True,
  'zelf': False,
  'mc': None},
 {'nr': 11,
  'titel': 'RESONANTIE: EIGENFREQUENTIE EN AANDRIJVING',
  'bron': '51–55',
  'theorie': '12 Resonantie, blz. 7–25; 10 Harmonische trillingen, eigenfrequentie blz. 31',
  'lp': 'LPD 18 F (★ resonantie); LPD 1 S, 2 S, 4 S, 5 S',
  'duur': 2,
  'sturing': 'BEGELEID + ONTWERP: frequentiestrategie zelf verfijnen rond de piek.',
  'type': 'onderzoekspracticum met gedempte veer',
  'context': 'Een brug kan sterk meetrillen als de aandrijffrequentie in de buurt van haar '
             'eigenfrequentie ligt. Met een traag draaiende motor onderzoek je de amplitude van een '
             'gedempte veer bij verschillende aandrijffrequenties.',
  'doelen': ['de eigenfrequentie f_e vooraf meten',
             'een resonantiecurve A(f) uit metingen opstellen',
             'demping door water bespreken',
             'de maximale amplitude binnen veilige grenzen houden'],
  'voor': [('Wat is de eigenfrequentie?', ''), ('Wat is een gedwongen trilling?', '')],
  'materiaal': ['regelbare laagtoerige motor met excenter, veer, massa, touw, wieltje, statieven en '
                'klemmen',
                'grote waterbak voor demping, meetlat, dun metalen staafje voor positie-indicator, '
                'stopwatch, Excel',
                'droge tafelzone voor motor en voeding'],
  'begrip': '**Resonantie**: grote respons als de aandrijffrequentie dichtbij de eigenfrequentie komt. '
            '**Demping**: energieverlies per trilling (hier door water). **Amplitude A** is de helft '
            'van het verschil tussen hoogste en laagste positie.',
  'formule': 'A = \\\\frac{B-O}{2} \\\\quad ; \\\\quad f = \\\\frac{N}{t} \\\\quad '
             '[A]=\\\\text{cm},[f]=\\\\text{Hz}',
  'veiligheid': ['Motor en voeding op droge tafel, waterbak apart; schakel uit vóór aanraken of '
                 'bijvullen.',
                 'Leerkracht controleert maximaal veilig toerental en veeruitslag voor deze '
                 'opstelling; stel geen universele spanning/stroom in.',
                 'Houd vingers en kleding weg van draaiend excenter/wieltje.',
                 'Stop direct als massa rand van bak raakt of statief beweegt.'],
  'onderzoek': 'Hoe hangt de amplitude A van een gedempte massa-veertrilling af van de '
               'aandrijffrequentie f rondom de vooraf gemeten f_e, bij dezelfde massa, veer en '
               'waterhoogte, tijdens dit labo?',
  'variabelen': 'O = aandrijffrequentie f; A = amplitude A; C = veer, massa, waterhoogte en '
                'opstelling.',
  'orientatie': [('Waar verwacht je de grootste A?', ''),
                 ('Waarom wacht je na verstellen van de motor met aflezen?', '')],
  'delen': [{'titel': 'Deel 1 – Vrije trilling en eigenfrequentie',
             'bron': '51–52',
             'vraag': 'Wat is de eigenfrequentie van het niet-aangedreven systeem?',
             'stappen': ['Zet motor uit, wijk massa voorzichtig een paar cm uit en laat zonder duw '
                         'los.',
                         'Meet de tijd van 10 of 20 hele trillingen in drie herhalingen.',
                         'Bereken T_e en f_e = 1/T_e.'],
             'kop': ['N', 't₁ (s)', 't₂ (s)', 't₃ (s)', 'T_e (s)', 'f_e (Hz)'],
             'rijen': 3,
             'verwerking': 'Bepaal het bereik rond f_e voor deel 2.',
             'figuur': 'sch_resonantie.png'},
            {'titel': 'Deel 2 – Gedwongen trilling en resonantiecurve',
             'bron': '52–55',
             'vraag': 'Neemt A toe bij f ≈ f_e en af aan beide kanten?',
             'stappen': ['Start met lage aandrijffrequentie en wacht tot de uitslag stabiel is.',
                         'Meet bij minstens acht frequenties; neem kleinere stappen nabij de piek.',
                         'Meet bij elke f bovenstand B en onderstand O; bereken A = (B−O)/2.',
                         'Zet A(f) als losse punten uit en duid f_e en de piekfrequentie aan.'],
             'kop': ['N cycli', 't (s)', 'f (Hz)', 'B (cm)', 'O (cm)', 'A (cm)'],
             'rijen': 8,
             'verwerking': 'Vergelijk piekfrequentie met vrije f_e en bespreek effect van '
                           'waterdemping.',
             'figuur': None}],
  'stem': 'Ontwerp een test van sterkere demping met andere waterhoogte: voorspelling, één constante '
          'motorfrequentie bij de piek, foto van instelling, minstens drie A-metingen per situatie.',
  'reflectie': [('Waarom is het resonantiepunt niet altijd precies f_e?', ''),
                ('Hoe bereken je A uit hoogste stand 18 cm en laagste stand 6 cm?', ''),
                ('Zoek zelf een nuttige toepassing van resonantie. [Internet toegelaten: gewone '
                 'zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Wat is het verschil tussen vrije en gedwongen trilling?', ''),
                ('Hoe zou je de piek beter in kaart brengen?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': False,
  'zelf': True,
  'mc': None},
 {'nr': 12,
  'titel': 'GOLVEN ZIEN: GOLFBAK EN STAANDE GOLVEN',
  'bron': '1; 27–28',
  'theorie': '13 Lopende golven, blz. 4–21 en 44–51; 13A Verschijnselen bij lopende golven; 14 Staande '
             'golven, blz. 4–21',
  'lp': 'LPD 19 F, 21 F, 22 F; LPD 1 S, 3 S, 4 S',
  'duur': 2,
  'sturing': 'GESLOTEN → BEGELEID: golfbeelden gegeven; eigen ontwerp met opening en frequentie.',
  'type': 'doorschuifpracticum met fysieke golfbak en applet',
  'context': 'Een golf verplaatst energie maar niet hetzelfde stukje water over de hele bak. In de '
             'projectie van de golfbak zie je cirkel- en vlakke golven, buiging en interferentie. Op '
             'een touw zoek je knopen en buiken.',
  'doelen': ['golflengte uit projectie en frequentie van een golf berekenen',
             'buiging bij smalle/brede opening en interferentie uitleggen',
             'staande golven met 1–4 buiken op een touw maken en tekenen',
             'water en elektrische trilbron strikt gescheiden houden'],
  'voor': [('Wat is het verschil tussen een lopende en een staande golf?', ''),
           ('Welke opening geeft sterkere buiging?', '')],
  'materiaal': ['golfbak op overheadprojector, gedestilleerd water, elektromagnetische trilbron met '
                'punt/staaf, frequentiegenerator',
                'ijzeren schermpjes met smalle en brede opening, hoogteregelaar, meetlat, '
                'camera/smartphone',
                'computer/tablet met golfbak-applet; trillingsbron met touw, voeding volgens typeplaat '
                'en statief, rolmeter'],
  'begrip': '**Golflengte λ**: afstand tussen twee opeenvolgende toppen. **Huygens**: elk punt van een '
            'golffront gedraagt zich als bron van nieuwe golfjes. **Knoop**: stil punt in een staande '
            'golf; **buik**: punt met grootste amplitude.',
  'formule': 'v = \\\\lambda f \\\\quad ; \\\\quad L=n\\\\frac{\\\\lambda}{2} \\\\quad '
             '[v]=\\\\text{m/s}',
  'veiligheid': ['Waterbak op stabiele tafel; projectie en voeding uit bij bijvullen; droge stekker, '
                 'handen en snoeren.',
                 'Leerkracht controleert toegestane spanning/frequentie voor gebruikte triller; geen '
                 'universeel maximum gokken.',
                 'Houd handen weg van bewegend touw; zet voeding uit vóór ander schermpje.',
                 'Bij defecte bak: applet als volwaardig alternatief; noteer dat het geen echte meting '
                 'is.'],
  'onderzoek': 'Hoe veranderen golflengte en buiging van een watergolf wanneer de frequentie en '
               'openingsbreedte afzonderlijk veranderen, en bij welke frequenties ontstaan één tot '
               'vier buiken op hetzelfde touw, geobserveerd tijdens dit labo?',
  'variabelen': 'O = f en opening; A = λ/buigingspatroon en buikentelling; C = waterdiepte, '
                'trillingsamplitude, touwlengte.',
  'orientatie': [('Als f stijgt bij dezelfde golfsnelheid, wat gebeurt er met λ?', ''),
                 ('Wat is bij één buik op een vast touw de relatie tussen L en λ?', '')],
  'delen': [{'titel': 'Deel 1 – Golfbak, applet en fysiek',
             'bron': '1 en 27–28',
             'vraag': 'Hoe verschillen cirkelgolven, vlakke golven en buiging/interferentie?',
             'stappen': ['In de applet: bewaar beelden van één puntbron met lage/hoge f, vlakke golf, '
                         '10/20 bronnen in rij.',
                         'Bewaar beelden van smalle/brede opening, twee bronnen in fase, tegenfase en '
                         'niet-coherent.',
                         'Fysieke bak: projecteer puntbron en staafbron, meet λ op projectie na '
                         'schaalmeting.',
                         'Plaats smalle en brede ijzeren opening; schets de golffronten erachter.'],
             'kop': ['situatie', 'f (Hz)', 'λ (cm)', 'schaal', 'schets / foto', 'verklaring'],
             'rijen': 9,
             'verwerking': 'Twee bronnen: leg maxima/minima uit; applet versus fysiek waargenomen '
                           'verschil.',
             'figuur': 'sch_golfbak.png'},
            {'titel': 'Deel 2 – Staande golven op een touw',
             'bron': '1 en theorie 14 blz. 21',
             'vraag': 'Bij welke frequenties ontstaan 1, 2, 3, 4 buiken?',
             'stappen': ['Span hetzelfde touw met dezelfde kracht en lengte L.',
                         'Verhoog frequentie tot het eerste duidelijke patroon; maak foto/schets en '
                         'tel knopen/buiken.',
                         'Herhaal tot vier buiken, noteer f_n en λ_n = 2L/n.',
                         'Vergelijk f_n met n·f_1.'],
             'kop': ['n (buiken)', 'knopen', 'L (m)', 'f_n (Hz)', 'λ_n (m)', 'v_n (m/s)'],
             'rijen': ['1', '2', '3', '4'],
             'verwerking': 'Trek conclusie voor f_n en duid één knoop en buik aan.',
             'figuur': 'sch_melde.png'}],
  'stem': 'Ontwerp met twee verstelbare schermpjes een opening waarbij de buiging maximaal zichtbaar '
          'is; fotografeer voor/tijdens/na, meet opening en λ, formuleer conclusie met b/λ.',
  'reflectie': [('Waarom buigt een golf meer na een smalle opening?', ''),
                ('Bij L = 0,60 m en drie buiken: bereken λ.', ''),
                ('Zoek zelf een toepassing van buiging of interferentie. [Internet toegelaten: gewone '
                 'zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waarom zijn de niet-coherente bronnen geen stabiel interferentiepatroon?', ''),
                ('Hoe weet je dat waterdeeltjes niet met de golf naar de overkant bewegen?', '')],
  'docent': [],
  'product': 'ingevulde werkbladen als één PDF',
  'peer': False,
  'zelf': False,
  'mc': None},
 {'nr': 13,
  'titel': 'GELUID: TRILLINGEN, SUPERPOSITIE EN DOPPLER',
  'bron': '55–56',
  'theorie': '15 Geluidsgolven, blz. 4–38, 49–68 en 86–102',
  'lp': 'LPD 20 F, 21 F; LPD 1 S, 3 S, 4 S, 5 S',
  'duur': 1,
  'sturing': 'GESLOTEN → BEGELEID: gegeven verkenning en eigen interferentievoorbeeld.',
  'type': 'kort applet- en geluidspracticum',
  'context': 'Een koptelefoon met ruisonderdrukking voegt een tweede geluid toe zodat je minder hoort. '
             'Je onderzoekt met een geluidsprogramma wat er gebeurt wanneer geluiden gelijk of '
             'tegengesteld zijn en wanneer een bron beweegt.',
  'doelen': ['frequentie, amplitude, toonhoogte en luidheid onderscheiden',
             'superpositie van twee geluidsignalen uitleggen',
             'het dopplereffect bij veranderende relatieve beweging beschrijven',
             'luistervolume veilig houden en bronnen kritisch controleren'],
  'voor': [('Welke grootheid bepaalt in hoofdzaak de toonhoogte?', ''),
           ('Hoe heet de optelling van twee trillingen?', '')],
  'materiaal': ['schoollaptop met werkende geluidsapp of geluidsgenerator, luidspreker of '
                'hoofdtelefoon, volumebegrenzer',
                'optioneel microfoon/phyphox spectrumanalyse, Doppler-applet op schoollaptop, Excel '
                'voor screenshots'],
  'begrip': '**Superpositie**: ogenblikkelijke uitwijkingen van twee golven worden opgeteld. '
            '**Tegenfase**: top van de ene en dal van de andere vallen samen en kunnen elkaar '
            'uitdoven. **Dopplereffect**: de waargenomen frequentie verandert als bron en luisteraar '
            'ten opzichte van elkaar bewegen.',
  'formule': 'f = \\\\frac{1}{T} \\\\quad [f]=\\\\text{Hz}',
  'veiligheid': ['Zet het geluid eerst zacht; geen harde hoofdtelefoon of plotselinge tonen.',
                 'De oude Soundry-links in bron zijn verouderd; gebruik alleen vooraf door de '
                 'leerkracht geteste schoolsoftware; geen download tijdens het labo.',
                 'Geen microfoonopnames van medeleerlingen zonder toestemming.',
                 'Bij geen applet: teken twee sinussen met zelf gekozen fase op ruitjespapier.'],
  'onderzoek': 'Hoe verandert de resulterende geluidsamplitude bij optelling van twee even luide tonen '
               'die in fase of tegenfase zijn, geobserveerd met schoolsoftware, en hoe verandert de '
               'gehoorde toonhoogte bij naderende/weggaande bron, tijdens dit labo?',
  'variabelen': 'O = faseverschil en richting bron; A = amplitude en waargenomen toonhoogte; C = '
                'basisfrequentie, volume.',
  'orientatie': [('Wat hoor je bij gelijke tonen in tegenfase?', ''),
                 ('Wat gebeurt er met de toonhoogte van naderende bron?', '')],
  'delen': [{'titel': 'Deel 1 – Soundry of geteste geluidsapp',
             'bron': '55–56',
             'vraag': 'Kunnen twee identieke golven samen sterker of zwakker zijn?',
             'stappen': ['Open de vooraf geïnstalleerde app; kies twee dezelfde zuivere tonen bij laag '
                         'volume.',
                         'Maak schermafbeeldingen van één toon, twee in fase en twee in tegenfase.',
                         'Lees amplitudes af of vergelijk piek-tot-piek zichtbaar; verklaar '
                         'superpositie.',
                         'Verander één frequentie en noteer hoe de som er anders uitziet.'],
             'kop': ['signaal', 'f₁ (Hz)', 'f₂ (Hz)', 'fase', 'A_res (relatief)', 'schermafbeelding'],
             'rijen': 4,
             'verwerking': 'Benoem nuttige toepassing: ruisonderdrukking, zelf opzoeken.',
             'figuur': None},
            {'titel': 'Deel 2 – Doppler in de applet',
             'bron': '56',
             'vraag': 'Wat verandert als de bron van de luisteraar weg beweegt?',
             'stappen': ['Laat de bron in de applet stil staan en teken golffronten vóór en achter.',
                         'Herhaal met naderende en weggaande bron; beschrijf de golflengte vóór en '
                         'achter.',
                         'Verhoog de bronsnelheid tot nabij of boven de golfsnelheid als de applet dat '
                         'toelaat; beschrijf het verschil.'],
             'kop': ['situatie', 'λ vóór', 'λ achter', 'toonhoogte', 'verklaring'],
             'rijen': 3,
             'verwerking': 'Bespreek het verschil tussen een bewegende bron en een stilstaande bron.',
             'figuur': None}],
  'stem': 'Ontwerp in de app een combinatie van twee tonen die duidelijk minder amplitude geeft dan '
          'één toon. Noteer f, fase, schermafbeelding en toets je ontwerp.',
  'reflectie': [('Waarom vermindert geluid bij twee tegengestelde signalen?', ''),
                ('Wat is de frequentie bij T = 0,004 s?', ''),
                ('Zoek zelf een toepassing van het dopplereffect. [Internet toegelaten: gewone '
                 'zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waarom werkt actieve ruisonderdrukking het best bij regelmatige achtergrondruis?',
                 ''),
                ('Is een lager geluid altijd een lagere frequentie?', '')],
  'docent': [],
  'product': 'ingevulde werkbladen als één PDF',
  'peer': False,
  'zelf': False,
  'mc': None},
 {'nr': 14,
  'titel': 'INTERFERENTIE AAN EEN ROOSTER: LASER, CD EN WIT LICHT',
  'bron': '1–11',
  'theorie': '16 Elektromagnetische golven, blz. 44–71; 13A Verschijnselen bij lopende golven',
  'lp': 'LPD 21 F, 23 F; LPD 1 S, 2 S, 3 S, 4 S',
  'duur': 3,
  'sturing': 'BEGELEID: roosterreeksen gegeven, eigen controle van CD-spoorafstand.',
  'type': 'lichtpracticum met rooster (groep 2–3)',
  'context': 'De groeven van een cd gedragen zich als een rooster. Eerst bepaal je de golflengte van '
             'een laserpen met echte roosters, dan draai je de vraag om en bepaal je de spoordichtheid '
             'van een cd. Bij wit licht verschijnen verschillende kleuren op andere plaatsen.',
  'doelen': ['λ uit l en y voor vier roosterconstanten bepalen',
             'de spoordichtheid en totale spoorlengte van een cd schatten',
             'de grenzen rood/violet en tussenkleuren van een spectrum meten',
             'laser veilig op laag scherm richten, nooit in het oog'],
  'voor': [('Wat betekent 100 lijnen per mm?', ''),
           ('Waarom verschijnt een spectrum bij wit licht?', '')],
  'materiaal': ['laserpen uitsluitend door leerkracht goedgekeurde klasse, meetlatten, scherm, '
                'roosterhouder',
                'roosters 80, 100, 300 en 600 lijnen/mm (indien aanwezig), cd, geodriehoek',
                'witlichtbron achter gleuf, eventuele kwikdamplamp alleen docentbediening, tweede '
                'rooster of cd, Excel'],
  'begrip': '**Roosterconstante a**: afstand tussen naburige roosterlijnen; a = 1/(aantal lijnen per '
            'meter). **Maximum van orde n**: heldere richting waarvoor a·sin θ = nλ. **Continu '
            'spectrum**: alle zichtbare kleuren; lijnenspectrum: afzonderlijke lijnen.',
  'formule': 'a\\\\sin\\\\theta = n\\\\lambda \\\\quad ; \\\\quad \\\\theta=\\\\arctan\\\\frac{y}{l}',
  'veiligheid': ['Laser nooit op ooghoogte en nooit in de richting van personen/spiegels; leerkracht '
                 'controleert laserklasse en bundelstop.',
                 'Kwikdamplamp kan heet zijn en uv uitzenden: alleen leerkracht bedienen; '
                 'scherm/veiligheidsinstructie van toestel volgen.',
                 'Scherm stabiel en gelabeld; meet links én rechts, niet in de directe bundel kijken.',
                 'Bij ontbrekend rooster: meet alleen met aanwezige roosters; verzin geen resultaten '
                 'voor de bronreeksen.',
                 'Gebruik een intacte CD als rooster; kras of verwijder de reflecterende laag niet '
                 '(de oude bronafbeelding toont die verouderde procedure).'], 
  'onderzoek': 'Hoe hangt de positie y van de n-de maxima af van roosterconstante a (80–600 lijnen/mm) '
               'bij dezelfde laser en vaste schermafstand l, en hoe groot is de spoordichtheid van een '
               'cd bij die laser, gemeten tijdens dit labo?',
  'variabelen': 'O = a en orde n; A = y/θ en λ; C = laser, l per meetreeks; CD als omgekeerde vraag '
                'met λ constant.',
  'orientatie': [('Wat moet constant zijn als je verschillende roosters vergelijkt?', ''),
                 ('Waarom meet je maxima aan beide zijden?', '')],
  'delen': [{'titel': 'Deel 1 – Laser met vier roosters',
             'bron': '1–4',
             'vraag': 'Leveren de roosters 80, 100, 300 en 600 lijnen/mm dezelfde λ?',
             'stappen': ['Zet laser, rooster en scherm op één lage lijn; laat controle door leerkracht '
                         'uitvoeren.',
                         'Bepaal a voor elk rooster. Meet l en voor meerdere ordes y links en rechts '
                         'van het centrale maximum.',
                         'Bereken θ = arctan(y/l) en λ = a sin θ/n voor elk bruikbaar maximum.',
                         'Neem per rooster een gemiddelde en vergelijk de waarden.'],
             'kop': ['rooster (lijnen/mm)',
                     'a (m)',
                     'l (m)',
                     'n',
                     'y links (m)',
                     'y rechts (m)',
                     'θ (°)',
                     'λ (nm)'],
             'rijen': 12,
             'verwerking': 'Voor 600 lijnen/mm zijn mogelijk slechts ordes 1–3 zichtbaar; bron heeft '
                           'aparte tabel per rooster.',
             'figuur': 'sch_rooster.png'},
            {'titel': 'Deel 2 – CD als rooster',
             'bron': '5–6',
             'vraag': 'Wat is de groefafstand op een cd en hoe lang is het spoor ongeveer?',
             'stappen': ['Houd de cd in een veilige hoek; richt de bundel nooit naar ogen.',
                         'Meet maxima voor de cd met gekende gemiddelde λ uit deel 1 en bereken a.',
                         'Meet de binnen- en buitenstraal van het beschreven ringgebied; bereken '
                         'aantal sporen = Δr/a.',
                         'Schat totale lengte met omtrek van de middelste cirkel en bespreek die '
                         'benadering.'],
             'kop': ['λ (nm)',
                     'n',
                     'l (m)',
                     'y (m)',
                     'a (m)',
                     'r_in (m)',
                     'r_uit (m)',
                     'sporen',
                     'lengte (m)'],
             'rijen': 3,
             'verwerking': 'Totale lengte ≈ (r_uit−r_in)/a · 2π·(r_in+r_uit)/2; bespreek spiraal '
                           'versus losse cirkels.',
             'figuur': None},
            {'titel': 'Deel 3 – Wit licht en lijnenspectrum',
             'bron': '8–11',
             'vraag': 'Liggen rood en violet op dezelfde afbuigingshoek?',
             'stappen': ['Plaats witlichtbron achter gleuf en rooster; meet l en de plaats van rode en '
                         'violette grens links/rechts.',
                         'Herhaal met tweede rooster of cd; meet ook groen en geel bij benadering.',
                         'Bekijk een kwikdamplamp enkel als docentdemo; schets lijnenspectrum en '
                         'vergelijk met continu spectrum.',
                         'Bereken grenzen van λ en bespreek onzekerheid door onscherpe kleurgrens.'],
             'kop': ['rooster',
                     'kleur',
                     'orde n',
                     'l (m)',
                     'y links (m)',
                     'y rechts (m)',
                     'θ (°)',
                     'λ (nm)'],
             'rijen': 8,
             'verwerking': 'Violet korter λ dan rood; in de bron twee roosterreeksen.',
             'figuur': None}],
  'stem': "Ontwerp een snelle test om twee onbekende cd's met verschillende spoordichtheid uit elkaar "
          'te houden zonder cd aan te raken: beschrijf voorspelling, methode, tabel, foto en '
          'conclusie.',
  'reflectie': [('Waarom geeft een kleiner a grotere afbuiging bij vaste λ en n?', ''),
                ('Een rooster heeft 500 lijnen/mm. Bereken a.', ''),
                ('Zoek zelf een toepassing van spectraal onderzoek. [Internet toegelaten: gewone '
                 'zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Waarom is een exacte rode spectrale grens lastig te meten?', ''),
                ('Hoe verschilt het spectrum van een gloeilamp van dat van een gasontladingslamp?',
                 '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': True,
  'zelf': False,
  'mc': None},
 {'nr': 15,
  'titel': 'LICHTBREKING: DE SPELDEPRIKPROEF',
  'bron': '11–15',
  'theorie': '16 Elektromagnetische golven, blz. 35–43 (breking en index)',
  'lp': 'LPD 21 F, 23 F; LPD 1 S, 2 S, 3 S, 4 S',
  'duur': 2,
  'sturing': 'BEGELEID: meet zes invalshoeken en bouw je eigen lichtpad op papier.',
  'type': 'optisch meetpracticum (groep 2–3)',
  'context': 'Een rietje lijkt te knikken in water. Met drie spelden en een plexiglazen balkje teken '
             'je echte lichtstralen en bepaal je de brekingsindex van het kunststof.',
  'doelen': ['een invalstraal, normaal en gebroken straal correct tekenen',
             'sin α/sin β voor zes hoekparen berekenen',
             'n van lucht naar kunststof uit een grafiek bepalen',
             'spelden en plexiglas zorgvuldig gebruiken'],
  'voor': [('Wat is de normaal?', ''),
           ('Als licht naar optisch dichter materiaal gaat, buigt het naar of van de normaal?', '')],
  'materiaal': ['A4 papier, vlak stuk karton of piepschuim, tape, plexiglazen balkje, 3 kopspeldjes',
                'meetlat, geodriehoek, scherp potlood, opbergdoosje voor spelden, Excel'],
  'begrip': '**Breking**: richtingsverandering van licht bij een overgang van middenstof. '
            '**Brekingsindex n**: de verhouding sin α/sin β bij overgang van lucht naar de tweede '
            'middenstof, in eenvoudige benadering.',
  'formule': 'n_{lucht\\\\to kunststof} = \\\\frac{\\\\sin\\\\alpha}{\\\\sin\\\\beta}',
  'veiligheid': ['Spelden na elke reeks in doosje; niet in de hand of op de grond laten liggen.',
                 'Plexiglas niet beschadigen of laten vallen; wees voorzichtig met scherpe randen.',
                 'Kies hoekreeks zonder totale interne reflectie voor licht uit lucht; markeer '
                 'invalspunt nauwkeurig.',
                 'Herhaal een hoek drie keer; lees met geodriehoek tot ca. 1° af.'],
  'onderzoek': 'Hoe hangt de brekingshoek β af van de invalshoek α (ca. 10–60°) voor licht van lucht '
               'naar hetzelfde plexiglas, geconstrueerd met drie spelden en geodriehoek tijdens dit '
               'labo?',
  'variabelen': 'O = α; A = β; C = hetzelfde balkje, grensvlak, invalspunt en opstellingswijze.',
  'orientatie': [('Waarom is het belangrijk het balkje op dezelfde lijn terug te zetten?', ''),
                 ('Welke verhouding verwacht je ongeveer constant?', '')],
  'delen': [{'titel': 'Deel 1 – Stralen construeren met drie spelden',
             'bron': '11–13',
             'vraag': 'Welke richting krijgt de gebroken straal bij dezelfde α?',
             'stappen': ['Kleef papier op karton; teken omtrek balkje, grensvlak en normaal in één '
                         'vast invalspunt.',
                         'Zet speld 1 en 2 op de invalstraal; kijk door het balkje van de andere '
                         'zijde.',
                         'Zet speld 3 op een plek waar de eerste twee achter elkaar lijken te staan; '
                         'herhaal bij een tweede invalshoek.',
                         'Haal balkje weg en teken stralen door de speldpunten; label α en β.'],
             'kop': ['proef', 'α (°)', 'β (°)', 'schets', 'opmerking'],
             'rijen': 2,
             'verwerking': 'Leg uit waarom twee waarnemers aan verschillende zijden niet hetzelfde '
                           'zien.',
             'figuur': None},
            {'titel': 'Deel 2 – De brekingsindex meten',
             'bron': '14–15',
             'vraag': 'Blijft sin α/sin β ongeveer constant?',
             'stappen': ['Teken zes invalshoeken tussen ca. 10° en 60° vanuit hetzelfde invalspunt.',
                         'Construeer zes uitgaande stralen en meet telkens β vanaf de normaal.',
                         'Bereken sin α en sin β; maak sin α als functie van sin β.',
                         'Bepaal n uit de rico en vergelijk met het klasgemiddelde.'],
             'kop': ['α (°)', 'β (°)', 'sin α', 'sin β', 'sin α / sin β'],
             'rijen': 6,
             'verwerking': 'Een rechte bijna door oorsprong, rico ≈ n; exact getal afhankelijk van '
                           'kunststof.',
             'figuur': None}],
  'stem': "Ontwerp een transparante 'raadsellijst': geef een ander duo een onbekend kunststofplaatje, "
          'laat ze met drie spelden beslissen of n groter/kleiner is dan bij jouw plaatje; noteer '
          'test, foto en uitleg.',
  'reflectie': [('Waarom kun je α en β niet rechtstreeks delen om n te bepalen?', ''),
                ('Bij α = 30° en β = 19,5°, schat n.', ''),
                ('Zoek zelf een toepassing van lichtbreking. [Internet toegelaten: gewone zoekmachine '
                 'zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Wat is de belangrijkste meetonzekerheid?', ''),
                ('Waarom is het klasgemiddelde bruikbaar?', '')],
  'docent': [],
  'product': 'Excel-verslagsjabloon (.xlsx)',
  'peer': False,
  'zelf': False,
  'mc': None},
 {'nr': 16,
  'titel': 'OPEN ONDERZOEK: EEN EIGEN VRAAG VAN BEGIN TOT POSTER',
  'bron': 'nieuw (LPD 6 S #)',
  'theorie': 'naar keuze uit theorie 01–16; afgestemd op het onderwerp van de gekozen vraag',
  'lp': 'LPD 6 S #; LPD 1 S, 2 S, 3 S, 4 S, 5 S; F-LPD naar keuze',
  'duur': 3,
  'sturing': 'OPEN: leerlingen kiezen vraag, meetplan, variabelen, analyse en presentatie zelf.',
  'type': 'open praktijkonderzoek (groep 2–3)',
  'context': "In de vorige labo's kreeg je een doel en meestal een opstelling. Nu ontwerp en voer je "
             'een volledig eigen onderzoek uit als bewijs van je onderzoekscompetentie. Je toont '
             'resultaat en onzekerheid op een wetenschappelijke A3-poster.',
  'doelen': ['een eigen meetbare SMART-onderzoeksvraag formuleren',
             "variabelen, methode, materiaallijst, risico's en herhalingen plannen",
             'resultaten met onzekerheid en grafiek analyseren',
             'een heldere A3-poster met hypothese, methode, data en besluit maken'],
  'voor': [('Wat zijn O, A en C van je onderzoek?', ''),
           ('Hoe controleer je of je meetplan realistisch is?', '')],
  'materiaal': ['zelf voorgestelde beperkte materiaallijst uit het schoollabo; beschikbaarheid vooraf '
                'laten bevestigen',
                'laptop met Excel, camera voor foto van opstelling, A3-poster als PDF; geen '
                'presentatie of PowerPoint',
                'toepasselijke PBM in overleg met de leerkracht'],
  'begrip': '**Onderzoekscyclus**: vraag → hypothese → plan → meting → analyse → besluit → '
            'communicatie. **Betrouwbaarheid**: mate waarin herhalingen een vergelijkbaar resultaat '
            'geven.',
  'formule': '\\\\bar{x} = \\\\frac{x_1+x_2+x_3}{3} \\\\quad [\\\\bar{x}]=[x]',
  'veiligheid': ['Je voert pas uit nadat de leerkracht jouw werkwijze en risicoanalyse schriftelijk '
                 'heeft goedgekeurd.',
                 'Meld maxima van stroom, spanning, temperatuur, massa en hoogte specifiek voor de '
                 'gekozen opstelling; geen algemene grens.',
                 'Plan minstens drie herhalingen per meetpunt, veilige opvang en stopcriterium.',
                 'Gebruik geen laser, netspanning of hete vloeistof zonder specifieke toestemming en '
                 'begeleiding.'],
  'onderzoek': 'Formuleer ZELF: Hoe hangt [afhankelijke meetgrootheid] af van [onafhankelijke '
               'grootheid] bij [constante voorwaarden en meetbereik], gemeten met [methode], tijdens '
               'dit labo?',
  'variabelen': 'O, A en C worden door de groep gemotiveerd en door leerkracht vooraf goedgekeurd.',
  'orientatie': [('Welke metingen zijn minimaal nodig om een verband te onderzoeken?', ''),
                 ('Wat doe je als de gemeten trend niet op je hypothese lijkt?', '')],
  'delen': [{'titel': 'Deel 1 – Voorbereiding en goedkeuring (lesuur 1)',
             'bron': 'nieuw',
             'vraag': 'Is de eigen vraag SMART, veilig en onderzoekbaar?',
             'stappen': ['Kies een vraag uit de inspiratielijst of bedenk zelf een andere.',
                         'Maak een variabelentabel (O/A/C), hypothese, materiaallijst, bereik, '
                         'stappen, herhalingen, verwachte grafiek en risicoanalyse.',
                         'Laat vraag en plan vóór de tweede les schriftelijk goedkeuren.'],
             'kop': ['O (onafhankelijk)',
                     'A (afhankelijk)',
                     'C (constant)',
                     'meetmethode',
                     'risico/maatregel'],
             'rijen': 4,
             'verwerking': 'Goedkeuring leerkracht: datum, naam en eventuele aanpassingen.',
             'figuur': None},
            {'titel': 'Deel 2 – Uitvoering en kwaliteitscontrole (lesuren 2–3)',
             'bron': 'nieuw',
             'vraag': 'Ondersteunen de metingen de hypothese?',
             'stappen': ['Bouw veilig op en laat de opstelling vóór inschakelen controleren.',
                         'Meet minstens vijf waarden van O met drie herhalingen; ruwe data meteen '
                         'noteren.',
                         'Controleer minstens één keer of je resultaat plausibel is met een schatting '
                         'of referentiewaarde.',
                         'Maak een foto/schema en noteer onverwachte omstandigheden; werk thuis de '
                         'A3-poster en Excel af.'],
             'kop': ['O (eenheid)',
                     'A₁ (eenheid)',
                     'A₂ (eenheid)',
                     'A₃ (eenheid)',
                     'Ā (eenheid)',
                     'opmerking'],
             'rijen': 5,
             'verwerking': 'Poster: titel/namen, SMART-vraag, hypothese, foto/schema + variabelen, '
                           'resultaten tabel/grafiek met assen en trendlijn, besluit, foutenanalyse, '
                           'bronnen. Max. ca. 300 woorden; leesbaar op 1,5 m.',
             'figuur': None}],
  'stem': 'Dit héle labo is de STEM-ontwerpopdracht: vraag, variabelen, meetstrategie en oplossing '
          'komen van jullie. Lever de test met foto, Excel-ruwe data en A3-poster als bewijs.',
  'reflectie': [('Wat moet de grafiek tonen?', ''),
                ('Waarom volstaat één meetpunt niet voor een verband?', ''),
                ('Zoek zelf één toepassing die met jouw vraag samenhangt. [Internet toegelaten: gewone '
                 'zoekmachine zoals Google, bron vermelden – geen AI-tool.]',
                 ''),
                ('Wat is jouw belangrijkste meetonzekerheid en hoe verlaag je die?', ''),
                ('Waarom mag je een onverwachte uitkomst niet uit de data verwijderen?', '')],
  'docent': [],
  'product': 'wetenschappelijke poster (A3, PDF) + Excel-bestand met ruwe data en grafieken',
  'peer': False,
  'zelf': True,
  'mc': None}]

# De bladzijden 43 en 46 van de bron zijn als volledige tekstpagina's gerasterd.
# Hun vragen staan hier expliciet (niet als slecht leesbare screenshot van tekst).
LABOS[8]['delen'][2]['vragen'] = [
    'Stonden de stippen telkens even ver uit elkaar op het bandje? Is dit een ERB?',
    'Welke functievorm herken je in de y(t)- en v(t)-grafiek van de halve trilling?',
    'Waar is de grootte van de snelheid maximaal: bij de uiterste stand of bij de evenwichtsstand? Motiveer met de grafiek.',
    'Bepaal amplitude A en periode T uit je meetreeks; noteer beide met eenheid.',
    'Bereken v_max = 2πA/T en vergelijk met de grootste gemeten |v|. Verklaar een eventueel verschil.',
]

INSPIRATIE = ['Hoe hangt de periode van een slinger af van de lengte bij een kleine, vaste beginhoek?',
 'Hoe hangt de versnelling van een wagentje af van de hellingshoek bij dezelfde massa?',
 'Hoe hangt de reikwijdte van een horizontale worp af van de beginhoogte bij vergelijkbare '
 'startsnelheid?',
 'Hoe hangt de uitrekking van een veer af van de hangmassa binnen het elastische bereik?',
 'Hoe hangt de periode van een massa-veersysteem af van de massa bij dezelfde veer?',
 'Hoe hangt de amplitude van een gedwongen veertrilling af van de aandrijffrequentie bij dezelfde '
 'demping?',
 'Hoe hangt de golflengte in een golfbak af van de frequentie bij vaste waterdiepte?',
 'Hoe hangt de frequentie van een staande golf op een touw af van het aantal buiken bij dezelfde '
 'touwspanning?',
 'Hoe hangt de omlooptijd van een rubberstop af van de baanstraal bij dezelfde hangmassa en veilige '
 'draaisnelheid?',
 'Hoe hangt de geluidsfrequentie van een trillende liniaal af van de vrije lengte bij dezelfde '
 'liniaal?',
 'Hoe hangt de gemeten brekingshoek af van de invalshoek bij hetzelfde plexiglas?',
 'Hoe hangt de plaats van een roostermaximum af van de roosterafstand bij dezelfde veilige laser en '
 'schermafstand?']

# ---------------------------------------------------------------------------
# Brongetrouwe uitvoeringsversie (vakgroepfeedback oktober 2026)
# De originele practicumopstellingen blijven staan. De rijen hieronder geven
# de concrete tijdtikkerstippen en tussentijdstippen weer; alleen de werkbladen,
# veiligheid en Excel-instructies zijn gemoderniseerd. t′ is de MIDDELTIJD van
# twee meetstippen. Δt is het interval (0,020 of 0,040 s), NOOIT de kolomnaam t′.
# t′ staat in elke tijdtikkertabel onmiddellijk LINKS van v voor Excel v(t′).

def _ticker_rows(n, dt, stride=1, x0=False, last_col=True):
    def dutch(v): return f'{v:.3f}'.replace('.', ',')
    rows=[]
    for i in range(n):
        t=i*dt
        rows.append([str(i*stride), dutch(t), '0' if i==0 and x0 else '', '',
                     dutch(t+dt/2) if i<n-1 else '', '', ''] if last_col else
                    [str(i*stride), dutch(t), '0' if i==0 and x0 else '', '',
                     dutch(t+dt/2) if i<n-1 else '', ''])
    return rows

_TICKER_NOTE = ('Kopieer in Excel voor x(t) de kolommen t en x. Bereken Δx tussen twee '
                'opeenvolgende gekozen meetstippen; Δt is per venster constant. '
                't′ = (t_begin + t_eind)/2 is het TIJDSTIP van de berekende snelheid, '
                'geen Δt en geen Δv. In de tabel staat t′ direct links van v: '
                'selecteer deze twee aangrenzende kolommen voor een XY-spreidingsgrafiek v(t′). '
                'De laatste meetstip levert geen nieuw venster en dus geen t′ of v.')

# Labo 1, deel 2: de eigen elektrische wagen en de tijdtikker (bron 68–72).
p=LABOS[0]['delen'][1]
p.update(titel='Deel 2 – Oorspronkelijk practicum: ERB met elektrisch wagentje en tijdtikker',
         nieuw_blad=True,
         stappen=[
          'Laat de leerkracht de passende 6,0 V~ laagspanningsbron en de wisselspanningsvoltmeter controleren. Zet de bron UIT vóór je carbonlint en bandje vastmaakt.',
          'Kleef het papieren bandje aan de aangedreven wagen, leid het recht door de klemmen van de tijdtikker en houd het vrije uiteinde zó dat de stippen midden op het bandje staan.',
          'Start de tijdtikker en het elektrisch wagentje; laat de wagen de rechte baan doorlopen. Stop met de schakelaar van het wagentje, zet de voeding uit en kleef het bandje RECHT op de tafel.',
          'Negeer de stippen bij optrekken en remmen. Kies stip 0 in het gelijkmatige middendeel, nummer telkens om de twee tijdtikkerstippen (Δt = 0,040 s), meet x in meter en bewaar het originele bandje.',
          'Vul de eigen meetwaarden in, bereken Δx en v = Δx/0,040 s, teken x(t) en v(t′) en bespreek de wiskundige kenmerken van beide grafieken.'],
         kop=['stip','t (s)','x (m)','Δx in 0,040 s (m)','t′ (s)','⟨v⟩ (m/s)'],
         rijen=_ticker_rows(22,0.040,x0=True,last_col=False),
         tabel_uitleg=_TICKER_NOTE,
         grafieken=['x(t): t op de horizontale as, x op de verticale; bepaal de richtingscoëfficiënt.',
                    'v(t′): selecteer de aangrenzende kolommen t′ en ⟨v⟩; is de snelheid ongeveer constant?'],
         verwerking='Bepaal de snelheid uit de rico van x(t) én de gemiddelde waarde van Δx/0,040 s. Licht afwijkingen door optrekken, remmen en bandwrijving toe.',
         vragen=['Waarom blijven de optrek- en remstippen buiten de ERB-meetreeks?',
                 'Hoe werkt de tijdtikker bij 50 Hz, en waarom is één tik 0,020 s maar één rij 0,040 s?'])
LABOS[0]['materiaal'][1]='elektrisch wagentje met schakelaar, rechte baan; tijdtikker (50 Hz), carbonlint, recht papierbandje ca. 1,1 m, kleefband, lange lat, wisselspanningsvoltmeter en gecontroleerde passende 6,0 V~ laagspanningsbron (bron blz. 68)'

# Labo 2: bron 79–85 en 86–92 blijven twee afzonderlijk uitvoerbare
# tijdtikkerpractica. Het tweede is uitdrukkelijk OPEN, niet slechts begeleid.
LABOS[1]['sturing']='DEEL 1 BEGELEID: originele EVRB met beginsnelheid. DEEL 2 OPEN PRACTICUM: ontwerp zelf de vertraagde-meting; behoud wagentje, tijdtikker en stijgende helling.'
p=LABOS[1]['delen'][0]
p.update(titel='Deel 1 – Oorspronkelijk practicum: EVRB met beginsnelheid op helling',
         nieuw_blad=True,
         stappen=[
          'Bouw de circa 1 m lange hellende baan met het wagentje (50 g) en ballast (bv. 200 g). Controleer de 50 Hz-tijdtikker, het carbonlint, de circa 1,10 m papierband, de veilige 6 V~ bron en een opvangblok.',
          'Laat het wagentje omlaag rijden. Negeer de te dicht bij elkaar liggende beginstippen: kies stip 0 iets verderop, waar de wagen AL een snelheid heeft. Kleef het bandje recht op de tafel.',
          'Meet vanaf stip 0 de plaats x om de twee tikken (tiknummers 0, 2, 4, …; Δt = 0,040 s). Behoud het bandje als bewijs en noteer x in de vooraf ingevulde tabel.',
          'Bereken de afstand Δx in elk venster van 0,040 s. Plaats v = Δx/0,040 s bij het midden van dat venster, t′ = 0,020; 0,060; 0,100 s …',
          'Teken x(t) en v(t′) in Excel als spreidingsgrafieken met trendlijn; extrapoleer de v(t′)-rechte naar t = 0 om v₀ te schatten; bereken a uit de rico en desgewenst per rij (v−v₀)/t′.'],
         kop=['stip','t (s)','x (m)','Δx in 0,040 s (m)','t′ (s)','vₜ via ⟨v⟩ (m/s)','(vₜ−v₀)/t′ (m/s²)'],
         rijen=_ticker_rows(9,0.040,stride=2,x0=True),tabel_uitleg=_TICKER_NOTE,
         grafieken=['x(t) uit t,x; beschrijf waarom de kromme geen rechte is.',
                    'v(t′) uit de twee aangrenzende kolommen t′,vₜ: snijpunt is v₀, rico is a.'],
         verwerking='Extrapoleer v₀ uit het assensnijpunt en bereken a eerst uit één grote driehoek op de trendlijn, daarna als gemiddelde van (vₜ−v₀)/t′. De nulpuntkeuze betekent niet v₀ = 0.',
         vragen=['Waarom is v₀ op de gekozen stip 0 niet nul?',
                 'Wat betekenen snijpunt en rico van v(t′)? Waarom is t′ niet de intervalduur Δt?'])
p=LABOS[1]['delen'][1]
p.update(titel='Deel 2 – Oorspronkelijk OPEN practicum: eenparig vertraagde beweging omhoog',
         nieuw_blad=True,
         open_opdracht=[
          'Onderzoek met het eigen wagentje en de tijdtikker of de beweging op een stijgende helling na het LOSLATEN eenparig vertraagt. Jij kiest de meetstrategie, de veilige helling, het passende duwtje, de nulstip, herhalingen en controlevariabelen.',
          'Behoud de originele proefopstelling: baan circa 1 m, wagentje met ballast (bron: 3 × 50 g), verticale bevestigingsstift, 50 Hz-tijdtikker, carbonlint, papierband, blokken en een gecontroleerde 6 V~ wisselspanningsbron. Laat plan en nulstip vóór het opmeten controleren.',
          'Randvoorwaarde: gebruik uitsluitend de stijgende fase NA loslaten en VÓÓR het keerpunt; meet elke twee tikken (Δt = 0,040 s). Leg zelf uit hoe je uit het bandje x(t) en v(t′) maakt.'],
         stappen=[
          'Ontwerp en noteer eerst je eigen reproduceerbare werkwijze. Oefen een veilig duwtje naar ongeveer de bovenkant van de baan ZONDER bandje; plaats een vangblok en houd een hand klaar om de wagen bovenaan veilig op te vangen.',
          'Laat de leerkracht de helling, voeding, handpositie en je plan goedkeuren. Bevestig het bandje, start de tijdtikker, geef het afgesproken duwtje en laat volledig los.',
          'Verantwoord zelf op het originele bandje waar stip 0 mag liggen: niet tijdens handcontact en niet na het keerpunt. Kleef recht, nummer 0, 2, 4 …, meet x en noteer t in de eigen tabel.',
          'Bereken Δx per 0,040 s, t′ en vₜ. Maak x(t) en v(t′) ONDER elkaar in Excel, met de corresponderende tabel links van elke grafiek; voeg trendlijn en vergelijking toe.',
          'Verklaar met de gekozen positieve richting het teken van snelheid en versnelling, en vergelijk de v(t′)-rico met de dalende-rit bij dezelfde baanhelling.'],
         kop=['stip','t (s)','x (m)','Δx in 0,040 s (m)','t′ (s)','vₜ via ⟨v⟩ (m/s)','a uit v(t′) (m/s²)'],
         rijen=_ticker_rows(9,0.040,stride=2,x0=True),tabel_uitleg=_TICKER_NOTE,
         grafieken=['x(t) en v(t′) onder elkaar met de bijbehorende tabel LINKS van elke grafiek (bron blz. 91).',
                    'Voeg aan beide grafieken een trendlijn met vergelijking toe; interpreteer het NEGATIEVE hellingsgetal van v(t′).'],
         verwerking='Een open practicum vraagt een eigen vooraf goedgekeurd plan én bewijs: origineel bandje met gekozen stip 0, ingevulde bronkolommen, twee Excel-grafieken, vergelijking en foutenanalyse.',
         vragen=['Waarom mag je de eerste stip tijdens het duwtje niet als meetnul kiezen?',
                 'Hoe herken je uit de trendlijn dat de opwaartse snelheid eenparig kleiner wordt?'])

# Labo 3: bron 20–26 / 73–78 (val); 15–20 / 58–61 (worp).
p=LABOS[2]['delen'][0]
p.update(titel='Deel 1 – Oorspronkelijk practicum: vrije val met triller en bandje',
         nieuw_blad=True,
         stappen=[
          'Klem de tijdtikker/triller aan een groot statief (dubbelnoot), controleer de passende voeding en leid een circa 1,5 m lang papierbandje RECHT door het toestel. Kleef onderaan circa 50 g vast en plaats een zachte opvangmat.',
          'Laat de triller eerst heel even op snelheid komen; laat het bandje met de massa daarna zonder extra duw los. Zet de voeding na de opname uit, kleef het bandje recht op de tafel en bewaar het.',
          'Kies stip 0 bij het begin van de vrije beweging. Nummer ELKE tik (Δt = 0,020 s) en meet x op het bandje vanaf een duidelijk nulpunt.',
          'Bereken per venster Δx en vₜ = Δx/0,020 s. Ken die snelheid toe aan de middentijd t′: 0,010; 0,030; 0,050 s …, NIET aan de tijd van een stip.',
          'Maak Excel-grafieken v(t′) en x(t). Bepaal g uit de rico van v(t′), vergelijk met ongeveer 9,81 m/s² en bespreek waarom vₜ op een middentijd de ogenblikkelijke snelheid bij constante a benadert.'],
         kop=['stip','t (s)','x (m)','Δx in 0,020 s (m)','t′ (s)','vₜ via ⟨v⟩ (m/s)','vₜ/t′ (m/s²)*'],
         rijen=_ticker_rows(17,0.020,x0=True),tabel_uitleg=_TICKER_NOTE+' *Laatste kolom alleen als de gekozen stip 0 praktisch samenvalt met het loslaten (v₀ ≈ 0); anders bepaal je g uit de rico van v(t′).',
         grafieken=['v(t′): selecteer alleen de direct aangrenzende kolommen t′ en vₜ; rico ≈ g.',
                    'x(t): gebruik t en x; vergelijk de kromming met x = ½gt² wanneer v₀ ≈ 0.'],
         verwerking='Toon één voorbeeld van Δx, t′ en vₜ met eenheden. Kies bij een niet-nul startsnelheid g uit de trendlijn in plaats van uit vₜ/t′.',
         vragen=['Waarom staan 0,010; 0,030; 0,050 s in de kolom t′, terwijl stippen op 0,000; 0,020; 0,040 s liggen?',
                 'Welke grootheid levert de rico van v(t′), en waarom kan vₜ/t′ fout zijn als de eerste stip pas na het loslaten gekozen is?'])
p=LABOS[2]['delen'][1]
p.update(titel='Deel 2 – Oorspronkelijk practicum: verticale worp, HANDMATIGE meetmethode',
         nieuw_blad=True,bron='15–18 en 58–59',
         vraag='Wat zijn de beginsnelheid, snelheid vlak voor de grond en maximale hoogte bij jouw verticale tennisbalworp?',
         stappen=[
          'Plaats TWEE meetlatten verticaal vanaf de vloer of op exact gemeten hoogte boven de vloer. Kies y = 0 op de vloer (of de bovenkant van de rustende bal) en spreek een loslaathoogte y₀ af, bijvoorbeeld 0,30 m.',
          'Zet twee stabiele smartphones/camera’s op: één filmt de regio van het hoogste punt, één de regio van de loslaathoogte. Houd in beide opnames de meetlat ongeveer even ver van de camera als de bal (parallaxcontrole).',
          'Verdeel de bronrollen: werper, timer, filmer hoogste punt, filmer loslaten; bij 2–3 leerlingen mogen rollen gecombineerd worden zonder het protocol te wijzigen. Werp de tennisbal zo verticaal mogelijk; meet met de stopwatch de TOTALE tijd t van loslaten tot de grond.',
          'Pauzeer de beelden op loslaten en hoogste punt. Lees y₀ en de GEMETEN maximale hoogte y_max met dezelfde rand van de bal af; herhaal de worp drie keer.',
          'Neem de positieve y-richting omhoog en g = 9,81 m/s². Bereken v₀ uit 0 = y₀ + v₀t − ½gt², v_grond = v₀ − gt, t_top = v₀/g en y_max,berekend = y₀ + v₀t_top − ½g t_top². Vergelijk de berekende hoogte met het filmbeeld.'],
         kop=['herhaling','y₀ uit loslaatfilm (m)','t tot vloer (s)','y_max uit topfilm (m)','v₀ (m/s)','v_grond (m/s)','t_top (s)','y_max,berekend (m)'],
         rijen=3,
         tabel_uitleg='Hier is t_top de berekende tijd tot de top van de WORP; dit is niet de middentijd t′ van de tijdtikker in deel 1.',
         grafieken=['Bij dit oorspronkelijke handmatige deel maak je eerst de hoogte- en tijdvergelijking; de volledige y(t)-grafiek volgt in Tracker in deel 3.'],
         verwerking='Werk de vier bronberekeningen uit en bereken per herhaling het verschil tussen de gefilmde en berekende tophoogte.',
         vragen=['Waarom moeten bal en meetlat ongeveer in hetzelfde cameravlak staan?',
                 'Waarom is v_grond negatief wanneer omhoog de positieve y-richting is?'])
LABOS[2]['delen'].append(dict(
    titel='Deel 3 – Oorspronkelijk practicum: volledige verticale worp met Tracker',
    bron='19–20 en 60–61',nieuw_blad=True,
    vraag='Leveren Tracker en de handmatige proef vergelijkbare y₀, v₀ en maximale hoogte?',
    stappen=[
     'Film een nieuwe verticale tennisbalworp van VÓÓR het loslaten tot NA het bereiken van de grond in één stabiele opname. Zet een verticale meetlat volledig in beeld, in hetzelfde vlak als de bal.',
     'Open het videobestand in Tracker, kalibreer de afstand met de meetlat en kies dezelfde oorsprong y = 0 op de vloer als in deel 2. Markeer tijdens de HELE beweging telkens dezelfde rand of het massamiddelpunt van de bal.',
     'Exporteer de Tracker-tabel met frame, tijd en y naar Excel; maak een XY-spreidingsgrafiek y(t) met punten. Bepaal y₀, y_max, v₀ en v_grond; toon de gebruikte berekening of modelvergelijking.',
     'Vergelijk Tracker met deel 2 voor y₀, t_top en y_max. Bespreek invloed van reactietijd, beeldfrequentie, schaal, camera-parallax en keuze van het gevolgde punt.'],
    kop=['frame','t (s)','y (m)','vᵧ (m/s)'],rijen=12,
    tabel_uitleg='Gebruik voor de video de door Tracker geëxporteerde echte frametijden; de 0,020 s-tiktijd uit het vrije-vallabo geldt NIET voor een camera.',
    grafieken=['y(t) uit de Tracker-gegevens in Excel: afzonderlijke meetpunten, gepaste trend en vergelijking.'],
    verwerking='Maak een vergelijkingstabel handmatig versus Tracker en geef per verschil een concrete meetoorzaak.',
    vragen=['Welke instelling kalibreert de schaal in Tracker en waarom moet de meetlat in het bewegingsvlak staan?',
            'Welke van de twee methoden geeft doorgaans de betrouwbaardere volledige baan, en waarom?']))
LABOS[2]['materiaal']=['deel 1: 50 Hz-triller/tijdtikker op groot statief, dubbelnoot, veilige voeding, twee snoeren, papierbandje ca. 1,5 m, circa 50 g massa, kleefband, rolmeter en zachte opvangmat',
                         'deel 2: tennisbal, twee VERTICALE meetlatten, stopwatch, twee smartphones op stabiele steunen voor loslaten en top',
                         'deel 3: één stabiele camera/smartphone die de hele baan filmt, zichtbare meetlat, computer met Tracker en Excel']
LABOS[2]['sturing']='Bronprotocol blijft intact: vrije val met triller; daarna de eigen verticale worp eerst handmatig met twee camera’s en stopwatch, dan de hele worp met Tracker; meetkeuzes en foutenanalyse door leerling.'

# Labo 4: de eigen open horizontale Trackerworp én de geverfde kogelbaan.
LABOS[3]['sturing']='Deel 1 OPEN: ontwerp zelf de volledige horizontale Trackerworp (bron blz. 56–57). Deel 2 BEGELEID: oorspronkelijke kogel/valgeul/verfproef op de plank (blz. 93–97).'
p=LABOS[3]['delen'][0]
p.update(titel='Deel 1 – Oorspronkelijk OPEN practicum: horizontale worp met Tracker',nieuw_blad=True,
         open_opdracht=[
          'Ontwerp ZELF de volledige opstelling en werkwijze om de balworp met Tracker te filmen en te analyseren. Kies uit eigen voorstel wat je meet (plaats, snelheid, versnelling), hoe je die berekent en welke formules je nodig hebt; leg dit vooraf ter goedkeuring voor.',
          'Beschikbare bronmiddelen: computer met Tracker, camera/smartphone, tennisbal, statief of stabiel oppervlak en zichtbare meetlat met cm-verdeling. Zorg voor een veilige opvang, een stabiele opname van de VOLLEDIGE worp en minimale parallax.'],
         stappen=[
          'Teken jouw eigen onderzoeksopzet, met assen, oorsprong, kalibratie en meetstrategie. Beslis zelf welke variabelen, formules en Tracker-data de horizontale en verticale component toetsbaar maken.',
          'Laat plan, camerastandpunt, meetlat in het baanvlak en veilige opvang vóór de uitvoering goedkeuren.',
          'Voer je eigen worp uit, bewaar de film, markeer de bal consequent in Tracker en exporteer je gekozen dataset met frametijden.',
          'Analyseer de volledige beweging: beschrijf horizontale én verticale positie, snelheid en eventuele versnelling. Maak bruikbare grafieken en trek een besluit over je oorspronkelijke onderzoeksvraag.'],
         kop=['frame','t (s)','x (m)','y (m)','vₓ (m/s)','vᵧ (m/s)'],rijen=10,
         tabel_uitleg='Dit is een hulpmiddel voor je EIGEN onderzoeksplan, niet een voorgeschreven meetreeks. Geef t, x en y (en berekende v indien gekozen) steeds met eenheid en de gekozen positieve richting.',
         grafieken=['Ontwerp zelf passende grafieken voor de horizontale en verticale component (bijvoorbeeld x(t), y(t) en y(x)).'],
         verwerking='Onderbouw het besluit met je zelf gekozen modellen, meetresultaten en onzekerheden; het verslag bevat het vooraf goedgekeurde onderzoeksplan.',
         vragen=['Hoe beperk je perspectieffouten als bal en meetlat in de video worden gevolgd?',
                 'Welke twee componenten verwacht je bij een horizontale worp zonder noemenswaardige luchtweerstand?'])
p=LABOS[3]['delen'][1]
p.update(titel='Deel 2 – Oorspronkelijk practicum: geverfde kogelbaan op schuine plank',nieuw_blad=True,
         stappen=[
          'Kleef één groot blad (of vier A4-bladen) op de circa 45 × 55 cm plank. Plaats de kleine valgeul EVENWIJDIG aan de bovenrand; laat de grote metalen kogel op papier een spoor maken met weinig afwasbare verf. Voorkom spatten en vang de kogel op.',
          'Vergelijk eerst de twee bewegingen afzonderlijk: plank VLAK, kogel BOVENAAN de kleine geul loslaten (ERB in x); plank SCHUIN, kogel BENEDEN op de kleine geul loslaten (EVRB in y). Noteer of schets beide sporen.',
          'Combineer nu beide: plank SCHUIN, kogel BOVENAAN dezelfde geul loslaten. Herhaal voor DRIE plankhellingen door het aantal houten blokken te veranderen; noteer het hoogteverschil per helling.',
          'Teken op elk spoor x- en y-assen door het startpunt. Meet x = 10, 15, 20 … 55 cm en construeer de corresponderende y evenwijdig aan de assen, ook wanneer x en y op papier niet perfect loodrecht staan.',
          'Vul voor elke x de drie gemeten y-waarden in en bereken y₁/x², y₂/x² en y₃/x²; maak voor de drie hellingen y(x) en een passend model.'],
         kop=['x (cm)','y₁ helling 1 (cm)','y₂ helling 2 (cm)','y₃ helling 3 (cm)','y₁/x² (1/cm)','y₂/x² (1/cm)','y₃/x² (1/cm)'],
         rijen=[str(x) for x in range(10,56,5)],
         grafieken=['Vergelijk de drie kogelsporen y(x). Controleer per helling of y/x² ongeveer constant blijft.'],
         verwerking='Behoud de drie beschilderde papieren sporen als bewijs, met plankenhoek, assen, 10–55 cm meetpunten en besluit waarom de combinatie ERB+EVRB een parabool is.',
         vragen=['Waarom moet de valgeul evenwijdig staan met de bovenrand van de plank?',
                 'Waarom helpt een constructielijn evenwijdig aan de y-as als de op papier getekende assen niet precies loodrecht staan?'])

# Labo 5: Newton blijft de originele katrol/schijfjes/tijdtikkerproef.
# De samenvatting wordt gekoppeld aan een echt invulbaar bandjesjabloon.
_raw_tape=dict(titel='Voorbeeldbandje per kracht- of massareeks (kopieer dit tabelformaat in Excel voor ELKE rit)',
               kop=['stip','t (s)','x (m)','Δx in 0,040 s (m)','t′ (s)','vₜ (m/s)','a uit trendlijn (m/s²)'],
               rijen=_ticker_rows(9,0.040,stride=2,x0=True))
for p in LABOS[4]['delen'][:2]:
    p['tabel_uitleg']='Bereken a uit de rico van v(t′) op een ECHT tijdtikkerbandje; '+_TICKER_NOTE
    p['extra_tabellen']=[_raw_tape]
    p['grafieken']=['Per rit een Excel v(t′)-grafiek: t′ en vₜ staan direct naast elkaar; bepaal a uit de rico. Vat de verkregen a-waarden daarna samen in de tabel erboven.']
LABOS[4]['delen'][0]['stappen'][0]='Behoud de eigen katrolopstelling: verplaats bij 2, 3, 4 en 5 schijfjes van 10,0 g de NIET-hangende schijfjes naar het wagentje, zodat de totale bewegende massa inclusief hangmassa constant blijft; gebruik de extra 150 g ballast uit de bron om wrijving te beperken.'
LABOS[4]['delen'][1]['stappen'][0]='Laat precies twee schijfjes van 10,0 g aan de hangzijde; vergeet hun massa niet bij m_tot. Gebruik het bronwagentje (50,0 g) met achtereenvolgens 50,0; 100,0; 150,0; 200,0 g ballast.'

# Labo 6: de bron HOUDT de lengte van de baan constant en stelt per hoek h=l sin α in.
# Een gelijke eindhoogte voor alle hoeken (vorig concept) zou een andere proef zijn.
p=LABOS[5]['delen'][0]
p.update(stappen=[
   'Meet de vaste BAANLENGTE l van het originele hellend vlak (ongeveer 40 cm) en de massa van het wagentje (bron 100 g). Bepaal voor α = 30°, 45° en 60° telkens de in te stellen hoogte h = l·sin α; de hoogte is dus NIET bij elke hoek gelijk.',
   'Stel de plank voor elk van de drie hoeken in via de berekende h en controleer de werkelijke hoogte met de meetlat.',
   'Trek hetzelfde wagentje per hoek eenmaal verticaal over h en eenmaal traag langs de helling over de vaste lengte l; meet F_vert en F_hel met dezelfde dynamometer.',
   'Bereken voor ELKE hoek W_vert = F_vert·h en W_hel = F_hel·l. Vergelijk kracht, weg en geleverde arbeid; verklaar een verschil door wrijving.'],
   kop=['α (°)','h = l sin α (m)','F_vert (N)','h (m)','F_hel (N)','l (m)','F_vert·h (J)','F_hel·l (J)'],
   rijen=['30','45','60'],
   verwerking='Vergelijk per hoek de twee producten F_vert·h en F_hel·l; een kleinere kracht werkt over een langere weg. De eindhoogte varieert in deze bronproef per hoek.',
   vragen=['Waarom verandert de hoogte h als l constant blijft en α van 30° naar 60° verandert?'])

# Labo 9: exacte bronreeksen voor beide veren en een apart vrij instructieblad.
p=LABOS[8]['delen'][0]
p.update(stappen=[
  'Veer 1 (soepele veer): hang na elkaar 30,0; 60,0; 90,0; 120,0; 150,0 g; meet de statische uitrekking Δy, bepaal F_z en k = F_z/Δy, en bereken het gemiddelde k₁.',
  'Meet met dezelfde vijf massa’s per keer de tijd van een gekozen vast aantal (bv. 20) kleine trillingen; bepaal T_gem, bereken T = 2π√(m/k₁) en de procentuele afwijking.',
  'Veer 2 (minder soepele veer): herhaal met de oorspronkelijke reeks 50,0; 100,0; 150,0; 200,0; 250,0 g; bepaal k₂, T_gem, T_berek en de procentuele afwijking.',
  'Bespreek waarom de grootste afwijking bij de kleinste massa kan optreden (masssa van de veer, reactietijd); maak voor elke veer een passende grafiek.'],
  kop=['veer','m (g)','F_z (N)','Δy (m)','k = F_z/Δy (N/m)','t₂₀ (s)','T_gem (s)','T_berek (s)','afwijking (%)'],
  rijen=[['veer 1',str(m),'','','','','','',''] for m in (30,60,90,120,150)] +
        [['veer 2',str(m),'','','','','','',''] for m in (50,100,150,200,250)])
p=LABOS[8]['delen'][1]
p.update(open_opdracht=['Bepaal een onbekende massa zonder balans. De onbekende massa mag NIET van de veer gehaald worden. Je mag gekende massa’s toevoegen (bron: vier maal 50,0 g), een veer, chronometer en meetlat gebruiken. Maak EERST jouw eigen instructieblad en voer het DAARNA zelf uit.'],
         tabel_uitleg='De onbekende massa blijft de hele tijd aan de veer; voeg telkens alleen een gekende massa toe.',
         stappen=['Schrijf je eigen instructieblad met meetplan, veiligheid, voorbeeldberekening en tabel; laat goedkeuren.',
                  'Houd de onbekende massa steeds aan dezelfde veer, voeg achtereenvolgens gekende massa’s toe en meet T per stap.',
                  'Gebruik T² tegen toegevoegde massa en/of een correcte fysische redenering om de onbekende massa te bepalen zonder een balans.',
                  'Vul en evalueer je eigen instructieblad: is de uitkomst reproduceerbaar?'])
p=LABOS[8]['delen'][2]
p.update(kop=['stip','t (s)','y (m)','Δy in 0,020 s (m)','t′ (s)','vₜ (m/s)'],
         rijen=_ticker_rows(18,0.020,last_col=False),
         tabel_uitleg=_TICKER_NOTE+' Voor de halve harmonische trilling wordt vₜ berekend uit Δy/0,020 s (teken volgens gekozen y-richting).',
         grafieken=['y(t) én v(t′) op afzonderlijke grafieken uit dezelfde bronregistratie.'])

# Labo 10: oorspronkelijke slingerproef: 10°/5°, houten/metalen bolletje,
# circa TIEN lengten en vergelijking T(l), T²(l), T²/l en g.
p=LABOS[9]['delen'][0]
p.update(stappen=['Stel de lengte van het metalen bolletje in op 1,00 m (ophangpunt tot zwaartepunt). Houd massa en lengte vast.',
                  'Meet voor een amplitude van circa 10° de tijd voor 20 hele cycli, start de stopwatch bij doorgang door de evenwichtsstand en tel daar vanaf nul. Herhaal drie keer.',
                  'Halveer de hoek tot circa 5° en herhaal dezelfde drie metingen van 20 cycli.',
                  'Vergelijk de twee gemiddelden binnen de meetonzekerheid.'],
         kop=['amplitude (°)','t₂₀,1 (s)','t₂₀,2 (s)','t₂₀,3 (s)','T_gem (s)'],
         rijen=['10','5'])
p=LABOS[9]['delen'][1]
p.update(stappen=['Laat de 1,00 m touwlengte en de hoek van hoogstens 10° gelijk. Meet eerst met het metalen bolletje en daarna met een houten bolletje.',
                  'Meet bij elk bolletje driemaal de tijd voor 20 perioden, bereken T_gem en vergelijk de resultaten binnen de onzekerheid.'],
         kop=['bolletje','t₂₀,1 (s)','t₂₀,2 (s)','t₂₀,3 (s)','T_gem (s)'],rijen=['metaal','hout'])
p=LABOS[9]['delen'][2]
p.update(stappen=['Gebruik opnieuw het metalen bolletje; kies circa TIEN slingerlengten, gemeten van ophangpunt tot massamiddelpunt. Houd de hoek kleiner dan 10°.',
                  'Meet per lengte de tijd voor 20 perioden en bereken T, T², T²/l en g = 4π²l/T².',
                  'Maak eerst T(l), daarna T²(l) in Excel; bepaal de vergelijking van de tweede trendlijn en vergelijk de gemiddelde g met 9,81 m/s².'],
         kop=['l (m)','t₂₀ (s)','T (s)','T² (s²)','T²/l (s²/m)','g (m/s²)'],rijen=10,
         grafieken=['Eerst T(l), dan T²(l); bepaal g per rij en via de rico van T²(l).'])

# Labo 1, deel 1: ook de luchtbelproef volgt de werkelijke bron (p. 63–67):
# twee buisstanden, tien afstanden en dezelfde voorzijde van de luchtbel.
p=LABOS[0]['delen'][0]
p.update(titel='Deel 1 – Oorspronkelijk practicum: luchtbel bij 90° en 45°',
         nieuw_blad=True,
         vraag='Is Δx/Δt ongeveer constant bij dezelfde buisstand en hoe verandert die verhouding tussen 90° en 45°?',
         stappen=[
          'Zet de vloeistofbuis op haar houten lat stevig VERTICAAL (90° met de horizontale). Gebruik de gradenboog en laat statief en klem controleren.',
          'Gebruik consequent de VOORKANT van de luchtbel als referentie voor starten en stoppen. Meet achtereenvolgens de tijd Δt voor Δx = 10,0; 20,0; …; 100,0 cm op de schaal.',
          'Stel dezelfde buis met dezelfde luchtbel in op 45° met de horizontale; meet voor DEZELFDE tien afstanden opnieuw Δt. Vul tijden en v = Δx/Δt voor BEIDE buisstanden in.',
          'Teken beide reeksen in ÉÉN x(t)-spreidingsdiagram met twee aparte rechte trendlijnen, bepaal hun rico’s en vergelijk de snelheid bij 90° en 45°.'],
         kop=['Δx (m)','Δt 90° (s)','v 90° = Δx/Δt (m/s)','Δt 45° (s)','v 45° = Δx/Δt (m/s)'],
         rijen=[[f'{i/10:.3f}'.replace('.',','),'','','',''] for i in range(1,11)],
         grafieken=['Beide standen in ÉÉN x(t)-spreidingsgrafiek met legendes 90° en 45°; x = Δx en t = Δt omdat je vanaf nul meet.'],
         verwerking='Bepaal bij beide standen de gemiddelde verhouding Δx/Δt en de helling van x(t). Wat is het verband tussen buishelling en luchtbelsnelheid?',
         vragen=['Waarom moet je telkens dezelfde VOORKANT van de luchtbel volgen?',
                 'Waarom mag je hier x = Δx en t = Δt noteren als je vanaf dezelfde nulpositie meet?'])
LABOS[0]['materiaal'][0]='luchtbel in vloeistofbuis op houten lat met schaal 0–100 cm, gradenboog, chronometer, statief, dubbelnoot en klem (bron blz. 63–64)'
LABOS[0]['onderzoek']='Hoe hangen x(t) en de snelheid van dezelfde luchtbel samen bij 90° en 45° van de buis, en is de elektrisch aangedreven wagen in zijn gelijkmatige middenfase een ERB, gemeten met chronometer en 50 Hz-tijdtikker tijdens dit labo?'
LABOS[0]['mc'][1]='Hoe hangen x(t) en de snelheid van dezelfde luchtbel samen bij 90° en 45° van de buis, en is de elektrisch aangedreven wagen in zijn gelijkmatige middenfase een ERB, gemeten met chronometer en 50 Hz-tijdtikker tijdens dit labo?'

# Ook de andere bronproeven behouden hun concrete activiteiten, niet alleen
# algemene 'golven' en 'geluid': golfbakbron p. 1 + 27–28; Soundry p. 55–56.
p=LABOS[11]['delen'][0]
p['stappen']=[
 'Applet (bron blz. 1): maak afzonderlijke schermafbeeldingen van puntbron met lage en hoge f, vlakke golf, 10 en 20 puntbronnen op een rij, Huygens bij smalle en brede opening, twee coherente bronnen in fase en tegenfase, en twee niet-coherente bronnen.',
 'Fysieke opstelling (bron blz. 27–28): plaats de golfbak op een overheadprojector of veilig gelijkwaardig projectiesysteem; vul met gedestilleerd water en laat stil worden. Houd alle elektrische kabels droog.',
 'Experiment 1: raak het wateroppervlak met de puntbron aan de elektromagnetische triller/frequentiegenerator en fotografeer de muurprojectie. Meet λ met de projectieschaal.',
 'Experiment 2: vervang door een staafvormige bron; fotografeer vlakke golffronten.',
 'Experiment 3 en 4: plaats weekijzeren kernen als smalle en vervolgens brede opening vóór de staafbron; fotografeer en verklaar de buiging.',
 'Experiment 5: bevestig twee coherente puntbronnen aan dezelfde triller (bv. met een latje), fotografeer de interferentie en vergelijk met de applet.' ]
p['grafieken']=['Zet voor elk van de vijf fysieke experimenten foto, opstelling, frequentie en uitleg bij de bijbehorende appletafbeelding.']
p['vragen']=['Welke bronopstelling in de fysieke golfbak levert nagenoeg rechte golffronten?',
              'Waarom moeten twee fysieke puntbronnen aan dezelfde triller bevestigd zijn voor een stabiel interferentiepatroon?']
p=LABOS[12]['delen'][0]
p['titel']='Deel 1 – The Soundry: beats en golfinterferentie (geteste vervangapp toegestaan)'
p['stappen']=[
 'Gebruik het oorspronkelijk Soundry-geluidlab indien nog bereikbaar; anders dezelfde opdrachten in een door de leerkracht VOORAF geteste app op laag volume. Noteer appnaam, versie en datum.',
 'BEATS: luister afzonderlijk naar 437 Hz en 443 Hz; combineer beide en leg periodieke zwevingen uit. Vergelijk ook twee tonen van dezelfde frequentie en twee andere ongelijke frequenties.',
 'WAVE: maak schermafbeeldingen van één golf, twee gelijke golven in fase en een golf met zijn tegengestelde (tegenfase); vergelijk optelling, versterking en uitdoving.',
 'Bewaar per situatie frequenties, fase, golfvorm/schermafbeelding en een toelichting in eigen woorden.' ]
p['kop']=['signaal','f₁ (Hz)','f₂ (Hz)','fase','uitkomst / beats (Hz)','schermafbeelding']
p['rijen']=[['toon A','437','','','',''],['toon B','443','','','',''],['A+B','437','443','','',''],
            ['gelijke tonen','','','','',''],['tegenfase','','','','','']]
p['vragen']=['Wat hoor je bij de afzonderlijke tonen 437 Hz en 443 Hz, en welke zwevingsfrequentie verwacht je bij hun combinatie?',
              'Wat gebeurt er bij twee gelijke, respectievelijk tegengestelde golven? Noem een toepassing van uitdoving.']
LABOS[12]['delen'].append(dict(
 titel='Deel 3 – Bronopdracht: harmonischen, golfvormen en ultrasoon geluid',
 bron='55–56',nieuw_blad=True,
 vraag='Wat maakt de golfvorm van een instrument anders, en wat is ultrasoon geluid?',
 stappen=['Gebruik de historische harmonics-applet uit de bron alleen indien die veilig en bereikbaar is; anders een vooraf geteste simulator met sinus, zaagtand, blokgolf en instrumentklanken. Noteer de gebruikte app.',
           'Zoek in een betrouwbare bron wat een harmonische is; bekijk een zuivere sinus, een willekeurig samengesteld signaal, klarinet en trompet. Schets en label de golfvormen.',
           'Stel een zaagtand en een blokgolf in; maak een schets of schermafbeelding van elk en leg uit welke harmonischen het verschil in klankkleur verklaren.',
           'Zoek met bronvermelding de definitie van ultrasoon geluid en minstens twee toepassingen; geef de frequentiegrens in Hz.'],
 kop=['signaal','grondfrequentie (Hz)','golfvorm: schets / afbeelding','harmonischen / klankkleur'],
 rijen=['zuivere sinus','klarinet','trompet','zaagtand','blokgolf'],
 verwerking='Benoem de harmonischen in de toon en beschrijf het effect op de klankkleur. Gebruik geen ongecontroleerde of verdwenen URL als zogenaamd gemeten bron.',
 vragen=['Wat is een harmonische toon en hoe beïnvloedt de harmonischenmix de klankkleur van klarinet en trompet?',
         'Wat is ultrasoon geluid? Geef twee toepassingen met bronvermelding.']))

# Onderzoeksvragen en doelteksten horen bij de werkelijk uit te voeren bronproef.
LABOS[5]['context']='Met hetzelfde originele hellend vlak (vaste baanlengte l) til je het wagentje voor 30°, 45° en 60° telkens over de bijbehorende hoogte h = l sin α. Binnen elke hoek vergelijk je verticaal en langs de helling; tussen de hoeken verandert h.'
LABOS[5]['onderzoek']='Hoe verschillen F_vert·h en F_hel·l voor hetzelfde wagentje bij een vaste baanlengte l en drie hoeken (30°, 45°, 60°, elk met h = l sin α), gemeten met dynamometer en meetlat tijdens dit labo?'
LABOS[5]['doelen']=['de hoogte h per hoek afleiden uit de vaste baanlengte l en α',
                    'bij iedere hoek F_vert over h vergelijken met F_hel over l',
                    'de arbeid F·s met eenheid J berekenen en een eventueel verschil door wrijving verklaren']
LABOS[8]['onderzoek']='Hoe veranderen k en T bij veer 1 (30–150 g) en veer 2 (50–250 g), en hoe bepaal je daarna een onbekende massa zonder balans terwijl ze aan de veer blijft, gemeten met chronometer tijdens dit labo?'
LABOS[9]['onderzoek']='Hoe verandert de periode T van de eigen slinger bij 10° versus 5°, metalen versus houten bolletje op 1,00 m, en bij circa tien verschillende slingerlengten, gemeten als tijd voor 20 cycli tijdens dit labo?'
LABOS[2]['onderzoek']='Wat is g uit een 50 Hz-bandje van een vrijvallende massa en welke v₀, t_top en y_max leveren de originele handmatige en Tracker-methoden bij een verticale tennisbalworp tijdens dit labo?'
LABOS[3]['onderzoek']='Welke positie-, snelheids- en versnellingscomponenten vind je uit een zelf ontworpen horizontale Trackerworp, en tonen drie kogelsporen op de schuine plank y ∝ x² tijdens dit labo?'

# Per apart afdrukbaar bronpracticum de eigen materialen herhalen.
LABOS[0]['delen'][1]['materiaal_deel']='eigen elektrisch wagentje met schakelaar, rechte baan, 50 Hz-tijdtikker, carbonlint, papierbandje, voltmeter en gecontroleerde 6 V~-bron (p. 68).'
LABOS[1]['delen'][0]['materiaal_deel']='wagentje 50 g met ballast circa 200 g, helling van circa 1 m, tijdtikker, 1,10 m papierbandje, carbonlint, lange lat en gecontroleerde voeding (p. 79).'
LABOS[1]['delen'][1]['materiaal_deel']='wagentje met drie ballastmassa’s van 50 g en verticaal staafje, helling van circa 1 m, blokken, tijdtikker, papierbandje, carbonlint en veilige 6 V~-bron (p. 86).'
LABOS[2]['delen'][1]['materiaal_deel']='tennisbal, twee verticale meetlatten, stopwatch, twee stabiele smartphones/camera’s bij loslaathoogte en hoogste punt (p. 15–18/58–59).'
LABOS[2]['delen'][2]['materiaal_deel']='computer met Tracker, smartphone/camera op statief, tennisbal en duidelijk zichtbare meetlat in dezelfde bewegingsvlakte (p. 19–20/60–61).'
LABOS[3]['delen'][0]['materiaal_deel']='computer met Tracker, camera/smartphone, tennisbal, statief of stabiel oppervlak en stevige cm-meetlat (p. 56–57).'
LABOS[3]['delen'][1]['materiaal_deel']='houten plank circa 45 × 55 cm, blokken, valgeul, grote metalen kogel, papier, weinig afwasbare verf, tekenlat en driehoek (p. 93).'
LABOS[12]['delen'][2]['materiaal_deel']='historische Soundry-/harmonics-app indien bereikbaar, anders een vooraf geteste simulator en een bron voor ultrasoon geluid (p. 55–56).'
