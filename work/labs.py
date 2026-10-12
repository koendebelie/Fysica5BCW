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
