# -*- coding: utf-8 -*-
"""Voorlopig invulbaar verslag, totdat het echte 5BCW-Excelbestand beschikbaar is.

Geen claim van letterlijke gelijkheid: de 5BCW-cursus verwijst naar een blanco
Excelbestand op Smartschool; dat bestand zelf staat niet in deze repository.
"""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.page import PageMargins
from learning_targets import STEM

OUT=Path(__file__).resolve().parent.parent/'Blanco_verslag_6BCW_CONCEPT.xlsx'
DARK='173859'; BLUE='DDEEF4'; PALE='F2F7FA'
w=Workbook(); s=w.active;s.title='Verslag'
s.sheet_view.showGridLines=False
s.column_dimensions['A'].width=4
for c in 'BCDEFGH':s.column_dimensions[c].width=18
s.column_dimensions['B'].width=24
s.column_dimensions['H'].width=26
s.merge_cells('B2:H2');s['B2']='TOEGEPASTE FYSICA 6BCW · BLANCO VERSLAG (CONCEPT)'
s['B2'].font=Font(size=16,bold=True,color='FFFFFF');s['B2'].fill=PatternFill('solid',fgColor=DARK)
s.row_dimensions[2].height=34
s.merge_cells('B3:H3');s['B3']='Niet identiek aan het originele 5BCW-Excelbestand op Smartschool; vervang zodra dat beschikbaar is.'
s['B3'].font=Font(italic=True,color='9A4B10',size=10)
for row,label in [(5,'Labo en titel'),(6,'Groepsleden / klas'),(7,'Datum en leerkracht')]:
 s.cell(row,2,label).font=Font(bold=True,color=DARK)
 s.merge_cells(start_row=row,start_column=3,end_row=row,end_column=8)
 s.cell(row,3).fill=PatternFill('solid',fgColor=PALE)

def section(row,title):
 s.merge_cells(start_row=row,start_column=2,end_row=row,end_column=8)
 cell=s.cell(row,2,title);cell.fill=PatternFill('solid',fgColor=DARK);cell.font=Font(bold=True,color='FFFFFF',size=11)
 s.row_dimensions[row].height=24

def blank(row,label,lines=2):
 s.cell(row,2,label).font=Font(bold=True,color=DARK)
 s.merge_cells(start_row=row,start_column=3,end_row=row+lines-1,end_column=8)
 cell=s.cell(row,3);cell.fill=PatternFill('solid',fgColor=PALE);cell.alignment=Alignment(vertical='top',wrap_text=True)
 for r in range(row,row+lines):s.row_dimensions[r].height=22

section(9,'1 · VERKENNEN EN ONDERZOEKEN  / 2')
blank(10,'Doel',2);blank(12,'Materiaal',2);blank(14,'Herhaalbare werkwijze',4)
blank(18,'SMART-onderzoeksvraag',3);blank(21,'Hypothese (vooraf)',3);blank(24,'Schema / foto: verwijzing',2)
section(27,'2 · UITVOEREN EN VERWERKEN  / 3')
s.merge_cells('B28:H28');s['B28']='Noteer hieronder ruwe gegevens met eigen grootheidsnamen en eenheden. Kopieer de rijen voor meerdere reeksen.'
s['B28'].alignment=Alignment(wrap_text=True)
for col in range(2,9):
 c=s.cell(29,col);c.fill=PatternFill('solid',fgColor=BLUE);c.font=Font(bold=True,color=DARK)
 c.value=f'grootheid + eenheid {col-1}'
for row in range(30,46):
 for col in range(2,9):
  c=s.cell(row,col);c.border=Border(bottom=Side(style='hair',color='B8CEDA'))
blank(47,'Twee voorbeeldberekeningen per soort',4)
blank(51,'Grafiek(en): punten, assen, eenheden, titel, trendlijn + vergelijking',4)
section(56,'3 · CONCLUDEREN  / 3')
blank(57,'Antwoord op vraag met meetgegevens',4);blank(61,'Theorie en hypothese',3)
blank(64,'Onzekerheden en reflectie',4)
section(69,'4 · ATTITUDE EN VERZORGING (productafspraken)  / 2')
blank(70,'Bestandsvorm en termijn',3)
s['B71']='Aantoonbaar groepsproduct';s['B72']='Feedbackblok behouden';blank(73,'Feedback leerkracht (niet verwijderen)',5)
s.merge_cells('B79:H79');s['B79']='Controle: t′ direct links van v in tijdtikkertabellen; maak een XY-grafiek v(t′).'
s['B79'].font=Font(bold=True,color=DARK)
section(81,'PRODUCTPUNTEN /10 · in te vullen door de leerkracht')
for row,label,maxpunt in [(82,'1. Verkennen & onderzoeken',2),(83,'2. Onderzoek uitvoeren',3),
                            (84,'3. Concluderen',3),(85,'4. Attitude en verzorging (product)',2)]:
 s.cell(row,2,label);s.cell(row,4,maxpunt);s.cell(row,5).fill=PatternFill('solid',fgColor=BLUE)
