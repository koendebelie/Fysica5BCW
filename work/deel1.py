# -*- coding: utf-8 -*-
"""Deel 1 – Algemene inleiding van de labocursus 6BCW."""
import kit as K

from labs import LABOS as COURSE_LABOS

# Indienen wordt afgeleid van de inhoudsbron. Het open onderzoek krijgt zijn eigen poster.
INDIEN = [
    ("1–6, 8–11, 14–15", "Excel-verslagsjabloon (.xlsx) met tabellen, grafieken en besluit.",
     "Meetreeksen die je grafisch verwerkt."),
    ("7, 12, 13", "Ingevulde werkbladen, schetsen en foto’s als één PDF.",
     "Verdiepings- en doorschuifpracticum met vooral schetsen en waarnemingen."),
    ("16", "Wetenschappelijke A3-poster (PDF) én Excel-bestand met ruwe data/grafieken.",
     "Open onderzoek met zelfstandige communicatie."),
]

SMART_ROWS = [
    ("S – Specifiek",
     "Eén duidelijk afgebakend verband tussen twee grootheden.",
     "Welke grootheid verander ik, welke meet ik, wat houd ik constant?",
     "Hoe hangt de versnelling van een wagentje af van de resulterende kracht (0,10-0,60 N) bij "
     "gelijkblijvende massa van 500 g?",
     "Hoe werkt beweging?"),
    ("M – Meetbaar",
     "Beide grootheden zijn te meten of waar te nemen.",
     "Met welk toestel, in welke eenheid, met welke nauwkeurigheid?",
     "… versnelling uit twee fotopoorten of uit de helling van de v(t)-grafiek (m/s²) …",
     "Gaat een zwaar voorwerp sneller?"),
    ("A – Aanvaardbaar",
     "Zinvol en relevant binnen het vak, veilig en ethisch.",
     "Waarom is dit de moeite waard? Mag en kan dit in het labo?",
     "… (basis van voertuigveiligheid en remsystemen) …",
     "Hoeveel g-kracht kan een leerling verdragen?"),
    ("R – Realistisch",
     "Haalbaar met het beschikbare materiaal en in de tijd.",
     "Heb ik het materiaal, lukt het in twee lesuren?",
     "… met de luchtbaan, fotopoorten en gewichtjes van het labo …",
     "Hoe hangt de slingerperiode af van de zwaartekracht op Jupiter?"),
    ("T – Tijdsgebonden",
     "Duidelijk wanneer en binnen welke periode het onderzoek klaar is.",
     "Wanneer meet ik, wanneer lever ik in?",
     "… gemeten tijdens dit labo, verslag binnen één week.",
     "Ooit eens uitzoeken."),
]


