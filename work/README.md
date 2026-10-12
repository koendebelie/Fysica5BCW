# Labocursus Toegepaste fysica 6BCW — fase 1

Deze map bevat bronkaart, generator, antwoorden, figuren, PDF-renderer en technische tests. **Wijzig werkbladen in de Python-bronnen en genereer opnieuw**, niet rechtstreeks in het DOCX. De inhoud is een didactische herwerking; voor resterende bronvergelijking zie `bronaftekening.md` en het eindrapport.

## Resultaten (in de repositoryhoofdmap)

- `Labocursus_6BCW_LEERLING.docx` en `.pdf` — 16 werkbladen en Bijlagen A–F;
- `Labocursus_6BCW_LEERKRACHT.docx` en `.pdf` — dezelfde invulvakken, met aanvullend rode modelantwoorden en leerkrachtnotities;
- `Bronpractica_6BCW_LEERLING.docx` en `.pdf` / `Bronpractica_6BCW_LEERKRACHT.docx` en `.pdf` — **26 zelfstandige bronpracticumbladen** met eigen OVUR, materiaal, meettabel, grafieken en besluiten. Gebruik deze afzonderlijk afdrukbare bladen wanneer je de oorspronkelijke proef als losse les uitvoert; de 16-labocursus levert de doorlopende leerlijn en bijlagen.
- `Bestellijst_nieuw_materiaal_6BCW.docx` en `.pdf` — te verifiëren raming;
- `Eindrapport_6BCW_fase1.md` — besluit, controle en open punten.

## Herbouw

Vanuit de repositoryhoofdmap, Python 3.11+:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r work/requirements.txt
python3 work/schems.py     # eigen schema's opnieuw tekenen
python3 work/build.py
python3 work/build.py --teacher
python3 work/build.py --source-worksheets
python3 work/build.py --source-worksheets --teacher
python3 work/render_pdf.py Labocursus_6BCW_LEERLING.docx
python3 work/render_pdf.py Labocursus_6BCW_LEERKRACHT.docx
python3 work/render_pdf.py Bronpractica_6BCW_LEERLING.docx
python3 work/render_pdf.py Bronpractica_6BCW_LEERKRACHT.docx
python3 work/render_pdf.py Bestellijst_nieuw_materiaal_6BCW.docx
python3 work/controle.py
python3 work/package.py      # ververs de download-ZIP pas na de inhoudelijke controle
```

`build.py` regenereert bij de eerste aanroep ook de bestellijst. Met `--source-worksheets` maakt dezelfde generator de bronproeven als zelfstandige werkbladen uit `source_sheets.py`; zonder die vlag bouwt hij de thematische cursus. `labs.py` bevat alleen leerlingvragen en werkplangegevens; **de brongetrouwe correcties staan onderaan dit bestand** (proefopstellingen, ingevulde originele meetstippen en t′-kolommen). `answers.py` bevat alle modelantwoorden en leerkrachtinhoud. `deel1.py` bevat de inleiding, `rubric_data.py` de letterlijk uit de 5BCW-referentiecursus overgenomen 10×5-rubric, `kit.py`/`omml.py` de Word- en OMML-hulpen. `schems.py` genereert de eigen schema's in `figs/`. `render_pdf.py` gebruikt Mammoth + xhtml2pdf en het meegeleverde DejaVu-lettertype (`fonts/LICENSE.txt`); Word-pagina-einden en typografie zijn **niet pixelidentiek** aan de PDF-leesversies. OfficeMath blijft in de DOCX als echte OMML; voor de PDF worden leesbare tekstequivalenten ingevoegd. De Word-inhoudsopgave is een veld: open in Word en werk het veld in zijn geheel bij (F9) vóór de definitieve druk.

## Bron en bewaking

- `bronoverzicht.md` groepeert de ongeordende 118 PDF-pagina's thematisch;
- `theorie_index.md` geeft de volgorde en hoofdstukken van de 17 theorie-PDF's;
- `bronaftekening.md` koppelt elke bronproef aan een labo, documenteert de gerichte tekst- en protocolaudit van de eigen practica en benoemt **niet-afgevinkte** detailvergelijkingen;
- `broninventaris.md` is de pagina-voor-pagina lijst; `figs/bron_manifest.tsv` inventariseert ingesloten rasterobjecten;
- `controle.py` test structurele eisen (16 koppen, 16 OMML, afbeeldingen, antwoordisolatie, PDF-uitvoer), niet de juistheid van elke bronzin.

De theorie-PDF's staan in `leerstof 6BCW/` op `main` van de GitHub-repository. De DOCX bevat per labo klikbare links naar de betrokken bestanden. Het bronpracticum en het leerplan staan lokaal in dezelfde map. Materiaalprijzen en voorraad zijn schattingen; apps en screenshots moeten vóór klasgebruik gecontroleerd worden.
