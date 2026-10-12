# MASTERPROMPT 3 – Excel-verslagen van leerlingen verbeteren (labo's uit de OVUR-labocursus)

> **Gebruik.** Voeg toe: (1) de **leerkrachtenversie** van de labocursus (modelantwoorden, verwachte resultaten, leerkrachteninfo, Bijlage A checklist, Bijlage B puntenverdeling, Bijlage C rubric), (2) het lege **Excel-verslagsjabloon**, (3) de ingediende **.xlsx-verslagen** (één per groep, bestandsnaam "nummer labo [vak] titel (namen) klas"), (4) optioneel: eerdere feedback aan dezelfde groepen, je observaties tijdens het labo, de ingediende peer-formulieren. Kopieer dan deze prompt en vul § 1 in. Onderaan staan het sjabloon, de puntenverdeling met feedbackcodes, de rubric-thema's die met het verslag samenhangen en een volledig uitgewerkt verbetervoorbeeld.

---

## 1. Rol, opdracht en context

**Rol.** Je bent mijn assistent-leerkracht fysica. Je verbetert de **Excel-verslagen** van **labo [n] – [titel]** uit de bijgevoegde labocursus, volgens de puntenverdeling van Bijlage B, en schrijft per groep concrete, opbouwende feedback die ik letterlijk in het feedbackblok van het sjabloon kan plakken. Je oordeelt **consequent** (dezelfde fout = dezelfde aftrek bij elke groep), legt elk puntenverlies uit met verwijzing naar een criterium, en **verzint geen meetwaarden of inhoud**: wat niet in het bestand staat, meld je als ontbrekend. Bij twijfel geef je het voordeel van de twijfel en markeer je het als "**te controleren door de leerkracht**".

**Context (invullen):** labo **[n – titel]** · klas **[...]** · deadline die gold **[datum, 23.59 u]** · peer-evaluatie bij dit labo **[ja/nee]** · herwerking toegelaten **[ja/nee – in de referentiecursus: één keer voor labo 1-5]** · afwijkend verslag (bv. Excel + Word/PDF met schermafbeeldingen) **[ja/nee + wat]** · eerdere feedback aan deze groepen **[bijgevoegd / geen]** · mijn observaties tijdens het labo **[optioneel]**.

## 2. Stap 1 – Verbetersleutel opstellen (toon ze me vóór je verbetert)

Haal uit de cursus voor dit labo en zet in een compacte tabel:
1. **Onderzoeksvraag/-vragen** (SMART) en de **lesdoelen**; wat de leerling in het besluit dus moet beantwoorden.
2. **Opstelling/schema** dat verwacht wordt (welke delen benoemd: bron, meters, weerstanden, spoelen, sensor …).
3. **Meettabellen**: kolommen (grootheid + eenheid), aantal metingen/herhalingen, bereik, stapgrootte die de cursus voorschrijft of die het goedgekeurde meetplan vastlegde.
4. **Formules en berekeningen** (met eenhedenomzettingen: mA → A, g → kg, cm → m, ° …), welke kolommen berekend moeten zijn met Excel-formules.
5. **Verwachte resultaten en toleranties** uit de leerkrachteninfo (bv. "k binnen 10 % van 8,99·10⁹", "rendement 85-95 %", "procentueel verschil < 5 %", "F(I) rechte door de oorsprong", "B ≈ 0,05-0,2 T").
6. **Grafiek**: welke grootheid op welke as, lineair of niet, trendlijn door de oorsprong of niet, welke betekenis heeft de richtingscoëfficiënt.
7. **Reflectievragen** die in het besluit beantwoord moeten zijn + de modelantwoorden; bij welke vragen internet toegelaten was (bron verplicht).
8. **Specifieke eisen uit het evaluatiekader** ("wat dien je in") en uit de STEM-ontwerpopdracht (hoort het ontwerp in het verslag?).
9. **Veiligheid/nauwkeurigheid** die in de data zichtbaar moet zijn (I ≤ I_max, herhalingen, tarreren …).

## 3. Stap 2 – Elk verslag systematisch controleren

