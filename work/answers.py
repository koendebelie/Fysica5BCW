# -*- coding: utf-8 -*-
"""Modelantwoorden; uitsluitend gebruiken bij build.py --teacher."""

ANSWERS = {
 'L9:deel3:vraag1': 'Niet constant: dicht opeen bij keerpunten en verder uiteen bij de evenwichtsstand; geen ERB.',
 'L9:deel3:vraag2': 'Bij benadering sinusvormige y(t) en cosinusvormige v(t), met een kwart periode faseverschil.',
 'L9:deel3:vraag3': 'In de evenwichtsstand: potentiële veerenergie is daar minimaal en kinetische energie maximaal.',
 'L9:deel3:vraag4': 'A = (y_max − y_min)/2; bij een correct afgebakende halve trilling tussen uiterste standen is T = 2 × de gemeten duur; meetwaarden verschillen per proef.',
 'L9:deel3:vraag5': 'v_max = 2πA/T in m/s; afwijkingen volgen uit eindige 0,020 s-tikintervallen, schaal-/afleesfouten en demping.','L10:SMART': 'Hoe hangt de periode T van een slinger af van amplitude (5–20°), massa van het bolletje en '
              'lengte l (0,20–0,80 m), gemeten met stopwatch bij dezelfde lokale g, tijdens dit labo?',
 'L10:docent': ['Bron meet amplitude, massa, lengte elk afzonderlijk; niet alleen l.',
                "De dia's van theorie 11 tonen T/√l ≈ 2,01 s/√m (lokaal g ≈ 9,81).",
                'Bij korte slinger wordt lengte-onzekerheid door straal bol relatief groter.',
                'Stopwatch: 20 periodes × 3 herhalingen.'],
 'L10:orientatie:1': 'T ∝ √l bij kleine hoek; T² ∝ l.',
 'L10:orientatie:2': 'Start/stopreactietijd weegt relatief minder op de gemeten tijd.',
 'L10:reflectie:1': 'In de bewegingsvergelijking valt m weg: zwaartekracht en traagheid schalen beide met '
                    'massa.',
 'L10:reflectie:2': 'T verdubbelt: T ∝ √l.',
 'L10:reflectie:3': 'Bijvoorbeeld schommel of Foucault-slinger; correct verklaren en bron vermelden.',
 'L10:reflectie:4': 'Je maakt de beginvoorwaarde minder reproduceerbaar en vergroot de amplitude.',
 'L10:reflectie:5': 'sin θ is dan niet precies θ (in radialen); de periode groeit licht met amplitude.',
 'L10:voor:1': 'Van ophangpunt tot het massamiddelpunt van het bolletje, niet tot de bovenkant.',
 'L10:voor:2': 'Bij kleine uitwijkhoeken, typisch onder ca. 10–15°.',
 'L11:SMART': 'Hoe hangt de amplitude A van een gedempte massa-veertrilling af van de aandrijffrequentie f '
              'rondom de vooraf gemeten f_e, bij dezelfde massa, veer en waterhoogte, tijdens dit labo?',
 'L11:docent': ['Bron vraagt A(f) bij gedempte trilling in water; opstelling vooraf testen op elektrische '
                'veiligheid.',
                'Voor f_e telt bron 10 of 20 cycli, herhaling verlaagt tijdsfout.',
                'Verwachte resonantiecurve met piek nabij f_e; niet elk toestel levert dezelfde f_e.',
                'Wijs erop dat het maximum bij demping iets kan verschuiven.'],
 'L11:orientatie:1': 'In de buurt van de eigenfrequentie f_e; bij demping niet noodzakelijk exact dezelfde '
                     'waarde.',
 'L11:orientatie:2': 'De transiënte trilling moet uitdempen zodat de stationaire amplitude meetbaar is.',
 'L11:reflectie:1': 'Demping en koppeling verschuiven de frequentie van maximale stationaire amplitude iets.',
 'L11:reflectie:2': 'A = (18−6)/2 = 6 cm.',
 'L11:reflectie:3': 'Bijvoorbeeld selectieve afstemming van radiokring; bron en eigen uitleg vereist.',
 'L11:reflectie:4': 'Vrij: systeem trilt na start rond f_e en dooft uit; gedwongen: aandrijving blijft '
                    'energie toevoegen op ingestelde f.',
 'L11:reflectie:5': 'Kleinere frequentiestappen en meerdere herhalingen rond de piek; grotere spreiding '
                    'melden.',
 'L11:voor:1': 'De frequentie waarmee het systeem vrij trilt na een korte uitwijking.',
 'L11:voor:2': 'Een voortdurende periodieke aandrijving dwingt het systeem tot trillen.',
 'L12:SMART': 'Hoe veranderen golflengte en buiging van een watergolf wanneer de frequentie en '
              'openingsbreedte afzonderlijk veranderen, en bij welke frequenties ontstaan één tot vier '
              'buiken op hetzelfde touw, geobserveerd tijdens dit labo?',
 'L12:docent': ['Bron blz. 1 bevat applet én staande golven; blz. 27–28 fysieke golfbak met overhead.',
                'Vervang eventueel defecte overhead door camera boven bak, maar noteer effect op schaal.',
                'Vul bak pas als alle voedingen uit en kabels droog zijn.',
                "Foto's van patronen met titel en uitleg vereist."],
 'L12:orientatie:1': 'λ = v/f daalt.',
 'L12:orientatie:2': 'L = λ/2.',
 'L12:reflectie:1': 'Volgens Huygens verspreiden secundaire golfjes zich zichtbaar rond de rand als opening '
                    'en λ vergelijkbaar zijn.',
 'L12:reflectie:2': 'λ = 2L/3 = 0,40 m.',
 'L12:reflectie:3': 'Bijvoorbeeld wifi om hoek of ruisonderdrukking; kies één, verklaar fysisch en citeer '
                    'bron.',
 'L12:reflectie:4': 'Hun onderling faseverschil verandert; maxima/minima blijven niet op dezelfde plek.',
 'L12:reflectie:5': 'Een licht dobbertje beweegt vooral op/neer rond een vaste plek terwijl het patroon '
                    'verder loopt.',
 'L12:voor:1': 'Lopend patroon verplaatst zich; staande golf heeft vaste knopen en buiken.',
 'L12:voor:2': 'Een opening waarvan de breedte vergelijkbaar is met de golflengte, dus relatief smal.',
 'L13:SMART': 'Hoe verandert de resulterende geluidsamplitude bij optelling van twee even luide tonen die in '
              'fase of tegenfase zijn, geobserveerd met schoolsoftware, en hoe verandert de gehoorde '
              'toonhoogte bij naderende/weggaande bron, tijdens dit labo?',
 'L13:docent': ['Bron verwijst naar Soundry (oude ThinkQuest-URL): internetbeschikbaarheid vooraf testen, '
                'niet afhankelijk maken van die site.',
                'Wijs op scheiding tussen amplitudeverandering (luidheid) en frequentieverandering '
                '(toonhoogte).',
                'Gebruik een frequentievoorbeeld onder 500 Hz en begrens volume.',
                'Superpositie in tegenfase werkt alleen in geschikte geometrie/frequentie.'],
 'L13:orientatie:1': 'Bij gelijke amplitude heffen ze elkaar idealiter op; in praktijk niet perfect.',
 'L13:orientatie:2': 'De waargenomen frequentie stijgt, dus de toon klinkt hoger.',
 'L13:reflectie:1': 'De drukvariaties zijn tegengesteld en tellen ongeveer tot nul op, bij gelijke amplitude '
                    'en faseverschil π.',
 'L13:reflectie:2': 'f = 1/T = 250 Hz.',
 'L13:reflectie:3': 'Bijvoorbeeld snelheidsradar of medische echografie; bron en eigen uitleg vereist.',
 'L13:reflectie:4': 'Een voorspelbaar, laagfrequent signaal laat zich gemakkelijker meten en met de juiste '
                    'tegenfase compenseren.',
 'L13:reflectie:5': "Nee, 'lager' kan zachter (kleinere amplitude) of een lagere toon (kleinere frequentie) "
                    'betekenen.',
 'L13:voor:1': 'De frequentie (Hz).',
 'L13:voor:2': 'Superpositie.',
 'L14:SMART': 'Hoe hangt de positie y van de n-de maxima af van roosterconstante a (80–600 lijnen/mm) bij '
              'dezelfde laser en vaste schermafstand l, en hoe groot is de spoordichtheid van een cd bij die '
              'laser, gemeten tijdens dit labo?',
 'L14:docent': ['Bron heeft vier roosters met eigen tabellen, links/rechts en ordegrenzen; niet als één '
                'gemiddelde overslaan.',
                'Voor zichtbare laser typisch enkele honderden nanometer; exacte waarde hangt van toestel '
                'af.',
                'Kwikdamplamp uitsluitend demo als schoolapparaat en risicoanalyse dat toestaan.',
                'Voor CD-spoorlengte bronbenadering met middelomtrek expliciet uitleggen.'],
 'L14:orientatie:1': 'Laser/wavelength en bij voorkeur l; anders l steeds noteren en in θ verwerken.',
 'L14:orientatie:2': 'Om scheve opstelling en nulpuntfout te herkennen en het gemiddelde te nemen.',
 'L14:reflectie:1': 'sin θ = nλ/a; kleiner a maakt θ groter zolang een maximum mogelijk is.',
 'L14:reflectie:2': 'a = (1/500) mm = 0,0020 mm = 2,0 µm.',
 'L14:reflectie:3': 'Bijvoorbeeld elementherkenning met emissielijnen; bron en eigen uitleg vereist.',
 'L14:reflectie:4': 'De overgang is geleidelijk en bron/scherm hebben beperkte resolutie; persoonlijke '
                    'kleurwaarneming verschilt.',
 'L14:reflectie:5': 'Gloeilamp: breed continu spectrum; gasontlading: losse emissielijnen afhankelijk van '
                    'het gas.',
 'L14:voor:1': 'Er zijn 100 roosterruimten in 1 mm; a = 0,010 mm = 10 µm.',
 'L14:voor:2': 'Elke golflengte heeft maxima onder een andere hoek.',
 'L15:SMART': 'Hoe hangt de brekingshoek β af van de invalshoek α (ca. 10–60°) voor licht van lucht naar '
              'hetzelfde plexiglas, geconstrueerd met drie spelden en geodriehoek tijdens dit labo?',
 'L15:docent': ['Bron gebruikt zes invallende/gebroken stralen en klasgemiddelde; behouden.',
                'De bron vraagt expliciet twee oogposities: gebruik als oriëntatievraag naar breking.',
                'Plastic balkje kan plexiglas (n ≈ 1,49) of ander kunststof zijn; geen exact n '
                'voorschrijven.',
                'Spelden voorzichtig uit het blad verwijderen en tellen.'],
 'L15:orientatie:1': 'Anders verander je invalspunt of grensvlak en kloppen de geconstrueerde stralen niet.',
 'L15:orientatie:2': 'sin α/sin β voor één paar middenstoffen.',
 'L15:reflectie:1': 'De wet van Snellius gebruikt de sinus van de hoeken, niet de verhouding van de hoeken '
                    'zelf.',
 'L15:reflectie:2': 'n ≈ sin(30°)/sin(19,5°) ≈ 0,500/0,334 ≈ 1,50.',
 'L15:reflectie:3': 'Bijvoorbeeld brillenglas of lens; geef bron en link met gemeten n.',
 'L15:reflectie:4': 'Speldpositie en hoekaflezing; bij kleine hoeken is de relatieve fout in β groter.',
 'L15:reflectie:5': 'Toevalsfouten kunnen uitmiddelen als de groepen dezelfde middenstof en methode '
                    'gebruiken; systematische fouten blijven.',
 'L15:voor:1': 'Een lijn loodrecht op het grensvlak in het invalspunt.',
 'L15:voor:2': 'Naar de normaal, dus β < α.',
 'L16:SMART': 'Formuleer ZELF: Hoe hangt [afhankelijke meetgrootheid] af van [onafhankelijke grootheid] bij '
              '[constante voorwaarden en meetbereik], gemeten met [methode], tijdens dit labo?',
 'L16:docent': ['Eén lesuur voorbereiding + twee uitvoering; verwerking thuis, geen PowerPoint of '
                'spreekbeurt.',
                'LPD 6 S # is het expliciete bewijsstuk van de onderzoekscompetentie.',
                'Vraag en veiligheid vóór uitvoeren goedkeuren; poster individuele bijdrage volgens '
                'observaties.',
                'Inspiratielijst moet aansluiten bij écht beschikbaar materiaal.'],
 'L16:orientatie:1': 'Meerdere waarden van O (liefst vijf of meer) en minstens drie herhalingen per waarde.',
 'L16:orientatie:2': 'Behoud ruwe data; controleer fouten; beschrijf afwijking eerlijk, geen metingen '
                     "'verbeteren'.",
 'L16:reflectie:1': 'De gemeten A-waarden tegen O met eenheden, punten los, best passende lijn/kromme met '
                    'vergelijking als zinvol.',
 'L16:reflectie:2': 'Een verband vergt variatie van O; één punt zegt niets over vorm of spreiding.',
 'L16:reflectie:3': 'Eigen toepassing, correcte fysica, betrouwbare bron in poster.',
 'L16:reflectie:4': 'Antwoord hangt van opstelling af; noem een concreet toestel/procedure en '
                    'verbetermaatregel.',
 'L16:reflectie:5': 'Ruwe data moeten intact blijven; alleen aantoonbare meetfouten als uitsluiting '
                    'documenteren en motiveren.',
 'L16:voor:1': 'O = wat je varieert, A = wat je meet, C = wat je gelijk houdt; hangt af van gekozen vraag.',
 'L16:voor:2': 'Beschikbaar materiaal, veilige waarden, tijd, meetbaar resultaat en goedkeuring leerkracht.',
 'L1:MC': 'B. A: onveilig en niet aanvaardbaar/realistisch (230 V); C: meetmethode en constante voorwaarden '
          'ontbreken; D: ander onderwerp (kracht/versnelling). B is specifiek voor beide metingen, meetbaar '
          '(x/t), aanvaardbaar, realistisch en tijdsgebonden.',
 'L1:SMART': 'Hoe hangen de plaats x van de luchtbel en van het wagentje af van de tijd t (0–0,6 s), gemeten '
             'met stopwatch en tijdtikker bij dezelfde baaninstelling, tijdens dit labo?',
 'L1:docent': ['50 Hz is alleen geldig voor de betrokken tijdtikker; label/voeding vooraf nazien.',
               'De luchtbelbuis kan bij omdraaien lucht insluiten; eerst proefmeting.',
               'Verwacht x(t) bijna lineair; geen vaste numerieke v zonder baanhelling.',
               'Laat leerlingen het verschil x(t) en t(x) expliciet benoemen.'],
 'L1:orientatie:1': 'Steeds ongeveer dezelfde afstand: Δx = v·0,020 s.',
 'L1:orientatie:2': 'Om toevalsfouten zichtbaar te maken en een gemiddelde te bepalen.',
 'L1:reflectie:1': 'x(t) is ongeveer een rechte met vaste helling; de stippen liggen bijna even ver uiteen.',
 'L1:reflectie:2': 'v = 0,24 m / 0,60 s = 0,40 m/s.',
 'L1:reflectie:3': 'Bijvoorbeeld een transportband: constante aanvoersnelheid voor verpakking; bron en eigen '
                   'uitleg vereist.',
 'L1:reflectie:4': 'Wrijving, variërende aandrijving of startversnelling; vergelijk eerste en laatste Δx.',
 'L1:reflectie:5': 'De rechte toont het model en de spreiding; verbindingslijntjes suggereren exact gekende '
                   'tussenwaarden.',
 'L1:voor:1': 'Afgelegde weg is de totale lengte van de baan; verplaatsing is eindplaats min beginplaats, '
              'met teken.',
 'L1:voor:2': 'De snelheid v = Δx/Δt, uitgedrukt in m/s.',
 'L2:SMART': 'Hoe hangt de snelheid v af van de tijd t tijdens een rit omlaag en een rit omhoog op dezelfde '
             'helling, bepaald uit 0,040 s-vensters van de tijdtikker, tijdens dit labo?',
 'L2:docent': ['Tijdvenster in bron: 0,040 s; niet per ongeluk 0,020 s invullen.',
               'Bron spreekt over 6 V wisselspanning; pas toe afhankelijk van label van de echte voeding.',
               'Wrijving maakt a omhoog en omlaag ongelijk; leg tekenafspraak vooraf vast.',
               'Let op dat leerling het keerpunt weglaat bij lineaire fit.'],
 'L2:orientatie:1': 'Een gekozen nulstip is alleen het begin van je meting; het wagentje kan daar al '
                    'bewegen.',
 'L2:orientatie:2': 'Een rechte met rico a; stijgend bij versnellen en dalend bij vertragen als v in de '
                    'rijrichting positief is.',
 'L2:reflectie:1': 'De versnelling a in m/s²; een negatieve rico betekent dalende snelheidscomponent.',
 'L2:reflectie:2': 'a = (0,2−0,8)/0,30 = −2,0 m/s².',
 'L2:reflectie:3': 'Bijvoorbeeld remschijf; het remkoppel zet bewegingsenergie om in warmte; bron vereist.',
 'L2:reflectie:4': 'Wrijving werkt steeds tegen de beweging in en draagt in de ene richting bij aan de '
                   'zwaartekrachtcomponent, in de andere richting niet.',
 'L2:reflectie:5': 'Een parabool: x = x₀ + v₀t + ½at²; v(t) is recht.',
 'L2:voor:1': 'De snelheidscomponent wordt per seconde kleiner in de gekozen positieve richting; m/s².',
 'L2:voor:2': 'Bij vaste 0,020 s neemt de snelheid toe.',
 'L3:SMART': 'Hoe verandert v (m/s) met t (s) van een vrijvallende massa en van een omhoog geworpen '
             'tennisbal, bepaald met tijdtikker en Tracker bij dezelfde lokale g, tijdens dit labo?',
 'L3:docent': ['Twee bronbladen voor vrije val en twee voor verticale worp: controleer dat geen kolom '
               'verloren gaat.',
               'Tijdtikker levert g in de orde 10 m/s²; stel geen gefingeerde tolerantie in voor Tracker.',
               'Leg referentiehoogte uit vóórdat leerlingen video analyseren.',
               'Camera moet in hetzelfde vlak als de schaal staan om parallax te vermijden.'],
 'L3:orientatie:1': 'Omdat de zwaartekracht neerwaarts gericht blijft en v elke seconde met ongeveer 9,81 '
                    'm/s afneemt.',
 'L3:orientatie:2': 'Kalibratielijn plaatsen op een lat in het bewegingsvlak waarvan de lengte bekend is.',
 'L3:reflectie:1': 'Alleen v_y = 0 op één ogenblik; de zwaartekracht werkt nog steeds, dus a_y ≈ −9,81 m/s².',
 'L3:reflectie:2': "t' = v₀/g = 3,0/9,81 ≈ 0,31 s.",
 'L3:reflectie:3': 'Bijvoorbeeld sporttechniek: spronghoogte meten met videoframes; bron en eigen uitleg '
                   'vereist.',
 'L3:reflectie:4': 'Schaalfout/kalibratie, onzuivere start, meetraam, framefrequentie, luchtweerstand en '
                   'tijdtikkerwrijving.',
 'L3:reflectie:5': "De absolute y'-waarde; de hoogtewinst y'−y₀ niet, als y consequent gemeten is.",
 'L3:voor:1': 'a = −g bij stijgen én dalen, zolang luchtweerstand klein is.',
 'L3:voor:2': 'De verticale snelheid is op dat ogenblik nul; de versnelling is nog steeds −g.',
 'L4:SMART': 'Hoe hangen x en de valafstand y van de tijd af bij een horizontale worp vanaf vaste hoogte, '
             'gemeten met Tracker en met een kogelspoor op een gelijkblijvend hellende plaat, tijdens dit '
             'labo?',
 'L4:docent': ['In bron is plankafmeting ca. 45 × 55 cm en verfspoor; gebruik waterafwasbare verf.',
               'Het plaatspoor is een didactische analogie, niet identiek aan een vrije horizontale worp.',
               'Laat leerlingen x(t), y(t) en y(x) onderscheiden.',
               'Verifieer dat Tracker vóór de les op schooltoestel werkt; alternatief: video handmatig frame '
               'voor frame.'],
 'L4:orientatie:1': 'Niet bij dezelfde beginhoogte en verwaarloosbare luchtweerstand; y-beweging '
                    'onafhankelijk van x-beweging.',
 'L4:orientatie:2': 'y ∝ x² als v₀ in x constant is: y = gx²/(2v₀²).',
 'L4:reflectie:1': 'Elimineer t: x = v₀t, y = ½gt², dus y = gx²/(2v₀²).',
 'L4:reflectie:2': 't = √(2h/g) = √(1,60/9,81) ≈ 0,40 s.',
 'L4:reflectie:3': 'Bijvoorbeeld een transportband met vallende korrels; bron en uitleg op basis van meting '
                   'vereist.',
 'L4:reflectie:4': 'Parallax en perspectief vervormen x en y; meetlat moet in hetzelfde vlak als de baan '
                   'staan.',
 'L4:reflectie:5': 'Op de plaat zorgen rolwrijving en component van zwaartekracht langs de plaat voor andere '
                   'snelheden dan een vrije worp in de lucht.',
 'L4:voor:1': 'vₓ blijft ongeveer constant.',
 'L4:voor:2': 'De valafstand groeit als ½gt².',
 'L5:SMART': 'Hoe hangt de versnelling a van wagentje en hangmassa af van de aandrijfkracht F (2–5 schijfjes '
             'van 10 g) bij vaste totale massa, en van de totale massa m bij twee vaste schijfjes, gemeten '
             'met tijdtikker tijdens dit labo?',
 'L5:docent': ['Bron schuift schijfjes tussen wagentje en hangzijde om m_tot constant te houden: expliciet '
               'benoemen.',
               'Verwachte verbanden: a ∝ F, a ∝ 1/m; afwijking bij lage F door wrijving.',
               'Meet geen spijkerslagen met leerlingen; leerkracht voorbereiding.',
               'Teken de krachten op hetzelfde aangrijpingspunt voor parallellogramconstructie.'],
 'L5:orientatie:1': 'a(F) bij vaste totale massa; a(1/m_tot) bij vaste kracht.',
 'L5:orientatie:2': 'Kracht en versnelling zijn vectoren.',
 'L5:reflectie:1': 'a = Fᵣ/m_tot; bij grotere massa wordt a kleiner.',
 'L5:reflectie:2': 'a = 0,40/0,20 = 2,0 m/s² (zonder wrijving).',
 'L5:reflectie:3': 'Bijvoorbeeld remweg zwaar beladen fiets; model en bron vergelijken.',
 'L5:reflectie:4': 'Katrol- en baanwrijving en rotatie van de katrol maken de netto kracht kleiner.',
 'L5:reflectie:5': 'Alleen als beide krachten evenwijdig zijn en dezelfde zin hebben.',
 'L5:voor:1': 'De vectoriële som van alle krachten op hetzelfde voorwerp.',
 'L5:voor:2': 'Ze versnelt samen met het wagentje en moet dus in m_tot zitten.',
 'L6:SMART': 'Hoe hangen de benodigde kracht F en afgelegde afstand s af van de hellingshoek (30°, 45°, 60°) '
             'bij dezelfde eindhoogte h, gemeten met dynamometer en lat tijdens dit labo?',
 'L6:docent': ['De bron gebruikt dynamometer 1 N bij 100 g: F_vert ≈ 0,981 N dicht bij eindbereik; voor '
               'wrijving beter 3 N reserve.',
               'De bron vergelijkt drie hoeken bij één hoogte; sommige combinaties vereisen langere baan dan '
               '40 cm. Kies h ≤ 0,15 m voor α = 30°.',
               'W_hel kan licht groter zijn door wrijving; geen exacte gelijkheid beloven.',
               'Vraag leerkracht de drie baanstanden vooraf te testen.'],
 'L6:orientatie:1': 'Nee, ΔE_z = mgΔh en hangt alleen van massa en hoogteverschil af.',
 'L6:orientatie:2': 'Ze vraagt extra arbeid, omgezet in warmte; de gemeten W kan groter zijn dan mgh.',
 'L6:reflectie:1': 'F_parallel = mg sin α zonder wrijving; kleinere hoek geeft kleinere component.',
 'L6:reflectie:2': 'ΔE_z = 0,10·9,81·0,20 = 0,196 J.',
 'L6:reflectie:3': 'Bijvoorbeeld een laadbrug; bron en uitleg over F en s vereist.',
 'L6:reflectie:4': 'Extra versnelling vraagt nettokracht; dynamometer leest dan niet alleen de '
                   'evenwichtskracht.',
 'L6:reflectie:5': 'Alleen de krachtcomponent langs de verplaatsing verricht arbeid: W = F s cos θ.',
 'L6:voor:1': 'joule (J) = newtonmeter (N·m).',
 'L6:voor:2': 'Anders is de toename van zwaarte-energie niet gelijk.',
 'L7:SMART': 'Hoe hangen de benodigde trekkracht F en de arm d (0,15–0,50 m) samen om een statief in '
             'evenwicht te houden en hoe verdelen last en macht zich bij drie typen hefboom, gemeten met '
             'dynamometer en lat tijdens dit labo?',
 'L7:docent': ['Deze bronproeven staan niet als afzonderlijk minimumdoel in de 6BCW-leerstof: label '
               'expliciet als verrijking, niet als bewijslabo voor LPD 15 F.',
               'Bron heeft vijf metingen per type voor steunpunt/last, één kwalitatieve machtvariant; '
               'behouden.',
               'Verwacht F(d) hyperbolisch, F(1/d) bijna recht.',
               'Vermijd scherpe spijkers uit andere bronproef.'],
 'L7:orientatie:1': 'Ja: bij constant moment M geldt F = M/d.',
 'L7:orientatie:2': 'De arm is de loodrechte afstand van het draaipunt tot de werklijn van de kracht.',
 'L7:reflectie:1': 'Bij evenwicht F_m d_m = F_l d_l; als d_m groter is, mag F_m kleiner zijn.',
 'L7:reflectie:2': 'F_m = 2·0,10/0,40 = 0,50 N.',
 'L7:reflectie:3': 'Bijvoorbeeld hefboom in gereedschap; leg armverhouding uit en citeer bron.',
 'L7:reflectie:4': 'Eigen gewicht van de stang, wrijving in draaipunt, niet-loodrechte kracht en afleesfout.',
 'L7:reflectie:5': 'Nee, de machtarm is dan kleiner dan de lastarm: F_m > F_l, maar de last beweegt '
                   'verder/sneller.',
 'L7:voor:1': 'De loodrechte afstand van de werklijn van je kracht tot het scharnier.',
 'L7:voor:2': 'Anders wordt het moment door onbedoelde wrijving/klemming beïnvloed.',
 'L8:SMART': 'Hoe hangen v en ω af van de straal r bij een draaiende platenspeler en hoe hangt F_cp af van r '
             'en omlooptijd T bij dezelfde rubberstop, gemeten met stopwatch en meetlat tijdens dit labo?',
 'L8:docent': ['Bron vereist afgerond glazen buisje; leerkracht moet draad/stop vooraf testen.',
               'Richtwaarden hangen van m_stop en r af, dus geen vaste numerieke F_cp.',
               'N = 20 toeren vermindert stopwatchfout.',
               'Voor platenspeler: ω gelijk maar v buiten groter.'],
 'L8:orientatie:1': 'ω is gelijk; v = ωr is groter voor de buitenste stip.',
 'L8:orientatie:2': "Via de draad levert het gewicht m'hang·g de spankracht, ongeveer de centripetale "
                    'kracht.',
 'L8:reflectie:1': 'De draad levert een naar binnen gerichte kracht die zijn snelheidsrichting telkens '
                   'verandert.',
 'L8:reflectie:2': 'ω = 2π/T = π rad/s ≈ 3,14 rad/s.',
 'L8:reflectie:3': 'Bijvoorbeeld een bocht in weg: wrijving levert F_cp; bron vermelden.',
 'L8:reflectie:4': 'Wrijving in het buisje, hoek van de draad en onconstante straal/snelheid.',
 'L8:reflectie:5': 'F_cp verviervoudigt, omdat F_cp ∝ v².',
 'L8:voor:1': 'Nee, enkel de grootte kan constant zijn; de richting verandert voortdurend.',
 'L8:voor:2': 'Naar het middelpunt van de cirkelbaan.',
 'L9:SMART': 'Hoe hangt de periode T van een trillende massa af van de aangehangen massa m (40–250 g) en de '
             'veerconstante k van twee veren, gemeten met chronometer en gecontroleerd met een tijdtikker '
             'tijdens dit labo?',
 'L9:docent': ["In bron twee veren, verschillende massa's en percentage-afwijking; bewaren.",
               'Leerlingen mogen onbekende massa niet losmaken (bronrandvoorwaarde).',
               'Tijdtikker-opdracht staat apart in bron: plannen binnen drie uren of als tweede meetpost.',
               'T²-versus-toegevoegde massa fit is de robustere methode dan een enkel T.'],
 'L9:orientatie:1': 'T verdubbelt (T ∝ √m).',
 'L9:orientatie:2': 'Bij evenwicht F_veer = F_z = mg en volgens Hooke F_veer = kΔy.',
 'L9:reflectie:1': 'Kwadrateren van T = 2π√(m/k) geeft T² = (4π²/k)m.',
 'L9:reflectie:2': 'T wordt half zo groot: T ∝ 1/√k.',
 'L9:reflectie:3': 'Bijvoorbeeld schokdemper/veer in voertuig; beschrijf effect van demping en bron.',
 'L9:reflectie:4': 'De veer zelf heeft massa die mee trilt; die is niet verwaarloosbaar ten opzichte van de '
                   'kleine hangmassa.',
 'L9:reflectie:5': 'Potentiële veerenergie is daar minimaal en kinetische energie maximaal als demping '
                   'gering is.',
 'L9:voor:1': 'De tijd voor één volledige heen-en-weerbeweging.',
 'L9:voor:2': 'De reactietijdfout weegt minder zwaar wanneer je een langere tijd meet.'}

