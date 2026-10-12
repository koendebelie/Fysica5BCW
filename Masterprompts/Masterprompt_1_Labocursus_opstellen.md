# MASTERPROMPT 1 – Volledige labocursus opstellen volgens de OVUR-methode (specificatie + voorbeelden)

> **Gebruik.** Kopieer deze volledige prompt (inclusief de bijlagen onderaan) in een agentic AI met bestandstoegang. Vul de blokken `[...]` in § 1 en § 2 in en voeg de opgesomde bronbestanden toe. De prompt bevat (a) de opdracht en werkwijze, (b) een gedetailleerde specificatie van structuur, inhoud en vormgeving, (c) de volledige lijst didactische eisen die uit eerdere feedbackrondes komt, (d) technische richtlijnen voor de generatie, (e) controlelijsten en (f) **letterlijke voorbeelden** van een afgewerkte cursus (Deel 1, een gesloten labo, een begeleid labo, de bijlagen) die als stijl- en kwaliteitsreferentie dienen. Het eindresultaat moet dezelfde kwaliteit, diepgang en lay-out hebben als die voorbeelden, maar dan voor de nieuwe klas en leerstof.

---

## 1. Rol, context en bronbestanden

**Rol.** Je bent een ervaren vakdidacticus fysica/STEM, technisch schrijver én programmeur. Je maakt voor mij, **[naam leerkracht]** (vak **[vak, bv. Toegepaste fysica]**, school **[school]**), een volledig herwerkte **labocursus** voor klas **[klas]**, afgestemd op leerplan **[leerplancode + titel + versie]**, voor de leerstof **[onderwerpen, bv. "mechanica: krachten, arbeid, energie"]**.

**Bronbestanden die ik toevoeg (alle verplicht volledig lezen en gebruiken):**
1. **Bestaande labocursus** (pdf + eventueel docx): de basis. Alle practica, figuren, schema's, tabellen, meetwaardenvoorbeelden en tekst moeten in de nieuwe cursus terugkomen, tenzij ik in § 2 zeg dat een labo vervalt. Maak eerst een **inventaris** (per pagina: labo, figuren, tabellen) en vink op het einde af dat alles is overgenomen.
2. **Voorbeeldwerkblad OVUR** (pdf): de exacte structuur (lesdoelen bovenaan, O-V-U-R, invulkaders, antwoordpagina) die elk werkblad moet volgen. De voorbeelden in Bijlage I-IV van deze prompt zijn daar al op gebaseerd.
3. **Leerplan** (pdf): gebruik de officiële nummering en formulering van de leerplandoelen (bv. "LPD 6 F", "LPD 4 S"); markeer onderzoekscompetentie-doelen (bv. "#") waar het leerplan dat doet.
4. **Excel-verslagsjabloon** (xlsx of pdf-afdruk) + de instructies/screencast-samenvatting voor leerlingen rond verslagen en groepswerk.
5. **Verslag vakvergadering / vakgroepafspraken** (pdf): deze info komt **uitsluitend** in de leerkrachtenversie (kaders "Leerkrachteninfo"), nooit in de leerlingenversie.
6. **Theoriecursus / handouts** per onderwerp (pdf): voor terminologie (gebruik dezelfde woorden als de theoriecursus en vermeld synoniemen), figuren om over te nemen, verwijzingen ("zie cursus D1, fig. 1.9"), opgavenummers om naar te verwijzen.
7. Eventueel: handleidingen van meetsoftware/apparatuur (bv. Pasco Capstone, Arduino, Coach), beschrijvingen van nieuwe practica, foto's van opstellingen, voorbeelden van vorige jaren.

**Als er geen voorbeeldwerkblad of sjabloon is meegegeven**: gebruik de voorbeelden in Bijlage I-IV van deze prompt als norm.

## 2. Wijzigingen aan het practicumpakket (invullen)

- Labo's die **vervallen**: **[...]**
- Labo's die **nieuw** zijn (met korte beschrijving, materiaal, en of het een DIY/bouwopdracht, simulatie-/applet-labo of meetlabo is): **[...]**
- Labo's die **samengevoegd/gesplitst** worden: **[...]**
- Meetsoftware/apparatuur waarvan een **handleiding geïntegreerd** moet worden (in het labo waar ze eerst gebruikt wordt + als bijlage): **[...]**
- **Open onderzoek** op het einde (verplicht): ja – met inspiratielijst van **[8-12]** onderzoeksvragen rond **[leerstof]**.
- Aantal lesuren per labo beschikbaar: **[bv. 1-2 lesuren per labo, 3 voor het open onderzoek]**; groepsgrootte **[2-3]**.
- Platform en afspraken: Smartschool (uploadzone, berichten), OneDrive voor groepswerk, deadline verslag = **[één week na het labo, 23.59 u]**.
- Materiaal dat zeker aanwezig is / zeker niet aanwezig is: **[...]**
- Specifieke wensen voor deze klas: **[...]**

Beslis zelf, en motiveer in het eindrapport: labovolgorde, richtduur, type, mate van sturing, indienwijze per labo (Excel-verslag / ingevulde werkbladen / Excel + Word-PDF / poster), labo's met peer-evaluatie (3 stuks voorstellen), labo's met zelfreflectie (4 stuks), SMART-leerlijnniveau per labo.

## 3. Globale structuur van de cursus (verplicht, in deze volgorde)

