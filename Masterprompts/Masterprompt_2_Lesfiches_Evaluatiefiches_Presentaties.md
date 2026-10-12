# MASTERPROMPT 2 – Lesfiches, evaluatiefiches en PowerPoints maken op basis van een OVUR-labocursus (specificatie + voorbeelden)

> **Gebruik.** Geef de AI de **leerlingenversie én de leerkrachtenversie** van de labocursus (docx + pdf; de docx bevat de figuren als bestanden, de pdf levert de echte paginanummers) en kopieer deze volledige prompt. Vul `[...]` in § 1 in. Onderaan staan **letterlijke voorbeelden** (een lesfiche, drie evaluatiefiches, het peer-evaluatiedocument en de slide-voor-slide opbouw van een labopresentatie) die de norm zijn voor vorm, toon en diepgang.

---

## 1. Rol, context en bronnen

**Rol.** Je bent vakdidacticus en lesmateriaalontwerper met programmeervaardigheden. Op basis van de bijgevoegde labocursus **[titel, klas, vak, leerplancode]** maak je drie pakketten:
- **(A) Lesfiches** – één Word-bestand per lesuur;
- **(B) Evaluatiefiches** – één Word-bestand per huiswerkopdracht + een overzichtsdocument + het document "Peer-evaluatie – werkwijze";
- **(C) PowerPointpresentaties** – één inleidende presentatie + één per labo.

Alles in het Nederlands (Vlaanderen), in de terminologie van de cursus, zonder vermelding van een schooljaar. Werk autonoom; neem beslissingen zelf en meld ze in het eindrapport. **Verzin nooit** paginanummers, leerplandoelen, lesdoelen of inhoud die niet in de cursus staat. Alles wat in de fiches en slides staat, moet letterlijk of herleidbaar uit de cursus komen.

**Context (invullen):** klas **[...]** · vak **[...]** · lesuren per labo als die afwijken van de richtduur in de cursus **[...]** · labo's met peer-evaluatie (zoals in de cursus of aangepast) **[...]** · platform Smartschool (uploadzone, berichten) en OneDrive · toetsen: **[per hoofdstuk / per trimester – welke labo's horen bij welke toets]**.

## 2. Stap 0 – De cursus volledig inlezen (verplicht vóór je iets maakt)

Maak per labo een gestructureerde inventaris (bv. JSON) met: nummer, titel, richtduur, type practicum, mate van sturing, lesdoelen (letterlijk), leerplandoelen (letterlijk), voorkennis-items, context, onderzoeksvraag/-vragen, doel, oriëntatievragen, SMART-oefening (niveau + opties), benodigdheden, theorie-items en formules (LaTeX of tekst), veiligheidsregels, werkplan, alle delen/proeven van de uitvoering (titel, stappen, tabellen met kopregel en rijen), figuren (bestandspad of paginanummer + bijschrift), uitleg-kaders, STEM-opdracht, reflectievragen (met de markering "internet toegelaten"), evaluatiekader (product/proces/indienen/peer), modelantwoorden en leerkrachteninfo (uit de leerkrachtenversie). Lees ook Deel 1 en de bijlagen (puntenverdeling, rubric, zelfreflectie/peer, software-handleiding).

Bepaal de **werkelijke paginanummers** door in de leerlingen-PDF te zoeken op de koppen ("LABO n –", "O – ORIËNTEREN", "V – VOORBEREIDEN", "U – UITVOEREN", "R – REFLECTEREN", "Bijlage X –"). Gebruik het paginanummer zoals het in de voettekst staat.

Doe dit bij voorkeur programmatisch (de cursus is gegenereerd met echte kopstijlen) zodat fiches en slides 1-op-1 met de cursus overeenkomen en bij een nieuwe cursusversie opnieuw gegenereerd kunnen worden.

## 3. (A) Lesfiches

**Bestanden**: map `Lesfiches/`, `Lesfiche_LaboNN_lesuurX.docx`, A4, Calibri 11, één tabel met twee kolommen (label lichtblauw D9E2F3, 4,2 cm breed; inhoud 12,8 cm), kop 1 "Lesfiche – Labo n – titel (lesuur x/y)", daaronder grijze regel "Vak • Klas • Leerplan • Lesmateriaal: [cursus], Labo n (p. a-b)", voettekst "Lesfiche labo n – lesuur x/y – [vak] [klas] – [school]".

**Aantal**: per labo evenveel fiches als lesuren in de richtduur (2 lesuren → 2 fiches; open onderzoek "1 u voorbereiding + 2 u uitvoering" → 3 fiches). Een labo van "1-2 lesuren" → 1 fiche (vermeld de uitloop).

**Rijen, exact in deze volgorde en met deze labels:**
1. **Titel** – "Labo n – titel (lesuur x/y)".
2. **Lesdoelen** – "De leerlingen kunnen …" (herformuleer de lesdoelen van de cursus; **niet** de letterlijke leerplandoelen). Verdeel de lesdoelen zinvol over de lesuren (lesuur 1: oriënteren/voorbereiden/eerste delen; lesuur 2: resterende delen, verwerking, reflectie) en voeg toe: "(Overige lesdoelen van dit labo: zie lesfiche lesuur …)".
3. **Leerplandoelen (basis)** – LPD-codes met omschrijving zoals in de cursus.
4. **Korte inhoud van de les** – 4-5 bullets met paginaverwijzing en tijdsindicatie: lesuur 1 = Oriënteren (p. …): context, onderzoeksvraag, bespreking oriëntatievragen (huiswerk) en SMART-oefening · Voorbereiden (p. …): benodigdheden, theorie, veiligheid, hypothese, werkplan/goedkeuring meetplan · Uitvoeren deel 1 (p. …): welke delen · Afsluiting: tussentijdse stand, opruimen, afspraken. Lesuur 2 = korte herhaling + veiligheidscheck · resterende delen · STEM-ontwerpopdracht(en) · Reflecteren (p. …): besluit, foutenanalyse, reflectievragen · toelichting verslag/indienen. Open onderzoek: voorbereidingsuur (vraag kiezen/SMART/variabelen/werkwijze/materiaal/risicoanalyse/goedkeuring), uitvoering 1/2, uitvoering 2/2 + afspraken poster.
5. **Gebruikte werkvormen** – concreet en passend bij het type practicum (onderzoekend leren in delen met doorschuifsysteem, groepjes van 2-3 met vaste rollen, bouwopdracht, demonstratie door de leerkracht, onderwijsleergesprek bij nabespreking, begeleid onderzoek met simulaties, apparatuurpracticum met instructiekaart, probleemoplossend practicum, ICT-verwerking met sensoren, open praktijkonderzoek met coaching …).
6. **Evaluatievorm** – altijd deze vijf bullets: (1) Procesevaluatie (40 %): observatie met de proces- en attituderubric, Bijlage C (p. …). (2) Productevaluatie (60 %): verslag/werkbladen/poster – zie evaluatiefiche "Verslag labo n" (Bijlage B, p. …). (3) Formatief: oriëntatievragen en SMART-oefening (evaluatiefiche "Voorbereiding labo n"), hypothese vóór de proef. (4) **Toets**: "de lesdoelen van dit labo komen aan bod op de toets van het bijhorende hoofdstuk (…)" met tussen haakjes het type vraag (bv. "F = B·I·l toepassen, grafiek interpreteren en B bepalen, derde wet van Newton in deze context"). (5) Peer-evaluatie met puntenverdeling (Bijlage D, p. …) – enkel bij de labo's die de cursus aanduidt.
7. **Paginanummers in de cursus** – "Labocursus p. a-b: lesdoelen/leerplandoelen p. …, O p. …, V p. …, U p. …, R p. …. Bijlagen: B p. …, C p. …" (+ software-bijlage waar relevant).
8. **Benodigdheden** – de lijst uit de V-fase, letterlijk.
9. **Huiswerk / voorbereiding** – lesuur 1: "Vóór lesuur 1: oriëntatievragen + voorkennis-check (p. …) en SMART-oefening" (+ software-installatie waar relevant); laatste lesuur: "Verslag/werkbladen indienen uiterlijk één week na het labo (23.59 u) via de Smartschool-uploadzone".