# Modelantwoorden bij de brongetrouwe herwerking van de originele practica.
# Getallen zijn voorbeeldwaarden; een echte meetsnelheid/g volgt uit de leerlingdata.
ANSWERS.update({
 'L1:deel2:vraag1': 'Optrekken en remmen zijn geen eenparige fase; alleen het middendeel is geschikt om constante v te toetsen.',
 'L1:deel2:vraag2': '50 Hz betekent 50 tikken per seconde: 0,020 s per tik. Nummeren om de twee tikken geeft 0,040 s tussen gekozen meetstippen.',
 'L2:deel1:vraag1': 'Stip 0 ligt ná de dicht opeen liggende startstippen: de wagen beweegt daar al; extrapolatie van v(t′) levert v₀ > 0.',
 'L2:deel1:vraag2': 'Het snijpunt geeft v₀ en de rico a. t′ is de tijd op het midden van een venster; Δt = 0,040 s is de vaste vensterduur.',
 'L2:deel2:vraag1': 'Tijdens contact met de hand wordt de wagen aangedreven: zijn vertraging is dan niet alleen de langscomponent van de zwaartekracht. Kies stip 0 pas na loslaten en vóór het keerpunt.',
 'L2:deel2:vraag2': 'Bij omhoog positief daalt de snelheid: een nagenoeg rechte v(t′) met negatieve richtingscoëfficiënt toont bij benadering constante negatieve a.',
 'L3:deel1:vraag1': 'Het midden van de intervallen [0;0,020], [0,020;0,040] enz. is 0,010; 0,030; enz. v = Δx/0,020 s hoort bij die middentijd.',
 'L3:deel1:vraag2': 'De rico is de (val)versnelling. Bij een later gekozen stip 0 is v₀ niet nul, dus v/t′ = g + v₀/t′ en geen zuivere g.',
 'L3:deel2:vraag1': 'Bij verschillende afstand tot de camera veroorzaakt perspectief/parallax een fout in de afgelezen hoogte ten opzichte van de meetlat.',
 'L3:deel2:vraag2': 'Met y omhoog positief en een eindsnelheid naar beneden is de y-component van de snelheid negatief: v_grond = v₀ − gt.',
 'L3:deel3:vraag1': 'Kalibreer in Tracker met de zichtbare meetlat. De meetlat en de baan moeten op nagenoeg gelijke camera-afstand liggen om schijnbare schaalverandering te vermijden.',
 'L3:deel3:vraag2': 'Tracker levert meer tijd-/plaatsparen over de hele baan en vermijdt stopwatchreactie, mits correcte schaal, camera, frametijd en consequente puntkeuze; vergelijk de daadwerkelijke meetonzekerheden.',
 'L4:deel1:vraag1': 'Zet bal en meetlat in hetzelfde vlak evenwijdig aan het beeldvlak, camera loodrecht en stabiel; kalibreer in Tracker en volg consequent hetzelfde punt.',
 'L4:deel1:vraag2': 'Horizontaal: x(t) ongeveer lineair en vₓ bijna constant. Verticaal: y(t) ongeveer kwadratisch, aᵧ ongeveer g naar beneden (teken afhankelijk van gekozen as).',
 'L4:deel2:vraag1': 'Dan geeft de valgeul eerst vooral een snelheidscomponent langs de x-as; de plankhelling voegt een y-versnelling toe. Zo blijven de componenten interpreteerbaar.',
 'L4:deel2:vraag2': 'De gemeten y-afstand wordt evenwijdig aan de zelf getekende y-as geconstrueerd; hierdoor vergelijk je steeds dezelfde richting zonder een schijnbaar loodrechte projectie in een scheve tekening.',
 'L6:deel1:vraag1': 'Bij constante lengte l geldt h = l·sin α; sin 60° is groter dan sin 30°. Dit is niet een proef op telkens dezelfde eindhoogte.',
})
ANSWERS['L1:docent'] += ['Bron blz. 68–72: eerst voltmeter en 6,0 V~ controleren, wagentje met schakelaar; kies uitsluitend de gelijkmatige middensectie. Om de twee 50 Hz-stippen = 0,040 s.',
                          'Laat de leerlingen t′ LINKS van ⟨v⟩ in Excel selecteren; t′ is een tijdstip op het midden van het venster, niet Δt of Δv.']
