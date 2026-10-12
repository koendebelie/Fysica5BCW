# 6BCW-labocursus · één cursus met 25 OVUR-labo's

De leerling- en leerkrachtenversies zijn verschillende uitgaven van **dezelfde cursus**. Er is geen afzonderlijke bronpracticumbundel. De werkbladen gebruiken de bestaande schoolopstellingen en geven geen bronpagina's of directe theorielinks aan leerlingen.

## Resultaten in de repositoryhoofdmap

- `Labocursus_6BCW_LEERLING.docx` / `.pdf` — 25 zelfstandige labo's en Bijlagen A–G.
- `Labocursus_6BCW_LEERKRACHT.docx` / `.pdf` — dezelfde proeven/invulvakken plus rode modelantwoorden.
- `Blanco_verslag_6BCW_CONCEPT.xlsx` — **voorlopig invulbaar verslag, géén letterlijke 5BCW-kopie**. De oorspronkelijke lege 5BCW-Exceltemplate staat volgens de referentiecursus op Smartschool, maar was niet meegeleverd. Vervang dit concept na ontvangst.
- `geluidlab.html` — zelfstandig, offline geluidshulpmiddel voor labo 20. Open lokaal in een browser; test geluid op de schoollaptop met laag volume.
- `Bestellijst_nieuw_materiaal_6BCW.docx` / `.pdf` — indicatieve checklist; voorraad/prijzen niet bevestigd.
- `Eindrapport_6BCW_fase1.md`, `work/leerplan_dekking_stem.md`, `work/bronaftekening.md`, `work/bronaftekening_ecb.md` — wijzigingen in beproefde practica, open controlepunten en brontraceerbaarheid (niet voor leerlingen).