Zie **Bijlage A** onderaan voor een volledig voorbeeld.

## 4. (B) Evaluatiefiches, overzicht en peer-document

**Bestanden**: map `Evaluatiefiches/`, zelfde lay-out als de lesfiches (kop 1 "Evaluatiefiche – …", grijze contextregel, tweekolomstabel, voettekst).

**Welke fiches (volledig, voor élke opdracht buiten de les):**
- `Evaluatiefiche_Voorbereiding_LaboNN.docx` voor elk labo: oriëntatievragen, voorkennis-check, SMART-oefening, en labo-specifieke voorbereiding (berekeningen vooraf, R_sub uitdrukken, ideeën meebrengen, software installeren → verwijzing naar aparte fiche).
- `Evaluatiefiche_Verslag_LaboNN.docx` voor elk labo met product, volgens de **indientabel** van de cursus: (a) Excel-verslag (sjabloon, bestandsnaam "nummer labo [vak] titel (namen) klas", inhoud volgens checklist Bijlage A, puntenverdeling 2-3-3-2), (b) ingevulde werkbladen als PDF via de uploadzone (puntenverdeling voor werkbladen: 1 Volledigheid /2 – 2 Kwaliteit waarnemingen & schetsen /3 – 3 Verklaringen & reflectie /3 – 4 Attitude /2), (c) combinatie Excel + Word/PDF met schermafbeeldingen (beide beschrijven), (d) poster + Excel-data (aparte fiche `Evaluatiefiche_Poster_LaboNN.docx`, met postercriteria en "bewijsstuk onderzoekscompetentie").
- `Evaluatiefiche_[Software]_installeren.docx` als de cursus een installatie-opdracht bevat: waar te vinden (portaal/site), hoe installeren (stappen), bewijs (schermafbeelding uploaden), deadline (dag vóór het labo), wat bij Mac/geen laptop, hoe hulp vragen (tijdens de les, een andere les, Smartschool-bericht), evaluatie via rubric-thema 1 (voorbereiding) en 8 (zelfstandigheid).
- `Evaluatiefiche_Zelfreflectie.docx` (bij de 4 labo's met zelfreflectie) en `Evaluatiefiche_Peer-evaluatie.docx` (bij de peer-labo's).

