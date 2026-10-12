# -*- coding: utf-8 -*-
"""Broninventaris van een labocursus-PDF, per pagina.

Gebruik:
    python3 analyse.py 'Labocursus 6BCW voorlopig.pdf' --output inventaris.md

Het script telt zowel ingesloten afbeeldingen als vectorfiguren. Vectorfiguren zijn
moeilijk automatisch te onderscheiden van tabellen en kaders: de pagina blijft dus
altijd visueel te controleren. Figuren worden NIET zonder controle gekopieerd.
"""
import argparse
import os
import re
from collections import defaultdict

try:
    import pymupdf as fitz
except ImportError:
    import fitz


def _clean(t):
    return re.sub(r"\s+", " ", t).strip()


def inventariseer(pdf, out):
    doc = fitz.open(pdf)
    lines = []
    lines.append("# Broninventaris: %s" % os.path.basename(pdf))
    lines.append("")
    lines.append("Pagina's: %d. Controleer handmatig welke pagina's samen één labo vormen. "
                 "Vink pas af na vergelijking met de nieuwe werkbladen.\n" % len(doc))
    lines.append("| Pagina | Labo/kop (eerste regels) | Beeldblokken | Vectorpaden | Tabelkandidaten | Status |")
    lines.append("|---:|---|---:|---:|---:|---|")
    details = []
    for i, page in enumerate(doc, 1):
        text = page.get_text("text")
        ln = [re.sub(r"\s+", " ", x).strip() for x in text.splitlines() if x.strip()]
        title = " / ".join(ln[:3])[:140].replace("|", "/")
        imgs = page.get_images(full=True)
        drawings = page.get_drawings()
        # find_tables kan bij complexe vectorfiguren ten onrechte tabellen herkennen
        try:
            tables = page.find_tables()
            ntable = len(tables.tables)
        except Exception:
            ntable = -1
        lines.append("| %d | %s | %d | %d | %s | ☐ |" % (
            i, title, len(imgs), len(drawings),
            str(ntable) if ntable >= 0 else "te controleren"))
        details.append((i, title, text, imgs, drawings, ntable))
    lines.extend(["", "## Uitgebreide inventaris per pagina", ""])
    for i, title, text, imgs, drawings, ntable in details:
        lines.append("### Pagina %d – %s" % (i, title))
        lines.append("")
        lines.append("- Afbeeldingen (ingesloten): %d; vectorfiguren/kaders/lijnen: %d; "
                     "herkende tabelkandidaten: %s." % (len(imgs), len(drawings), ntable))
        if imgs:
            for k, im in enumerate(imgs, 1):
                xref, smask, width, height, bpc, colorspace, *_ = im
                lines.append("  - Beeld %d: xref %d; %d × %d px; kleurtype %s; "
                             "nummer/bijschrift handmatig te controleren." % (
                    k, xref, width, height, colorspace))
        lines.append("- Controle: tekst, vragen, figuren, tabellen en data vergelijken met nieuw labo. ☐")
        lines.append("")
        lines.append("```text")
        lines.append(text.strip()[:6000] or "[geen extraheerbare tekst — handmatig bekijken]")
        lines.append("```")
        lines.append("")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return len(doc)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--output", default="inventaris.md")
    args = ap.parse_args()
    print(inventariseer(args.pdf, args.output), "pagina's gelezen →", args.output)