ANSWERS['L2:docent'] += ['Bron blz. 79–85: oorspronkelijk bandje met 0,2,4,... en t′=0,020;0,060;...; extrapoleer v₀ en bepaal de rico van v(t′).',
                          'Bron blz. 86–92: behoud het omhoog geduwde wagentje als APART OPEN PRACTICUM. Keur eigen plan en stip 0 na loslaten goed. Grafieken x(t) en v(t′) onder elkaar met tabellen links.']
ANSWERS['L3:docent'] += ['Twee ECHTE proeven: 50 g aan bandje door statieftriller (blz. 20–26/73–78), en verticale tennisbalworp: eerst twee camerabeelden + stopwatch, daarna de hele baan met Tracker (blz. 15–20/58–61).',
                          'Handmatige worp: 0 = y₀ + v₀t − ½gt², dus v₀=(½gt²−y₀)/t; v_grond=v₀−gt; t_top=v₀/g; y_top=y₀+v₀²/(2g). Noem tijd tot top t_top om niet te verwarren met tikker-middentijd t′.',
                          'Uit 50 Hz-bandje volgt v voor t′ = 0,010;0,030;... s. Als nulstip later ligt, gebruik rico v(t′) voor g, niet v/t′.']
ANSWERS['L4:docent'] += ['Horizontale Trackerworp uit bron 56–57 blijft ECHT OPEN: laat leerlingen zelf camerastand, meetvariabelen en formules voorstellen; keur pas na veiligheids- en perspectiefcontrole goed.',
                          'Schuine-plankproef blz. 93–97: laat leerlingen vlak/boven, schuin/beneden en schuin/boven onderscheiden. Drie hellingen, x=10–55 cm in stappen van 5 cm, y₁/y₂/y₃ en y/x².']