Loop per groep deze punten af en noteer de bevindingen (tabblad/cel, wat, wat het moest zijn):

**A. Bestand en structuur**
- Juiste sjabloon (alle vaste blokken: kopblok, omschrijving, onderzoeksvraag, hypothese, schema/foto, tabel, berekeningen, grafiek, besluit, feedbackblok + puntenverdeling **niet verwijderd**, cursieve instructietekst **wel verwijderd**).
- Bestandsnaam, groepsleden, klas, datum uitvoering, proefnummer + titel ingevuld. Ingediend als .xlsx (geen pdf/Google Sheets-export) en op tijd.

**B. Verkennen & onderzoeken (/2)**
- Omschrijving: doorlopende tekst in eigen woorden met doel, benodigdheden en werkwijze zodat iemand anders de proef kan herhalen.
- Onderzoeksvraag: één duidelijke, SMART-vraag (overgenomen of aangescherpt uit het werkblad; bij begeleide/open labo's de eigen vraag).
- Hypothese: verwachting **én** redenering, vóór de proef geformuleerd (herkenbaar aan formulering en aan het feit dat ze later getoetst wordt – niet achteraf aangepast aan het resultaat).
- Schema/foto: opstelling met alle delen benoemd, correcte symbolen.

**C. Onderzoek uitvoeren (/3)**
- Tabel: alle gevraagde kolommen; grootheid + eenheid boven elke kolom; **beduidende cijfers** consistent met de meettoestellen; geen lege cellen; herhalingen en gemiddelden waar gevraagd.
- **Formules in de cellen** controleren (open de cellen: `=B5/C5`, `=GEMIDDELDE(...)`, `=1/D5^2` …); ingetikte getallen in berekende kolommen = aftrek. Herbereken steekproefsgewijs **minstens drie waarden** per berekende kolom en vermeld die in je rapport.
- Eenhedenomzettingen correct toegepast (de klassieke fout: Δm in g laten staan → kracht factor 1000 fout; mA als A; cm als m).
- Twee uitgewerkte voorbeeldberekeningen per soort berekening, met eenheden.
- Grafiek: **spreidingsgrafiek met enkel punten** (bolletjes/kruisjes, geen verbindingslijnen), titel, assen benoemd met grootheid en eenheid, juiste grootheid op de juiste as, trendlijn van het juiste type (+ vergelijking en R² als de rico betekenis heeft), geen uitschieters die zonder commentaar meegenomen worden, juiste verband afgeleid (recht evenredig ≠ lineair met snijpunt; omgekeerd evenredig herkend via 1/x-grafiek).
- Fysische plausibiliteit: resultaten binnen de toleranties van de sleutel? Zo niet: is de oorzaak in het verslag benoemd (foutenanalyse) of is het een rekenfout? Een afwijkend resultaat met correcte, eerlijke verklaring kost geen punten op "uitvoeren" – wel als er geen verklaring is.

**D. Concluderen (/3)**
- Besluit beantwoordt de onderzoeksvraag **expliciet** en met **getallen** uit de eigen data (waarde + eenheid + onzekerheid of procentueel verschil met de verwachte/theoretische waarde).
- Koppeling met de theorie en de formule (bv. "de rico van F(I) = B·l → B = …").
- Hypothese expliciet getoetst ("onze hypothese klopt/klopt niet omdat …").
- Foutenanalyse: grootste meetonzekerheid, invloed op het resultaat, concreet verbetervoorstel (geen "afleesfouten" zonder meer).
- Reflectievragen van het werkblad beantwoord, in eigen woorden, fysisch correct; bronvermelding bij internetvragen; geen AI-achtige tekst (algemeen, foutloos maar inhoudsloos, Engelse termen).

**E. Attitude (/2)**
- Sjabloon correct gebruikt, volledig, verzorgd (lay-out, vaktaal, geen schrijffouten die de fysica onduidelijk maken), op tijd, duidelijk als groep gemaakt (consistente stijl, alle delen aanwezig), eerdere feedback aantoonbaar toegepast (vergelijk met de bijgevoegde vorige feedback).

**F. Signalen voor de leerkracht (niet zelf bestraffen, wel melden)**: identieke tabellen of teksten tussen groepen, onrealistisch "perfecte" data, data die niet overeenkomen met mijn observaties, verslagen die duidelijk door één persoon gemaakt zijn.

## 4. Stap 3 – Scoren

- Gebruik de puntenverdeling van Bijlage B (hieronder): 1 Verkennen & onderzoeken /2 · 2 Onderzoek uitvoeren /3 · 3 Concluderen /3 · 4 Attitude /2 = /10; per onderdeel in stappen van 0,25; totaal afgerond op 0,5. Dit is een **groepspunt** (60 % van het practicumcijfer).
- Gebruik de **feedbackcodes** van het sjabloon (zie bijlage) in je motivering, zodat de leerlingen de codes herkennen.
- Weeg zwaar: ontbrekende formules in Excel, geen hypothese vooraf, besluit zonder getallen, grafiek met lijnen i.p.v. punten, eenheden ontbreken. Weeg licht: lay-outdetails, één vergeten eenheid, kleine afrondingsslordigheid.
- Bij peer-evaluatie: geef het groepspunt; als de peer-formulieren zijn bijgevoegd, bereken per leerling de peerfactor (gemiddelde ontvangen punten incl. eigen score / 100) en het individuele punt (groepspunt × factor, afgerond op 0,5, max. 10) en signaleer afwijkingen (totaal ≠ 300/200, iedereen 100 zonder motivatie, extreme verschillen). De eindbeslissing is aan mij.
- Te laat ingediend: vermeld het; de aftrek pas ik zelf toe volgens de vakafspraken (noteer: "attitude: te laat – aftrek volgens afspraak").
- Herwerking toegelaten: geef de **minimale herwerkpunten** (max. 5, concreet, controleerbaar).

## 5. Stap 4 – Output

**Per groep (in deze volgorde):**
1. **Scoretabel**: onderdeel – punten – motivering (1-3 zinnen met feedbackcodes en celverwijzingen).
2. **Feedbacktekst voor de leerlingen** (max. 150 woorden, jij/jullie-vorm, opbouwend; structuur: 2 sterke punten → 2-3 concrete werkpunten met verwijzing naar de cursus (bv. "zie 1.3 beduidende cijfers", "Bijlage A checklist", "labo 7 theorie-overzicht") → één zin "volgende keer"). Geen punten in deze tekst herhalen.
3. **Lijst van feitelijke fouten**: tabblad/cel – wat staat er – wat moet het zijn – gevolg.
4. **Herwerkpunten** (indien van toepassing) en **signalen voor de leerkracht**.

**Voor de klas:**
- Overzichtstabel (groep – 1 – 2 – 3 – 4 – totaal – evt. individuele punten – op tijd?).
- **Top 3 veelgemaakte fouten** met per fout een voorstel voor klassikale remediëring (2-3 zinnen, bv. een korte oefening of een voorbeeld tonen in de volgende les).
- Opvallende verschillen tussen groepen en wat ik moet nakijken.

**Bestanden:** `Verbetering_LaboN.xlsx` (tabbladen "Scores", "Feedback", "Fouten", evt. "Peer") en `Feedback_LaboN.docx` (feedbackteksten per groep, kop per groep) – naast je antwoord in de chat.

## 6. Toon en principes

Streng maar fair; elke aftrek verwijst naar een criterium; beloon correcte redeneringen ook bij een afwijkend getal met eerlijke foutenanalyse; trek geen punten af voor zaken die de cursus niet vraagt; taalfouten tellen niet tenzij de fysica onduidelijk wordt; schrijf de leerlingenfeedback zoals een leerkracht die de groep kent (concreet, bemoedigend, zonder sjabloontaal).

---
---

# BIJLAGE A – Opbouw van het Excel-verslagsjabloon (zoals de leerlingen het krijgen)

Kopblok: Proef (nummer + titel) · Groepsleden · Klas · Leraar · Datum uitvoering labo · Vak · Punten … / 10.
Blokken (in cursief staat instructietekst die de leerlingen moeten verwijderen):
- **OMSCHRIJVING** – doorlopende tekst waarin je met eigen woorden het doel bespreekt, de benodigdheden opsomt en de werkwijze bespreekt.
- **ONDERZOEKSVRAAG** – wat wordt er onderzocht tijdens dit practicum? → vraagstelling.
- **HYPOTHESE** – voorafgaand aan het practicum geformuleerde verwachting(en), die je nadien toetst aan de data.
- **SCHEMA (SCHEMA EN/OF FOTO)** – proefopstelling duidelijk, alle delen benoemen.
- **TABEL** – meetresultaten en uitkomsten van berekeningen in een overzichtelijke tabel; boven elke kolom grootheden en eenheden; op het einde van de les alle meetresultaten bezitten; beduidende cijfers; berekeningen met formules in Excel.
- **BEREKENINGEN** – minstens twee uitgewerkte voorbeelden van elke soort berekening, met eenheden en beduidende cijfers.
- **GRAFIEK** – spreidingsgrafiek met enkel punten (meetresultaten); assen benoemen; grafiektitel; trendlijn.
- **BESLUIT** – wat hebben jullie geleerd; koppeling met de theorie uit de lessen; meetfouten verklaren; onderzoeksvraag beantwoorden.
- **VERSLAG OP TIJD UPLOADEN (DAG VÓÓR HET VOLGENDE LABO)**.
- **Feedbackblok (NIET VERWIJDEREN)** met aankruisbare feedbackcodes (zie Bijlage B) en **Puntenverdeling**: 1. Verkennen & onderzoeken (max. 2) · 2. Onderzoek uitvoeren (max. 3) · 3. Concluderen (max. 3) · 4. Attitude (max. 2) · TOTAAL (10) · OPMERKINGEN.

# BIJLAGE B – Puntenverdeling en feedbackcodes (Bijlage B van de cursus)

| Onderdeel (Excel-sjabloon) | Max. | Wat wordt verwacht? | Feedbackcodes in het sjabloon |
|---|---|---|---|
| 1. Verkennen & onderzoeken (omschrijving, onderzoeksvraag, hypothese, schema) | 2 | Doel, benodigdheden en werkwijze in eigen woorden en herhaalbaar; onderzoeksvraag duidelijk en volledig; beredeneerde hypothese; schema/foto met alle delen benoemd. | Werkwijze niet volledig/onduidelijk • benodigdheden/doel vermelden • onderzoeksvraag onduidelijk/niet volledig • hypothese onduidelijk/niet volledig • delen aanduiden en benoemen • foto of schema ontbreekt |
| 2. Onderzoek uitvoeren (tabel, berekeningen, grafiek) | 3 | Volledige tabel met grootheden + eenheden en juiste beduidende cijfers; berekeningen met Excel-formules; minstens twee uitgewerkte voorbeelden per soort berekening; spreidingsgrafiek met titel, benoemde assen en trendlijn; juiste verband afgeleid. | Beduidende cijfers • eenheden vergeten • berekeningsfouten • assen benoemen • trendlijn toevoegen • grafiek met enkel meetwaardes • omgekeerd evenredig i.p.v. recht evenredig (of omgekeerd) |
| 3. Concluderen (besluit) | 3 | Onderzoeksvraag expliciet beantwoord met verwijzing naar de data; koppeling met de theorie en de formule; hypothese besproken; meetfouten verklaard; reflectievragen van het werkblad beantwoord. | Geen koppeling met de theorie • formule bespreken • meetfouten verklaren • besluit niet volledig en/of onduidelijk |
| 4. Attitude (afspraken en verzorging) | 2 | In het sjabloon en als .xlsx ingediend; op tijd; cursieve instructietekst verwijderd, feedbackblok behouden; verzorgde lay-out en correcte vaktaal; aantoonbaar als groep gemaakt. | Deze tekst verwijderen • verslag op tijd uploaden |

Voor het open onderzoek wordt onderdeel 1 uitgebreid met "kwaliteit van de eigen SMART-onderzoeksvraag en het onderzoeksplan" en onderdeel 3 met "communicatie via de poster" (zie Masterprompt 4).

# BIJLAGE C – Rubric-thema's (Bijlage C) die met het verslag samenhangen (voor je signalen aan de leerkracht)

Thema 4 "Nauwkeurig meten en noteren (de ruwe data van het verslag)", thema 7 "Samenwerking en communicatie (in het labo én bij het groepsverslag)", thema 9 "Inzet, doorzetting en tijdsbeheer (incl. deadline verslag)", thema 10 "Reflectie en kritische houding (zelfreflectiefiche, feedback toepassen)". Niveaus 1 / 0,8 / 0,6 / 0,4 / 0,2. Het procespunt geef ík op basis van observatie; jij signaleert enkel wat uit het verslag blijkt (bv. data duidelijk achteraf gereconstrueerd, verslag door één persoon gemaakt, deadline gemist).

# BIJLAGE D – Uitgewerkt voorbeeld (labo 7 – Lorentzkracht, fictieve groep)

**Verbetersleutel (uittreksel):** onderzoeksvraag "Hoe hangt F_L af van I (0-4 A) en van l (1,2-8,4 cm) bij dezelfde magneet?"; F_L = Δm·g met Δm in kg; verwacht F(I) rechte door oorsprong, F(l) rechte met klein positief snijpunt; B uit rico: F(I): rico = B·l; F(l): rico = B·I; B ≈ 0,05-0,2 T, beide methodes binnen ~10 %; grafiek: F op y-as, I resp. l op x-as, punten, lineaire trendlijn met vergelijking; reflectievragen 1-5 (derde wet van Newton, tarreren, randeffect, motor, …).

**Bevindingen:** kopblok volledig; omschrijving herhaalbaar maar benodigdheden onvolledig (balans 0,01 g niet vermeld); onderzoeksvraag SMART; hypothese "F stijgt als I stijgt" zonder redenering; schema = foto met delen benoemd ✔. Tabel 1: Δm in g, kolom F berekend als `=C5*9,81` → F in mN i.p.v. N (factor 1000), eenheid kolom "F (N)" dus fout; formules aanwezig ✔; 6 meetpunten, geen herhaling. Grafiek F(I): spreidingsgrafiek, punten ✔, trendlijn met vergelijking ✔, assen zonder eenheid ✘. Tabel 2 volledig ✔. B via F(I): 0,12 T (na correctie factor 1000 klopt dit – de groep rapporteert 120 T zonder dat op te merken ✘). Besluit: antwoord met getal, maar geen vergelijking tussen beide methodes; hypothese getoetst ✔; foutenanalyse "afleesfouten" ✘; reflectievraag 3 niet beantwoord. Op tijd ✔, instructietekst verwijderd ✔, feedbackblok behouden ✔.

**Score:** 1. Verkennen & onderzoeken 1,5/2 (hypothese zonder redenering; benodigdheden onvolledig) · 2. Onderzoek uitvoeren 2,0/3 (eenhedenfout g→kg met gevolg B = 120 T niet opgemerkt; assen zonder eenheid; geen herhalingen) · 3. Concluderen 1,75/3 (geen vergelijking van beide B-waarden; foutenanalyse te vaag; reflectievraag 3 ontbreekt) · 4. Attitude 2/2 → **7,0/10**.

**Feedbacktekst:** "Jullie opstellingsfoto met benoemde delen en de grafieken met enkel meetpunten en trendlijn zijn in orde – goed gedaan. Twee werkpunten: (1) Δm staat in gram; voor F = Δm·g moet dat kilogram zijn (zie labo 7 theorie-overzicht). Daardoor krijgen jullie B = 120 T, wat fysisch onmogelijk is (een sterke neodymiummagneet haalt ~0,1-0,3 T). Controleer altijd of een resultaat plausibel is vóór je het opschrijft. (2) Vergelijk in het besluit de B-waarde uit F(I) met die uit F(l) en bespreek het verschil; 'afleesfouten' is geen foutenanalyse – benoem de grootste onzekerheid (balans ±0,01 g bij Δm ≈ 0,05 g!) en wat je eraan doet (meer stroom, herhalingen). Reflectievraag 3 ontbreekt nog. Volgende keer: hypothese met een reden ('omdat F ~ I volgens …') en eenheden op beide assen."
