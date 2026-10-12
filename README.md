# Labocursus Toegepaste fysica 5BCW – elektrostatica, elektriciteit & elektromagnetisme

Volledig herwerkte labocursus volgens de OVUR-methode (leerplan III-BCSW-d), met leerkrachtenversie, lesfiches, evaluatiefiches, presentaties en de generatorscripts.

## Inhoud
| Map / bestand | Inhoud |
|---|---|
| `Labocursus_5BCW_LEERLING.docx/.pdf` | Leerlingenversie (11 labo's, bijlagen A-F) |
| `Labocursus_5BCW_LEERKRACHT.docx/.pdf` | Leerkrachtenversie met modelantwoorden en leerkrachteninfo |
| `Presentaties/` | 12 PowerPoints (inleiding + 1 per labo), sprekersnotities = modelantwoorden |
| `Lesfiches/` | 20 lesfiches (één per lesuur) |
| `Evaluatiefiches/` | 25 evaluatiefiches (voorbereidingen, verslagen, poster, Capstone-installatie) |
| `Overzicht_evaluatiefiches_en_lesfiches.docx`, `Peer-evaluatie_werkwijze.docx`, `Bestellijst_nieuw_materiaal.docx` | Overzicht, peer-methode (300 punten / peerfactor), bestellijst nieuw materiaal |
| `Masterprompts/` | 4 masterprompts om cursus, fiches/presentaties en verbetering met AI te (her)genereren |
| `work/` | Generatorscripts: `build.py` (cursus, `--teacher`), `answers.py`, `capture.py` → `events.json`, `make_ppt.py`, `docs_extra.py`, `omml.py`; `figs/` figuren |
| `uploads/` | Bronmateriaal (oorspronkelijke cursus, leerplan, voorbeeldwerkblad, Excel-sjabloon, Capstone-handleiding) |

## Opnieuw genereren
```bash
pip install python-docx python-pptx pymupdf pillow pypdf
cd work
python3 build.py && python3 build.py --teacher      # cursussen (docx)
soffice --headless --convert-to pdf --outdir .. ../Labocursus_5BCW_*.docx
python3 capture.py && python3 make_ppt.py            # presentaties
python3 docs_extra.py                                # lesfiches, evaluatiefiches, overzicht, peer, bestellijst
```