**Rijen per fiche, in deze volgorde:** Opdracht (concreet, in stappen; thuis/individueel of groepswerk) · Waar vind je ze? (paginanummers) · Deadline en indienen (tijdstip, uploadzone, één upload per groep, bestandsnaam) · **Hoe wordt dit geëvalueerd?** (criteria met punten of rubric-thema's, gewicht 60/40, groepspunt/individueel, peerfactor, herwerken mogelijk?) · **Leerplandoelen** (letterlijk) · **Lesdoelen die geëvalueerd worden** ("De leerling kan …") · Hulp/Vragen.

**Overzicht**: `Overzicht_evaluatiefiches_en_lesfiches.docx` met (1) inleiding over de weging 60/40 en de peerfactor, (2) tabel van alle evaluatiefiches (labo, soort, opdracht, telt mee in, bestandsnaam), (3) samenvattende tabel per labo (voorbereiding / product / proces / peer / zelfreflectie), (4) lijst van alle lesfiches.

**Peer-document**: `Peer-evaluatie_werkwijze.docx` voor leerlingen en ouders: 1 Waarom? · 2 Hoe verdeel je de punten? (100 punten per groepslid: 300 bij drie, 200 bij twee; verdelen volgens werkelijke bijdrage aan labo én verslag; voorbeelden; totaal exact; motiveren; individueel en vertrouwelijk; wat niet mag) · 3 Hoe berekent de leerkracht het individuele punt? (peerfactor = gemiddelde ontvangen punten incl. eigen score / 100; individueel punt = groepspunt × peerfactor, afgerond op 0,5, max. 10; leerkracht kan begrenzen 0,7-1,2 en bijsturen) · 4 Rekenvoorbeeld in tabel (drie leerlingen) · 5 Formulier (labo, groep, ingevuld door, datum; tabel groepslid/punten/motivatie; totaal; handtekening). Zie **Bijlage C** onderaan.

## 5. (C) PowerPointpresentaties

**Bestanden**: map `Presentaties/`, 16:9 (13,33 × 7,5 in), `00_Inleiding_labocursus.pptx` en `NN_LaboN_[korte titel].pptx`. Doel: de leerkracht leidt het labo in en legt **alles** uit terwijl de leerlingen de cursus volgen; de presentatie volgt de cursus dus 1-op-1 en laat niets weg.

**Opbouw inleidende presentatie**: titelslide → Deel 1 van de cursus, onderdeel per onderdeel (OVUR-tabel, sturingsleerlijn, SMART-tabel, veiligheid en veiligheidsverantwoordelijke, meten en noteren, Excel-sjabloon, groepswerk, indientabel, peer-evaluatie, evaluatie 60/40, overzicht labo's × LPD) → overzichtslide "Wat staat er dit jaar op het programma?" (alle labo's met sturing) → Bijlagen A (checklist), B (puntenverdeling), C (rubric, gesplitst over meerdere slides, 2-3 thema's per slide), D (zelfreflectie, peer-evaluatie).

**Opbouw per labo** (zie Bijlage D onderaan voor een volledig voorbeeld): 
1. Titelslide in de labokleur: titel, "Richtduur • Type practicum", "Mate van sturing", "Werkwijze: O – V – U – R", kenmerkende figuur van het labo rechts; **notities** = volledige leerkrachteninfo.
2. Slide LESDOELEN (groen accent) · slide LEERPLANDOELEN (oranje accent) · slide VOORKENNIS (paars accent; modelantwoorden in notities).
3. Tussenslide **O – ORIËNTEREN** (lichtblauwe achtergrond, brede balk, één regel wat de fase is + de onderdelen) → de onderdelen Context · Onderzoeksvraag · Doel van het onderzoek · Oriëntatievragen (notities: modelantwoorden) · Onderzoeksvraag (stap 1: vraag gegeven + aparte SMART-oefening met tabel; stap 2 en 3: de vraag wordt níét getoond – de slide toont de vier opties A-D resp. de instructie om zelf te formuleren + lege S-M-A-R-T-rij; de juiste/voorbeeldvraag staat enkel in de notities). **Elk onderdeel is een kopje in de labokleur, niet automatisch een aparte slide**: kleine opeenvolgende onderdelen van dezelfde fase worden op één slide gecombineerd (titel = de fase, bv. "O – Oriënteren"), zolang de tekst op 16 pt past.
4. Tussenslide **V – VOORBEREIDEN** → Benodigdheden · Theorie-overzicht (met formules als echte vergelijkingen; splitsen indien nodig) · UITLEG-kaders · VEILIGHEID // NAUWKEURIGHEID (rood accent) · Hypothese (vaste tekst: "Formuleer vóór de proef een beredeneerde verwachting …", "Een hypothese mag fout blijken …") · Werkplan.
5. Tussenslide **U – UITVOEREN** → per Deel/Proef één (of meer) slide(s): onderzoeksvraag van het deel, hypothese-cue, uitvoering in stappen, lege meettabel als één cursieve regel ("Tabel 1 – … – invullen op het werkblad; kolommen: I (A) | m (g) | …" – géén aparte slide met een lege tabel), figuur rechts; STEM-ONTWERPOPDRACHT (groen-blauw accent); uitleg-kaders; software-stappen in het kort.
6. Tussenslide **R – REFLECTEREN** → Besluit (vaste tekst) · Foutenanalyse en betrouwbaarheid (vaste tekst) · Reflectievragen (genummerd; notities: modelantwoorden) · Communicatie/poster (open onderzoek) · slide **WAT, HOE EN WANNEER WORDT GEËVALUEERD IN DIT LABO?** (grijs accent).
7. Software-handleiding (bv. meetsoftware) als extra slides achteraan bij het labo waar ze hoort, met alle schermafbeeldingen.

**Vormgeving**: titelbalk (1,0 in hoog) in de labokleur met witte titel 26 pt (20 pt bij lange titels); voettekst "Labo n • [vak] [klas] • slidenummer" 9 pt grijs; kleur per leerstofblok (bv. blauw 1F4E79, groen 00695C, paars 6A1B9A, rood C62828, oranje EF6C00); verticale kleuraccentbalk links bij kaders (lesdoelen, leerplandoelen, voorkennis, veiligheid, STEM, evaluatie); tekst 15-22 pt automatisch gekozen zodat de tekst past; tekst links (8,0 in breed) en figuur rechts (4,3 in) – bij korte tekst (≤ 4 regels) figuur groot eronder over de volledige breedte; meerdere figuren in een raster met bijschriften (10 pt cursief grijs); tabellen met kopregel in de labokleur, rijen afwisselend wit/lichtgrijs, lettergrootte 12-16 pt, kolombreedte volgens tekstlengte.

**Tekst – telegramstijl (mijn vaste voorkeuren, allemaal toepassen):**
1. **Eén zin = één bullet**; de eerste zin van een alinea is de hoofdbullet (•), volgende zinnen worden ingesprongen sub-bullets (–). Genummerde stappen blijven genummerd (nummering loopt door over vervolgslides).
2. **Korter zonder informatieverlies**: eindpunten weg; aanloopjes schrappen ("Je kan…", "In dit labo…", "Let op:", "Daarom…"); **lidwoorden weglaten** (de/het/een) behalve waar de zin anders onbegrijpelijk wordt; afkortingen (bv., ca., max., min., t.o.v., i.f.v., o.a., m.a.w., evt.); "daarna/vervolgens" → "→"; percentages, getallen en eenheden ongewijzigd laten. Nooit inhoud, getallen, voorwaarden of uitzonderingen schrappen.
3. **Witruimte**: ≥ 14 pt na elke hoofdbullet, 6 pt tussen sub-bullets; maximaal ± 8 hoofdbullets per slide.
4. **Splitsen in plaats van verkleinen, maar nooit (bijna) lege slides**: past de tekst niet bij 16 pt, splits dan de slide ("Titel (vervolg)"). Omgekeerd: een slide die minder dan ± 40 % gevuld is, wordt samengevoegd met het volgende onderdeel van dezelfde fase (het volgende onderdeel mag dan doorlopen op een vervolgslide). Doel: de leerkracht loopt in één vlotte beweging door het labo, in exact dezelfde volgorde en met dezelfde kopjes als de cursus. Lege meettabellen als één regel met de kolomnamen; lange tabellen met veel herhaling als eerste rijen + "… (zie werkblad)". Richtcijfer: 15-35 slides per labo, afhankelijk van het aantal delen.
5. **Formules als echte vergelijkingen** (formule-editor/OMML, geen platte tekst): lange breukstrepen, indices, exponenten, vectorpijlen, Griekse letters; gecentreerd, vet, in de labokleur, 4-6 pt groter dan de tekst; met een tekstfallback voor viewers zonder OMML. Inline symbolen in de tekst mogen gewoon tekst zijn met correcte sub-/superscript (F_L → F<sub>L</sub>, r² …).
6. **Alle figuren** van de cursus overnemen, met bijschrift; de kenmerkende figuur op de titelslide; bij een gesplitste slide de figuur **herhalen** op elke vervolgslide.
7. **Notities**: modelantwoorden bij elke slide met vragen ("Modelantwoord – [begin van de vraag]…: …"), leerkrachteninfo op de titelslide. Nooit zichtbaar op de slide zelf (de leerlingen zien de presentatie).
8. Geen schooljaar; geen "station" (de cursus gebruikt "Deel 1, Deel 2, …").

**Voorbeeld van de herformulering** (cursustekst → slide):
- Cursus: "De magneet oefent een kracht uit op de geleider, maar de geleider oefent dan ook een even grote, tegengestelde kracht uit op de magneet (derde wet van Newton, zie kader). Zetten we de magneet op een elektronische balans, dan lezen we een massaverschil af waaruit we de kracht berekenen."
- Slide: "• Magneet oefent kracht uit op geleider → geleider oefent even grote, tegengestelde kracht uit op magneet (derde wet van Newton, zie kader)" / "      – Magneet op elektronische balans → massaverschil aflezen → kracht berekenen".

**Technische aanpak (aanbevolen)**: genereer de presentaties met een script (python-pptx) uit dezelfde gestructureerde inventaris als de fiches; implementeer een "telegram"-functie (zinnen splitsen op . ! ? ; met bescherming van afkortingen en decimalen, lidwoorden en aanloopjes verwijderen, hoofdletter herstellen), een passend-maak-functie (lettergrootte 22 → 15 pt kiezen op basis van geschat aantal regels; anders splitsen), een OMML-injectie voor vergelijkingen (mc:AlternateContent met a14:m + fallback-run), en een controlestap (render via LibreOffice naar PDF en bekijk miniaturen van alle slides). Controleer programmatisch: geen slide zonder titel, geen lege slide, aantal figuren per presentatie = aantal figuren in het labo, geen "schooljaar", geen "station".

## 6. Oplevering en eindrapport

- Mappen `Lesfiches/`, `Evaluatiefiches/`, `Presentaties/` + `Overzicht_evaluatiefiches_en_lesfiches.docx` + `Peer-evaluatie_werkwijze.docx`; alles bewerkbaar (.docx/.pptx) met echte kopstijlen.
- **Eindrapport**: tabel per labo (lesuren → aantal lesfiches; evaluatiefiches; aantal slides; aantal figuren in cursus vs. presentatie), paginanummers die je gebruikte, genomen beslissingen (verdeling lesdoelen over lesuren, toetsverwijzingen, peer-labo's), onduidelijkheden of fouten die je in de cursus tegenkwam.

---
---

# BIJLAGE A – Voorbeeld lesfiche (labo 9, lesuur 1/2) – letterlijk
# Lesfiche – Labo 9 – Elektromagnetische inductie: fluxverandering als oorzaak van spanning (lesuur 1/2)
Vak: Toegepaste fysica  •  Klas: 5BCW  •  Leerplan: III-BCSW-d (juni 2024)  •  Lesmateriaal: Labocursus Fysica 5BCW (leerlingenversie), Labo 9 (p. 66-74)
| Titel | Labo 9 – Elektromagnetische inductie: fluxverandering als oorzaak van spanning (lesuur 1/2) |
| Lesdoelen | De leerlingen kunnen aantonen dat een spanning geïnduceerd wordt in een spoel enkel wanneer de magnetische flux door de spoel verandert. / De leerlingen kunnen de invloed van snelheid van de beweging, sterkte van de magneet, aantal windingen en zin van de beweging/polariteit op de inductiespanning onderzoeken en koppelen aan de wet van Faraday en de wet van Lenz. / De leerlingen kunnen inductie opwekken met een elektromagneet die in- en uitgeschakeld wordt (flux verandert zonder beweging). / (Overige lesdoelen van dit labo: zie lesfiche lesuur 2.) |
| Leerplandoelen (basis) | LPD 7 F: elektromagnetische inductie analyseren en kwantificeren; wet van Faraday en Lenz; opwekken van wisselspanning. / LPD 1 S, 3 S: onderzoek met sensoren, ICT-verwerking. LPD 5 S: toepassingen. |
| Korte inhoud van de les | Oriënteren (p. 66): context, onderzoeksvraag, bespreking oriëntatievragen (huiswerk) en SMART-oefening. / Voorbereiden (p. 67): benodigdheden, theorie, veiligheid, hypothese, werkplan (en goedkeuring van het eigen meetplan waar van toepassing). / Uitvoeren – deel 1 (p. 69): Proef 1 – Inductiespanning met multimeters (magneet beweegt); Proef 2 – Inductiespanning door een elektromagneet (niets beweegt). / Afsluiting: tussentijdse stand, materiaal opruimen, afspraken voor lesuur 2. |
| Gebruikte werkvormen | Onderzoekspracticum met multimeters en Pasco-sensor per 2-3; ICT-verwerking (Capstone); ontwerp- en bouwopdracht mini-generator. |
| Evaluatievorm | Procesevaluatie (40 %): observatie met de proces- en attituderubric, Bijlage C (p. 88). / Productevaluatie (60 %): verslag/werkbladen – zie evaluatiefiche 'Verslag labo 9' (Bijlage B, p. 86). / Formatief: oriëntatievragen en SMART-oefening (evaluatiefiche 'Voorbereiding labo 9'), hypothese vóór de proef. / Toets: de lesdoelen van dit labo komen aan bod op de toets van het bijhorende hoofdstuk (wet van Faraday en Lenz toepassen, fluxverandering herkennen, U(t)-grafiek met pieken interpreteren). / Peer-evaluatie met puntenverdeling na dit labo (Bijlage D, p. 91). |
| Paginanummers in de cursus | Labocursus p. 66-74: lesdoelen/leerplandoelen p. 66, O p. 66, V p. 67, U p. 69, R p. 72. Bijlagen: B p. 86, C p. 88, F p. 96 (Capstone). |
| Benodigdheden | Drie spoelen (verschillend aantal windingen: ……, ……, ……), staafmagneet (2 stuks), weerstand, weekijzeren kern, twee multimeters, regelbare spanningsbron, snoeren, Pasco Voltage Sensor, Pasco Interface, laptop met Pasco Capstone (zie handleiding 'Werken met Pasco Capstone en sensoren'). |
| Huiswerk / voorbereiding | Vóór lesuur 1: oriëntatievragen + voorkennis-check (p. 66) en SMART-oefening. / Vóór het labo: Pasco Capstone installeren (Bijlage F). |

---

# BIJLAGE B – Voorbeelden evaluatiefiches (Verslag labo 9 – afwijkend verslag; Voorbereiding labo 4; software installeren) – letterlijk
# Evaluatiefiche – Pasco Capstone installeren (vóór labo 9)
Vak: Toegepaste fysica  •  Klas: 5BCW  •  Leerplan: III-BCSW-d (juni 2024)  •  Lesmateriaal: Labocursus Fysica 5BCW (leerlingenversie)
| Opdracht (thuis, individueel) | Installeer Pasco Capstone op je eigen Windows-laptop volgens Bijlage F van de cursus (p. 96). / Waar vind je het programma? https://portal.academicsoftware.com → tabblad 'Software' → zoek 'Pasco' → 'Pasco Capstone' → 'Download Pasco Capstone'. / Hoe installeren? ZIP uitpakken → .exe uitvoeren en stappen volgen → programma één keer starten en afsluiten → in C:\ProgramData\PASCO Scientific het bestand 'ResourceFiles.rc' vervangen door dat uit de ZIP-map (ProgramData is een verborgen map: Beeld → 'Verborgen items' aanvinken). / Bewijs: maak een schermafbeelding van het startscherm van Capstone (met 'Hardware Setup' zichtbaar) en upload ze in de uploadzone 'Capstone geïnstalleerd'. / Mac of geen eigen laptop? Meld dit vooraf; je werkt dan op een schoollaptop (de installatie-opdracht vervalt, de bediening tijdens het labo niet). |
| Deadline | Uiterlijk de dag vóór labo 9 om 23.59 u. |
| Hoe wordt dit geëvalueerd? | Proces: thema 1 'Voorbereiding' (en thema 8 'Zelfstandigheid') van de rubric in Bijlage C. / Geslaagd = schermafbeelding tijdig geüpload en Capstone werkt bij het begin van labo 9 (interface wordt gevonden via Bluetooth of USB-kabel). / Niet geïnstalleerd zonder melding = niveau 'onvoldoende' voor thema 1 bij labo 9. |
| Leerplandoelen | LPD 3 S: labotechnieken en ICT-hulpmiddelen (sensoren, meetsoftware) correct gebruiken. / LPD 7 F (voorbereiding op het inductielabo). |
| Lesdoelen | De leerling kan Pasco Capstone installeren, de PASCO 550-interface verbinden (Bluetooth of USB) en de spanningssensor configureren. / De leerling kan een U(t)-meting opnemen en een schermafbeelding maken. |
| Vragen of problemen? | Stel ze tijdens de les fysica, tijdens een andere les of via een bericht op Smartschool – zodra je vastloopt, niet pas de avond vóór het labo. Veelvoorkomende oplossingen: Bijlage F, kader 'Problemen oplossen'. |

---

# Evaluatiefiche – Verslag labo 9: Elektromagnetische inductie: fluxverandering als oorzaak van spanning
Vak: Toegepaste fysica  •  Klas: 5BCW  •  Leerplan: III-BCSW-d (juni 2024)  •  Lesmateriaal: Labocursus Fysica 5BCW (leerlingenversie)
| Opdracht (groepswerk) | Maak het verslag in het Excel-verslagsjabloon van Smartschool ('nummer labo TF titel (namen) 5BCW') – geen eigen Word/Google-document. / Voeg voor proef 3-4 een Word/PDF toe met alle Capstone-schermafbeeldingen, elk met titel en uitleg (Faraday/Lenz). / Inhoud volgens Bijlage A (checklist, p. 86): omschrijving, SMART-onderzoeksvraag, hypothese, schema/foto, tabel, berekeningen, grafiek, besluit + reflectievragen. |
| Product van dit labo | volledige waarnemingstabellen met verklaringen, schermafbeeldingen met uitleg (duidelijke titels, pieken benoemd), antwoord op de onderzoeksvraag met Faraday en Lenz, vergelijking meettoestellen, toepassing. |
| Deadline en indienen | Uiterlijk één week na het labo, 's avonds vóór de les van de volgende week om 23.59 u, in de uploadzone van Toegepaste fysica. Eén upload per groep, alle namen in bestandsnaam en kopblok. Te laat of niet in het juiste formaat: aftrek volgens de vakafspraken. |
| Hoe wordt dit geëvalueerd? (60 % van het practicumcijfer, groepspunt) | 1. Verkennen & onderzoeken (/2) – Omschrijving in eigen woorden, SMART-onderzoeksvraag, hypothese met redenering, correct schema/foto. / 2. Onderzoek uitvoeren (/3) – Volledige tabel met grootheden en eenheden, beduidende cijfers, Excel-formules, twee uitgewerkte voorbeeldberekeningen, correcte grafiek (punten, assen, trendlijn). / 3. Concluderen (/3) – Besluit beantwoordt de onderzoeksvraag en koppelt aan theorie; hypothese getoetst; foutenanalyse; reflectievragen in eigen woorden. / 4. Attitude (/2) – Sjabloon correct gebruikt, volledig, op tijd, verzorgd; feedback van vorige verslagen toegepast. / Totaal /10. Feedback in het feedbackblok van het sjabloon (of als commentaar op de PDF). Herwerken één keer mogelijk voor labo 1-5. / Peer-evaluatie: het groepspunt wordt vermenigvuldigd met je peerfactor (Bijlage D). |
| Leerplandoelen | LPD 7 F: elektromagnetische inductie analyseren en kwantificeren; wet van Faraday en Lenz; opwekken van wisselspanning. / LPD 1 S, 3 S: onderzoek met sensoren, ICT-verwerking. LPD 5 S: toepassingen. |
| Lesdoelen die geëvalueerd worden | De leerling kan aantonen dat een spanning geïnduceerd wordt in een spoel enkel wanneer de magnetische flux door de spoel verandert. / De leerling kan de invloed van snelheid van de beweging, sterkte van de magneet, aantal windingen en zin van de beweging/polariteit op de inductiespanning onderzoeken en koppelen aan de wet van Faraday en de wet van Lenz. / De leerling kan inductie opwekken met een elektromagneet die in- en uitgeschakeld wordt (flux verandert zonder beweging). / De leerling kan een Pasco Voltage Sensor en Capstone correct gebruiken om snelle spanningspieken te registreren, en schermafbeeldingen correct interpreteren en annoteren. / De leerling kan toepassingen van inductie (generator, dynamo, inductiekookplaat, detectielus, draadloos laden) verklaren. |
| Hulp | Screencast Excel-sjabloon op Smartschool; Bijlage A (p. 86) en B (p. 86); afspraken groepswerk en OneDrive: cursus 1.4. Vragen via Smartschool-bericht of tijdens de les. |

---

# Evaluatiefiche – Voorbereiding labo 4: Schakelen van weerstanden: serie, parallel en gemengd
Vak: Toegepaste fysica  •  Klas: 5BCW  •  Leerplan: III-BCSW-d (juni 2024)  •  Lesmateriaal: Labocursus Fysica 5BCW (leerlingenversie)
| Opdracht (thuis, individueel) | Beantwoord de oriëntatievragen van labo 4 (p. 33) schriftelijk op het werkblad. / Doorloop de voorkennis-check (p. 33) en herhaal wat nodig is. / Maak de SMART-oefening (onderzoeksvraag kiezen/formuleren) op het werkblad. / Bereken vooraf de substitutieweerstand van schakelingen a-f (met de beschikbare weerstanden) en vul ze in de tabellen in. |
| Waar vind je ze? | Labocursus p. 33-34 (lesdoelen, voorkennis, O-fase). SMART: p. 3. |
| Deadline | Vóór het begin van het labo (de leerkracht controleert bij de start; wie niet voorbereid is, rekent eerst en krijgt pas daarna materiaal). |
| Hoe wordt dit geëvalueerd? | Formatief + proces: thema 1 'Voorbereiding' en thema 2 'Hypothese en onderzoekend denken' van de proces- en attituderubric (Bijlage C) – niveau 1 / 0,8 / 0,6 / 0,4 / 0,2. / Criteria: alle vragen beantwoord, in eigen woorden, fysisch correct, SMART-oefening met motivering. Berekeningen volledig uitgeschreven. / Modelantwoorden worden na het labo klassikaal besproken; de voorbereiding telt niet als afzonderlijk punt maar weegt mee in het procespunt (40 %). |
| Leerplandoelen | LPD K1: grootheden kwantificeren in serie-, parallel- en gemengde gelijkstroomkringen. / LPD 1 S, 2 S, 3 S: meten, verwerken met juiste eenheden, veilig werken. |
| Lesdoelen die aan bod komen | De leerling kan de substitutieweerstand van serie-, parallel- en gemengde schakelingen berekenen vóór de meting. / De leerling kan een schakeling correct opbouwen vanuit een schema en V- en A-meter juist plaatsen. / De leerling kan de substitutieweerstand experimenteel bepalen via de wet van Ohm uit minstens drie (U, I)-koppels en een U(I)-grafiek. / Een SMART-onderzoeksvraag herkennen/formuleren (leerlijn onderzoeksvragen). |
| Vragen? | Tijdens de les fysica, tijdens een andere les of via een Smartschool-bericht – vóór het labo. |

---

# BIJLAGE C – Voorbeeld "Peer-evaluatie – werkwijze" – letterlijk
# Peer-evaluatie bij groepsopdrachten – werkwijze (Toegepaste fysica 5BCW)
Voor leerlingen (en ouders). Van toepassing bij de labo's die de leerkracht aanduidt (voorzien: labo 6 circuitpracticum, labo 9 inductie, labo 11 open onderzoek).
# 1. Waarom?
Het verslag van een labo is een groepswerk en krijgt één groepspunt. Niet iedereen draagt altijd evenveel bij. Met de peer-evaluatie beoordelen de groepsleden elkaar én zichzelf, zodat het groepspunt eerlijk omgezet wordt in een individueel punt.
# 2. Hoe verdeel je de punten?
Elke leerling krijgt 100 punten per groepslid om te verdelen: 300 punten in een groep van drie, 200 in een groep van twee.
Je verdeelt die punten over jezelf en je groepsleden volgens ieders werkelijke bijdrage aan het labo (voorbereiding, uitvoering, veiligheid, inzet) én aan het verslag (OneDrive, delen afgewerkt, nalezen).
Vind je dat iedereen evenveel deed: iedereen 100. Vind je dat jij zelf minder deed: bv. jezelf 90, de twee anderen elk 105. Vind je dat iemand duidelijk minder deed: bv. 80 voor die persoon, 110 voor de anderen.
Het totaal moet exact 300 (of 200) zijn. Je motiveert elke score met een concreet voorbeeld. Je vult de fiche individueel in; de groepsleden zien elkaars scores niet.
Niet toegelaten: afspreken dat iedereen 100 geeft 'om van af te zijn', of iemand straffen om persoonlijke redenen. De leerkracht toetst de scores aan de eigen observaties.
# 3. Hoe berekent de leerkracht het individuele punt?
Peerfactor van een leerling = (gemiddelde van alle punten die hij/zij kreeg, de eigen score inbegrepen) / 100.
Individueel verslagpunt = groepspunt × peerfactor, afgerond op 0,5 en begrensd op 10/10.
De leerkracht kan de factor begrenzen (bv. tussen 0,7 en 1,2) of bijsturen wanneer de verdeling niet overeenstemt met wat in de klas geobserveerd werd; dat wordt dan met de groep besproken.
# 4. Rekenvoorbeeld (groep van drie, groepspunt 7,5/10)
# 5. Formulier
Labo nr.: ……   Groep: …………………………   Ingevuld door: …………………………………   Datum: ……/……/……
Handtekening leerling: ……………………………   (De leerkracht bewaart dit formulier vertrouwelijk.)
|  | Punten van An | Punten van Bram | Punten van Chloé | Gemiddeld → factor | Individueel punt |
| aan An | 100 | 110 | 110 | 106,7 → 1,07 | 7,5 × 1,07 = 8,0 |
| aan Bram | 100 | 90 | 80 | 90 → 0,90 | 7,5 × 0,90 = 6,5 (6,75 → 6,5) |
| aan Chloé | 100 | 100 | 110 | 103,3 → 1,03 | 7,5 × 1,03 = 7,5 (7,7 → 7,5) |
| totaal gegeven | 300 | 300 | 300 |  |  |
| Groepslid | Punten | Motivatie (concreet: wat deed deze persoon?) |
| Ikzelf: …………………… |  |  |
| …………………… |  |  |
| …………………… |  |  |
| TOTAAL (300 of 200) |  |  |

---

# BIJLAGE D – Voorbeeld slide-voor-slide opbouw van een labopresentatie (labo 7, 18 slides)

Legende: "(1 figuur)" = afbeelding op de slide; ingesprongen regels = tekst zoals op de slide; "[TABEL]" = pptx-tabel; "[NOTITIES]" = sprekersnotities. Formules staan hier als tekstfallback; in de pptx zijn het echte vergelijkingen.

**Slide 1** (1 figuur)
    Labo 7 – Experimentele bepaling van de Lorentzkracht
    Richtduur: 2 lesuren • Type practicum: onderzoekspracticum (per 2-3)
    Mate van sturing: begeleid
    Werkwijze: O – V – U – R
    HAST  •  Toegepaste fysica 5BCW  •  Labocursus volgens de OVUR-methode
    [NOTITIES: LEERKRACHTENINFO: • Stel de blauwe bron vooraf in stroombegrenzing (max. 5 A) en laat de leerlingen enkel de stroomknop bedienen. • Verwachte resultaten: Δm van ca. 0,05-0,5 g; F(I) rechte door de oorsprong; F(l) rechte met klein positief snijpunt (randeffect). B ≈ 0,05-0,2 T afhankelijk van het magneetjuk; beide methodes binnen ~10 %. • Veelgemaakte fout: Δm in gram laten staan → F een factor 100]

**Slide 2**
    LESDOELEN – na dit labo kan je …
    • De grootte van magnetische kracht op stroomvoerende geleider meten via massaverschil op balans (F = Δm·g)
    • Het verband tussen F en stroomsterkte I en tussen F en lengte l van geleider experimenteel bepalen en grafisch voorstellen
    • Uit grafieken afleiden dat F ~ I en F ~ l bij dezelfde magneet (B constant), formule F = B·I·l formuleren en magnetische veldsterkte B van onze magneet bepalen uit richtingscoëfficiënt
    • De derde wet van Newton (actie en reactie – zie uitleg) gebruiken om te verklaren waarom balans massaverschil aangeeft
    LEERPLANDOELEN (III-BCSW-d / III-BCW-d)
    • LPD 6 F: magnetische kracht op stroomvoerende rechte geleider kwantificeren (F = B·I·l·sin α)
    • LPD 1 S: verbanden onderzoeken, hypothese toetsen
    – LPD 2 S: eenheden (tesla, N, g→kg)
    – LPD 4 S: modelleren

**Slide 3**
    VOORKENNIS – check vóór je begint
    • Zwaartekracht F = m·g met g = 9,81 m/s²
    • Richting van de Lorentzkracht (labo 6, deel 5)
    • Recht evenredig verband herkennen in grafiek

**Slide 4**
    O – ORIËNTEREN
    Wat gaan we onderzoeken en waarom?
    Context – onderzoeksvraag – doel – oriëntatievragen (voorbereid thuis) – SMART-oefening

**Slide 5**
    Context
    • In labo 6 zag je dat stroomvoerende geleider in magnetisch veld kracht ondervindt
    – Nu meten we hoe groot die kracht is
    – Magneet oefent kracht uit op geleider, maar geleider oefent dan ook even grote, tegengestelde kracht uit op magneet (derde wet van Newton, zie kader)
    – Zetten we magneet op elektronische balans, dan lezen we massaverschil af waaruit we kracht berekenen
    – Deze kracht doet elke elektromotor draaien
    – We beschikken over één magneet: magnetische veldsterkte (fluxdichtheid) B blijft in dit hele labo dezelfde en kunnen we dus niet variëren – wel bepalen

**Slide 6**
    Onderzoeksvraag (leerlijn SMART – stap 2: jij kiest)
    Je krijgt onderzoeksvraag van dit labo niet meer kant-en-klaar
    – Hieronder staan vier voorstellen; slechts één is goede SMART-onderzoeksvraag voor dit labo
    – Omcirkel ze – dat wordt jullie onderzoeksvraag
    • A. Hoe hangt de Lorentzkracht af van magnetische inductie B van magneet?
    • B. Hoe hangt kracht af van lengte van geleider?
    • C. Waarom draait elektromotor?
    • D. Hoe hangt de Lorentzkracht op geleider (bepaald uit Δm op balans) af van stroomsterkte (0 tot 4 A, bij vaste lengte) en van horizontale lengte van geleider (1,2 tot 8,4 cm, bij I = 3,0 A), telkens bij dezelfde magneet, tijdens dit labo?
    Verantwoord per letter waarom jouw keuze SMART is, en schrijf bij elk ander voorstel in één zin welke letter ontbreekt (of waarom het niet over juiste onderwerp gaat)
    Onderzoeksvraag (leerlijn SMART – stap 2: jij kiest) – invullen op werkblad; kolommen: Mijn keuze | S | M | A | R | T
    [NOTITIES: Modelantwoord – SMART-keuze 7…: D. A: niet realistisch – we hebben één magneet, B kunnen we niet variëren. B: lijkt goed, maar welke kracht, hoe gemeten, wat blijft constant? (niet S/M). C: geen verband tussen grootheden. Verantwoording D: S = F vs. I (bij vaste l) en F vs. l (bij vaste I), telkens B constant – twee deelonderzoeken, elk met één variabele; M = Δm op de balans → F = Δm·g; A = basis ]

**Slide 7**
    O – Oriënteren
    Doel van het onderzoek
    • Twee verbanden experimenteel bepalen (F(I) bij vaste l en F(l) bij vaste I, telkens met dezelfde magneet) en grafisch verwerken
    • Formule F = B·I·l afleiden en B van onze magneet bepalen
    • Kritisch reflecteren over meetmethode
    Oriëntatievragen (beantwoord vóór het labo)
    1. Teken opstelling: magneet op balans, geleider horizontaal tussen polen
    – Teken B, I en kracht op geleider
    – Welke kracht werkt op magneet (derde wet van Newton, zie kader) en wat doet dat met aflezing van balans?
    2. Welke grootheid moet je constant houden bij onderzoek van F(I)?
    – En bij F(l)?
    [NOTITIES: Modelantwoord – Teken de opstelling: magneet op balans, geleider horizontaal…: Kracht op geleider F = I·l × B (linkerhandregel). Volgens de derde wet van Newton werkt op de magneet een even grote, tegengestelde kracht: wordt de geleider omhoog geduwd, dan wordt de magneet omlaag geduwd → balans leest meer af (en omgekeerd). Modelantwoord – Welke grootheid moet je constant houden bij het onderzoek ]

**Slide 8**
    V – VOORBEREIDEN
    Hoe pakken we het aan?
    Benodigdheden – theorie – veiligheid – hypothese – werkplan

**Slide 9**
    Benodigdheden • Theorie-overzicht
    Benodigdheden
    • Blauwe stroombron (max. 5 A), 2 blauwe kabels, 1 rode kabel, multimeter (A), statief, elektronische balans (0,01 g), magneetjuk met neodymiummagneten, set geleiders met verschillende horizontale lengtes (bv. 1,2 – 2,2 – 3,2 – 4,2 – 6,4 – 8,4 cm), bevestigingsstuk
    Theorie-overzicht
    • Kracht uit massaverschil
    – Als men door geleider met lengte l in magnetisch veld stroom stuurt, ontstaat aantrekkings- of afstotingskracht tussen magneet en geleider
    – Die kracht geeft massaverschil Δm op elektronische balans
    – Bij aantrekking leest balans kleinere massa af, bij afstoting grotere (bij opstelling die in handboek besproken wordt is dit net omgekeerd!)
    – Grootte van de Lorentzkracht volgt uit:
    • Verwachte wet
    – Voor geleider loodrecht op veld verwachten we F ~ I en F ~ l:

**Slide 10**
    Benodigdheden • Theorie-overzicht (vervolg)
    • Grafisch
    – Richtingscoëfficiënt van F(I) bij vaste l is B·l; die van F(l) bij vaste I is B·I
    – B is magnetische veldsterkte (ook fluxdichtheid genoemd, eenheid tesla) van onze magneet: dezelfde in beide delen
    • Derde wet van Newton (actie en reactie)
    – Krachten komen altijd in paren voor: als voorwerp A kracht uitoefent op voorwerp B, dan oefent B tegelijk even grote kracht in tegengestelde zin uit op A
    – Hier: magneet duwt (of trekt) aan geleider met F_L; geleider duwt (of trekt) dus even hard aan magneet
    – Omdat magneet op balans staat, 'weegt' hij daardoor iets meer of minder: dat verschil is Δm
    – (De wetten van Newton zie je volledig in zesde jaar.)

**Slide 11**
    VEILIGHEID // NAUWKEURIGHEID • Hypothese
    VEILIGHEID // NAUWKEURIGHEID
    • Mag stroomsterkte NOOIT groter zijn dan 5 A (grens van geleiders en blauwe bron)
    – Schakel stroom enkel in tijdens aflezen (geleider wordt warm)
    • Balans tarreren (= op nul zetten met knop 'TARE'/'0') met magneet erop en stroom uit; zo lees je rechtstreeks Δm af
    – Niet op tafel leunen tijdens meting (trillingen)
    • Neodymiummagneten: knelgevaar en weg van elektronica en bankkaarten
    – Geleider mag magneet niet raken
    Hypothese
    • Formuleer vóór proef beredeneerde verwachting: wat verwacht je en waarom?
    Hypothese mag fout blijken – dat is geen slecht resultaat, maar leerpunt
    – Noteer ze op werkblad

**Slide 12**
    V – Voorbereiden
    Werkplan
    • Stellen meetplan zelf op (zie kader)
    – Verwerking: tabellen → F berekenen → twee grafieken met trendlijn door oorsprong → B bepalen
    STEM-ONTWERPOPDRACHT (LPD 4 S) – stel zelf het meetplan op
    • Deel 1 – F(I): welke geleider kies je en waarom?
    – Welk bereik van I (max. 5 A!) en welke stapgrootte?
    – Hoeveel meetpunten heb je min. nodig voor betrouwbare rechte?
    – Herhaal je metingen?
    • Deel 2 – F(l): welke vaste I kies je (groot genoeg voor meetbare Δm, veilig)?
    – Welke lengtes?
    • Noteer je plan hieronder en laat goedkeuren
    – Vul → tabellen in met jóuw gekozen waarden

**Slide 13**
    U – UITVOEREN
    Meten, noteren, observeren – volgens plan
    Noteer alles meteen op het werkblad: tabellen, waarnemingen, foto's

**Slide 14** (1 figuur)
    U – Uitvoeren
    Opstelling (stroombalans): magneetjuk staat op balans, geleider hangt horizontaal tussen polen en wordt gevoed door stroombron (ampèremeter op bron aflezen)
    – Balans meet reactiekracht op magneet; druk eerst TARE
    Tabel 1 – Verband tussen stroomsterkte en Lorentzkracht (l = …… m, m₀ = …… g)
    Invullen op werkblad; kolommen: I (A) | m (g) | Δm (kg) | F_L = Δm·g (N)
    Tabel 2 – Verband tussen lengte van de geleider en Lorentzkracht (I = …… A)
    Invullen op werkblad; kolommen: l (m) | m (g) | Δm (kg) | F_L (N)
    Grafische STEM-opdracht
    • Grafiek 1: F_L (y) i.f.v. I (x)
    – Grafiek 2: F_L (y) i.f.v. l (x)
    – Trendlijn door oorsprong, vergelijking noteren
    Opstelling (stroombalans): het magneetjuk staat op de balans, de geleider hangt horizontaal tussen de polen en wordt gevoed door de stroombron (ampèremeter op de bron aflezen). De balans meet de reactiekracht op de magneet; druk eerst TARE.

**Slide 15**
    R – REFLECTEREN
    Kloppen de resultaten? Wat leren we eruit?
    Besluit – foutenanalyse – reflectievragen – verslag en evaluatie

**Slide 16**
    Besluit • Foutenanalyse en betrouwbaarheid
    Besluit
    • Beantwoord onderzoeksvraag, onderbouwd met je metingen (getallen, grafiek)
    • Klopt je hypothese?
    – Leg uit
    Foutenanalyse en betrouwbaarheid
    • Wat is grootste meetonzekerheid in dit labo?
    • Hoe zou je proef verbeteren (meer herhalingen, ander meetbereik, betere opstelling)?

**Slide 17**
    Reflectievragen
    1. Leid uit beide verbanden formule af voor de Lorentzkracht op stroomvoerende geleider
    – Eén factor hebben we niet onderzocht (hoek tussen I en B): hoe zit die in volledige formule en hoe zou je die experimenteel onderzoeken?
    2. Komen twee waarden van B overeen?
    – Welke meting (Δm, I of l) draagt meest bij tot onzekerheid?
    – Hoe nauwkeurig is 'l' eigenlijk gedefinieerd (randeffecten van veld)?
    3. Waarom moest je stroom enkel kort inschakelen?
    – Welk effect heeft opwarming op je meting (denk aan temperatuurafhankelijkheid van weerstand van metaal)?
    4. Elektromotor bevat spoel met 200 windingen van 5 cm lengte in veld van 0,2 T bij 2 A
    – Bereken kracht op één zijde van spoel
    5. Verklaar met derde wet van Newton (kader bij theorie) waarom kracht op geleider meetbaar is via balans waarop magneet staat
    6. Waarom konden we invloed van B niet onderzoeken?
    – Hoe zou je dat wél kunnen doen (materiaal, werkwijze)?
    [NOTITIES: Modelantwoord – Leid uit beide verbanden een formule af voor de Lorentzkrach…: F ~ I en F ~ l → F = B·I·l, met B de evenredigheidsconstante (magnetische veldsterkte, T). Volledige formule: F = B·I·l·sin α, met α de hoek tussen I en B; onderzoek door de geleider te draaien t.o.v. het veld (hoekverdeelschijf) en F(α) uit te zetten tegen sin α. Modelantwoord – Komen de twee waarden van B overeen? Wel]

**Slide 18**
    WAT, HOE EN WANNEER WORDT GEËVALUEERD IN DIT LABO?
    • PRODUCT (60 %) – wat: twee complete tabellen met correcte eenheden (g→kg!), twee grafieken met trendlijn, afleiding van F = B·I·l, bepaling van B met vergelijking van beide methodes, foutenanalyse, reflectie
    • PRODUCT – hoe en wanneer: puntenverdeling /10 (Bijlage B), groepspunt, feedback in feedbackblok; deadline = één week na labo, 23.59 u, Smartschool-uploadzone
    • PRODUCT – wat dien je in: Excel-verslagsjabloon (twee tabellen, twee grafieken, bepaling van B)
    • PROCES & ATTITUDE (40 %) – wat: I ≤ 5 A gerespecteerd en stroom kort ingeschakeld, balans correct getarreerd, geduldig en nauwkeurig afgelezen, samenwerking
    • PROCES & ATTITUDE – hoe: observatie door leerkracht met rubric van Bijlage C (10 thema's × 5 niveaus), individueel punt
    • PEER-EVALUATIE: niet voorzien bij dit labo (tenzij leerkracht dit aankondigt)

