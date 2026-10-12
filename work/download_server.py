# -*- coding: utf-8 -*-
"""Eenvoudige afgeschermde downloadpagina voor de 6BCW-oplevering."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote, unquote, urlparse
import html
import mimetypes
import os

ROOT = Path(__file__).resolve().parent.parent
FILES = [
    ('Alles in één ZIP-pakket', 'Fysica6BCW_fase1_download.zip', 'Alles: cursussen, bestellijst, verslag, scripts en gebruikte bron-PDF’s'),
    ('Leerlingencursus · DOCX', 'Labocursus_6BCW_LEERLING.docx', 'Bewerkbaar Word-bestand'),
    ('Leerlingencursus · PDF', 'Labocursus_6BCW_LEERLING.pdf', 'PDF-leesversie'),
    ('Leerkrachtencursus · DOCX', 'Labocursus_6BCW_LEERKRACHT.docx', 'Met rode modelantwoorden'),
    ('Leerkrachtencursus · PDF', 'Labocursus_6BCW_LEERKRACHT.pdf', 'PDF-leesversie'),
    ('Bestellijst · DOCX', 'Bestellijst_nieuw_materiaal_6BCW.docx', 'Bewerkbare voorraad- en budgetcheck'),
    ('Bestellijst · PDF', 'Bestellijst_nieuw_materiaal_6BCW.pdf', 'PDF-leesversie'),
    ('Eindrapport', 'Eindrapport_6BCW_fase1.md', 'Controle en resterende open punten'),
]
ALLOWED = {name for _, name, _ in FILES}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        if path == '/':
            cards = ''.join(
                '<a class="card" href="/download/'+quote(name)+'" download="'+html.escape(name,quote=True)+'">'
                '<span class="icon">'+('⬇' if name.endswith('.zip') else '↧')+'</span>'
                '<span class="copy"><strong>'+html.escape(title)+'</strong><small>'+html.escape(desc)+'</small></span>'
                '<span class="action">Downloaden →</span></a>'
                for title,name,desc in FILES if (ROOT/name).is_file()
            )
            page = '''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>6BCW · Downloads</title><style>
            :root{font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:#1e3040;background:#f1f5f9}
            *{box-sizing:border-box}body{margin:0}main{max-width:860px;margin:0 auto;padding:48px 20px 90px}
            .eyebrow{color:#256c58;font-size:13px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}h1{color:#173b61;margin:12px 0;font-size:clamp(30px,5vw,46px);line-height:1.13}
            .intro{max-width:720px;color:#526477;font-size:17px;line-height:1.6;margin:0 0 34px}.notice{background:#fff5df;border-left:4px solid #cd8f22;padding:14px 18px;margin:22px 0 30px;border-radius:6px;line-height:1.5}
            h2{font-size:18px;margin:32px 0 14px}.grid{display:grid;gap:10px}.card{display:flex;align-items:center;gap:16px;padding:17px 19px;background:#fff;border:1px solid #dae3eb;border-radius:11px;text-decoration:none;color:#20384e;box-shadow:0 2px 9px #19354c0a}.card:hover,.card:focus-visible{border-color:#1c7658;box-shadow:0 4px 14px #19354c20;outline:none}.icon{display:grid;place-items:center;flex:none;width:42px;height:42px;border-radius:10px;background:#e9f5ee;color:#16745b;font-size:23px}.copy{display:grid;gap:3px}.copy strong{font-size:15px}.copy small{font-size:13px;color:#637488}.action{margin-left:auto;white-space:nowrap;font-size:13px;font-weight:700;color:#176d51}@media(max-width:560px){.action{display:none}main{padding-top:28px}}
            </style></head><body><main><div class="eyebrow">HAST · Toegepaste fysica 6BCW</div><h1>Download je cursusbestanden</h1><p class="intro">Kies het complete ZIP-pakket of download ieder bestand apart. Een klik start de download direct in je browser.</p><div class="notice"><strong>Let op:</strong> dit is de conceptversie voor de vakgroep. De letterlijke detailcontrole tegen alle bronpagina’s staat nog open; lees het eindrapport vóór klasgebruik.</div><h2>Bestanden</h2><div class="grid">'''+cards+'''</div></main></body></html>'''
            body=page.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type','text/html; charset=utf-8')
            self.send_header('Content-Length',str(len(body)))
            self.end_headers();self.wfile.write(body)
            return
        if path.startswith('/download/'):
            name=unquote(path[len('/download/'):])
            if name in ALLOWED and (ROOT/name).is_file():
                target=ROOT/name
                self.send_response(200)
                self.send_header('Content-Type',mimetypes.guess_type(name)[0] or 'application/octet-stream')
                self.send_header('Content-Disposition',f'attachment; filename="{name}"')
                self.send_header('Content-Length',str(target.stat().st_size))
                self.send_header('Cache-Control','no-store')
                self.end_headers()
                with target.open('rb') as f:
                    while data:=f.read(65536):self.wfile.write(data)
                return
        self.send_error(404,'Bestand niet gevonden')

if __name__=='__main__':
    port=int(os.environ.get('PORT','8765'))
    print(f'Downloadpagina op 0.0.0.0:{port}',flush=True)
    ThreadingHTTPServer(('0.0.0.0',port),Handler).serve_forever()