ANSWERS['L6:docent'] += ['Correctie op eerste concept: de originele bronproef heeft de baanlengte l CONSTANT en h=l·sin α per hoek; niet dezelfde hoogte bij alle drie hoeken.']
ANSWERS.update({
 'L1:deel1:vraag1': 'Kies consequent voor- of achterkant: de bel heeft een lengte, zodat wisselen van referentie de afgelegde afstand systematisch vertekent.',
 'L1:deel1:vraag2': 'Bij dezelfde gekozen nulpositie geldt x₀ = 0 en t₀ = 0, zodat x−x₀ = x en t−t₀ = t. Bij een andere nul is dit niet vanzelf waar.',
})
ANSWERS['L1:SMART']='Hoe hangen x(t) en de snelheid van dezelfde luchtbel samen bij 90° en 45° van de buis, en is de elektrisch aangedreven wagen in zijn gelijkmatige middenfase een ERB, gemeten met chronometer en 50 Hz-tijdtikker tijdens dit labo?'
ANSWERS['L1:docent'] += ['Bron p. 63–67: buis ECHT bij 90° en 45°, x = 0,100–1,000 m in stappen 0,100 m; bij elke afstand dezelfde voorkant van de luchtbel en beide x(t)-reeksen op één grafiek.']
ANSWERS.update({
 'L12:deel1:vraag1': 'Een staafvormige bron genereert aan het midden van de bak bij benadering rechte, vlakke golffronten.',
 'L12:deel1:vraag2': 'Bevestiging aan dezelfde triller koppelt de frequentie en fase: daardoor blijft het faseverschil en dus het interferentiepatroon in de tijd stabiel.',
 'L13:deel1:vraag1': '437 en 443 Hz verschillen weinig in toonhoogte; samen geven ze 6 zwevingen per seconde (|443−437| = 6 Hz).',
 'L13:deel1:vraag2': 'Gelijke golven in fase versterken, precies tegengesteld en even sterk doven ze uit; bijvoorbeeld actieve ruisonderdrukking benadert dit met een antigeluid.',
 'L13:deel3:vraag1': 'Een harmonische heeft een frequentie die een geheel veelvoud is van de grondfrequentie; andere sterktes van harmonischen geven verschillende klankkleur bij dezelfde toonhoogte.',
 'L13:deel3:vraag2': 'Ultrasoon geluid heeft een frequentie hoger dan het menselijke gehoorbereik (ruwweg > 20 000 Hz); bijvoorbeeld medische echografie en afstandsmeting met echo. Vraag correcte bronvermelding.',
})
ANSWERS['L12:docent'] += ['Bron 27–28: laat ALLE vijf fysieke golfbakexperimenten uitvoeren: punt-, staafbron, smalle/brede opening, twee coherente bronnen; koppel ze aan negen appletbeelden uit bron blz. 1.']
ANSWERS['L13:docent'] += ['Bewaar de eigen Soundry-vragen p. 55–56 ook bij vervangapp: 437+443 Hz beats, gelijke/tegengestelde golven, Doppler, harmonischen (klarinet/trompet, zaagtand, blokgolf), ultrasoon. Historische URL is niet geverifieerd.']
ANSWERS['L6:SMART']='Hoe verschillen F_vert·h en F_hel·l voor hetzelfde wagentje bij een vaste baanlengte l en drie hoeken (30°, 45°, 60°, elk met h = l sin α), gemeten met dynamometer en meetlat tijdens dit labo?'
ANSWERS['L9:SMART']='Hoe veranderen k en T bij veer 1 (30–150 g) en veer 2 (50–250 g), en hoe bepaal je daarna een onbekende massa zonder balans terwijl ze aan de veer blijft, gemeten met chronometer tijdens dit labo?'
ANSWERS['L10:SMART']='Hoe verandert de periode T van de eigen slinger bij 10° versus 5°, metalen versus houten bolletje op 1,00 m, en bij circa tien verschillende slingerlengten, gemeten als tijd voor 20 cycli tijdens dit labo?'
ANSWERS['L3:SMART']='Wat is g uit een 50 Hz-bandje van een vrijvallende massa en welke v₀, t_top en y_max leveren de originele handmatige en Tracker-methoden bij een verticale tennisbalworp tijdens dit labo?'
ANSWERS['L4:SMART']='Welke positie-, snelheids- en versnellingscomponenten vind je uit een zelf ontworpen horizontale Trackerworp, en tonen drie kogelsporen op de schuine plank y ∝ x² tijdens dit labo?'
