# Eindrapport — OVUR-labocursus Toegepaste fysica 6BCW

**HAST • leerkracht De Belie K. • fase 1 • 12 oktober 2026**

## 1. Opgeleverde bestanden

| Bestand | Inhoud |
|---|---|
| `Labocursus_6BCW_LEERLING.docx` / `.pdf` | Bewerkbaar werkboek en PDF-leesversie: 16 labo's, algemene inleiding en Bijlagen A–F. PDF: 102 blz. |
| `Labocursus_6BCW_LEERKRACHT.docx` / `.pdf` | Dezelfde invulvakken, met daaronder rode modelantwoorden en didactische aanwijzingen. PDF: 116 blz. |
| `Bestellijst_nieuw_materiaal_6BCW.docx` / `.pdf` | Inkoop-/voorraadcheck met indicatieve, **niet geverifieerde** prijzen; PDF: 1 blz. |
| `work/` | Herbouwbare Word-generator (`build.py --teacher`), gescheiden vragen/antwoorden, oorspronkelijke en nieuwe schema's, PDF-renderer, broninventaris, controlescript en handleiding. |

Dit is een **bruikbare conceptversie voor vakgroepfeedback, niet een afgetekende letterlijke reproductie** van het volledige voorlopige practicumpakket. Zie §4 voor de nog open oplevervoorwaarde.

## 2. Opbouw en didactische keuzes

De 16 werkbladen volgen de theorievolgorde: 1 ERB (luchtbel/wagentje), 2 EVRB en vertragen, 3 vrije val en verticale worp, 4 horizontale worp en parabool, 5 Newton/resultante, 6 arbeid, 7 krachtmoment/hefbomen als **verdieping**, 8 ECB/centripetale kracht, 9 massa-veer, 10 slinger, 11 resonantie, 12 golfbak/staande golven, 13 geluid/Doppler, 14 rooster/CD/spectra, 15 breking en 16 open onderzoek met poster. De dubbele bronbladen over vrije val en verticale worp zijn samengevoegd; de bestaande proeven zijn thematisch terug te vinden via `work/bronaftekening.md`. Elke proef heeft minimaal één schema of bronfiguur, een STEM-ontwerpopdracht, OVUR-fasen, leerplandoelen, materiaal, veiligheid, meettabel, verwerking en reflectie. De relevante theorie-PDF's zijn met bestandsnaam en klikbare GitHub-link vermeld.

Labo 1 laat de leerling bij SMART **stap 2** de beste vraag kiezen en verantwoorden; labo's 2–16 laten een eigen vraag formuleren (**stap 3**). De onderzoeksvrijheid loopt op naar labo 16: eigen vraag, controle van variabelen/risico's, ruwe data en wetenschappelijke A3-poster. Product/proces telt **60/40**; de productverdeling staat in Bijlage B en de individuele proces- en attituderubric in Bijlage C. De rubric heeft 10 thema's en 5 niveaus en is cel voor cel gelijk aan de overeenkomstige tabel uit de 5BCW-referentiecursus (66/66 cellen). Beperkte peer-evaluatie is voorzien bij labo 5, 10 en 14; individuele zelfreflectie na labo 2, 6, 9 en 16. Er zijn geen presentaties, lesfiches of evaluatiefiches aangemaakt.

## 3. Technische en visuele controle

`PYTHONPATH=work python3 work/controle.py` is uitgevoerd op de uiteindelijke documenten. Beide DOCX'en hebben 16 labo-koppen als echte Word-kopstijl, 16 OfficeMath/OMML-formules en 22 afbeeldingen; de leerlingenversie heeft 507 tabellen, de leerkrachtenversie 741 (extra antwoord-/notitiekaders). De invulvakken staan nu **ook in de leerkrachtenversie**. Het leerlingenbestand bevat geen modelantwoordlabels. Een steekproef van PDF-pagina's, inclusief de eerste leerling- en leerkrachtpagina en de liggende rubric, is visueel bekeken: figuren, tabellen, antwoorden en invulvakken zijn leesbaar; de rubric staat op twee liggende pagina's. Beide PDF's hebben inhoud op iedere pagina. De PDF's zijn vanuit de DOCX opgebouwd zonder LibreOffice; hun paginering en typografie zijn **niet exact gelijk** aan Word. De DOCX behoudt echte OMML, de PDF gebruikt leesbare tekstweergaven van dezelfde formules.

