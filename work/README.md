# 6BCW-labocursus · één cursus met 25 OVUR-labo's

De leerling- en leerkrachtenversies zijn verschillende uitgaven van **dezelfde cursus**. Er is geen afzonderlijke bronpracticumbundel. De werkbladen gebruiken de bestaande schoolopstellingen en geven geen bronpagina's of directe theorielinks aan leerlingen.

## Resultaten in de repositoryhoofdmap

- `Labocursus_6BCW_LEERLING.docx` / `.pdf` — 25 zelfstandige labo's en Bijlagen A–F.
- `Labocursus_6BCW_LEERKRACHT.docx` / `.pdf` — dezelfde proeven/invulvakken plus rode modelantwoorden.
- `Blanco_verslag_6BCW_CONCEPT.xlsx` — **voorlopig invulbaar verslag, géén letterlijke 5BCW-kopie**. De oorspronkelijke lege 5BCW-Exceltemplate staat volgens de referentiecursus op Smartschool, maar was niet meegeleverd. Vervang dit concept na ontvangst.
- `geluidlab.html` — zelfstandig, offline geluidshulpmiddel voor labo 20. Open lokaal in een browser; test geluid op de schoollaptop met laag volume.
- `Bestellijst_nieuw_materiaal_6BCW.docx` / `.pdf` — indicatieve checklist; voorraad/prijzen niet bevestigd.
- `Eindrapport_6BCW_fase1.md`, `work/bronaftekening.md` — wijzigingen in beproefde practica, open controlepunten en brontraceerbaarheid (niet voor leerlingen).

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

`course_sheets.py` bepaalt de 25 afzonderlijke OVUR-bladen en de SMART-leerlijn: labo 1 krijgt een volledig voorbeeld; labo 2 kiest uit vier vragen; vanaf labo 3 formuleren leerlingen zelfstandig. `labs.py` bewaart de opstellingen, tabelkolommen en stappen, inclusief brongetrouwe protocollen en gerichte verbeteringen onderaan; `answers.py` geeft de docentsleutels. `rubric_data.py` bevat de **ongewijzigde** 5BCW-proces-/attituderubric. `build.py` voegt de gemeenschappelijke bijlagen toe; `kit.py` levert de Word-opmaak. `blanco_verslag.py` regenereert het als concept gemarkeerde spreadsheet. Bewerk eerst de Python-bron en regenereer alle uitgaven; corrigeer niet alleen één DOCX.

`render_pdf.py` gebruikt Mammoth/xhtml2pdf en het ingesloten DejaVu-lettertype. PDF- en Word-paginering hoeven niet precies overeen te komen. `controle.py` test 25 koppen, gescheiden antwoorden, alle t′/v-kolomparen, het onveranderde 5BCW-rubric, PDF-inhoud en het gemarkeerde spreadsheet; dit is **geen inhoudelijke aftekening** van de volledige 118 pagina’s of de daadwerkelijke schoolvoorraad.

`bronaftekening.md` koppelt de proeven aan de voorlopige 6BCW-cursus en documenteert wat is aangepast/geschrapt. `broninventaris.md` en `figs/UITSLUITINGEN.txt` bevatten nog niet gecontroleerde vectorfiguren/uitgesloten foto's. Theorieonderwerpen volgen de PDF-volgorde in `leerstof 6BCW/`, maar de werkbladen geven bewust geen dianummers of externe links.