s['D86']='Totaal /10';s['E86']='=SUM(E82:E85)'
s.merge_cells('B87:H87');s['B87']='Product 60 % (groepspunt); proces/attitude 40 % (individueel volgens Bijlage C).'
s.merge_cells('B88:H88');s['B88']='Indienen via Smartschool: één week na het labo, uiterlijk 23.59 u; concrete datum/zone vooraf door de leerkracht.'
s.freeze_panes='B30'
s.sheet_properties.pageSetUpPr.fitToPage=True
s.page_setup.orientation='landscape';s.page_setup.paperSize=s.PAPERSIZE_A4;s.page_setup.fitToWidth=1;s.page_setup.fitToHeight=3
s.print_options.horizontalCentered=True;s.print_area='B2:H88';s.page_margins=PageMargins(left=.3,right=.3,top=.5,bottom=.5,header=.2,footer=.2)
kaart=w.create_sheet('STEM-doelkaart')
kaart.sheet_view.showGridLines=False
for col,width in {'A':13,'B':55,'C':67,'D':27,'E':26,'F':55}.items():
 kaart.column_dimensions[col].width=width
kaart.merge_cells('A1:F1');kaart['A1']='STEM-DOELKAART 6BCW · bewijs en feedforward (geen extra cijfer)'
kaart['A1'].font=Font(size=14,bold=True,color='FFFFFF')
kaart['A1'].fill=PatternFill('solid',fgColor=DARK)
kaart.append(['Leerplandoel','Wat moet je aantonen?','Verplicht bewijs in deze cursus',
              'Vindplaats','Nog niet / op weg / aangetoond','Feedback + volgende stap'])
verplicht={
 1:'Labo 04/07/15/25: vraag, hypothese, data en besluit.',
 2:'Labo 02/09/21/25: symbolen, SI, meetresolutie, beduidende cijfers en machten van tien.',
 3:'Labo 05/12/21/25: veilige opstelling, betrouwbaar meetbewijs en duurzaam opruimen.',
 4:'Labo 07: twee opvangontwerpen, model, videotoets en hertoets na bijsturing.',
 5:'Labo 20: dB-berekening en twee maatschappelijke perspectieven op geluidsbeperking.',
 6:'Labo 25: zeven fasen, vooraf goedgekeurd inhoudelijk F-LPD en schoolafspraak (#).'
}
for k,betekenis in STEM.items():
 r=k+2
 kaart.cell(r,1,f'{k} S');kaart.cell(r,2,betekenis);kaart.cell(r,3,verplicht[k])
 for col in range(1,7):
  c=kaart.cell(r,col);c.alignment=Alignment(vertical='top',wrap_text=True)
  c.border=Border(bottom=Side(style='thin',color='B8CEDA'))
 kaart.row_dimensions[r].height=60
for c in kaart[2]:
 c.font=Font(bold=True,color=DARK);c.fill=PatternFill('solid',fgColor=BLUE)
 c.alignment=Alignment(wrap_text=True,vertical='top')
kaart.row_dimensions[2].height=32
kaart.merge_cells('A12:F12')
kaart['A12']='Kopieer deze doelkaart per leerling. Noteer naam: ……………  ·  De status volgt uit groepsproduct én individuele uitleg/observatie.'
kaart['A12'].alignment=Alignment(wrap_text=True)
kaart.row_dimensions[12].height=30
kaart.merge_cells('A10:F10')
kaart['A10']='De docent kent geen zes bonuspunten toe: zie product /10 (60 %) en proces /10 (40 %) in Bijlage B/C.'
kaart['A10'].alignment=Alignment(wrap_text=True)
kaart.sheet_properties.pageSetUpPr.fitToPage=True
kaart.page_setup.orientation='landscape';kaart.page_setup.paperSize=kaart.PAPERSIZE_A3
kaart.page_setup.fitToWidth=1;kaart.page_setup.fitToHeight=1
kaart.print_area='A1:F12'
w.save(OUT)
print(OUT)