1. **Voorblad**: "LABOCURSUS [VAK]", ondertitel met de leerstofblokken, "[vak] • [klas]" (geen schooljaar), "Werkbladen volgens de OVUR-methode – Oriënteren – Voorbereiden – Uitvoeren – Reflecteren", invulregels (naam, klas/nummer, leerkracht, labogroep), onderaan verwijzing naar het leerplan. Leerkrachtenversie: extra rode regel "LEERKRACHTENVERSIE – met modelantwoorden, verwachte resultaten en didactische tips (rood gemarkeerd)".
2. **Inhoud**: automatische inhoudsopgave (Word TOC-veld op kop 1-2) + instructie om bij te werken; daaronder een statische lijst als fallback voor PDF-lezers zonder veldupdate.
3. **Deel 1 – Algemene inleiding** met exact deze onderdelen (zie Bijlage I voor de volledige referentietekst; herschrijf naar de nieuwe leerstof maar behoud structuur, tabellen en toon):
   - 1.1 Zo werk je met deze cursus: de OVUR-methode (tabel fase/wat doe je/op het werkblad) · Leerlijn van gesloten naar open (tabel niveau/wie bepaalt wat/labo's) · Een goede onderzoeksvraag is SMART (uitleg van de leerlijn in drie stappen: labo 1-3 vraag gegeven + samen bespreken waarom SMART, labo 4-7 meerkeuze met geloofwaardige afleiders + verantwoording per letter, labo 8-11 zelf formuleren + verantwoorden per letter; tabel met per letter betekenis, controlevraag, goed voorbeeld, slecht voorbeeld – voorbeelden uit de nieuwe leerstof; typische vorm "Hoe hangt [afhankelijke grootheid] af van [onafhankelijke grootheid] bij [constante voorwaarden]?").
   - 1.2 Veiligheid en afspraken in het labo (algemene regels; rol van de **veiligheidsverantwoordelijke** uitgeschreven: wat doet die vóór, tijdens en na de proef; wisselen per labo; leerstofspecifieke risico's).
   - 1.3 Meten, noteren en verwerken (tabel afspraak/toelichting: grootheid-symbool-eenheid, beduidende cijfers, meetonzekerheid, herhaalde metingen, grafieken met **meetpunten als bolletjes of kruisjes**, digitaal werken, databeheer, internet bij reflectievragen).
   - 1.4 Het verslag: 1.4.1 Excel-sjabloon (tabel onderdeel/wat komt erin/aandachtspunten) · 1.4.2 Groepswerk zo pak je het aan (OneDrive, taakverdeling, iedereen leest alles, één upload) · **"Niet elk labo = een Excel-verslag" met de indientabel** (labo – wat dien je in – hoe) · **Peer-evaluatie bij een beperkt aantal labo's** (korte uitleg 300-puntenmethode, verwijzing Bijlage D).
   - 1.5 Evaluatie: product (verslag 60 %) en proces & attitude (40 %), tabel met wat/wie/hoe/wanneer.
   - 1.6 Overzicht labo's en leerplandoelen (tabel labo/titel/type/richtduur/sturing/LPD's) + legende van alle LPD's.
4. **Labo 1 … Labo n** – elk op een nieuwe pagina, volgens de werkbladspecificatie in § 4.
5. **Bijlagen**: A Excel-verslagsjabloon: opbouw en checklist · B Productevaluatie: het verslag (60 %) · C Proces- en attituderubric (40 %) – liggende pagina · D Zelfreflectie- en peer-evaluatiefiche · E Naslag (begrippenlijst + naslagtabellen + formuleoverzicht) · F (en verder) handleidingen meetsoftware/apparatuur met schermafbeeldingen. Zie Bijlage IV van deze prompt voor de referentietekst van A-E; de rubric moet **letterlijk** overgenomen worden (10 thema's × 5 niveaus) en enkel waar nodig aangepast aan de leerstof (bv. "A-meter in serie" → leerstofspecifiek voorbeeld).

## 4. Specificatie van één werkblad (per labo, exact deze volgorde en benamingen)

| # | Onderdeel | Inhoudelijke eisen |
|---|---|---|
| 1 | Kop | Kop 1: "LABO n – TITEL IN HOOFDLETTERS: ONDERTITEL". Regel: Naam / Klas / Nr. / Datum met invulpuntjes. Regel: **Richtduur** (x lesuren) + **Type practicum** (bv. begrips- en onderzoekspracticum in delen / apparatuurpracticum / onderzoekspracticum met sensoren / open praktijkonderzoek; met groepsgrootte). Regel: **Mate van sturing** (één zin, cursief, bv. "BEGELEID → OPEN: onderzoeksvraag gegeven, meetplan stel je zelf op"). |
| 2 | Kader **LESDOELEN – na dit labo kan je …** (groen) | 4-7 lesdoelen, elk één concreet, toetsbaar handelingswerkwoord ("meten", "verklaren met het model van …", "uit de grafiek afleiden dat …", "bouwen en testen", "veilig …"), met de kernformule of het kernbegrip erin. Laatste lesdoel gaat steeds over veilig/nauwkeurig/gestructureerd werken of rapporteren. |
| 3 | Kader **LEERPLANDOELEN (leerplancode)** (oranje) | LPD-nummers met korte omschrijving; vakdoelen én STEM-/onderzoeksdoelen; bij het open onderzoek het onderzoekscompetentie-doel. |
| 4 | Kader **VOORKENNIS – check vóór je begint** (paars) | 2-4 korte vragen/items die de leerling moet beheersen (formules, regels, verwijzing naar eerder labo of theoriecursus). In de leerkrachtenversie staan de antwoorden eronder. |
| 5 | (enkel leerkrachtenversie) Kader **LEERKRACHTENINFO – didactische tips, verwachte resultaten, valkuilen** (rood) | 3-6 bullets: opstelling vooraf, instellingen, verwachte meetwaarden/orde van grootte en tolerantie, typische fouten van leerlingen, timing, info uit de vakvergadering, differentiatie. |
| 6 | **O – ORIËNTEREN** (kop 2) | Kop 3 **Context**: 1-2 alinea's, concreet en herkenbaar (dagelijks leven, techniek, beroep), link met vorig labo, en één zin "wat doen we in dit labo". Kop 3 **Onderzoeksvraag**: 1-3 vragen als bullets, SMART geformuleerd. Kop 3 **Doel van het onderzoek**: 2-4 bullets (wat kunnen/kennen ze erna). Kop 3 **Oriëntatievragen (beantwoord vóór het labo)**: 2-4 genummerde vragen met invulkader (2 regels), die voorkennis activeren en voorspellen; modelantwoord in leerkrachtversie. Leerlijn onderzoeksvragen – **vanaf stap 2 wordt de onderzoeksvraag in de O-fase NIET meer gegeven**: de kop "Onderzoeksvraag" wordt dan vervangen door de oefening zelf (kop 3 "Onderzoeksvraag (leerlijn SMART – stap 2: jij kiest)" resp. "… stap 3: jij formuleert)"); alleen in stap 1 staat de vraag onder "Onderzoeksvraag" én volgt daarna de kop 3 **Oefenen op onderzoeksvragen (leerlijn SMART – stap 1: de vraag krijg je)**. Eisen aan elke juiste/gegeven vraag: ze dekt het **hele labo** (alle delen of verbanden, eventueel met twee deelonderzoeken van elk één variabele), noemt wat gevarieerd, gemeten en constant gehouden wordt, met bereik en meetmethode, en eindigt op "tijdens dit labo" (nooit "tijdens labo 4"); geen interne jargonwoorden zoals "plank" of "duo X". Inhoud per stap – *given* (labo 1-3): "Stap 1 van de leerlijn: de onderzoeksvraag krijg je. We bekijken samen waarom ze SMART is." + de onderzoeksvraag (vet/cursief) + opdrachtje "onderstreep wat je verandert (O), omcirkel wat je meet (A), kader rond wat constant blijft (C)" + ingevulde tabel Letter / Waarom is deze vraag SMART? (S, M, A, R, T elk één concrete zin over déze vraag); *mc* (labo 4-7): "Stap 2 van de leerlijn: vier voorstellen, maar slechts één is een goede SMART-onderzoeksvraag voor dit labo. Omcirkel ze." + 4 opties A-D die er allemaal geloofwaardig uitzien: één SMART, één die goed lijkt maar een letter mist (bv. kracht niet meetbaar gemaakt, geen bereik, geen constante voorwaarden), één die net naast het onderwerp zit (bv. een I(U)-verband i.p.v. de inwendige schakeling), één die niet realistisch is met het labomateriaal (bv. B variëren met één magneet, 5 kernmaterialen) – geen flauwe afleiders zoals "Hoe werkt magnetisme?"; daarna "Verantwoord per letter waarom jouw keuze SMART is, en schrijf bij elk ander voorstel in één zin welke letter ontbreekt" + tabel Mijn keuze / S / M / A / R / T + 3 invulregels; *self* (labo 8-11): "Stap 3 van de leerlijn: formuleer zelf een SMART-onderzoeksvraag voor [onderwerp] en verantwoord per letter waarom ze SMART is. Gebruik de vorm 'Hoe hangt … af van … bij …?'" + tabel Mijn onderzoeksvraag / S / M / A / R / T. In de leerkrachtenversie bij elke stap een modelantwoord (given: O/A/C benoemd; mc: juiste letter + per afleider welke letter ontbreekt + verantwoording per letter; self: voorbeeldvraag + waarop streng/mild zijn). |
| 7 | **V – VOORBEREIDEN** (kop 2) | Kop 3 **Benodigdheden**: volledige lijst per groep (toestellen met bereik/instelling, materialen met afmetingen/aantallen, software, eigen laptop…). Kop 3 **Theorie-overzicht**: korte, vetgedrukte kernbegrippen met uitleg in 1-3 zinnen, formules met de formule-editor (met eenheden), verwijzing naar de theoriecursus; **uitleg-kaders** ("UITLEG – …") voor begrippen die nog niet gezien zijn. Kader **VEILIGHEID // NAUWKEURIGHEID** (rood): 3-6 bullets, leerstofspecifiek, met de **maximale stroom/spanning/temperatuur/… voor dít labo** (situatiegebonden, nooit een standaardwaarde voor alle labo's), controle door de leerkracht vóór inschakelen, nauwkeurigheidsafspraken (bereiken, herhalingen, tarreren…), alternatieven bij technische problemen (USB i.p.v. Bluetooth, schoollaptop…). Kop 3 **Hypothese**: cursieve instructie + invulkader (3 regels). Kop 3 **Werkplan** (bij begeleide/open labo's): bullets wat de leerlingen zelf vastleggen (rollen, volgorde, meetbereik, stappen, herhalingen) + "laat je plan goedkeuren". |
| 8 | **U – UITVOEREN** (kop 2) | Opgedeeld in Kop 3 **"Deel 1 – titel", "Deel 2 – titel", …** (of "Proef 1 …"); **nooit "station"**. Per deel: onderzoeksvraag van het deel (vet label "Onderzoeksvraag:"), "Hypothese:" met regel, "Uitvoering:" met genummerde stappen in korte zinnen, meettabel (kolommen = grootheid (eenheid); rijen vooraf ingevuld waar zinvol; lege rijen met vaste hoogte), plaats voor "Foto / schets", "Waarneming:" en "Verklaring:" met invulkaders, "Reflectie:"-vraagjes. Figuren uit de oude cursus en nieuwe schema's met bijschrift (cursief, grijs, met bron). Bij doorschuifpractica: tijd per deel en volgorde-instructie. Minstens één kader **STEM-ONTWERPOPDRACHT (LPD …) – titel** (groen-blauw) per labo: doel, randvoorwaarden, wat ze noteren (onderzoeksvraag, variabelen, werkwijze, resultaat, besluit), of ze het effectief bouwen en welk bewijs (foto/test) verwacht wordt. Bij open labo's: variabelentabel (onafhankelijk/afhankelijk/constant) en voorbeeldtabel "als steun". |
| 9 | **R – REFLECTEREN** (kop 2) | Kop 3 **Besluit**: cursief "Antwoord op de onderzoeksvraag, onderbouwd met je metingen. Klopt je hypothese?" + kader 4 regels. Kop 3 **Foutenanalyse en betrouwbaarheid**: cursief "Grootste meetonzekerheid? Hoe verbeter je de proef?" + 3 regels. Kop 3 **Reflectievragen**: 4-7 genummerde vragen met 2 regels elk, oplopend: begrip (verklaar met model), toepassing (voorspel/bereken), techniek/maatschappij (laat leerlingen **zelf** een voorbeeld zoeken i.p.v. het voor te zeggen), kritische vraag (betrouwbaarheid, verbetering), eventueel ontwerpvraag. Voeg bij vragen waar opzoeken zinvol is letterlijk toe: " [Internet toegelaten: gewone zoekmachine zoals Google, bron vermelden – geen AI-tool.]". Modelantwoorden in de leerkrachtversie. |
| 10 | Kader **WAT, HOE EN WANNEER WORDT GEËVALUEERD IN DIT LABO?** (grijs) | Zes vaste regels: "PRODUCT (60 %) – wat: …" (concreet product van dit labo) · "PRODUCT – hoe en wanneer: puntenverdeling /10 (Bijlage B), groepspunt, feedback in het feedbackblok; deadline = één week na het labo, 23.59 u, Smartschool-uploadzone." · "PRODUCT – wat dien je in: …" (uit de indientabel) · "PROCES & ATTITUDE (40 %) – wat: …" (2-3 observeerbare accenten van dit labo) · "PROCES & ATTITUDE – hoe: observatie door de leerkracht met de rubric van Bijlage C (10 thema's × 5 niveaus), individueel punt." · "PEER-EVALUATIE: ja – … (werkwijze: Bijlage D)" of "niet voorzien bij dit labo (tenzij de leerkracht dit aankondigt)". |

**Omvang per labo**: 5-11 pagina's, evenwichtig over alle labo's (geen rijk eerste labo en mager laatste). Elk labo bevat minstens 1 figuur, 1 tabel, 1 formule (indien relevant) en 1 STEM-kader.

**Sturingsleerlijn** (voorbeeld uit de referentiecursus – pas aan):
- Labo 1: GESLOTEN → BEGELEID. Delen 1-5: werkwijze gegeven; Deel 6: je ontwerpt zelf een proef.
- Labo 2: BEGELEID. Deel 1: werkwijze gegeven; Deel 2-4: je stelt zelf het meetplan op; Deel 5: open ontwerpuitdaging.
- Labo 3: GESLOTEN (apparatuurpracticum): werkwijze volledig gegeven – focus op correct meten.
- Labo 4: GESLOTEN + ONTWERP: metingen volgens schema; daarna ontwerp je zelf een schakeling met opgelegde weerstand.
- Labo 5: BEGELEID: je kiest zelf de meetstrategie; daarna ontwerp je een black box voor een ander duo.
- Labo 6: BEGELEID: per deel eigen hypothese en conclusie; Deel 8: eigen onderzoeksvraag.
- Labo 7: BEGELEID → OPEN: onderzoeksvraag gegeven, meetplan (bereik, stappen, herhalingen) stel je zelf op.
- Labo 8: BEGELEID + OPEN BOUWOPDRACHT: eigen ontwerp van een homopolaire motor.
- Labo 9: BEGELEID → OPEN: eigen variabelenlijst voor de sensormetingen; ontwerp van een mini-generator.
- Labo 10: OPEN WERKPLAN: doel en materiaal gegeven, procedure en tabellen maak je zelf (voorbeeld als steun).
- Labo 11: OPEN: volledige onderzoekscyclus zelfstandig (onderzoekscompetentie).

**Indientabel** (voorbeeld uit de referentiecursus – pas aan):
- Labo 1: ingevulde werkbladen (foto's/scan van dit labo, incl. schetsen) als één PDF in de uploadzone – GEEN Excel-verslag (doorschuifpracticum).
- Labo 2: Excel-verslagsjabloon (tabellen + grafieken F(1/r²) en E(1/r²)) + schermafbeeldingen van de veldlijnen in het tabblad 'Schema'.
- Labo 3: ingevulde werkbladen als PDF in de uploadzone – GEEN Excel-verslag (kort apparatuurpracticum).
- Labo 4: Excel-verslagsjabloon (tabellen a-f, U(I)-grafieken, ontwerpopdracht in 'Besluit').
- Labo 5: Excel-verslagsjabloon (tabel + redenering per box; eigen black box als schema in 'Schema').
- Labo 6: ingevulde werkbladen (delen 1-8 met foto's) als PDF in de uploadzone – GEEN Excel-verslag (doorschuifpracticum).
- Labo 7: Excel-verslagsjabloon (twee tabellen, twee grafieken, bepaling van B).
- Labo 8: ingevulde werkbladen (incl. schetsen motor/luidspreker en foto van de homopolaire motor) als PDF in de uploadzone – GEEN Excel-verslag.
- Labo 9: Excel-verslagsjabloon voor proef 1-2 + Word/PDF met Capstone-schermafbeeldingen en uitleg voor proef 3-4 (samen uploaden).
- Labo 10: Excel-verslagsjabloon (eigen tabel volgens je werkplan, U₂(U₁)-grafiek, rendement).
- Labo 11: wetenschappelijke poster (PDF, A3) + Excel-bestand met ruwe data en grafieken.

## 5. Didactische eisen – vaste feedback die altijd geldt

**Taal en begrijpelijkheid**
1. Eenvoudige, duidelijke taal; korte zinnen; "je"-vorm voor leerlingen. Elk moeilijk of vakspecifiek woord wordt bij eerste gebruik uitgelegd (tussen haakjes of in een uitleg-kader) én opgenomen in de begrippenlijst van Bijlage E. Vermijd woorden als "geannoteerd", "gemonteerd", "kwantificeren" zonder uitleg; schrijf "schermafbeelding met titel en uitleg", "vastgemaakt", "meten hoe groot".
2. Gebruik de **terminologie van de theoriecursus** en vermeld het synoniem (bv. "influentie (in de theoriecursus 'elektrostatische inductie' genoemd)").
3. Leg begrippen die op dat moment nog niet gezien zijn kort uit in een kader "UITLEG – …" (bv. derde wet van Newton, wervelstromen, Weiss-gebieden, joule-effect, fluxverandering, "oppervlakte onder een piek zonder integralen"). Nooit veronderstellen dat iets gekend is omdat het later in het curriculum komt.
4. Verwijs naar concrete, bekende voorbeelden uit hun opleiding of leefwereld (bv. "microcontroller zoals de Raspberry Pi Pico uit het vierde jaar", "oplader van je laptop").
5. Vermeld geen schooljaar in de teksten (de cursus blijft meerdere jaren bruikbaar).

**Fysica en opstelling**
6. Beschrijf de opstelling zoals ze er echt is; pas onderzoeksvraag en uitleg daaraan aan (bv. één magneet → B constant: "we kunnen B niet variëren, wel bepalen").
7. Maximale stroom/spanning/etc. per labo bepalen op basis van het materiaal (I_max van de spoel, grenzen van bron en geleiders); nooit één standaard "max. 5 A" overal.
8. Ontwerp- en bouwopdrachten concreet: wat ontwerpen ze, bouwen ze het effectief, met welk materiaal, welke test geldt als geslaagd, welk bewijs (foto, meting) komt in het verslag.
9. Alternatieven voor technische risico's (kabel i.p.v. Bluetooth, schoollaptop, reservemateriaal).

**Onderzoeksvaardigheden en leerlijnen**
10. Sturingsleerlijn gesloten → begeleid → open, zichtbaar bovenaan elk labo én in Deel 1; SMART-leerlijn in drie stappen (gegeven + bespreken / meerkeuze met geloofwaardige afleiders + verantwoording / zelf + verantwoording) met de oefening in élk labo.
11. Grafieken: meetpunten als bolletjes of kruisjes (spreidingsgrafiek), nooit verbonden; aparte trendlijn met vergelijking als de richtingscoëfficiënt betekenis heeft.
12. Hypothese altijd vóór de proef, met redenering; expliciet getoetst in het besluit.
13. Het open onderzoek: 1 lesuur voorbereiding (vraag kiezen/opstellen, SMART, variabelen, werkwijze, materiaallijst, risicoanalyse, goedkeuring) + 2 lesuren uitvoering; verwerking en **wetenschappelijke poster (A3, PDF)** thuis; geen PowerPoint, geen presentatie, geen peerfeedback; inspiratielijst + eigen vraag toegelaten; checklist poster (titel/namen, SMART-vraag, hypothese, methode met foto/schema en variabelen, resultaten tabel + grafiek met assen/eenheden/trendlijn, besluit, foutenanalyse en verbetervoorstel, bronnen; leesbaar vanop 1,5 m, max. ca. 300 woorden).

**Evaluatie**
14. Product 60 % (puntenverdeling /10: 1 Verkennen & onderzoeken /2, 2 Onderzoek uitvoeren /3, 3 Concluderen /3, 4 Attitude /2) en proces & attitude 40 % (rubric 10 thema's × 5 niveaus 1/0,8/0,6/0,4/0,2, som /10). Geen rubric voor het product.
15. Per labo het evaluatiekader met wat/hoe/wanneer en wat precies wordt ingediend (Excel-verslag óf ingevulde werkbladen als PDF via de uploadzone óf combinatie óf poster) – beslis per labo (doorschuifpractica en korte apparatuurpractica → werkbladen; meetlabo's met tabellen/grafieken → Excel).
16. Peer-evaluatie enkel bij een beperkt aantal groepslabo's (3 voorstellen; leerkracht kan wijzigen), 300-puntenmethode met peerfactor, uitgelegd in Deel 1 en Bijlage D; zelfreflectiefiche bij 4 labo's.
17. Vakvergaderingsinfo, didactische tips, verwachte waarden en modelantwoorden enkel in de leerkrachtenversie (rode kaders "Modelantwoord:" direct onder de vraag; "Leerkrachteninfo" na de voorkennis).

**Volledigheid**
18. Alle figuren van de oude cursus overnemen (bijgesneden, scherp, met bijschrift en bron "cursus …, fig. …"); extra figuren (foto's van opstellingen, schema's, internetbeelden met bron) alleen als ze echt iets bijbrengen. Niets uit de oude cursus vergeten (tabellen, meetwaardenvoorbeelden, vragen).
19. Benodigdheden per labo volledig; **bestellijst** apart (enkel nieuw materiaal dat een gewoon fysicalabo niet heeft: item, aantal voor n groepen, richtprijs, waar te koop, kolom "controleren of al aanwezig").
20. Verwijzingen kloppen (bijlagen, paragraafnummers, "zie labo n deel m").

## 6. Vormgeving en technische eisen

- A4 staand, marges 2 cm (boven/onder 1,8 cm), Calibri 10,5-11 pt; rubric op een liggende pagina.
- **Echte Word-kopstijlen**: Kop 1 = Deel/Labo/Bijlage, Kop 2 = O/V/U/R en paragrafen van Deel 1, Kop 3 = onderdelen – zodat de automatische inhoudsopgave werkt en de leerkracht de cursus kan bewerken.
- Kaders als 1-cel-tabellen met lichte achtergrondkleur en gekleurde titel: lesdoelen groen (E8F5E9), leerplandoelen geel (FFF8E1), voorkennis paars (F3E5F5), veiligheid rood (FDECEA), STEM groen-blauw (E0F2F1), uitleg blauw (E8F1FA), evaluatie grijs (EEEEEE), leerkrachtinfo/modelantwoord roze (FFF3F3) met rode tekst.
- Invulkaders = omrande vakken met vaste hoogte (geen puntjeslijnen); tabellen met rasterlijnen, kopregel lichtblauw (D9E2F3), vaste kolombreedtes.
- Formules met de **formule-editor** (OMML), gecentreerd, met eenheden tussen vierkante haken waar zinvol; inline symbolen (F, I, Δm) in de lopende tekst gewoon als tekst met correcte sub-/superscript.
- Afbeeldingen: JPG/PNG ≤ 900 px breed, gecentreerd, bijschrift cursief grijs 9 pt.
- Voettekst: "Labocursus [vak] [klas] – [leerstof] – pagina n"; elk labo en elke bijlage start op een nieuwe pagina.
- Bestandsnamen: `Labocursus_[klas]_LEERLING.docx/.pdf` en `Labocursus_[klas]_LEERKRACHT.docx/.pdf`; bestellijst `Bestellijst_nieuw_materiaal.docx`.

## 7. Werkwijze (zo verwacht ik dat je te werk gaat)

1. **Analyse**: extraheer tekst en figuren uit alle bronbestanden; maak de inventaris (labo's, figuren, tabellen, leerplandoelen); noteer onduidelijkheden.
2. **Ontwerp**: labovolgorde, duur, type, sturing, SMART-niveau, indienwijze, peer/zelfreflectie-labo's, STEM-opdracht per labo; toon me dit overzicht in het eindrapport.
3. **Generatie uit één bron**: schrijf een script (bv. Python + python-docx + een LaTeX→OMML-helper) met een vlag voor de leerkrachtenversie, zodat beide versies identiek zijn op de rode kaders na. Modelantwoorden in een apart woordenboek (vraag → antwoord) zodat ze consequent onder de juiste vraag komen.
4. **Controle**: zet beide versies om naar PDF, render elke pagina en controleer visueel (afgesneden tabellen, lege pagina's, formules, figuren, kaders die over pagina's breken, nummering). Controleer met zoekopdrachten: geen "station", geen schooljaar, geen onverklaarde moeilijke woorden, geen "max. 5 A" buiten het labo waar het hoort, alle figuurbestanden gebruikt, vakvergaderingsinfo enkel in de leerkrachtversie.
5. **Oplevering**: beide docx + pdf, bestellijst, en een **eindrapport** met: labo-overzichtstabel, genomen beslissingen, afgevinkte checklist van § 3-6, inventaris "figuren oude cursus → pagina nieuwe cursus", openstaande vragen voor de leerkracht.

## 8. Kwaliteitsnorm

De kwaliteit, diepgang en toon van de bijlagen hieronder zijn de norm. Lees ze vóór je begint: Bijlage I (Deel 1 volledig), Bijlage II (een gesloten/begeleid eerste labo met doorschuifdelen en bouwopdracht – labo 1 van de referentiecursus), Bijlage III (een begeleid meetlabo met eigen meetplan en grafische verwerking – labo 7), Bijlage IV (bijlagen A-E incl. de volledige rubric), Bijlage V (structuur van een software-handleiding). Markeringen in de voorbeelden: `[KADER: …]` = gekleurd kader, `[FIGUUR: …]` = afbeelding met bijschrift, `$$…$$` = formule in de formule-editor, `Modelantwoord` en `LEERKRACHTENINFO` = enkel leerkrachtenversie. Alles wat in de voorbeelden na een vraag als modelantwoord staat, hoort in de nieuwe cursus eveneens volledig uitgewerkt te zijn.

---
---

# BIJLAGE I – Referentietekst Deel 1 (volledig)

# Deel 1 – Algemene inleiding

## 1.1 Zo werk je met deze cursus: de OVUR-methode
Elk werkblad volgt dezelfde vier fasen van de onderzoekscyclus. Lees vóór elk labo de lesdoelen en leerplandoelen: daarop worden verslag én labowerk beoordeeld.
| Fase | Wat doe je? | Op het werkblad |
|---|---|---|
| O – Oriënteren | Wat, waarom, welke voorkennis? | Context, onderzoeksvraag, doel, oriëntatievragen. |
| V – Voorbereiden | Plan maken: stappen, materiaal, veiligheid, hypothese. | Benodigdheden, theorie, veiligheid, hypothese, werkplan. |
| U – Uitvoeren | Meten, noteren, observeren volgens plan. | Procedure, tabellen, grafische STEM-opdracht, foto's. |
| R – Reflecteren | Kloppen de resultaten? Wat kan beter? Besluit en link met de maatschappij. | Besluit, foutenanalyse, reflectievragen. |

### Leerlijn: van gesloten naar open practica (STEM-doelen 1 S, 4 S, 6 S)
Doorheen het jaar krijg je stap voor stap meer verantwoordelijkheid: eerst voer je een gegeven werkwijze nauwkeurig uit, daarna stel je zelf meetplannen op, ontwerp je oplossingen en ten slotte doorloop je een volledige onderzoekscyclus. Bij elk labo staat bovenaan de 'mate van sturing'. Opdrachten in een groen kader ('STEM-ontwerpopdracht') los je zelf op: er is geen vaste werkwijze, wel een duidelijk doel en duidelijke randvoorwaarden.
| Niveau | Wie bepaalt wat? | Labo's |
|---|---|---|
| Gesloten | Vraag, werkwijze en tabel gegeven – jij meet, noteert en redeneert nauwkeurig. | 1 (deel 1-5), 3, 4 |
| Begeleid | Vraag gegeven; jij kiest meetstrategie, variabelen, bereik en tabelopbouw. Ontwerpopdrachten met randvoorwaarden. | 2, 5, 6, 7, 8, 9 |
| Open | Jij stelt het werkplan of de onderzoeksvraag op; de leerkracht keurt goed en coacht. | 10, 11 |

### Een goede onderzoeksvraag is SMART
Elk onderzoek start met een goede onderzoeksvraag. In het zesde jaar moet je die volledig zelf kunnen opstellen; in deze cursus oefen je dat in drie stappen. Stap 1 (labo 1-3): je krijgt de onderzoeksvraag en we bespreken samen waarom ze SMART is. Stap 2 (labo 4-7): je kiest de SMART-vraag uit vier voorstellen die er allemaal goed uitzien, maar waarvan er drie niet SMART zijn of net naast het onderwerp zitten – en je verantwoordt je keuze per letter. Stap 3 (labo 8-11): je formuleert de onderzoeksvraag zelf en legt per letter uit waarom ze SMART is.
*Een SMART-vraag is bijna altijd van de vorm: 'Hoe hangt [afhankelijke grootheid] af van [onafhankelijke grootheid] bij [constante voorwaarden]?' of 'Wat is de invloed van … op …?'*
| Letter | Betekenis | Controlevraag | Voorbeeld (goed) | Voorbeeld (slecht) |
|---|---|---|---|---|
| S – Specifiek | Eén duidelijk afgebakend verband tussen twee grootheden. | Welke grootheid verander ik, welke meet ik, wat houd ik constant? | Hoe hangt de Lorentzkracht op een geleider van 4,2 cm af van de stroomsterkte (0-4 A) bij dezelfde magneet? | Hoe werkt magnetisme? |
| M – Meetbaar | Beide grootheden zijn te meten of waar te nemen. | Met welk toestel, in welke eenheid? | … kracht via Δm op de balans (g → N) … | Is magnetisme sterk? |
| A – Aanvaardbaar | Zinvol en relevant binnen het vak, veilig, ethisch. | Waarom is dit de moeite waard? Mag en kan dit in het labo? | … (basis van de elektromotor) … | Hoeveel stroom kan een leerling verdragen? |
| R – Realistisch | Haalbaar met het beschikbare materiaal en in de tijd. | Heb ik het materiaal, lukt het in 2 lesuren? | … met de balans en magneet van het labo … | Hoe hangt de kracht af van B? (we hebben maar één magneet) |
| T – Tijdsgebonden | Duidelijk wanneer/binnen welke periode het onderzoek klaar is. | Wanneer meet ik, wanneer lever ik in? | … gemeten tijdens dit labo, verslag binnen één week. | Ooit eens uitzoeken. |

## 1.2 Veilig werken in het elektriciteitslabo
Geldt bij elk labo en telt mee in de procesevaluatie (thema 5).
- Opbouwen met bron UIT en knop op 0; elke opstelling laten controleren vóór inschakelen.
- De maximale stroomsterkte verschilt per proef: ze staat telkens op het werkblad en/of op het toestel (I_max). Respecteer ze altijd; bij twijfel vraag je het aan de leerkracht.
- A-meter in serie, V-meter parallel. A-meter over de bron = kortsluiting (zekering springt).
- Multimeter: grootste bereik eerst. Snoer na stroommeting terug uit de A-klem.
- Geen blanke geleiders aanraken onder spanning; warme draden → bron onmiddellijk uit.
- Water en elektriciteit: enkel waar uitdrukkelijk gevraagd (bv. waterstraal labo 1), nooit bij ingeschakelde bronnen; gemorst water meteen opdrogen.
- Neodymiummagneten: weg van gsm, bankkaart, laptop, pacemaker en elkaar (knelgevaar).
- Hoogspanning (Van de Graaff, veldlijnenvoeding): enkel de leerkracht.
- Orde: geen snoeren over de tafelrand, geen tassen in looppaden, werkpost opruimen en materiaal terugleggen.

## 1.3 Meten, noteren en verwerken
| Afspraak | Toelichting |
|---|---|
| Grootheid – symbool – eenheid | Elke kolomkop: symbool + SI-eenheid, bv. U (V), I (A), R (Ω). |
| Beduidende cijfers | Zoveel cijfers als het toestel betrouwbaar geeft (2,34 V); een resultaat niet nauwkeuriger dan de minst nauwkeurige meting. |
| Meetonzekerheid | Afleesnauwkeurigheid per toestel noteren (digitale meter: ± laatste cijfer; lat: ± 0,5 mm) en bespreken in de foutenanalyse. |
| Herhaalde metingen | Minstens 3× meten, gemiddelde; grote spreiding = weinig betrouwbaar. |
| Grafieken | Titel, grootheid + eenheid op de assen, meetpunten als kruisjes of bolletjes (niet verbinden), best passende lijn (geen verbind-de-punten); bij recht evenredig: rechte door de oorsprong, rico bepalen. |
| Digitaal | Excel/Sheets of Pasco Capstone: tabel, spreidingsgrafiek, trendlijn + vergelijking; schermafbeelding in het verslag. |
| Databeheer | Ruwe data meteen en chronologisch op het werkblad; nooit 'verbeteren'. |
| Internet bij reflectievragen | Enkel bij vragen waar het uitdrukkelijk vermeld staat ('Internet toegelaten'). Gebruik een gewone zoekmachine (Google, Bing …) en vermeld je bron. AI-tools (ChatGPT, Copilot …) om je antwoord te laten schrijven zijn niet toegelaten: het antwoord moet in je eigen woorden en vanuit jouw metingen komen. |

## 1.4 Het laboverslag: Excel-sjabloon, groepswerk en deadline

### 1.4.1 Altijd het Excel-verslagsjabloon gebruiken
Voor elk labo maak je het verslag in het blanco Excel-verslagdocument dat op Smartschool staat (map 'Toegepaste fysica – labo'). Je gebruikt altijd dit sjabloon – geen eigen Word- of Google-document – en je levert het ook als Excel-bestand (.xlsx) in. Op Smartschool vind je naast het sjabloon een screencast die stap voor stap toont hoe je elk onderdeel invult (tabellen met formules, spreidingsgrafiek met trendlijn, besluit). Bekijk die screencast vóór je eerste verslag en opnieuw als je twijfelt.
Het sjabloon bevat dezelfde onderdelen als de OVUR-werkbladen, in deze volgorde:
| Onderdeel in het Excel-sjabloon | Wat komt erin? (OVUR-fase) | Aandachtspunten uit het sjabloon |
|---|---|---|
| Kopblok | Groepsleden, klas, datum uitvoering, nummer en titel van de proef (bestandsnaam: 'nummer labo TF titel (namen) 5BCW'). | Volledig invullen; dit is ook de bestandsnaam bij het uploaden. |
| OMSCHRIJVING | Doorlopende tekst in eigen woorden: doel, benodigdheden en werkwijze (O + V). | Geen opsomming kopiëren van het werkblad; schrijf zo dat iemand anders de proef kan herhalen. |
| ONDERZOEKSVRAAG | Wat wordt er onderzocht? (O) | Eén duidelijke, afgebakende vraagstelling. |
| HYPOTHESE | Je verwachting vóór de proef, met redenering (V). | Wordt in het besluit getoetst aan de data. |
| SCHEMA (schema en/of foto) | Proefopstelling met alle delen benoemd (V). | Correcte symbolen; foto's duidelijk en van uitleg voorzien. |
| TABEL | Meetresultaten en berekende waarden (U). | Grootheid + eenheid boven elke kolom; beduidende cijfers; berekeningen met Excel-formules (niet met de hand ingetikt). |
| BEREKENINGEN | Minstens twee uitgewerkte voorbeelden van elke soort berekening (U). | Formule → invullen met eenheden → resultaat. |
| GRAFIEK | Spreidingsgrafiek met enkel punten, assen benoemd, titel, trendlijn (U). | Geen lijngrafiek; vergelijking van de trendlijn tonen als je de rico nodig hebt. |
| BESLUIT | Antwoord op de onderzoeksvraag, koppeling met de theorie, meetfouten verklaren, hypothese bevestigd/verworpen (R). | Hier horen ook de antwoorden op de reflectievragen van het werkblad (individueel verwoord). |
| Feedbackblok + puntenverdeling | Niet verwijderen! De leerkracht gebruikt dit om te verbeteren en de punten in te vullen. | Alle cursieve instructietekst verwijder je pas als het verslag helemaal klaar is. |

### Niet elk labo = een Excel-verslag: wat dien je wanneer in?
| Labo | Wat dien je in? | Waarom? |
|---|---|---|
| 2, 4, 5, 7, 10 | Excel-verslagsjabloon (volledig verslag met tabellen, grafieken en besluit). | Meetreeksen die je grafisch verwerkt: dit is het echte onderzoeksverslag. |
| 9 | Excel-verslagsjabloon (proef 1-2) + Word/PDF met Capstone-schermafbeeldingen en uitleg (proef 3-4). | De sensormetingen zijn beelden, geen tabellen. |
| 1, 3, 6, 8 | Je ingevulde werkbladen uit deze cursus (incl. schetsen, foto's), gescand of gefotografeerd als één PDF in de uploadzone. | Doorschuif- of kortere practica met vooral waarnemingen; een Excel-verslag heeft hier weinig meerwaarde. |
| 11 | Wetenschappelijke poster (PDF) + Excel met ruwe data en grafieken. | Open onderzoek: communicatie via een poster. |
Bij elk labo staat dit ook in het evaluatiekader onderaan. Eén upload per groep, zelfde deadline voor alles.

### 1.4.2 Een groepswerk – zo pak je het aan
Het verslag is één groepswerk per labogroep: iedereen is verantwoordelijk voor het hele verslag en krijgt er hetzelfde punt voor. 'Ieder een stukje zonder naar de rest te kijken' is géén groepswerk.
- Deel het Excel-bestand meteen na het labo via OneDrive (één persoon maakt het aan vanuit het sjabloon, deelt met bewerkingsrechten): één document, geen losse versies.
- Verdeel de onderdelen (omschrijving, tabel + berekeningen, grafiek, besluit) en spreek af wie wat wanneer afwerkt; zet dat in de groepschat.
- Werk ook samen, tegelijk: op school of via videocall (Teams). Besluit en foutenanalyse maak je samen – daar wordt het meest op gelet.
- Lees elkaars delen na: eenheden, beduidende cijfers, Excel-formules, beantwoordt het besluit de onderzoeksvraag? Een fout van een ander is ook jouw fout.
- Iedereen heeft op het einde van de les alle meetresultaten (foto van het werkblad of meteen in het gedeelde bestand).
- Begin op tijd (dag van het labo of de dag erna): reken op minstens twee werkmomenten. De avond van de deadline lukt een groepswerk niet.
- Problemen in de groep? Meld ze tijdig aan de leerkracht; de procesevaluatie en (bij sommige labo's) de peer-evaluatie verrekenen individuele inzet.

> **[KADER: DEADLINE EN INDIENEN]**
> - Uiterlijk één week na het uitvoeren van het labo, 's avonds vóór de les van de volgende week (dus de avond vóór het volgende labo), om 23.59 u.
> - Als Excel-bestand (.xlsx), gemaakt in het sjabloon, in de uploadzone van Smartschool van het vak Toegepaste fysica. Eén upload per groep, met alle namen in het kopblok en in de bestandsnaam.
> - Te laat of niet in het sjabloon = aftrek volgens de afspraken van het vak/schoolreglement. Technische problemen zijn geen excuus: upload tijdig een voorlopige versie en vervang ze eventueel nog vóór de deadline.
> - Voor labo 9 (inductie) komt daar een Word/PDF met Capstone-schermafbeeldingen en uitleg bij (zie werkblad en Bijlage F); voor labo 11 een poster.


## 1.5 Evaluatie: product (verslag) en proces & attitude
Bij elk labo word je op twee manieren geëvalueerd. Samen vormen ze het practicumcijfer: 60 % voor het verslag (product) en 40 % voor proces en attitude.
|  | PRODUCTEVALUATIE – 60 % | PROCES- EN ATTITUDE-EVALUATIE – 40 % |
|---|---|---|
| Wat? | Het Excel-verslag van de groep (plus eventuele extra producten: Word/PDF met schermafbeeldingen bij labo 9, poster bij labo 11). | Wat je individueel doet tijdens het labo én hoe je het groepswerk aanpakt: voorbereiding, veilig en nauwkeurig werken, samenwerking, zelfstandigheid, orde, inzet, reflectie. |
| Wanneer? | Na het indienen van het verslag. | Tijdens elk labo (observatie door de leerkracht) en bij het nakijken van het verslag (groepswerk, stiptheid). |
| Hoe? | Puntenverdeling onderaan het Excel-sjabloon, /10: 1. Verkennen & onderzoeken (/2) – 2. Onderzoek uitvoeren (/3) – 3. Concluderen (/3) – 4. Attitude (/2). De leerkracht noteert feedback in het feedbackblok van het sjabloon (zie Bijlage B voor wat er per onderdeel verwacht wordt). | Eén rubric met 10 thema's (Bijlage C). Per thema een niveau: Uitstekend (1) – Goed (0,8) – Voldoende (0,6) – Onvoldoende (0,4) – Slecht (0,2) → score /10. |
| Punt | Groepspunt: iedereen van de groep krijgt hetzelfde cijfer. | Individueel punt. |
| Gewicht | 60 % van het practicumcijfer | 40 % van het practicumcijfer |
| Feedback | Schriftelijk in het feedbackblok van het Excel-sjabloon; één keer herwerken mogelijk voor labo 1-5. | Korte mondelinge feedback op het einde van het labo; de ingevulde rubric is te bekijken; zelfreflectiefiche (Bijlage D) om de 3 labo's. |

> **[KADER: De 10 thema's van de proces- en attituderubric (Bijlage C)]**
> - 1 Voorbereiding  •  2 Hypothese en onderzoekend denken  •  3 Opstelling bouwen en meettoestellen gebruiken  •  4 Nauwkeurig meten en noteren  •  5 Veilig werken
> - 6 Zorg voor materiaal, orde en netheid  •  7 Samenwerking en communicatie (in het labo én bij het groepsverslag)  •  8 Zelfstandigheid en probleemoplossend handelen  •  9 Inzet, doorzetting en tijdsbeheer (incl. deadline)  •  10 Reflectie en kritische houding


### Peer-evaluatie bij een beperkt aantal labo's
Bij enkele groepsopdrachten (voorzien bij labo 6, 9 en 11; de leerkracht kan dit aanpassen) beoordeel je jezelf en je groepsleden met een puntenverdeling. In een groep van drie verdeelt elke leerling 300 punten over zichzelf en de twee anderen (in een groep van twee: 200 punten). Vond je dat iedereen evenveel deed, dan geef je iedereen 100. Vind je dat je zelf minder deed, geef je bv. jezelf 90 en de anderen elk 105. Uit de punten die je van iedereen krijgt, berekent de leerkracht je peerfactor (gemiddeld ontvangen punten / 100). Het groepspunt voor het verslag wordt met jouw peerfactor vermenigvuldigd: zo wordt het groepspunt een individueel punt. Werkwijze en formulier: Bijlage D en het aparte document op Smartschool.

## 1.6 Overzicht labo's en leerplandoelen
| Labo | Titel | Fysica-LPD | STEM-LPD | Sturing |
|---|---|---|---|---|
| 1 | Elektrostatica I: elektroscoop en kleine proeven | 2 F, 3 F | 1 S, 3 S, 4 S, 5 S | gesloten → begeleid |
| 2 | Elektrostatica II: wet van Coulomb en elektrisch veld (applets) | 2 F, 3 F | 1 S, 2 S, 4 S | begeleid |
| 3 | Kleurcode en multimeter | K1 | 2 S, 3 S | gesloten |
| 4 | Schakelen van weerstanden + ontwerp | K1 | 1 S, 2 S, 3 S, 4 S | gesloten + ontwerp |
| 5 | Black boxen | K1 | 1 S, 4 S | begeleid |
| 6 | Circuitpracticum elektromagnetisme | 5 F, 6 F | 1 S, 3 S, 5 S | begeleid |
| 7 | Lorentzkracht experimenteel | 6 F | 1 S, 2 S, 4 S | begeleid → open |
| 8 | EM-krachtwerking in toepassingen + motor bouwen | 6 F | 4 S, 5 S | begeleid + ontwerp |
| 9 | Elektromagnetische inductie (sensoren) | 7 F | 1 S, 3 S, 4 S | begeleid → open |
| 10 | Transformator | 7 F (extra) | 1 S, 2 S, 5 S | open werkplan |
| 11 | Open onderzoek | naar keuze | 1 S, 6 S (#) | open |
Legende: LPD 1 S onderzoek voeren – 2 S grootheden/eenheden/beduidende cijfers – 3 S labotechnieken en veilig werken – 4 S oplossing ontwikkelen – 5 S wisselwerking met maatschappij – 6 S onderzoekscyclus (#onderzoekscompetentie). Fysica: 2 F elektrische krachtwerking (wet van Coulomb, influentie) – 3 F elektrisch veld (veldsterkte, veldlijnen) – 5 F magnetisch veld – 6 F magnetische kracht op geleider – 7 F inductie – K1 gelijkstroomkringen.


---

# BIJLAGE II – Referentie: eerste labo (gesloten → begeleid, doorschuifdelen, bouwopdracht)

# LABO 1 – ELEKTROSTATICA I: BOUW JE EIGEN ELEKTROSCOOP EN ONTDEK LADING
Naam: ……………………………………………   Klas: ………   Nr.: ……   Datum: ……/……/……
Richtduur: 2 lesuren     Type practicum: begrips- en onderzoekspracticum in delen / doorschuifsysteem (groepjes van 2-3)
Mate van sturing: GESLOTEN → BEGELEID. Delen 1-5: werkwijze gegeven; Deel 6: je ontwerpt zelf een proef.

> **[KADER: LESDOELEN – na dit labo kan je …]**
> - uitleggen hoe een voorwerp geladen wordt door wrijving en door contact, en dit duiden met de tribo-elektrische reeks;
> - een eenvoudige elektroscoop bouwen, de werking ervan verklaren en ermee aantonen of een voorwerp geladen is;
> - het verschil tussen opladen door contact en door influentie waarnemen en verklaren met het model van vrije elektronen (geleider) en dipolen (isolator);
> - het teken van een onbekende lading bepalen met een geladen elektroscoop;
> - experimenteel aantonen dat gelijknamige ladingen afstoten en ongelijknamige aantrekken;
> - het principe van elektrische schermwerking (kooi van Faraday) waarnemen en toepassingen noemen;
> - veilig, nauwkeurig en gestructureerd waarnemen en rapporteren.


> **[KADER: LEERPLANDOELEN (III-BCSW-d / III-BCW-d)]**
> - LPD 2 F: elektrische krachtwerking analyseren; elektrostatische influentie; opladen door wrijving/contact (tribo-elektrische reeks).
> - LPD 3 F: veldlijnenpatronen (radiaal, dipool, homogeen) – via demo-opstelling; kooi van Faraday.
> - LPD 1 S, 3 S: hypothese formuleren, waarnemen, veilig werken. LPD 5 S: toepassingen in de maatschappij (poedercoating, printer, luchtzuivering, explosiegevaar bij tanken).


> **[KADER: VOORKENNIS – check vóór je begint]**
> - Wat is een elektrische lading? Welke twee soorten bestaan er en wat is de eenheid?
> - Wat is het verschil tussen een geleider en een isolator op atomair niveau?
> - Wet van Coulomb (kwalitatief): hoe verandert de kracht als de afstand verdubbelt?

> *Modelantwoord (enkel leerkrachtversie): Lading is een eigenschap van deeltjes (elektron: –, proton: +) die elektrische krachtwerking veroorzaakt. Twee soorten: positief en negatief. Eenheid: coulomb (C); 1 C = 6,25·10¹⁸ elementaire ladingen.*
> *Modelantwoord (enkel leerkrachtversie): In een geleider (metaal) zijn de buitenste elektronen vrij beweeglijk (elektronengas); in een isolator zijn alle elektronen gebonden aan hun atoom/molecuul en kunnen ze enkel lokaal verschuiven (polarisatie).*
> *Modelantwoord (enkel leerkrachtversie): F ~ 1/r²: bij dubbele afstand wordt de kracht 4× kleiner; bij drievoudige afstand 9× kleiner.*

> **[LEERKRACHTENINFO]**
> - Materiaal vooraf testen bij droog weer; bij hoge luchtvochtigheid werkt het slecht – eventueel verwarming hoger zetten of een haardroger gebruiken op de wrijfstaven.
> - Elektroscoop: een metalen deksel werkt NIET (kortsluit de draad); gebruik een plastic/kartonnen deksel of isoleer de doorvoer met een stukje rietje. Blaadjes 1×4 cm van dunne huishoudfolie; zwaardere folie geeft weinig uitslag.
> - Verwachte resultaten deel 1: nadering → uitslag, verdwijnt bij wegnemen (influentie); contact → blijvende uitslag; vinger → ontlading. Deel 2: PVC-PVC afstoting, PVC-glas aantrekking; ballon/haar negatief; glas/zijde positief. Deel 3: waterstraal wordt altijd aangetrokken (dipool), ongeacht het teken. Blikje rolt naar de ballon; de plastic liniaal (isolator) wordt amper beïnvloed. Deel 4: in de kooi geen reactie; gsm in folie zonder papier wordt vaak nog bereikt (folie raakt antenne / onvolledige afscherming) – met papier ertussen en goed gesloten meestal 'niet bereikbaar'.
> - Teken onbekende lading: eerst de elektroscoop opladen door contact met PVC (negatief), dan naderen: uitslag groter = negatief, kleiner = positief. Laat dit expliciet redeneren.
> - Veldlijnen in olie: ricinusolie of slaolie + griesmeel/gras­zaad, elektroden op 5-10 kV (hoogspanningsvoeding met stroombegrenzing); enkel demo. Van de Graaff: haar rechtop lukt best met lang, droog haar op een geïsoleerd bankje.
> - Timing: 15 min bouwen, 4×12 min delen 2-4, 15 min demo, rest reflectie. Reflectievragen 5-6 als huiswerk.


> **[KADER: LEERKRACHTENINFO – didactische tips, verwachte resultaten, valkuilen]**
> - Materiaal vooraf testen bij droog weer; bij hoge luchtvochtigheid werkt het slecht – eventueel verwarming hoger zetten of een haardroger gebruiken op de wrijfstaven.
> - Elektroscoop: een metalen deksel werkt NIET (kortsluit de draad); gebruik een plastic/kartonnen deksel of isoleer de doorvoer met een stukje rietje. Blaadjes 1×4 cm van dunne huishoudfolie; zwaardere folie geeft weinig uitslag.
> - Verwachte resultaten deel 1: nadering → uitslag, verdwijnt bij wegnemen (influentie); contact → blijvende uitslag; vinger → ontlading. Deel 2: PVC-PVC afstoting, PVC-glas aantrekking; ballon/haar negatief; glas/zijde positief. Deel 3: waterstraal wordt altijd aangetrokken (dipool), ongeacht het teken. Blikje rolt naar de ballon; de plastic liniaal (isolator) wordt amper beïnvloed. Deel 4: in de kooi geen reactie; gsm in folie zonder papier wordt vaak nog bereikt (folie raakt antenne / onvolledige afscherming) – met papier ertussen en goed gesloten meestal 'niet bereikbaar'.
> - Teken onbekende lading: eerst de elektroscoop opladen door contact met PVC (negatief), dan naderen: uitslag groter = negatief, kleiner = positief. Laat dit expliciet redeneren.
> - Veldlijnen in olie: ricinusolie of slaolie + griesmeel/gras­zaad, elektroden op 5-10 kV (hoogspanningsvoeding met stroombegrenzing); enkel demo. Van de Graaff: haar rechtop lukt best met lang, droog haar op een geïsoleerd bankje.
> - Timing: 15 min bouwen, 4×12 min delen 2-4, 15 min demo, rest reflectie. Reflectievragen 5-6 als huiswerk.


## O – ORIËNTEREN

### Context
Een ballon die aan het plafond blijft kleven, een vonk als je een deurklink aanraakt, haren die rechtop staan als je een trui uittrekt: allemaal elektrostatica. Statische lading kan ook gevaarlijk zijn (vonkoverslag bij het tanken, in meelsilo's of operatiezalen) of juist nuttig (poedercoating van fietsframes, laserprinters, elektrostatische luchtfilters, sorteren van kunststoffen).
In dit labo bouw je eerst een eigen meettoestel – een elektroscoop – uit een bokaal, ijzerdraad en aluminiumfolie. Daarna gebruik je dat toestel om in verschillende delen de eigenschappen van lading te onderzoeken.

### Onderzoeksvraag
- Hoe kan ik met eenvoudig materiaal aantonen dat een voorwerp elektrisch geladen is en welk teken de lading heeft?
- Wat is het verschil tussen opladen door contact en door influentie?
- Welke materialen laden gemakkelijk op en hoe voorspel je het teken van de lading?

### Doel van het onderzoek
- Een werkende elektroscoop bouwen en de gevoeligheid ervan testen.
- Lading, krachtwerking tussen ladingen, influentie en schermwerking kwalitatief onderzoeken en verklaren met het deeltjesmodel.
- Waarnemingen gestructureerd noteren (tabel + schets van ladingsverdeling) en koppelen aan toepassingen.

### Oriëntatievragen (beantwoord vóór het labo)
1. Teken een atoom en duid aan welke deeltjes verplaatst kunnen worden bij het opladen van een voorwerp. Waarom kunnen protonen niet verplaatst worden?
> *Modelantwoord (enkel leerkrachtversie): Enkel elektronen (in de schil) kunnen verplaatst worden. Protonen zitten vast in de kern, gebonden door de sterke kernkracht; ze verplaatsen vraagt kernreacties, niet wrijving.*
2. Een PVC-buis wordt met een wollen doek gewreven. Zoek in de tribo-elektrische reeks (Bijlage E) op welk teken de buis en de doek krijgen.
> *Modelantwoord (enkel leerkrachtversie): Wol staat hoger in de reeks dan PVC → wol geeft elektronen af en wordt positief; PVC neemt elektronen op en wordt negatief.*
3. Waarom werken elektrostatica-proeven slecht op een vochtige dag?
> *Modelantwoord (enkel leerkrachtversie): Een dun waterlaagje op de oppervlakken geleidt (zeker met opgeloste ionen) en voert de lading snel af naar de omgeving/aarde. Ook de lucht geleidt beter bij hoge vochtigheid.*

### Oefenen op onderzoeksvragen (leerlijn SMART – stap 1: de vraag krijg je)
*In labo 1-3 krijg je de onderzoeksvraag. We bekijken samen waarom ze SMART is – vanaf labo 4 kies je ze zelf.*
Onderzoeksvraag: Welke voorwerpen uit onze set (PVC-buis, glazen staaf, ballon, rietje, …) worden geladen door wrijven, welk teken krijgt hun lading, en hoe gedraagt een geladen voorwerp zich tegenover een ongeladen geleider (influentie) en in een kooi van Faraday – aangetoond met een zelfgebouwde elektroscoop, tijdens dit labo?
*Doe zelf: onderstreep in de vraag de grootheid die je verandert (O), omcirkel de grootheid die je meet (A) en zet een kader rond wat constant blijft (C). Lees daarna de tabel: zo verantwoord je een onderzoeksvraag letter per letter.*
| Letter | Waarom is deze vraag SMART? |
|---|---|
| S – Specifiek | Afgebakend: een vaste set voorwerpen, drie duidelijke deelvragen (geladen of niet? welk teken? wat doet een geladen voorwerp met een geleider en met een kooi?) en één meettoestel: je eigen elektroscoop. Niet 'hoe werkt statische elektriciteit?'. |
| M – Meetbaar | Waarneembaar: de uitslag van de blaadjes (ja/nee en groter/kleiner), het teken via een vooraf geladen elektroscoop, het blikje dat rolt, de gsm die wel/niet rinkelt. Elke waarneming komt in een tabel. |
| A – Aanvaardbaar | Zinvol en veilig: dit zijn de basisverschijnselen van het hele hoofdstuk elektrostatica; de spanningen zijn hoog maar de ladingen piepklein, dus ongevaarlijk. |
| R – Realistisch | Haalbaar: alle materiaal is eenvoudig, de elektroscoop bouw je in 15 minuten en de delen 2-4 zijn kort. |
| T – Tijdsgebonden | In de tijd: alles tijdens dit labo (2 lesuren), werkblad meteen ingevuld en als PDF ingediend. |
> *Modelantwoord (enkel leerkrachtversie): O = de voorwerpen/handelingen (wrijven, naderen, aanraken, in de kooi); A = uitslag en teken via de elektroscoop, gedrag van blikje/gsm; C = dezelfde elektroscoop, dezelfde doeken. Bespreek klassikaal dat een kwalitatieve, afgebakende vraag ook SMART is, en dat 'Hoe werkt statische elektriciteit?' dat niet is (niet S, niet M).*

## V – VOORBEREIDEN

### Benodigdheden
- Per groep: glazen bokaal met deksel (plastic of metalen deksel met gaatje, of karton), ca. 15 cm stevige ijzer- of koperdraad, aluminiumfolie, schaar, plakband, priem/nagel om een gaatje te maken.
- Wrijfmaterialen: PVC-buis (grijs), plexiglas- of glazen staaf, ballonnen, wollen doek, zijden/katoenen doek, papieren handdoek, rietjes (plastic).
- Klein materiaal: papiersnippers, peper en zout, leeg aluminium drankblikje, horlogeglas of draad om een staaf vrij op te hangen, piepschuimbolletje aan nylondraad (pendel), kraan met dunne waterstraal.
- Kooi van Faraday: metaalgaas of extra aluminiumfolie, een gsm.
- Demo-opstelling leerkracht (deel 5) (optioneel): Van de Graaff-generator, hoogspanningsvoeding met elektroden in petrischaal met olie en griesmeel (veldlijnen), neonlampje.

### Theorie-overzicht
Lading en behoud van lading. Bij wrijving gaan elektronen van het ene materiaal naar het andere: het ene wordt negatief (elektronenoverschot), het andere even sterk positief (tekort). Lading wordt niet gemaakt, enkel verplaatst. Eenheid: coulomb (C); elementaire lading e = 1,6·10⁻¹⁹ C.
Tribo-elektrische reeks. Een lijst van materialen: het materiaal dat hoger staat (bv. glas, haar, wol) geeft elektronen af en wordt positief; het lagere (bv. PVC, teflon) neemt op en wordt negatief.
Krachtwerking. Gelijknamige ladingen stoten elkaar af, ongelijknamige trekken elkaar aan. De kracht neemt sterk af met de afstand (wet van Coulomb):
$$ F = k \cdot \frac{|Q_1| \cdot |Q_2|}{r^2} \quad \text{met } k = 8,99 \cdot 10^9 \ \text{N·m²/C²} $$
Elektroscoop. Een geleider (draad + bolletje) met twee lichte, beweeglijke blaadjes. Breng je lading op het bolletje, dan verdeelt die zich over de hele geleider; de blaadjes krijgen gelijke lading en wijken uit. Hoe groter de lading, hoe groter de uitslag.
Influentie (in de theoriecursus 'elektrostatische inductie' genoemd). Een geladen voorwerp in de buurt van een geleider verplaatst de vrije elektronen erin: aan de ene kant ontstaat een overschot, aan de andere een tekort, zonder contact. In een isolator verschuiven de ladingen enkel binnen elk molecuul (polarisatie, dipolen). Daardoor trekt een geladen voorwerp ook ongeladen voorwerpen aan.
Schermwerking. In een geladen geleider zit alle lading aan de buitenkant; binnenin is het elektrisch veld nul (kooi van Faraday).

> **[KADER: VEILIGHEID // NAUWKEURIGHEID]**
> - Statische ontladingen van wrijfproeven zijn ongevaarlijk, maar houd elektronica (gsm, laptop) uit de buurt behalve bij de Faraday-proef.
> - Van de Graaff en hoogspanningsvoeding: enkel de leerkracht bedient ze. Personen met een pacemaker houden afstand.
> - Voorzichtig met schaar, priem en de uiteinden van de ijzerdraad (ogen!). Glazen bokaal: niet laten vallen.
> - Werk met droge handen en droog materiaal; wrijf stevig maar kort.


### Hypothese
*Formuleer een beredeneerde verwachting (wat verwacht je en waarom?):*

### Werkplan
- Verdeel de rollen: bouwer, waarnemer/notulist, 'wrijver'. Wissel per deel.
- Bouw eerst de elektroscoop (deel 1) en test hem. Doorloop daarna delen 2-5 in willekeurige volgorde (max. 15 min per deel).
- Noteer bij elk deel: hypothese → waarneming → schets van de ladingsverdeling → verklaring.

## U – UITVOEREN

### Deel 1 – Bouw en test je elektroscoop (verplicht eerst)
[FIGUUR: gen_elektroscoop.jpg]
[FIGUUR: es/p3_0.jpg]
[FIGUUR: es/p3_1.jpg]
*Links: zelfgebouwde elektroscoop uit een bokaal, koperdraad en aluminiumfolie.*
1. Maak een gaatje in het deksel. Plooi het uiteinde van de draad tot een haakje (L- of J-vorm) en steek de draad door het deksel, zodat het haakje ca. 3 cm boven de bodem van de bokaal hangt. Fixeer met plakband; de draad mag het glas niet raken.
2. Knip twee strookjes aluminiumfolie (ca. 1 cm × 4 cm) en hang ze over het haakje zodat ze vrij naast elkaar hangen. Druk ze niet plat tegen elkaar.
3. Frommel een bolletje aluminiumfolie (Ø 2-3 cm) rond het bovenste uiteinde van de draad. Draai het deksel op de bokaal.
4. Test: wrijf een PVC-buis met wol en nader het bolletje langzaam zonder te raken. Wat doen de blaadjes? Haal de buis weg. Wat gebeurt er?
5. Raak nu het bolletje aan met de gewreven buis en haal de buis weg. Wat gebeurt er nu? Raak daarna het bolletje aan met je vinger.
6. Verbeter de gevoeligheid (dunnere strookjes, langer, lichter) en noteer wat de uitslag beïnvloedt.
| Handeling | Waarneming blaadjes (schets of beschrijving) | Blijft de uitslag na wegnemen? | Verklaring (ladingsverdeling) |
|---|---|---|---|
| Geladen buis nadert (geen contact) |  |  |  |
| Geladen buis raakt bolletje |  |  |  |
| Vinger raakt bolletje |  |  |  |
| Ballon gewreven aan haar nadert |  |  |  |
*Schets je elektroscoop met de ladingsverdeling (teken + en –) in de drie situaties:*

### Deel 2 – Tribo-elektrische reeks en krachtwerking
1. Hang een gewreven PVC-buis vrij op (draadlus of op een horlogeglas). Nader met een tweede gewreven PVC-buis. Nader daarna met een gewreven glazen/plexiglas staaf.
2. Wrijf twee ballonnen aan je haar en hang ze naast elkaar aan draadjes. Houd daarna je hand ertussen.
3. Laad verschillende materialen op (PVC/wol, glas/zijde, rietje/papier, ballon/haar) en test ze telkens tegen de opgehangen, bekende negatief geladen PVC-buis: aantrekking of afstoting? Leid het teken af en controleer met de tribo-elektrische reeks.
| Materiaal gewreven met … | Hypothese teken (reeks) | Waarneming t.o.v. PVC⁻ | Besluit teken | Klopt? |
|---|---|---|---|---|
| PVC – wol |  |  |  |  |
| Glas – zijde |  |  |  |  |
| Ballon – haar |  |  |  |  |
| Rietje – papier |  |  |  |  |
| … – … |  |  |  |  |

### Deel 3 – Influentie: geladen voorwerpen trekken ongeladen voorwerpen aan
[FIGUUR: es/p8_0.jpg] – *Elektrostatische influentie bij een elektroscoop (cursus D1, fig. 1.9): a) geladen staaf nadert, b) en c) ladingsverdeling.*
[FIGUUR: es/p8_0.jpg]
*Elektrostatische influentie bij een elektroscoop (cursus D1, fig. 1.9): a) geladen staaf nadert, b) en c) ladingsverdeling.*
1. Strooi papiersnippers en een mengsel van peper en zout op tafel. Houd een gewreven buis erboven op verschillende afstanden. Wat wordt eerst aangetrokken? Waarom springen sommige snippers na contact weer weg?
2. Leg een leeg aluminium blikje op zijn zij en nader het met een gewreven ballon. Kan je het blikje laten rollen zonder het aan te raken? Kan het ook met een geladen isolator (plastic liniaal) in plaats van het blikje? Verklaar het verschil geleider/isolator.
3. Open de kraan tot een dunne, gladde waterstraal. Nader met een gewreven PVC-buis en daarna met een gewreven glasstaaf. Wordt de straal aangetrokken of afgestoten? Hangt dat af van het teken van de lading?
4. Bepaal het teken van een onbekende lading: laad je elektroscoop op met de PVC-buis (contact, dus negatief). Nader nu met een onbekend geladen voorwerp. Uitslag groter → zelfde teken; kleiner → tegengesteld teken. Leg uit waarom dat zo is.
| Proef | Hypothese | Waarneming | Verklaring met schets ladingsverdeling |
|---|---|---|---|
| Snippers / peper en zout |  |  |  |
| Rollend blikje (geleider) |  |  |  |
| Plastic liniaal i.p.v. blikje (isolator) |  |  |  |
| Waterstraal met PVC⁻ / glas⁺ |  |  |  |
| Teken van onbekende lading: voorwerp = … |  |  |  |

### Deel 4 – Kooi van Faraday (schermwerking)
1. Zet een opgeladen elektroscoop in een omhulsel van metaalgaas of wikkel de bokaal (niet het bolletje) in aluminiumfolie die je met de aarde (kraan/radiator) verbindt. Nader met een sterk geladen buis. Reageert de elektroscoop nog? Vergelijk met en zonder omhulsel.
2. Wikkel een gsm volledig in aluminiumfolie en bel ernaar. Herhaal met een laagje papier ertussen (zodat de folie de gsm niet raakt). Wat stel je vast? Wat heeft dit te maken met elektrische velden?
*Noem drie toepassingen van elektrische schermwerking (zie leerplan: auto bij blikseminslag, microgolfoven, coaxkabel, ...) en leg bij één ervan uit hoe het werkt:*

### Deel 5 – DEMO door de leerkracht: elektrisch veld zichtbaar maken en Van de Graaff
[FIGUUR: es/p42_0.jpg] – *Lichte draadjes op de kap van een bandgenerator worden afgestoten (cursus D3, fig. 1.22).*
[FIGUUR: es/p42_0.jpg]
*Lichte draadjes op de kap van een bandgenerator worden afgestoten (cursus D3, fig. 1.22).*
[FIGUUR: gen_vandegraaff.jpg] – *Van de Graaff-generator: de haren krijgen dezelfde lading en stoten elkaar af.*
[FIGUUR: gen_vandegraaff.jpg]
*Van de Graaff-generator: de haren krijgen dezelfde lading en stoten elkaar af.*
Kijk aandachtig en schets wat je ziet. Veldlijnenpatronen met griesmeel in olie: (a) één puntelektrode (radiaal veld), (b) twee puntelektroden met tegengestelde lading (dipool), (c) twee evenwijdige plaatelektroden (homogeen veld). Van de Graaff: haren rechtop, 'vliegende' aluminiumschaaltjes, neonlampje dat oplicht op afstand.
| Opstelling | Schets veldlijnenpatroon | Waar is het veld het sterkst? Hoe zie je dat? |
|---|---|---|
| (a) puntlading – radiaal |  |  |
| (b) twee tegengestelde ladingen – dipool |  |  |
| (c) twee platen – homogeen |  |  |

### Deel 6 – Ontwerp je eigen proef

> **[KADER: STEM-ONTWERPOPDRACHT (LPD 4 S) – één bewering, één proef]**
> - Kies één bewering en ontwerp zelf een proef om ze te testen met het materiaal op tafel: (A) 'De uitslag van de elektroscoop hangt af van het aantal wrijfbewegingen.' (B) 'Een geladen voorwerp verliest zijn lading sneller in vochtige lucht (adem erop).' (C) 'Langere/dunnere blaadjes maken de elektroscoop gevoeliger.' (D) eigen bewering (laat goedkeuren).
> - Randvoorwaarden: 10 minuten, één variabele tegelijk, minstens 3 herhalingen, waarnemingen in een eigen tabel.
> - Noteer: onderzoeksvraag – wat varieer je / wat houd je constant – werkwijze (3-5 stappen) – resultaat – besluit.


## R – REFLECTEREN

### Besluit
*Antwoord op de onderzoeksvraag, onderbouwd met je metingen. Klopt je hypothese?*

### Foutenanalyse en betrouwbaarheid
*Grootste meetonzekerheid? Hoe verbeter je de proef?*

### Reflectievragen
1. Verklaar met het deeltjesmodel waarom de blaadjes van de elektroscoop al uitwijken als de geladen buis het bolletje nog niet raakt, en waarom ze terugvallen als je de buis wegneemt.
> *Modelantwoord (enkel leerkrachtversie): Influentie: de negatieve buis stoot de vrije elektronen van de geleider (bolletje+draad+blaadjes) weg naar de blaadjes. De blaadjes worden beide negatief en stoten elkaar af; het bolletje wordt positief. Haal je de buis weg, dan herverdelen de elektronen zich gelijkmatig: de geleider is netto nog ongeladen → blaadjes vallen terug. Pas bij contact gaat er netto lading over en blijft de uitslag.*
2. Een leerling beweert: 'Door te wrijven maak je lading.' Weerleg of bevestig dit met één van je proeven.
> *Modelantwoord (enkel leerkrachtversie): Fout: lading wordt niet gemaakt maar verplaatst (behoud van lading). Bewijs: in deel 2 wordt de wollen doek positief terwijl de buis negatief wordt – de doek trekt de negatieve PVC-buis aan. Beide ladingen zijn even groot en tegengesteld.*
3. Waarom trekt een geladen buis zowel een negatief geladen als een ongeladen papiersnipper aan? Kan afstoting voorkomen bij een ongeladen voorwerp?
> *Modelantwoord (enkel leerkrachtversie): Een ongeladen snipper wordt gepolariseerd (influentie): de kant dichtst bij de buis krijgt tegengestelde lading en de aantrekking op die kant is groter dan de afstoting op de verdere kant (F ~ 1/r²) → netto aantrekking. Een ongeladen voorwerp kan nooit afgestoten worden; pas nadat het bij contact lading overneemt (zelfde teken) springt het weg.*
4. Waarom moet een tankwagen geaard worden vóór het lossen van brandstof? Koppel aan wat je in deel 2/3 zag.
> *Modelantwoord (enkel leerkrachtversie): Stromende brandstof wrijft langs de leiding en laadt op (tribo-elektrisch, zoals in deel 2). De lading hoopt zich op de geïsoleerde wagen op tot een vonk overslaat (influentie op nabije geleiders, deel 3) – met explosiegevaar door brandstofdampen. Aarding voert de lading continu af.*
5. Leg uit hoe poedercoating of een laserprinter gebruikmaakt van elektrostatische krachten. [Internet toegelaten: gewone zoekmachine zoals Google, bron vermelden – geen AI-tool.]
> *Modelantwoord (enkel leerkrachtversie): Poedercoating: het poeder wordt in het spuitpistool negatief geladen, het geaarde werkstuk is positief → poeder wordt aangetrokken en blijft gelijkmatig kleven (ook achterkant door veldlijnen), daarna gebakken. Laserprinter: de laser ontlaadt een geladen trommel op de plaatsen van de tekst; toner (geladen) kleeft enkel op die plaatsen en wordt op papier overgebracht en gefixeerd.*
6. Je wil je elektroscoop omvormen tot een toestel dat de grootte van de lading schat (kwantitatief). Wat zou je toevoegen of veranderen? (ontwerpvraag, LPD 4 S)
> *Modelantwoord (enkel leerkrachtversie): Schaalverdeling (gradenboog) achter de blaadjes, één vast blad en één beweeglijk blad (of een lichte naald op een as), reproduceerbare lading (bv. vast aantal wrijfbewegingen), ijken met een gekende lading (bv. via een condensator en een bekende spanning). Elektronisch: een veldmeter/elektrometer.*

> **[KADER: WAT, HOE EN WANNEER WORDT GEËVALUEERD IN DIT LABO?]**
> - PRODUCT (60 %) – wat: werkende elektroscoop met schets, volledig ingevulde waarnemingstabellen met verklaringen (ladingsschetsen), antwoorden op reflectievragen, maatschappelijke link.
> - PRODUCT – hoe en wanneer: puntenverdeling /10 (Bijlage B), groepspunt, feedback in het feedbackblok; deadline = één week na het labo, 23.59 u, Smartschool-uploadzone.
> - PRODUCT – wat dien je in: ingevulde werkbladen (foto's/scan van dit labo, incl. schetsen) als één PDF in de uploadzone – GEEN Excel-verslag (doorschuifpracticum).
> - PROCES & ATTITUDE (40 %) – wat: zorgvuldige bouw, systematisch waarnemen (hypothese vóór de proef!), rolverdeling en samenwerking, veilig omgaan met scherp materiaal en demo-opstelling, opruimen.
> - PROCES & ATTITUDE – hoe: observatie door de leerkracht met de rubric van Bijlage C (10 thema's × 5 niveaus), individueel punt.
> - PEER-EVALUATIE: niet voorzien bij dit labo (tenzij de leerkracht dit aankondigt).



---

# BIJLAGE III – Referentie: begeleid meetlabo met eigen meetplan (labo 7)

# LABO 7 – EXPERIMENTELE BEPALING VAN DE LORENTZKRACHT
Naam: ……………………………………………   Klas: ………   Nr.: ……   Datum: ……/……/……
Richtduur: 2 lesuren     Type practicum: onderzoekspracticum (per 2-3)
Mate van sturing: BEGELEID → OPEN: onderzoeksvraag gegeven, meetplan (bereik, stappen, herhalingen) stel je zelf op.

> **[KADER: LESDOELEN – na dit labo kan je …]**
> - de grootte van de magnetische kracht op een stroomvoerende geleider meten via een massaverschil op een balans (F = Δm·g);
> - het verband tussen F en de stroomsterkte I en tussen F en de lengte l van de geleider experimenteel bepalen en grafisch voorstellen;
> - uit de grafieken afleiden dat F ~ I en F ~ l bij dezelfde magneet (B constant), de formule F = B·I·l formuleren en de magnetische veldsterkte B van onze magneet bepalen uit de richtingscoëfficiënt;
> - de derde wet van Newton (actie en reactie – zie uitleg) gebruiken om te verklaren waarom de balans een massaverschil aangeeft.


> **[KADER: LEERPLANDOELEN (III-BCSW-d / III-BCW-d)]**
> - LPD 6 F: magnetische kracht op een stroomvoerende rechte geleider kwantificeren (F = B·I·l·sin α).
> - LPD 1 S: verbanden onderzoeken, hypothese toetsen. LPD 2 S: eenheden (tesla, N, g→kg). LPD 4 S: modelleren.


> **[KADER: VOORKENNIS – check vóór je begint]**
> - Zwaartekracht F = m·g met g = 9,81 m/s².
> - Richting van de Lorentzkracht (labo 6, deel 5).
> - Recht evenredig verband herkennen in een grafiek.


> **[LEERKRACHTENINFO]**
> - Stel de blauwe bron vooraf in stroombegrenzing (max. 5 A) en laat de leerlingen enkel de stroomknop bedienen.
> - Verwachte resultaten: Δm van ca. 0,05-0,5 g; F(I) rechte door de oorsprong; F(l) rechte met klein positief snijpunt (randeffect). B ≈ 0,05-0,2 T afhankelijk van het magneetjuk; beide methodes binnen ~10 %.
> - Veelgemaakte fout: Δm in gram laten staan → F een factor 1000 fout; balans niet tarreren met stroom uit.


> **[KADER: LEERKRACHTENINFO – didactische tips, verwachte resultaten, valkuilen]**
> - Stel de blauwe bron vooraf in stroombegrenzing (max. 5 A) en laat de leerlingen enkel de stroomknop bedienen.
> - Verwachte resultaten: Δm van ca. 0,05-0,5 g; F(I) rechte door de oorsprong; F(l) rechte met klein positief snijpunt (randeffect). B ≈ 0,05-0,2 T afhankelijk van het magneetjuk; beide methodes binnen ~10 %.
> - Veelgemaakte fout: Δm in gram laten staan → F een factor 1000 fout; balans niet tarreren met stroom uit.


## O – ORIËNTEREN

### Context
In labo 6 zag je dat een stroomvoerende geleider in een magnetisch veld een kracht ondervindt. Nu meten we hoe groot die kracht is. De magneet oefent een kracht uit op de geleider, maar de geleider oefent dan ook een even grote, tegengestelde kracht uit op de magneet (derde wet van Newton, zie kader). Zetten we de magneet op een elektronische balans, dan lezen we een massaverschil af waaruit we de kracht berekenen. Deze kracht doet elke elektromotor draaien. We beschikken over één magneet: de magnetische veldsterkte (fluxdichtheid) B blijft in dit hele labo dezelfde en kunnen we dus niet variëren – wel bepalen.

### Onderzoeksvraag (leerlijn SMART – stap 2: jij kiest)
*Je krijgt de onderzoeksvraag van dit labo niet meer kant-en-klaar. Hieronder staan vier voorstellen; slechts één is een goede SMART-onderzoeksvraag voor dit labo. Omcirkel ze – dat wordt jullie onderzoeksvraag.*
- A. Hoe hangt de Lorentzkracht af van de magnetische inductie B van de magneet?
- B. Hoe hangt de kracht af van de lengte van de geleider?
- C. Waarom draait een elektromotor?
- D. Hoe hangt de Lorentzkracht op een geleider (bepaald uit Δm op de balans) af van de stroomsterkte (0 tot 4 A, bij vaste lengte) en van de horizontale lengte van de geleider (1,2 tot 8,4 cm, bij I = 3,0 A), telkens bij dezelfde magneet, tijdens dit labo?
*Verantwoord per letter waarom jouw keuze SMART is, en schrijf bij elk ander voorstel in één zin welke letter ontbreekt (of waarom het niet over het juiste onderwerp gaat).*
| Mijn keuze | S | M | A | R | T |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
> *Modelantwoord (enkel leerkrachtversie): D. A: niet realistisch – we hebben één magneet, B kunnen we niet variëren. B: lijkt goed, maar welke kracht, hoe gemeten, wat blijft constant? (niet S/M). C: geen verband tussen grootheden. Verantwoording D: S = F vs. I (bij vaste l) en F vs. l (bij vaste I), telkens B constant – twee deelonderzoeken, elk met één variabele; M = Δm op de balans → F = Δm·g; A = basis van de elektromotor; R = de zes geleiders en balans zijn aanwezig; T = deel 2 van labo 7 + verslag binnen een week.*

### Doel van het onderzoek
- Twee verbanden experimenteel bepalen (F(I) bij vaste l en F(l) bij vaste I, telkens met dezelfde magneet) en grafisch verwerken.
- De formule F = B·I·l afleiden en B van onze magneet bepalen.
- Kritisch reflecteren over de meetmethode.

### Oriëntatievragen (beantwoord vóór het labo)
1. Teken de opstelling: magneet op balans, geleider horizontaal tussen de polen. Teken B, I en de kracht op de geleider. Welke kracht werkt op de magneet (derde wet van Newton, zie kader) en wat doet dat met de aflezing van de balans?
> *Modelantwoord (enkel leerkrachtversie): Kracht op geleider F = I·l × B (linkerhandregel). Volgens de derde wet van Newton werkt op de magneet een even grote, tegengestelde kracht: wordt de geleider omhoog geduwd, dan wordt de magneet omlaag geduwd → balans leest meer af (en omgekeerd).*
2. Welke grootheid moet je constant houden bij het onderzoek van F(I)? En bij F(l)?
> *Modelantwoord (enkel leerkrachtversie): Bij F(I): de lengte l (zelfde geleider), de positie in het veld en B. Bij F(l): de stroomsterkte I, de positie en B.*

## V – VOORBEREIDEN

### Benodigdheden
- Blauwe stroombron (max. 5 A), 2 blauwe kabels, 1 rode kabel, multimeter (A), statief, elektronische balans (0,01 g), magneetjuk met neodymiummagneten, set geleiders met verschillende horizontale lengtes (bv. 1,2 – 2,2 – 3,2 – 4,2 – 6,4 – 8,4 cm), bevestigingsstuk.

### Theorie-overzicht
Kracht uit massaverschil. Als men door een geleider met lengte l in een magnetisch veld een stroom stuurt, ontstaat een aantrekkings- of afstotingskracht tussen magneet en geleider. Die kracht geeft een massaverschil Δm op de elektronische balans. Bij aantrekking leest de balans een kleinere massa af, bij afstoting een grotere (bij de opstelling die in het handboek besproken wordt is dit net omgekeerd!). De grootte van de Lorentzkracht volgt uit:
$$ F_L = \Delta m \cdot g \qquad \text{met } \Delta m = |m_{met\ stroom} - m_{zonder\ stroom}| \ \text{in kg en } g = 9,81\ \text{m/s}^2 $$
Verwachte wet. Voor een geleider loodrecht op het veld verwachten we F ~ I en F ~ l:
$$ F_L = B \cdot I \cdot l \cdot \sin\alpha \qquad [B] = \text{T} = \frac{\text{N}}{\text{A} \cdot \text{m}} $$
Grafisch. De richtingscoëfficiënt van F(I) bij vaste l is B·l; die van F(l) bij vaste I is B·I. B is de magnetische veldsterkte (ook fluxdichtheid genoemd, eenheid tesla) van onze magneet: dezelfde in beide delen.
Derde wet van Newton (actie en reactie). Krachten komen altijd in paren voor: als voorwerp A een kracht uitoefent op voorwerp B, dan oefent B tegelijk een even grote kracht in tegengestelde zin uit op A. Hier: de magneet duwt (of trekt) aan de geleider met F_L; de geleider duwt (of trekt) dus even hard aan de magneet. Omdat de magneet op de balans staat, 'weegt' hij daardoor iets meer of minder: dat verschil is Δm. (De wetten van Newton zie je volledig in het zesde jaar.)

> **[KADER: VEILIGHEID // NAUWKEURIGHEID]**
> - In dit labo mag de stroomsterkte NOOIT groter zijn dan 5 A (grens van de geleiders en de blauwe bron). Schakel de stroom enkel in tijdens het aflezen (geleider wordt warm).
> - Balans tarreren (= op nul zetten met de knop 'TARE'/'0') met de magneet erop en de stroom uit; zo lees je rechtstreeks Δm af. Niet op de tafel leunen tijdens de meting (trillingen).
> - Neodymiummagneten: knelgevaar en weg van elektronica en bankkaarten. Geleider mag de magneet niet raken.


### Hypothese
*Formuleer een beredeneerde verwachting (wat verwacht je en waarom?):*

### Werkplan
- Jullie stellen het meetplan zelf op (zie kader). Verwerking: tabellen → F berekenen → twee grafieken met trendlijn door de oorsprong → B bepalen.

> **[KADER: STEM-ONTWERPOPDRACHT (LPD 4 S) – stel zelf het meetplan op]**
> - Deel 1 – F(I): welke geleider kies je en waarom? Welk bereik van I (max. 5 A!) en welke stapgrootte? Hoeveel meetpunten heb je minstens nodig voor een betrouwbare rechte? Herhaal je metingen?
> - Deel 2 – F(l): welke vaste I kies je (groot genoeg voor een meetbare Δm, veilig)? Welke lengtes?
> - Noteer je plan hieronder en laat het goedkeuren. Vul daarna de tabellen in met jóuw gekozen waarden.


## U – UITVOEREN
[FIGUUR: gen_lorentz_balans.jpg] – *Opstelling (stroombalans): het magneetjuk staat op de balans, de geleider hangt horizontaal tussen de polen en wordt gevoed door de stroombron (ampèremeter op de bron aflezen). De balans meet de reactiekracht op de magneet; druk eerst TARE.*
[FIGUUR: gen_lorentz_balans.jpg]
*Opstelling (stroombalans): het magneetjuk staat op de balans, de geleider hangt horizontaal tussen de polen en wordt gevoed door de stroombron (ampèremeter op de bron aflezen). De balans meet de reactiekracht op de magneet; druk eerst TARE.*

### Tabel 1 – Verband tussen stroomsterkte en Lorentzkracht (l = …… m, m₀ = …… g)
| I (A) | m (g) | Δm (kg) | F_L = Δm·g (N) |
|---|---|---|---|

### Tabel 2 – Verband tussen lengte van de geleider en Lorentzkracht (I = …… A)
| l (m) | m (g) | Δm (kg) | F_L (N) |
|---|---|---|---|

### Grafische STEM-opdracht
Grafiek 1: F_L (y) in functie van I (x). Grafiek 2: F_L (y) in functie van l (x). Trendlijn door de oorsprong, vergelijking noteren.
Rico grafiek 1 = …………… N/A = B·l  →  B = …………… T          Rico grafiek 2 = …………… N/m = B·I  →  B = …………… T          Gemiddelde B = …………… T

## R – REFLECTEREN

### Besluit
*Antwoord op de onderzoeksvraag, onderbouwd met je metingen. Klopt je hypothese?*

### Foutenanalyse en betrouwbaarheid
*Grootste meetonzekerheid? Hoe verbeter je de proef?*

### Reflectievragen
1. Leid uit beide verbanden een formule af voor de Lorentzkracht op een stroomvoerende geleider. Eén factor hebben we niet onderzocht (de hoek tussen I en B): hoe zit die in de volledige formule en hoe zou je die experimenteel onderzoeken?
> *Modelantwoord (enkel leerkrachtversie): F ~ I en F ~ l → F = B·I·l, met B de evenredigheidsconstante (magnetische veldsterkte, T). Volledige formule: F = B·I·l·sin α, met α de hoek tussen I en B; onderzoek door de geleider te draaien t.o.v. het veld (hoekverdeelschijf) en F(α) uit te zetten tegen sin α.*
2. Komen de twee waarden van B overeen? Welke meting (Δm, I of l) draagt het meest bij tot de onzekerheid? Hoe nauwkeurig is 'l' eigenlijk gedefinieerd (randeffecten van het veld)?
> *Modelantwoord (enkel leerkrachtversie): Typisch B ≈ 0,05-0,2 T (magneetjuk). Grootste onzekerheid: Δm (0,01 g op enkele 0,1 g) en vooral l: het veld van het magneetjuk is niet scherp begrensd (randeffecten), zodat de 'effectieve lengte' groter is dan de nominale lengte van de geleider → F(l)-rechte gaat niet exact door de oorsprong.*
3. Waarom moest je de stroom enkel kort inschakelen? Welk effect heeft opwarming op je meting (denk aan de temperatuurafhankelijkheid van de weerstand van een metaal)?
> *Modelantwoord (enkel leerkrachtversie): Bij 4-5 A warmt de geleider (en de bron) op: luchtstromingen beïnvloeden de balans, de weerstand stijgt (labo 6) waardoor de ingestelde stroom verandert, en de magneet kan opwarmen (neodymium verliest sterkte bij T > 80 °C).*
4. Een elektromotor bevat een spoel met 200 windingen van 5 cm lengte in een veld van 0,2 T bij 2 A. Bereken de kracht op één zijde van de spoel.
> *Modelantwoord (enkel leerkrachtversie): F = N·B·I·l = 200 · 0,2 T · 2 A · 0,05 m = 4 N.*
5. Verklaar met de derde wet van Newton (kader bij de theorie) waarom de kracht op de geleider meetbaar is via de balans waarop de magneet staat.
6. Waarom konden we de invloed van B niet onderzoeken? Hoe zou je dat wél kunnen doen (materiaal, werkwijze)?
> *Modelantwoord (enkel leerkrachtversie): We hebben één magneet, dus B is constant. Onderzoeken van F(B) vereist verschillende magneten of een elektromagneet met regelbare stroom (B ~ I_spoel) of een teslameter om B te meten en te variëren met de afstand tussen de polen.*

> **[KADER: WAT, HOE EN WANNEER WORDT GEËVALUEERD IN DIT LABO?]**
> - PRODUCT (60 %) – wat: twee complete tabellen met correcte eenheden (g→kg!), twee grafieken met trendlijn, afleiding van F = B·I·l, bepaling van B met vergelijking van beide methodes, foutenanalyse, reflectie.
> - PRODUCT – hoe en wanneer: puntenverdeling /10 (Bijlage B), groepspunt, feedback in het feedbackblok; deadline = één week na het labo, 23.59 u, Smartschool-uploadzone.
> - PRODUCT – wat dien je in: Excel-verslagsjabloon (twee tabellen, twee grafieken, bepaling van B).
> - PROCES & ATTITUDE (40 %) – wat: I ≤ 5 A gerespecteerd en stroom kort ingeschakeld, balans correct getarreerd, geduldig en nauwkeurig afgelezen, samenwerking.
> - PROCES & ATTITUDE – hoe: observatie door de leerkracht met de rubric van Bijlage C (10 thema's × 5 niveaus), individueel punt.
> - PEER-EVALUATIE: niet voorzien bij dit labo (tenzij de leerkracht dit aankondigt).



---

# BIJLAGE IV – Referentie: Bijlagen A-E (sjabloon-checklist, puntenverdeling, rubric, zelfreflectie/peer, naslag)

# Bijlage A – Het Excel-verslagsjabloon: opbouw en checklist
Het sjabloon 'nummer labo TF titel (namen) 5BCW.xlsx' staat op Smartschool, samen met de screencast. Gebruik deze checklist vóór je uploadt.

| Onderdeel (Excel) | Checklist | ✔ |
|---|---|---|
| Kopblok | Groepsleden, klas, datum uitvoering, nummer + titel proef ingevuld; bestandsnaam = 'nummer labo TF titel (namen) 5BCW'. | ☐ |
| Omschrijving | Doorlopende tekst in eigen woorden: doel – benodigdheden – werkwijze (herhaalbaar). | ☐ |
| Onderzoeksvraag | Eén duidelijke vraag, overgenomen/aangescherpt uit het werkblad. | ☐ |
| Hypothese | Verwachting + redenering, vóór de proef geformuleerd. | ☐ |
| Schema / foto | Opstelling met alle delen benoemd; correcte symbolen voor bron, meters, weerstanden, spoelen. | ☐ |
| Tabel | Grootheid + eenheid per kolom; beduidende cijfers; berekende kolommen via Excel-formules. | ☐ |
| Berekeningen | Minstens twee uitgewerkte voorbeelden per soort berekening, met eenheden. | ☐ |
| Grafiek | Spreidingsgrafiek met enkel punten; assen benoemd met eenheid; titel; trendlijn (+ vergelijking indien rico nodig). | ☐ |
| Besluit | Antwoord op de onderzoeksvraag; koppeling met theorie/formule; hypothese besproken; meetfouten verklaard; reflectievragen van het werkblad beantwoord. | ☐ |
| Feedbackblok & puntenverdeling | NIET verwijderd. Cursieve instructietekst wél verwijderd. | ☐ |
| Groepswerk | Gedeeld via OneDrive, door iedereen nagelezen, iedereen kent de inhoud van het hele verslag. | ☐ |
| Indienen | Als .xlsx in de uploadzone Smartschool, uiterlijk de avond vóór de les van volgende week. | ☐ |


# Bijlage B – Productevaluatie: het verslag (60 %)
Het verslag wordt niet met een rubric beoordeeld, maar volgens de puntenverdeling die onderaan het Excel-sjabloon staat. Hieronder staat per onderdeel wat er verwacht wordt en welke feedbackcodes uit het sjabloon erbij horen.

| Onderdeel (Excel-sjabloon) | Max. | Wat wordt verwacht? | Feedbackcodes in het sjabloon |
|---|---|---|---|
| 1. Verkennen & onderzoeken (omschrijving, onderzoeksvraag, hypothese, schema) | 2 | Doel, benodigdheden en werkwijze in eigen woorden en herhaalbaar; onderzoeksvraag duidelijk en volledig; beredeneerde hypothese; schema/foto met alle delen benoemd. | Werkwijze niet volledig/onduidelijk • benodigdheden/doel vermelden • onderzoeksvraag onduidelijk/niet volledig • hypothese onduidelijk/niet volledig • delen aanduiden en benoemen • foto of schema ontbreekt |
| 2. Onderzoek uitvoeren (tabel, berekeningen, grafiek) | 3 | Volledige tabel met grootheden + eenheden en juiste beduidende cijfers; berekeningen met Excel-formules; minstens twee uitgewerkte voorbeelden per soort berekening; spreidingsgrafiek met titel, benoemde assen en trendlijn; juiste verband afgeleid. | Beduidende cijfers • eenheden vergeten • berekeningsfouten • assen benoemen • trendlijn toevoegen • grafiek met enkel meetwaardes • omgekeerd evenredig i.p.v. recht evenredig (of omgekeerd) |
| 3. Concluderen (besluit) | 3 | Onderzoeksvraag expliciet beantwoord met verwijzing naar de data; koppeling met de theorie en de formule; hypothese besproken; meetfouten verklaard; reflectievragen van het werkblad beantwoord. | Geen koppeling met de theorie • formule bespreken • meetfouten verklaren • besluit niet volledig en/of onduidelijk |
| 4. Attitude (afspraken en verzorging) | 2 | In het sjabloon en als .xlsx ingediend; op tijd (avond vóór de les van volgende week); cursieve instructietekst verwijderd, feedbackblok behouden; verzorgde lay-out en correcte vaktaal; aantoonbaar als groep gemaakt. | Deze tekst verwijderen • verslag op tijd uploaden (dag vóór het volgende labo) |

Voor labo 11 (open onderzoek) wordt onderdeel 1 uitgebreid met 'kwaliteit van de eigen SMART-onderzoeksvraag en het onderzoeksplan' en onderdeel 3 met 'communicatie via de poster'.

# Bijlage C – Proces- en attituderubric (40 %)
Eén rubric voor proces én attitude, met tien thema's. Per thema duidt de leerkracht één niveau aan; de score is de som van de tien niveaus (/10). Product-aspecten die samenhangen met het werk in het labo (voorbereiding, data, groepswerk, deadline) zijn in de thema's verwerkt. Naam: …………………………………   Labo: ……   Datum: ……/……/……
**Score: …… / 10  (= 40 % van het practicumcijfer)        Opmerkingen: ……………………………………………………………………………………………**

| Thema | Uitstekend (1) | Goed (0,8) | Voldoende (0,6) | Onvoldoende (0,4) | Slecht (0,2) |
|---|---|---|---|---|---|
| 1. Voorbereiding (oriëntatievragen, voorbereidende berekeningen, lesdoelen gelezen) | Werkblad volledig voorbereid: oriëntatievragen en berekeningen correct uitgewerkt; weet precies wat het doel en de werkwijze zijn en kan dit uitleggen. | Voorbereiding gemaakt met kleine fouten of hiaten; kent doel en werkwijze. | Voorbereiding gedeeltelijk; moet tijdens het labo nog zaken opzoeken of narekenen. | Nauwelijks voorbereid; start pas na uitleg van de leerkracht. | Niet voorbereid, werkblad niet bij; kan niet starten. |
| 2. Hypothese en onderzoekend denken | Formuleert vóór elke proef een beredeneerde hypothese, benoemt variabelen (onafhankelijk/afhankelijk/constant), toetst ze expliciet aan de data. | Hypothese vooraf genoteerd en getoetst; redenering soms beknopt. | Hypothese genoteerd maar als 'gokje' of pas tijdens de proef; toetsing beperkt. | Hypothese enkel na aansporing of achteraf ingevuld. | Geen hypothese; voert uit zonder na te denken over het verwachte resultaat. |
| 3. Opstelling bouwen en meettoestellen gebruiken | Bouwt zelfstandig en correct vanuit het schema; A-meter in serie, V-meter parallel, juiste bereiken, AC/DC juist; laat spontaan controleren vóór inschakelen. | Bouwt correct met één kleine verbetering na controle; laat controleren. | Heeft hulp nodig bij het schema of de meetbereiken; laat controleren na herinnering. | Meerdere fouten in de opstelling; bron ingeschakeld zonder controle. | Kan de opstelling niet bouwen; herhaaldelijk foute of onveilige aansluitingen. |
| 4. Nauwkeurig meten en noteren (de ruwe data van het verslag) | Meet zorgvuldig en herhaalt metingen; noteert onmiddellijk, chronologisch, met symbool, eenheid en juiste beduidende cijfers; beschikt op het einde van de les over alle data (ook digitaal gedeeld). | Meet zorgvuldig; noteert volledig met kleine slordigheden in eenheden of cijfers. | Metingen volledig maar slordig genoteerd; eenheden of herhalingen ontbreken soms. | Onvolledige of onbetrouwbare metingen; data moeten achteraf gereconstrueerd worden. | Data ontbreken, zijn onleesbaar of verzonnen. |
| 5. Veilig werken | Past alle veiligheidsregels spontaan toe (bron uit bij opbouwen, I_max, geen contact met blanke geleiders, magneten/warmte/water), signaleert risico's bij anderen. | Werkt veilig; één keer herinnerd aan een regel. | Werkt meestal veilig maar moet meermaals herinnerd worden. | Negeert regels (bv. stroom boven I_max, geen controle) ondanks opmerkingen. | Onveilig gedrag dat anderen of materiaal in gevaar brengt; wordt uit de proef gehaald. |
| 6. Zorg voor materiaal, orde en netheid | Gaat zorgzaam om met toestellen; werkpost ordelijk tijdens het labo; ruimt volledig op en legt alles terug zoals gevonden; meldt defecten. | Zorgzaam en ordelijk; ruimt op met kleine onvolkomenheden. | Werkpost rommelig; ruimt op na aansporing. | Slordig met materiaal; onvolledig opgeruimd. | Laat materiaal achter of beschadigt het door onzorgvuldigheid. |
| 7. Samenwerking en communicatie (in het labo én bij het groepsverslag) | Verdeelt taken, wisselt rollen, luistert en overlegt; neemt niet over en haakt niet af; deelt het verslag via OneDrive, werkt aan het geheel mee en leest het werk van anderen na; positieve peerfeedback. | Werkt goed samen en draagt bij aan het hele verslag; kleine onevenwichten in de taakverdeling. | Werkt mee maar eerder passief of dominant; bijdrage aan het verslag beperkt tot het eigen deel. | Weinig overleg; laat anderen het werk doen of werkt alleen; verslag niet als groep nagekeken. | Werkt niet samen, stoort de groep of levert geen bijdrage aan het groepsverslag. |
| 8. Zelfstandigheid en probleemoplossend handelen | Start zelf, zoekt bij problemen eerst zelf een oplossing (handleiding, schema, controle van de kring) en stelt daarna gerichte vragen; controleert of resultaten plausibel zijn en stuurt bij. | Werkt grotendeels zelfstandig; vraagt gericht hulp wanneer nodig. | Heeft regelmatig hulp nodig; vraagt onmiddellijk zonder eerst zelf te zoeken. | Wacht af tot de leerkracht of de partner het oplost. | Geeft op bij het eerste probleem; onderneemt niets. |
| 9. Inzet, doorzetting en tijdsbeheer (incl. deadline verslag) | Blijft tot het einde geconcentreerd en nieuwsgierig; rondt het labo binnen de tijd af; de groep start tijdig met het verslag en dient het ruim op tijd in als .xlsx in het sjabloon. | Goede inzet; labo en verslag op tijd klaar. | Wisselende inzet of tijdsdruk; verslag net op tijd of in laatste moment gemaakt. | Weinig inzet; labo niet afgewerkt binnen de tijd of verslag te laat. | Ongeïnteresseerd, afgeleid of stoort; verslag (veel) te laat of niet ingediend. |
| 10. Reflectie en kritische houding | Bespreekt spontaan meetfouten en betrouwbaarheid, formuleert verbetervoorstellen, vult de zelfreflectiefiche eerlijk en diepgaand in en past eerdere feedback aantoonbaar toe. | Reflecteert zinvol; past de meeste feedback toe. | Reflectie oppervlakkig ('afleesfouten'); feedback gedeeltelijk toegepast. | Reflecteert enkel na aansporing; herhaalt dezelfde fouten. | Geen reflectie; feedback wordt genegeerd. |

### Observatieblad leerkracht (per labo) – niveau per thema invullen (1 / 0,8 / 0,6 / 0,4 / 0,2)

| Leerling | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | /10 | Opmerking |
|---|---|---|---|---|---|---|---|---|---|---|---|---|


# Bijlage D – Zelfreflectie- en peer-evaluatiefiche

### D.1 Zelfreflectie (in te vullen na labo 4, 6, 9 en 11)

| Vraag | Mijn antwoord |
|---|---|
| Scoor jezelf op de 10 thema's van de rubric in Bijlage C (1 / 0,8 / 0,6 / 0,4 / 0,2) en motiveer één sterk punt en één werkpunt. |  |
| Welke vaardigheid (meten, schema's, grafieken, berekenen, onderzoeksvragen formuleren, samenwerken, veilig werken) beheers ik nu beter dan bij het vorige reflectiemoment? |  |
| Wat ga ik bij het volgende labo concreet anders doen? |  |
| Welke feedback op mijn verslagen heb ik toegepast? |  |


### D.2 Peer-evaluatie met puntenverdeling (enkel bij de labo's die de leerkracht aanduidt: voorzien bij labo 6, 9 en 11)
Zo werkt het: elke leerling verdeelt 100 punten per groepslid (groep van 3 → 300 punten, groep van 2 → 200 punten) over zichzelf én de andere groepsleden, volgens ieders werkelijke bijdrage aan het labo en het verslag. Iedereen evenveel gedaan → iedereen 100. Zelf minder gedaan → bv. jezelf 90, de twee anderen 105. Je vult de fiche individueel en eerlijk in (de leerkracht ziet ze, je groepsleden niet) en motiveert je keuze kort.
Berekening door de leerkracht: peerfactor = (gemiddelde van de punten die je van alle groepsleden, jezelf inbegrepen, kreeg) / 100. Individueel verslagpunt = groepspunt × peerfactor (afgerond, maximum 10/10). Voorbeeld: groepspunt 7,5; jij kreeg 105, 105 en 90 → gemiddeld 100 → factor 1,00 → 7,5. Een groepslid dat 80, 85 en 90 kreeg → factor 0,85 → 6,4. De leerkracht kan de factor begrenzen of bijsturen als de verdeling niet strookt met de observaties.
Labo nr.: ……   Groep: ………………………   Ingevuld door: ………………………………   Totaal te verdelen: 300 (groep van 3) / 200 (groep van 2)

| Groepslid (naam) | Punten | Korte motivatie (wat deed deze persoon concreet?) |
|---|---|---|
| Ikzelf:  |  |  |
| Totaal (controleer: 300 of 200) |  |  |

Een apart document op Smartschool legt deze werkwijze ook uit voor de ouders en bevat het invulformulier (digitaal).

# Bijlage E – Naslag

### E.0 Begrippenlijst – moeilijke woorden uit deze cursus

| Begrip | Betekenis in eenvoudige woorden |
|---|---|
| Influentie (elektrostatische inductie) | Ladingen in een voorwerp verschuiven doordat een geladen voorwerp in de buurt komt, zonder aanraking. |
| Elektrostatische inductie | Andere naam voor influentie; wordt in de theoriecursus gebruikt. |
| Superpositie | Krachten of veldsterkten van verschillende ladingen tel je als vectoren (pijlen) bij elkaar op. |
| Substitutieweerstand | De ene weerstand die een hele schakeling kan vervangen zonder dat de stroom verandert. |
| Tolerantie | De toegelaten afwijking van een onderdeel t.o.v. zijn opgegeven waarde (bv. ± 5 %). |
| Tarreren | Een balans op nul zetten met wat er al op ligt (knop TARE/0). |
| Weissgebieden | Gebiedjes in ijzer waarin alle atoommagneetjes dezelfde kant op wijzen. |
| Remanentie | Het 'blijven plakken' van magnetisme in staal nadat de magneet weg is. |
| Galvanisch gescheiden | Twee kringen zonder elektrische verbinding, enkel gekoppeld via een magnetisch veld (relais, transformator). |
| Derde wet van Newton | Actie = reactie: oefent A een kracht uit op B, dan oefent B een even grote, tegengestelde kracht uit op A. |
| Magnetische flux / fluxverandering | Aantal veldlijnen door een winding / de toename of afname daarvan in de tijd. |
| Wervelstromen | Kringvormige stromen in een massief stuk metaal, veroorzaakt door een veranderende flux; ze remmen en verwarmen. |
| Joule-effect | Warmteontwikkeling in een weerstand door stroom: P = I²·R. |
| Hysterese | Energieverlies doordat ijzer telkens opnieuw ommagnetiseerd wordt (50× per seconde bij netspanning). |
| Lekflux | Veldlijnen van de eerste spoel die niet door de tweede spoel gaan. |
| Gelamelleerd | Opgebouwd uit dunne, geïsoleerde plaatjes (tegen wervelstromen). |
| Bemonsteringsfrequentie | Hoeveel metingen per seconde een sensor doet (Hz). |
| SMART | Specifiek, Meetbaar, Aanvaardbaar, Realistisch, Tijdsgebonden – kenmerken van een goede onderzoeksvraag. |
| Peerfactor | Getal (rond 1) dat zegt hoeveel jij volgens je groepsleden bijdroeg; vermenigvuldigt het groepspunt. |


### E.1 Tribo-elektrische reeks (vereenvoudigd)
Van het materiaal dat een positieve lading krijgt (geeft gemakkelijk elektronen af) naar het materiaal dat negatief wordt (neemt elektronen op). Wrijf je twee materialen tegen elkaar, dan wordt het hoogste in de lijst positief, het laagste negatief. Hoe verder uit elkaar, hoe sterker de lading.

| + positief |  |  |  |  |  |  |  |  |  |  | − negatief |
|---|---|---|---|---|---|---|---|---|---|---|---|
| lucht | mensenhuid / leer | glas | mensenhaar | nylon | wol | zijde | papier | katoen | hout / barnsteen | hard rubber / ballon | PVC / teflon |

Bron: samengesteld op basis van gangbare tribo-elektrische reeksen (o.a. leerplan III-BCSW-d, LPD 2 F).

### E.2 Kleurcode voor weerstanden
De waarde wordt gecodeerd met vier of vijf kleurringen. De ring die de tolerantie aangeeft (%) is steeds iets breder dan de andere ringen of staat verder van de rest: zo bepaal je de volgorde van de ringen. Bij 6 ringen geeft de laatste ring de temperatuurcoëfficiënt.
[FIGUUR: kleurcode.png]
[FIGUUR: kleurcode.png]

| Kleur | Ring 1 (cijfer) | Ring 2 (cijfer) | (Ring 3) (cijfer) | Ring 4 of 3 (vermenigvuldiger) | Tolerantie | Eventueel temp. coëff. (ppm/K) |
|---|---|---|---|---|---|---|
| Zwart | – | 0 | 0 | × 1 | – | – |
| Bruin | 1 | 1 | 1 | × 10 | ± 1 % | 100 |
| Rood | 2 | 2 | 2 | × 100 | ± 2 % | 50 |
| Oranje | 3 | 3 | 3 | × 1 000 | – | 15 |
| Geel | 4 | 4 | 4 | × 10 000 | – | 25 |
| Groen | 5 | 5 | 5 | × 100 000 | ± 0,5 % | – |
| Blauw | 6 | 6 | 6 | × 1 000 000 | ± 0,25 % | 10 |
| Violet | 7 | 7 | 7 | × 10⁷ | ± 0,1 % | 5 |
| Grijs | 8 | 8 | 8 | × 10⁸ | – | – |
| Wit | 9 | 9 | 9 | × 10⁹ | – | – |
| Goud | – | – | – | × 0,1 | ± 5 % | – |
| Zilver | – | – | – | × 0,01 | ± 10 % | – |
| Geen ring | – | – | – | – | ± 20 % | – |


### E.3 Nuttige constanten en tabelwaarden

| Grootheid | Waarde |
|---|---|
| Elementaire lading e | 1,602·10⁻¹⁹ C |
| Constante van Coulomb k | 8,99·10⁹ N·m²/C² |
| Valversnelling g | 9,81 m/s² |
| Soortelijke weerstand (20 °C): Cu / Al / Fe / constantaan / nikkeline | 1,7·10⁻⁸ / 2,8·10⁻⁸ / 1,0·10⁻⁷ / 4,9·10⁻⁷ / 4,0·10⁻⁷ Ω·m |
| Temperatuurcoëfficiënt α (20 °C): Cu / Fe / Al / constantaan / koolstof | 3,9·10⁻³ / 5,0·10⁻³ / 4,0·10⁻³ / ≈1·10⁻⁵ / ≈ −5·10⁻⁴ K⁻¹ |
| Magnetische permeabiliteit vacuüm μ₀ | 4π·10⁻⁷ T·m/A |


---

# BIJLAGE V – Referentie: structuur van een software-handleiding als bijlage (bv. meetsoftware)

- Kop 1 "Bijlage F – [software] installeren en [sensor] aansluiten"; inleiding: waarom, welke laptop/OS, wat vooraf.
- F.1 Installatie in genummerde stappen (waar downloaden – academisch softwareportaal of site –, uitpakken, installeren, eerste start, eventuele bestanden vervangen), telkens met een schermafbeelding (twee naast elkaar in een tabel zonder randen) en bijschrift.
- F.2 Verbinden met de interface (Bluetooth én kabel-alternatief), met schermafbeelding van de hardware-setup.
- F.3 Sensor configureren (poort, meetbereik, bemonsteringsfrequentie), grafiek aanmaken, assen instellen.
- F.4 Meting opnemen, pieken aflezen, oppervlakte/gereedschappen gebruiken, schermafbeelding maken (sneltoets), resultaat in het verslag plaatsen met titel en uitleg.
- Kader "Problemen oplossen" (verbinding niet gevonden, geen signaal, verkeerde eenheid …) en kader "Evaluatie van de installatie-opdracht" (bewijs = schermafbeelding uploaden vóór een deadline; hulp vragen tijdens de les, een andere les of via Smartschool).
- Dezelfde stappen staan in verkorte vorm ("[software] in 7 stappen") in het labo waar de software gebruikt wordt, met verwijzing naar de bijlage.