## Herbouw vanuit de repositoryhoofdmap (Python 3.11+)

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r work/requirements.txt
python3 work/schems.py                    # alleen wanneer schema's gewijzigd zijn
python3 work/blanco_verslag.py
python3 work/build.py                    # leerling + bestellijst
python3 work/build.py --teacher          # leerkracht
python3 work/render_pdf.py Labocursus_6BCW_LEERLING.docx
python3 work/render_pdf.py Labocursus_6BCW_LEERKRACHT.docx
python3 work/render_pdf.py Bestellijst_nieuw_materiaal_6BCW.docx
python3 work/controle.py
python3 work/package.py                  # bouw ZIP pas na controle
```

`course_intro.py` verzorgt een titelpagina, inhoudsopgave en zes inleidende hoofdstukken naar het didactische model van de 5BCW-cursus. `course_guidance.py` geeft elk van de 25 labo’s een eigen context, twee voorkennisvragen met docentantwoorden, concrete leerdoelen, begrippen, een toepassing, alleen voor de leerkracht een volledige SMART-voorbeeldvraag en (waar zinvol) bewerkbare OfficeMath met een PDF-equivalent. `course_sheets.py` bepaalt de 25 afzonderlijke OVUR-bladen en de SMART-leerlijn: labo 1 krijgt een volledig voorbeeld; labo 2 kiest uit vier vragen; vanaf labo 3 formuleren leerlingen zelfstandig. `goal_evidence.py` legt voor alle 100 lesdoelen het concrete beoordelingsbewijs vast. `learning_targets.py` vertaalt het 80-pagina-leerplan naar per-blad correcte F-/STEM-LPD, vier toetsbare lesdoelen, doelcheck en formatieve tussenstop; `review_data.py` bevat de extra per-deelproef-reflecties met docentantwoorden en de 25 specifieke in te dienen productbewijzen; `labs.py` bewaart de opstellingen, tabelkolommen en stappen, inclusief brongetrouwe protocollen en gerichte verbeteringen onderaan; `answers.py` geeft de docentsleutels. `rubric_data.py` bevat de **ongewijzigde** 5BCW-proces-/attituderubric. `build.py` voegt de gemeenschappelijke bijlagen toe; `kit.py` levert de Word-opmaak. `blanco_verslag.py` regenereert het als concept gemarkeerde spreadsheet. Bewerk eerst de Python-bron en regenereer alle uitgaven; corrigeer niet alleen één DOCX.

`render_pdf.py` gebruikt Mammoth/xhtml2pdf en het ingesloten DejaVu-lettertype. PDF- en Word-paginering hoeven niet precies overeen te komen. `controle.py` test 25 koppen, vier lesdoelen + 100 concrete bewijscriteria en doelcheck per blad, doelbewijs voor STEM 1–6 en precies één O/V/U/R-cyclus per blad, alle meettabelrijen/antwoordsets en de 25 werkelijk ingebedde passende figuren, 22 echte OfficeMath-formules én hun PDF-equivalenten, gescheiden antwoorden, alle t′/v-kolomparen, het onveranderde 5BCW-rubric, PDF-inhoud en het gemarkeerde spreadsheet; dit is **geen inhoudelijke aftekening** van de volledige 118 pagina’s of de daadwerkelijke schoolvoorraad. De evaluatie volgt de 5BCW-verhouding (60% groepsproduct, 40% individueel proces; standaard één week, 23.59 u) met concrete per-blad-producten; de leerkracht bevestigt datum, uploadzone en schooltemplate.

Bij labo 25 vereist 6 S (#) bovendien vóór het experiment een goedgekeurd inhoudelijk F-doel en een vastgelegde schoolafspraak over de formele onderzoekscompetentie; de leerkracht tekent dit aan op het werkblad.

`bronaftekening_ecb.md` tekent de acht proeven van de extra GitHub-PDF (18 blz.) afzonderlijk af, waaronder de gerasterde halve-trillingpagina’s. De aanvullende PDF is mee verpakt. `bronaftekening.md` koppelt de proeven aan de voorlopige 6BCW-cursus en documenteert wat is aangepast/geschrapt. `broninventaris.md` en `figs/UITSLUITINGEN.txt` bevatten nog niet gecontroleerde vectorfiguren/uitgesloten foto's. Theorieonderwerpen volgen de PDF-volgorde in `leerstof 6BCW/`, maar de werkbladen geven bewust geen dianummers of externe links.

## Leerplan, beoordeling en beperking

`work/leerplan_dekking_stem.md` documenteert wat in het leerplan daadwerkelijk bij **LPD 1–6 S** en de betrokken Fysica-LPD staat. Labo 07 bevat verplicht een veilig ontwerp–test–bijstuurtraject voor 4 S, labo 20 een onderbouwde maatschappelijke geluidsafweging en dB-rekenstap voor 5 S, labo 25 de zeven aantoonbare fasen van 6 S. Elk van de 25 bladen heeft vier genummerde leerlinglesdoelen met vier eigen bewijscriteria, twee controlepunten, een vier-rijige doelcheck en een docentennotitie voor tussentijdse feedback. Elk groepslid geeft bij labo 07, 20 en 25 een eigen korte onderbouwing; Bijlage B geeft per STEM-doel een beslisregel en gerichte vervolgstap, en Bijlage G wordt per leerling ingevuld. Bijlage B koppelt het doelbewijs aan de bestaande 2+3+3+2 productpunten, Bijlage C blijft letterlijk de 5BCW-procesrubric en Bijlage G is een STEM-doelkaart met status en feedforward **zonder extra bonuspunten**. Ook het CONCEPT-spreadsheet bevat een doelkaart als tweede tabblad.

Een aangeboden en beoordeelbare gelegenheid is nog geen garantie dat iedere leerling het doel **behaald** heeft. De leerkracht controleert echte producten/observaties en moet de overige vakgebonden doelen van de volledige studierichting buiten dit fysicabestand aftekenen. De oorspronkelijke school-Exceltemplate, toestelvoorraad en concrete inleverdatum moeten nog door de school worden bevestigd.
