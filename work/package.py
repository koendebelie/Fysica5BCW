# -*- coding: utf-8 -*-
"""Maak één overdraagbaar fase-1-pakket na het bouwen en controleren."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT=Path(__file__).resolve().parent.parent
OUTPUT=ROOT/'Fysica6BCW_fase1_download.zip'
REQUIRED=[
 'Labocursus_6BCW_LEERLING.docx','Labocursus_6BCW_LEERLING.pdf',
 'Labocursus_6BCW_LEERKRACHT.docx','Labocursus_6BCW_LEERKRACHT.pdf',
 'Blanco_verslag_6BCW_CONCEPT.xlsx','geluidlab.html',
 'Bestellijst_nieuw_materiaal_6BCW.docx','Bestellijst_nieuw_materiaal_6BCW.pdf',
 'Eindrapport_6BCW_fase1.md',
 'leerstof 6BCW/Labocursus 6BCW voorlopig.pdf',
 'leerstof 6BCW/labocursus ECB tril golven.pdf',
 'leerstof 6BCW/III-BCSW-d_juni_24.pdf',
 'Labocursus_5BCW_LEERLING.docx',  # origineel voor de rubric-reproductiecontrole
]
if __name__=='__main__':
    files=REQUIRED+[str(p.relative_to(ROOT)) for p in (ROOT/'work').rglob('*')
                    if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.log')]
    with ZipFile(OUTPUT,'w',ZIP_DEFLATED,compresslevel=6) as archive:
        for file in files:
            path=ROOT/file
            if not path.is_file(): raise FileNotFoundError(path)
            archive.write(path,file)
    with ZipFile(OUTPUT) as archive:
        assert archive.testzip() is None, 'ZIP is beschadigd'
        print(f'{OUTPUT.name}: {len(archive.namelist())} bestanden, {OUTPUT.stat().st_size} bytes')