def build(doc, T):
    K.h1(doc, "Deel 1 – Algemene inleiding")

    # ------------------------------------------------------------------ 1.1
    K.h2(doc, "1.1 Zo werk je met deze cursus: de OVUR-methode")
    K.p(doc, "Elk werkblad volgt dezelfde vier fasen van de onderzoekscyclus. Lees vóór elk labo de "
             "lesdoelen en de leerplandoelen: daarop worden je verslag én je labowerk beoordeeld.")
    K.tabel(doc,
            ["Fase", "Wat doe je?", "Op het werkblad"],
            [["O – Oriënteren", "Wat, waarom, welke voorkennis?", "Context, onderzoeksvraag, doel, oriëntatievragen."],
             ["V – Voorbereiden", "Plan maken: stappen, materiaal, veiligheid, hypothese.",
              "Benodigdheden, theorie, veiligheid, hypothese, werkplan."],
             ["U – Uitvoeren", "Meten, noteren, observeren volgens plan.",
              "Procedure, tabellen, STEM-opdracht, schetsen en foto's."],
             ["R – Reflecteren", "Kloppen de resultaten? Wat kan beter? Besluit en link met de maatschappij.",
              "Besluit, foutenanalyse, reflectievragen."]],
            widths=[2100, 3800, 3738])

    K.h3(doc, "Leerlijn: van gesloten naar open practica (LPD 1 S, 4 S, 6 S)")
    K.p(doc, "Doorheen het jaar krijg je stap voor stap meer verantwoordelijkheid: eerst voer je een "
             "gegeven werkwijze nauwkeurig uit, daarna stel je zelf meetplannen op, ontwerp je oplossingen "
             "en ten slotte doorloop je een volledige onderzoekscyclus. Bij elk labo staat bovenaan de "
             "'mate van sturing'. Opdrachten in een groen kader ('STEM-ontwerpopdracht') los je zelf op: "
             "er is geen vaste werkwijze, wel een duidelijk doel en duidelijke randvoorwaarden.")
    K.tabel(doc,
            ["Niveau", "Wie bepaalt wat?", "Labo's"],
            [["Gesloten", "Vraag, werkwijze en tabel gegeven – jij meet, noteert en redeneert nauwkeurig.",
              "1, 12, 13 (basisdelen)"],
             ["Begeleid", "Jij formuleert de vraag en kiest meetstrategie, variabelen, bereik "
                          "en tabelopbouw. Ontwerpopdrachten met randvoorwaarden.",
              "2–11, 14–15"],
             ["Open", "Jij stelt het werkplan én de onderzoeksvraag op; de leerkracht keurt goed en coacht.",
              "16"]],
            widths=[1500, 6100, 2038])

    K.h3(doc, "Een goede onderzoeksvraag is SMART")
    K.p(doc, "Elk onderzoek start met een goede onderzoeksvraag. In het zesde jaar moet je die volledig "
             "zelf kunnen opstellen; in deze cursus oefen je dat in twee stappen. "
             "**Stap 2 (labo 1, het opfrislabo):** je kiest de SMART-vraag uit vier voorstellen die er "
             "allemaal goed uitzien, maar waarvan er drie niet SMART zijn of net naast het onderwerp "
             "zitten – en je verantwoordt je keuze per letter. "
             "**Stap 3 (labo 2 tot en met 16):** je formuleert de onderzoeksvraag helemaal zelf en legt "
             "per letter uit waarom ze SMART is.")
    K.p(doc, "*Een SMART-vraag is bijna altijd van de vorm: 'Hoe hangt [afhankelijke grootheid] af van "
             "[onafhankelijke grootheid] bij [constante voorwaarden]?' of 'Wat is de invloed van … op …?'*",
        italic=True)
    K.tabel(doc,
            ["Letter", "Betekenis", "Controlevraag", "Voorbeeld (goed)", "Voorbeeld (slecht)"],
            SMART_ROWS,
            widths=[1450, 2200, 2200, 2500, 1288], size=9)

    # ------------------------------------------------------------------ 1.2
    K.h2(doc, "1.2 Veilig werken in het mechanica- en golvenlabo")
    K.p(doc, "Deze regels gelden bij elk labo en tellen mee in de procesevaluatie (thema 5).")
    K.bullets(doc, [
        "Bewegende en vallende voorwerpen: houd handen en voeten buiten de baan van een wagentje, "
        "een slinger of een vallend gewicht. Zet een vangnet of een doos onder een valopstelling.",
        "Bouw elke opstelling stevig op (statiefklemmen vast, geen wiebelende planken) en laat ze "
        "controleren vóór je laat bewegen of loslaat.",
        "Maximale belasting: respecteer per labo de opgegeven grens voor massa's, hoek of spanning. "
        "Die staat op het werkblad bij 'Veiligheid // nauwkeurigheid' en verschilt per proef.",
        "Water in de golfbak en elektriciteit horen niet bij elkaar: zet de trilbron en de voeding "
        "nooit aan de rand van de bak en houd de stekker droog.",
        "Laser (labo 14): nooit op ooghoogte, nooit in de richting van een persoon of een glimmend "
        "oppervlak, en enkel de door de leerkracht uitgedeelde laserklasse.",
        "Geluid (labo 13): bij luidere tonen blijf je niet met je oor vlak bij de bron.",
        "Veren en elastieken: niet uitrekken tot in je gezicht; een losschietende veer kan verwonden.",
        "Orde: geen tassen in de looppaden, geen snoeren over de tafelrand, werkpost opruimen en "
        "materiaal terugleggen zoals je het vond.",
        "Meld elk defect of elke losse klem onmiddellijk aan de leerkracht.",
    ])
    K.h3(doc, "De veiligheidsverantwoordelijke van de groep")
    K.p(doc, "Bij elk labo duidt je groep één veiligheidsverantwoordelijke aan. Die rol wisselt per labo "
             "en wordt genoteerd op het werkblad. De veiligheidsverantwoordelijke is geen 'baas' van de "
             "groep, maar het aanspreekpunt voor veiligheid.")
    K.tabel(doc,
            ["Moment", "Wat doet de veiligheidsverantwoordelijke?"],
            [["Vóór de proef",
              "Leest het kader 'VEILIGHEID // NAUWKEURIGHEID' hardop voor; checkt de opstelling (klemmen "
              "vast, baan vrij, vangnet klaar, maxima gerespecteerd); laat de opstelling controleren door "
              "de leerkracht vóór de eerste meting."],
             ["Tijdens de proef",
              "Houdt toezicht op de afgesproken maxima en op de omgeving (looppad vrij, geen water bij "
              "elektriciteit, laser niet op ooghoogte); grijpt in als een groepslid een risico neemt en "
              "roept de leerkracht bij twijfel."],
             ["Na de proef",
              "Controleert of alles uit staat, of de opstelling volledig ontmanteld en opgeruimd is en of "
              "het materiaal onbeschadigd terug in de kast ligt; meldt defecten."]],
            widths=[2200, 7438])

    # ------------------------------------------------------------------ 1.3
    K.h2(doc, "1.3 Meten, noteren en verwerken")
    K.tabel(doc,
            ["Afspraak", "Toelichting"],
            [["Grootheid – symbool – eenheid",
              "Elke kolomkop: symbool + SI-eenheid, bv. x (m), v (m/s), a (m/s²), T (s), m (kg), F (N)."],
             ["Beduidende cijfers",
              "Zoveel cijfers als het toestel betrouwbaar geeft (0,235 m); een resultaat is nooit "
              "nauwkeuriger dan de minst nauwkeurige meting die erin zit."],
             ["Meetonzekerheid",
              "Noteer de afleesnauwkeurigheid per toestel (lat: ± 0,5 mm; digitale weegschaal: ± 0,01 g; "
              "fotopoort: ± 0,001 s) en bespreek ze in de foutenanalyse."],
             ["Herhaalde metingen",
              "Minstens 3× meten en het gemiddelde nemen; grote spreiding betekent weinig betrouwbaar. "
              "Bij trillingen meet je liefst 10 of 20 periodes in één keer."],
             ["Grafieken",
              "Titel, grootheid + eenheid op beide assen, meetpunten als kruisjes of bolletjes (nooit "
              "verbinden), best passende lijn of kromme; bij een rechte de richtingscoëfficiënt bepalen "
              "en zeggen wat die betekent."],
             ["Lineariseren",
              "Verwacht je een kwadratisch verband (T ~ √l, x ~ v₀², F ~ v²)? Zet dan de juiste grootheid "
              "op de horizontale as zodat je een rechte krijgt, en benoem die as duidelijk."],
             ["Digitaal",
              "Excel of Sheets voor tabel, spreidingsgrafiek en trendlijn met vergelijking; "
              "Pasco Capstone, een bewegingssensor of video-analyse voor de meting zelf; "
              "schermafbeelding met titel en uitleg in het verslag."],
             ["Databeheer",
              "Ruwe data meteen en chronologisch op het werkblad of in het gedeelde bestand; nooit "
              "'verbeteren'."],
             ["Internet bij reflectievragen",
              "Enkel bij vragen waar het uitdrukkelijk vermeld staat ('Internet toegelaten'). Gebruik een "
              "gewone zoekmachine en vermeld je bron. AI-tools (ChatGPT, Copilot …) om je antwoord te "
              "laten schrijven zijn niet toegelaten: het antwoord moet in je eigen woorden en vanuit jouw "
              "metingen komen."]],
            widths=[2800, 6838])

    # ------------------------------------------------------------------ 1.4
    K.h2(doc, "1.4 Het laboverslag: Excel-sjabloon, groepswerk en deadline")
    K.h3(doc, "1.4.1 Altijd het Excel-verslagsjabloon gebruiken")
    K.p(doc, "Voor de labo's met meetreeksen maak je het verslag in het blanco Excel-verslagdocument dat "
             "op Smartschool staat (map 'Toegepaste fysica – labo'). Je gebruikt altijd dit sjabloon – "
             "geen eigen Word- of Google-document – en je levert het ook als Excel-bestand (.xlsx) in. "
             "Naast het sjabloon vind je op Smartschool een screencast die stap voor stap toont hoe je "
             "elk onderdeel invult (tabellen met formules, spreidingsgrafiek met trendlijn, besluit). "
             "Bekijk die screencast vóór je eerste verslag en opnieuw als je twijfelt.")
    K.tabel(doc,
            ["Onderdeel in het Excel-sjabloon", "Wat komt erin? (OVUR-fase)", "Aandachtspunten uit het sjabloon"],
            [["Kopblok", "Groepsleden, klas, datum uitvoering, nummer en titel van de proef (O + V).",
              "Volledig invullen; dit is ook de bestandsnaam bij het uploaden (… 6BCW)."],
             ["OMSCHRIJVING", "Doorlopende tekst in eigen woorden: doel, benodigdheden en werkwijze (O + V).",
              "Geen opsomming kopiëren van het werkblad; schrijf zo dat iemand anders de proef kan herhalen."],
             ["ONDERZOEKSVRAAG", "Wat wordt er onderzocht? (O)", "Eén duidelijke, afgebakende vraagstelling."],
             ["HYPOTHESE", "Je verwachting vóór de proef, met redenering (V).",
              "Wordt in het besluit getoetst aan de data."],
             ["SCHEMA (schema en/of foto)", "Proefopstelling met alle delen benoemd (V).",
              "Correcte symbolen; foto's duidelijk en van uitleg voorzien."],
             ["TABEL", "Meetresultaten en berekende waarden (U).",
              "Grootheid + eenheid boven elke kolom; beduidende cijfers; berekeningen met Excel-formules "
              "(niet met de hand ingetikt)."],
             ["BEREKENINGEN", "Minstens twee uitgewerkte voorbeelden van elke soort berekening (U).",
              "Formule → invullen met eenheden → resultaat."],
             ["GRAFIEK", "Spreidingsgrafiek met enkel punten, assen benoemd, titel, trendlijn (U).",
              "Geen lijngrafiek; vergelijking van de trendlijn tonen als je de richtingscoëfficiënt nodig hebt."],
             ["BESLUIT", "Antwoord op de onderzoeksvraag, koppeling met de theorie, meetfouten verklaren, "
                         "hypothese bevestigd/verworpen (R).",
              "Hier horen ook de antwoorden op de reflectievragen van het werkblad (individueel verwoord)."],
             ["Feedbackblok + puntenverdeling", "Niet verwijderen!",
              "De leerkracht gebruikt dit om te verbeteren en de punten in te vullen. Alle cursieve "
              "instructietekst verwijder je pas als het verslag helemaal klaar is."]],
            widths=[2450, 3300, 3888], size=9)

    K.h3(doc, "Niet elk labo = een Excel-verslag: wat dien je wanneer in?")
    K.tabel(doc, ["Labo", "Wat dien je in?", "Waarom?"], INDIEN, widths=[900, 4300, 4438], size=9)
    K.p(doc, "Bij elk labo staat dit ook in het evaluatiekader onderaan het werkblad. Eén upload per groep, "
             "dezelfde deadline voor alles.")

    K.h3(doc, "1.4.2 Een groepswerk – zo pak je het aan")
    K.bullets(doc, [
        "Het verslag is één groepswerk per labogroep: iedereen is verantwoordelijk voor het hele verslag "
        "en krijgt er hetzelfde punt voor. 'Ieder een stukje zonder naar de rest te kijken' is géén groepswerk.",
        "Deel het Excel-bestand meteen na het labo via OneDrive (één persoon maakt het aan vanuit het "
        "sjabloon en deelt met bewerkingsrechten): één document, geen losse versies.",
        "Verdeel de onderdelen (omschrijving, tabel + berekeningen, grafiek, besluit) en spreek af wie wat "
        "wanneer afwerkt; zet dat in de groepschat.",
        "Werk ook samen, tegelijk: op school of via videocall (Teams). Besluit en foutenanalyse maak je "
        "samen – daar wordt het meest op gelet.",
        "Lees elkaars delen na: eenheden, beduidende cijfers, Excel-formules, beantwoordt het besluit de "
        "onderzoeksvraag? Een fout van een ander is ook jouw fout.",
        "Iedereen heeft op het einde van de les alle meetresultaten (foto van het werkblad of meteen in "
        "het gedeelde bestand).",
        "Begin op tijd (dag van het labo of de dag erna): reken op minstens twee werkmomenten. De avond "
        "van de deadline lukt een groepswerk niet.",
        "Problemen in de groep? Meld ze tijdig aan de leerkracht; de procesevaluatie en (bij sommige "
        "labo's) de peer-evaluatie verrekenen individuele inzet.",
    ])
    K.kader(doc, "DEADLINE EN INDIENEN", [
        "Uiterlijk één week na het uitvoeren van het labo, 's avonds vóór de les van de volgende week "
        "(dus de avond vóór het volgende labo), om 23.59 u.",
        "In de uploadzone van Smartschool bij het vak Toegepaste fysica: Excel-bestand (.xlsx) uit het "
        "sjabloon, of één PDF van je ingevulde werkbladen, of de poster (labo 16) – zie de indientabel "
        "hierboven. Eén upload per groep, met alle namen in het kopblok en in de bestandsnaam.",
        "Te laat of niet in het sjabloon = aftrek volgens de afspraken van het vak/schoolreglement. "
        "Technische problemen zijn geen excuus: upload tijdig een voorlopige versie en vervang ze "
        "eventueel nog vóór de deadline.",
    ], soort="deadline")

    # ------------------------------------------------------------------ 1.5
    K.h2(doc, "1.5 Evaluatie: product (verslag) en proces & attitude")
    K.p(doc, "Bij elk labo word je op twee manieren geëvalueerd. Samen vormen ze het practicumcijfer: "
             "60 % voor het verslag (product) en 40 % voor proces en attitude.")
    K.tabel(doc,
            ["", "PRODUCTEVALUATIE – 60 %", "PROCES- EN ATTITUDE-EVALUATIE – 40 %"],
            [["Wat?",
              "Het Excel-verslag van de groep (plus eventuele extra producten: werkbladen-PDF, poster bij "
              "labo 16).", 
              "Wat je individueel doet tijdens het labo én hoe je het groepswerk aanpakt: voorbereiding, "
              "veilig en nauwkeurig werken, samenwerking, zelfstandigheid, orde, inzet, reflectie."],
             ["Wanneer?", "Na het indienen van het verslag.",
              "Tijdens elk labo (observatie door de leerkracht) en bij het nakijken van het verslag "
              "(groepswerk, stiptheid)."],
             ["Hoe?",
              "Puntenverdeling onderaan het Excel-sjabloon, /10: 1. Verkennen & onderzoeken (/2) – "
              "2. Onderzoek uitvoeren (/3) – 3. Concluderen (/3) – 4. Attitude (/2). De leerkracht noteert "
              "feedback in het feedbackblok van het sjabloon (zie Bijlage B voor wat er per onderdeel "
              "verwacht wordt).",
              "Eén rubric met 10 thema's (Bijlage C). Per thema een niveau: Uitstekend (1) – Goed (0,8) – "
              "Voldoende (0,6) – Onvoldoende (0,4) – Slecht (0,2) → score /10."],
             ["Punt", "Groepspunt: iedereen van de groep krijgt hetzelfde cijfer.", "Individueel punt."],
             ["Gewicht", "60 % van het practicumcijfer", "40 % van het practicumcijfer"],
             ["Feedback",
              "Schriftelijk in het feedbackblok van het Excel-sjabloon.",
              "Korte mondelinge feedback op het einde van het labo; de ingevulde rubric is te bekijken; "
              "zelfreflectiefiche (Bijlage D) bij labo 2, 6, 9 en 16."]],
            widths=[1500, 4069, 4069], size=9)
    K.kader(doc, "De 10 thema's van de proces- en attituderubric (Bijlage C)", [
        "1 Voorbereiding  •  2 Hypothese en onderzoekend denken  •  3 Opstelling bouwen en meettoestellen "
        "gebruiken  •  4 Nauwkeurig meten en noteren  •  5 Veilig werken",
        "6 Zorg voor materiaal, orde en netheid  •  7 Samenwerking en communicatie (in het labo én bij het "
        "groepsverslag)  •  8 Zelfstandigheid en probleemoplossend handelen  •  9 Inzet, doorzetting en "
        "tijdsbeheer (incl. deadline)  •  10 Reflectie en kritische houding",
    ], soort="lp")
    K.h3(doc, "Peer-evaluatie bij een beperkt aantal labo's")
    K.p(doc, "Bij enkele groepsopdrachten (voorzien bij labo 5, 10 en 14; de leerkracht kan dit aanpassen) "
             "beoordeel je jezelf en je groepsleden met een puntenverdeling. In een groep van drie verdeelt "
             "elke leerling 300 punten over zichzelf en de twee anderen (in een groep van twee: 200 punten). "
             "Vond je dat iedereen evenveel deed, dan geef je iedereen 100. Vind je dat je zelf minder deed, "
             "geef je bv. jezelf 90 en de anderen elk 105. Uit de punten die je van iedereen krijgt, berekent "
             "de leerkracht je peerfactor (gemiddeld ontvangen punten / 100). Het groepspunt voor het verslag "
             "wordt met jouw peerfactor vermenigvuldigd: zo wordt het groepspunt een individueel punt. "
             "Werkwijze en formulier: Bijlage D en het aparte document op Smartschool.")

    # ------------------------------------------------------------------ 1.6
    K.h2(doc, "1.6 Overzicht labo's en leerplandoelen")
    rows = []
    for labo in COURSE_LABOS:
        fys = ", ".join(x for x in labo["lp"].split(";")[0].split(", "))
        stem = labo["lp"].split(";")[-1].strip()
        rows.append([str(labo["nr"]), labo["titel"].capitalize(), labo["type"],
                     str(labo["duur"]), labo["sturing"].split(":")[0], fys, stem])
    K.tabel(doc, ["Labo", "Titel", "Type", "Uren", "Sturing", "Fysica-LPD", "STEM-LPD"], rows,
            widths=[700, 2650, 1750, 500, 1450, 1500, 1088], size=8.5)
    K.p(doc, "★ = specifiek minimumdoel dat in het leerplan met een sterretje is aangeduid "
             "(wrijvingskracht bij 12 F, resonantie bij 18 F). "
             "(#) = onderzoekscompetentie: het bewijsstuk van LPD 6 S.", size=9, italic=True, color="555555")
    K.kader(doc, "Legende van de leerplandoelen (III-BCSW-d, versie januari 2024)", [
        "**Fysica.** 1 F: fysische problemen oplossen met en zonder formularium · "
        "12 F: dynamica van systemen in één en twee dimensies (drie wetten van Newton, ★ invloed "
        "wrijvingskracht) · "
        "13 F: verband tussen positie, tijdstip, snelheid en versnelling bij de eenparig versnelde "
        "rechtlijnige beweging (★ ogenblikkelijke en gemiddelde waarde) · "
        "14 F: horizontale worp · "
        "15 F: hoeksnelheid, baansnelheid en centripetale versnelling bij de ECB · "
        "16 F: gravitatiekracht en gravitatieveld (★ analogie tussen elektrisch veld en gravitatieveld) · "
        "17 F: arbeid als omzetting van energie bij een niet-constante kracht · "
        "18 F: harmonische trillingen (★ resonantie) · "
        "19 F: lopende golven (★ verband tussen frequentie, golflengte en golfsnelheid) · "
        "20 F: geluidsgolven en de decibelschaal · "
        "21 F: verschijnselen bij lopende golven (★ weerkaatsing, breking, interferentie, buiging) · "
        "22 F: staande golven · "
        "23 F: elektromagnetische golven (★ verband tussen energie van een golf en frequentie).",
        "**STEM.** 1 S: onderzoek aan de hand van een wetenschappelijke methode · 2 S: gegevens en "
        "meetwaarden met de juiste symbolen, grootheden en eenheden · 3 S: geschikte labotechnieken voor "
        "betrouwbare informatie, veilig werken · 4 S: een oplossing ontwikkelen voor een probleem · "
        "5 S: wisselwerking tussen wetenschappen, technologie en de maatschappij · "
        "6 S: een onderzoekscyclus in samenhang doorlopen (# onderzoekscompetentie).",
    ], soort="uitleg", size=9.5)