**Nog in Word uitvoeren:** de automatische inhoudsopgave bijwerken met F9 → *In zijn geheel bijwerken* vóór drukken. De verwijzingen in de PDF-inhoudslijst zijn titels, geen automatisch berekende paginanummers.

## 4. Open punten vóór definitieve klasuitgave

1. **Bronintegriteit — belangrijkste beperking.** De 118 pagina's van `Labocursus 6BCW voorlopig.pdf` zijn thematisch in kaart gebracht, maar de detailvakjes in `work/broninventaris.md` en `work/bronaftekening.md` blijven terecht **niet afgevinkt**. De nieuwe meettabellen zijn didactisch opnieuw opgebouwd; niet elke originele rij, vraag, vectorfiguur en tabel is letterlijk of beeld-voor-beeld vergeleken/overgenomen. Een volledige letterlijke bronovername is hiermee dus **niet aangetoond**. De vakgroep moet de bron-PDF per pagina naast de nieuwe werkbladen leggen en ontbrekende details in `work/labs.py` en `work/answers.py` verwerken. Bladzijden 43 en 46 bevatten gerasterde tekst: vijf bijbehorende vragen zijn expliciet als bewerkbare tekst in labo 9 verwerkt, maar ook die pagina's vereisen nog eindcontrole.
2. **Afbeeldingen.** Van 25 geïndexeerde rasterobjecten zijn 15 verschillende originele objecten in de cursussen geplaatst; 7 eigen schema's vullen aan. Twee foto's met herkenbare leerlingen zijn om privacyredenen niet opnieuw verdeeld; de onveilige oude CD-dia met krasinstructie is door een veilig schema vervangen. Vier zwarte/onleesbare blokken zijn niet gebruikt en één dubbele grafiek is slechts eenmaal opgenomen. Rasterpagina's 43/46 blijven als broncontrole-assets, niet als cursusfoto. **Vectorfiguren en lijntekeningen zijn niet volledig figuur-voor-figuur gereconstrueerd.** Zie `work/figs/UITSLUITINGEN.txt`.
3. **Materiaal en veiligheid.** Controleer effectief aanwezige tijdtikkers en veilige laagspanningsvoedingen, roosters (80/100/300/600 lijnen per mm), opvang/stootblokken, golfbak, regelbare resonantieset, laserklasse en scherm, eventuele kwikdamplamp en afsluitbare speldenbak. Beperk of vervang kwiklamp en laseropstelling volgens lokaal schoolbeleid. De bestellijst vermeldt richtprijzen, geen leveranciersoffertes of bevestigde voorraad. Laat de opstelling van het open onderzoek vooraf expliciet goedkeuren.
4. **Digitale bronnen.** De historische Soundry-/Doppler-/golfbakapps en de 6BCW Excel-sjabloon-/screencastlocatie moeten lokaal getest of vervangen worden. Voor Tracker staat een startgids in Bijlage F, maar **geen echte lokale schermafbeeldingen**: voeg die met licentie-/privacycontrole toe als de vakgroep die verlangt.
5. **Leerplan en lokaal beleid.** Labo 7 (moment/hefbomen) is behouden als verdieping zonder afzonderlijk LPD 12–23 F; laat de leerkracht de inzet en beschikbare lestijd bevestigen. De rubric is bewust letterlijk uit 5BCW overgenomen; één criterium noemt daarom elektrische A-/V-meters en AC/DC, wat niet bij elk 6BCW-labo past. Wijzig de rubric alleen na expliciete vakgroepbeslissing. Controleer de geldende inleverzone, deadlines en posterafspraken.

## 5. Herbouw en feedbackronde

Installeer de dependencies in `work/requirements.txt` en voer de commando's in `work/README.md` uit. Wijzig vragen/meetprotocollen in `labs.py`, de leerkrachtantwoorden in `answers.py`, gedeelde opmaak in `kit.py` of `build.py`, en start de generator opnieuw met en zonder `--teacher`. Wijzig **niet uitsluitend de DOCX**: zo blijven leerling, leerkracht en PDF synchroon. Laat na een inhoudelijke broncontrole nog één proefdruk en praktijktest met de echte toestellen uitvoeren.
