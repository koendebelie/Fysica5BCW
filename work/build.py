# -*- coding: utf-8 -*-
"""Genereer labocursus 6BCW uit één inhoudsbron.

    PYTHONPATH=work python3 work/build.py            # leerlingen
    PYTHONPATH=work python3 work/build.py --teacher  # leerkrachten

De PDF-leesversie wordt gemaakt met `render_pdf.py`. Wijzig de inhoud in
`course_sheets.py` en `labs.py`, niet achteraf in Word.
"""
import argparse
from pathlib import Path


import kit as K
from rubric_data import RUBRIC
from learning_targets import STEM, STEM_BORGING

ROOT = Path(__file__).resolve().parent.parent

EXTRA_FIGS = {
 (8,1):[('sch_ecb_trein_plaat.png','Speelgoedtrein op spoor én platenspeler met twee gemarkeerde stralen.')],
 (1,2):[('sch_tijdtikker_wagentje.png','Eigen elektrisch wagentje met 50 Hz-tijdtikker, papierbandje en 6 V~-voeding (schema naar bron blz. 68–72).')],
 (2,2):[('bron_p086_2.png','Wagentje op stijgende helling (bron: voorlopige cursus blz. 86).')],
 (3,2):[('sch_verticale_worp_tweecamera.png','Twee camera’s: één filmt de loslaathoogte, één het hoogste punt; hetzelfde meetlatvlak (eigen schema naar bron blz. 16–18).')],
 (4,1):[('sch_worp.png','Horizontale worp: leg zelf x- en y-assen en schaal vast (eigen schema naar bron blz. 56–57).')],
 (5,3):[('bron_p104_1.png','Krachtenparallellogram met twee dynamometers (bron: voorlopige cursus blz. 104).')],
 (7,1):[('bron_p109_1.png','Krachtarm bij een draaibaar statiefje (bron: voorlopige cursus blz. 109).')],
 (7,2):[('bron_p116_1.png','Tussenstandige last (bron: voorlopige cursus blz. 116).'),
         ('bron_p117_1.png','Tussenstandige macht (bron: voorlopige cursus blz. 117).')],
 (14,2):[('sch_cd_sporen.png','CD-sporen als rooster (nieuw, veilig schema; de vraag komt uit de voorlopige cursus blz. 5–6 en 62).')],
}

FIG_BEST = {
 1:('sch_luchtbel_twee_standen.png','Dezelfde luchtbel bij 90° en 45°; volg steeds dezelfde voorkant (schema naar bron blz. 63–67).'),
 2:('bron_p079_1.png','Tijdtikker en hellend vlak (bron: voorlopige 6BCW-cursus, blz. 79).'),
 3:('bron_p026_1.png','Voorbeeld van een v(t)-grafiek bij valbeweging (bron: voorlopige cursus, blz. 26).'),
 4:('bron_p093_1.png','Geverfd kogelspoor op een schuine plank (bron: voorlopige cursus, blz. 93).'),
 5:('bron_p097_1.png','Wagentje, tijdtikker en katrol (bron: voorlopige cursus, blz. 97).'),
 6:('bron_p106_1.png','Wagentje op hellend vlak, dynamometer en hoogte h (bron: voorlopige cursus, blz. 106).'),
 7:('bron_p113_1.png','Hefboom met tussenstandig steunpunt (bron: voorlopige cursus, blz. 113).'),
 8:('bron_p033_1.png','Draaiende massa en hangmassa (bron: voorlopige cursus, blz. 33).'),
 9:('sch_massa_veer.png','Massa-veersysteem (schematische tekening).'),
 10:('sch_slinger.png','Slinger, lengte tot massamiddelpunt (schematische tekening).'),
 11:('bron_p051_1.png','Gedempte veer met aandrijving (bron: voorlopige cursus, blz. 51).'),
 12:('sch_golfbak.png','Golfbak als onderzoeksmiddel (schematische tekening).'),
 13:('sch_geluid.png','Twee tonen in tegenfase en hun som (schematische tekening).'),
 14:('bron_p002_1.png','Laserlicht achter een rooster (bron: voorlopige cursus, blz. 2).'),
 15:('bron_p012_1.png','Twee kijkrichtingen bij de speldeprikproef (bron: voorlopige cursus, blz. 12).'),
 16:('sch_slinger.png','Voorbeeld: slinger met vast te houden variabelen (schematische tekening).'),
}


# Werkbladnummer is niet hetzelfde als het nummer van het oorspronkelijke themalabo.
# Deze vier bladen vragen een specifiek schema, niet de standaardfiguur van hun thema.
FIG_SHEET = {
 14:('sch_halve_trilling_tijdtikker.png','Massa, veer, getekend carbonlint en 50 Hz-triller bij een halve trilling.'),
 19:('sch_melde.png','Staande golf op een touw: knopen en buiken.'),
 23:('sch_witlicht_spectra.png','Wit licht geeft een continu spectrum; een gasontlading afzonderlijke lijnen.'),
 25:('sch_open_onderzoek.png','Van eigen onderzoeksvraag naar controleerbaar bewijs en poster.'),
}

def _start_appendix(doc, text):
    K.pagebreak(doc);K.h1(doc,text)


def appendices(doc, teacher):
    _start_appendix(doc,'Bijlage A – Het Excel-verslagsjabloon: opbouw en checklist')
    K.p(doc,"Gebruik voorlopig het invulbare bestand 'Blanco_verslag_6BCW_CONCEPT.xlsx'; de 5BCW-referentie verwijst voor het originele blanco Excel-bestand naar Smartschool. Raadpleeg de schoolspecifieke indienafspraken en "
            "controleer de versie van het formulier vóór je indient. Dit concept is GEEN letterlijke kopie van het ontbrekende originele Excel-bestand.")
    checks=[
        ('Kopblok','Groepsleden, klas, uitvoeringsdatum, labonummer en titel; bestandsnaam bevat 6BCW.'),
        ('OMSCHRIJVING','Doel, materiaal en werkwijze in eigen woorden; door een ander herhaalbaar.'),
        ('ONDERZOEKSVRAAG','Eén eigen SMART-vraag die alle delen van het labo dekt.'),
        ('HYPOTHESE','Verwachting met redenering, genoteerd vóór de proef.'),
        ('SCHEMA / FOTO','Opstelling met onderdelen, meettoestellen en maatwaarden benoemd.'),
        ('TABEL','Ruwe data, symbool en eenheid per kolom; berekende kolommen met Excel-formule.'),
        ('BEREKENINGEN','Twee uitgewerkte voorbeelden per soort: formule → waarden met eenheid → resultaat.'),
        ('GRAFIEK','Spreidingsgrafiek met losse punten, assen + eenheid, titel, passende trendlijn/vergelijking.'),
        ('BESLUIT','Data beantwoorden vraag, theorieverbinding, hypothese, foutenanalyse, reflectievragen.'),
        ('FEEDBACKBLOK','Niet verwijderen; cursieve sjabloontekst op het einde wel verwijderen.'),
        ('GROEPSWERK','OneDrive gedeeld, ieders bijdrage, iedereen leest alles na.'),
        ('INDIENEN','Eén upload per groep in Smartschool uiterlijk één week na het labo, 23.59 u; juiste bestandssoort.')]
    K.tabel(doc,['Onderdeel (Excel)','Checklist','✔'],[[x,y,'☐'] for x,y in checks],widths=[2500,6538,600],size=9)

    _start_appendix(doc,'Bijlage B – Productevaluatie: het verslag (60 %)')
    K.p(doc,'Er is geen rubric voor het product: de punten volgen de verdeling van het Excel-sjabloon. '
            'Ook werkbladen-PDF en poster worden op dezelfde vier onderdelen (/10) beoordeeld.')
    K.tabel(doc,['Onderdeel','Max.','Wat wordt verwacht?','Typische feedbackcodes'],[
        ['1. Verkennen & onderzoeken','2','Eigen SMART-vraag, doel, materiaal, herhaalbare werkwijze, hypothese en schema/foto.','Doel/variabelen ontbreken • hypothese onduidelijk • schema zonder labels'],
        ['2. Onderzoek uitvoeren','3','Volledige ruwe data, eenheden, beduidende cijfers, voorbeelden van Excel-berekeningen, spreidingsgrafiek met juiste assen en trend.','Eenheden • berekening • punten niet verbinden • trendlijn toevoegen'],
        ['3. Concluderen','3','Beantwoord de vraag uit meetgegevens, koppel aan theorie, toets hypothese, bespreek meetfouten, reflectievragen.','Geen meetgegevens in besluit • hypothese niet getoetst • foutenanalyse te vaag'],
        ['4. Attitude en verzorging','2','Gevraagde bestandssoort, op tijd ingediend, feedbackblok bewaard, verzorgd en aantoonbaar als groep.','Verkeerd sjabloon • te laat • instructietekst niet verwijderd']
    ],widths=[2200,600,4438,2400],size=8.8)
    K.p(doc,'De 2 productpunten voor bestandsvorm, tijdigheid en verzorging beoordelen het INGELEVERDE product; de individuele werkhouding tijdens het practicum staat uitsluitend in Bijlage C. Product- en procespunten worden elk eerst /10 berekend: eindpunt = 0,60 × product + 0,40 × proces.',size=9.5)
    K.h3(doc,'STEM-doelbewijs binnen deze /10, geen bonuspuntentabel')
    K.tabel(doc,['STEM-doel','Waar beoordeel je het productbewijs?','Wat is minimaal zichtbaar?'],[
        ['1 S + 6 S','/2 vraag/plan en /3 besluit','Een toetsbare eigen vraag en een controleerbare conclusie; bij labo 25 zeven fasen, vooraf goedgekeurd inhoudelijk F-LPD en schoolafspraak over #.'],
        ['2 S + 3 S','/3 uitvoeren, en individueel proces in Bijlage C','Originele meetreeks met SI, beduidende cijfers, nauwkeurigheid; veilige opstelling en echte observatie. Geen dubbel procespunt.'],
        ['4 S – labo 07','/2 model/keuze; /3 test; /3 besluit/bijsturing','Twee opvangvarianten met x≈v₀√(2h/g), twee keer getoetst aan originele video (voor en na bijsturing).'],
        ['5 S – labo 20','/3 analyse; /3 afgewogen besluit','dB-rekenstap, twee maatregelen, twee betrokkenen en minstens één beperking.'],
    ],widths=[1450,2330,5858],size=8.2)
    K.h3(doc,'Beslisregels voor aantonen en opnieuw proberen (zonder extra punten)')
    K.tabel(doc,['STEM-doel','Aangetoond als ...','Als bewijs nog ontbreekt ...'],[
        ['1 S','een toetsbare vraag, eerlijk origineel meetbewijs en een conclusie die de data niet tegenspreekt samenhang vertonen','stel vraag/variabelen scherper en herleid één besluit opnieuw uit data'],
        ['2 S','symbool, SI, resolutie en passende beduidende cijfers bij ruwe data én berekening kloppen; schaalomzetting waar relevant','herbereken één representatieve rij inclusief eenheid, 10-macht en afronding'],
        ['3 S','veiligheidsakkoord, geschikt toestel, duurzame werkwijze en echte ruwe data door de docent zijn geobserveerd','voer een veilige herdemonstratie uit; fabriceer geen achteraf verzonnen observatie'],
        ['4 S','twee opvangvarianten, model, echte videotoets, aantoonbare bijsturing en hertoets én eigen toelichting aanwezig zijn','toon de modelberekening opnieuw en toets de aangepaste marge aan het echte meetinterval'],
        ['5 S','dB-intensiteitsfactor, twee technieken, twee betrokkenen, nadeel én eigen afweging samenhangen','maak een nieuw advies met correcte getallen en een tegenargument vanuit andere betrokkene'],
        ['6 S (#)','zeven fasen, originele data, passende F-inhoud en schoolafspraak samen met eigen onderzoeksverantwoording aanwezig zijn','vul ontbrekende fase met werkelijk bewijs aan en licht de eigen planwijziging toe; school bepaalt formele aftekening'],
    ],widths=[900,4370,4368],size=8.0)
    K.p(doc,'Deze criteria begeleiden de status per LEERLING: controleer bij 4 S, 5 S en 6 S zowel het groepsproduct '
            'als diens korte eigen toelichting en tijdens het werk geobserveerde bijdrage. Vorm de product- en '
            'procespunten nog steeds alleen met Bijlage B/C. Laat bij ontbrekend bewijs de status open en '
            'geef een concrete gelegenheid tot bijsturen; “nog niet” is geen automatisch extra cijfer.',size=9)
    K.p(doc,'De docent noteert per doel in Bijlage G aangetoond / op weg / nog niet, citeert het bewijs en '
            'geeft één volgende stap. Het hele STEM-leerplan omvat ook andere vakken: deze cursus '
            'tekent uitsluitend de hier zichtbare fysica-gerelateerde doelbewijzen af.',size=9.2)
    K.p(doc,'Bij het open onderzoek telt bij onderdeel 1 de eigen vraag en het plan; bij onderdeel 3 de kwaliteit '
            'van de wetenschappelijke poster. Een peerfactor kan alleen worden toegepast wanneer de leerkracht dit vooraf aankondigt.',size=9.5)

    K.landscape_section(doc)
    K.h1(doc,'Bijlage C – Proces- en attituderubric (40 %)')
    K.p(doc,'Naam: ……………………………………………    Labo: ……    Datum: ……/……/……     Score: …… / 10    Opmerkingen: ………………………………',size=9)
    K.p(doc,'Per thema één niveau: uitstekend 1 · goed 0,8 · voldoende 0,6 · onvoldoende 0,4 · slecht 0,2. '
            'Tel de tien scores op; het resultaat is /10 en telt voor 40 %.',size=9)
    # Letterlijke rubric uit 5BCW: geen contextvoorbeelden of niveaucriteria aanpassen.
    rows=[row[:] for row in RUBRIC]
    K.tabel(doc,rows[0],rows[1:],widths=[1900]+[2650]*5,size=7.3)
    K.h3(doc,'Observatieblad leerkracht (per labo)')
    if teacher:
        K.tabel(doc,['Leerling']+[str(i) for i in range(1,11)]+['/10','Opmerking'],
                [['']*13 for _ in range(4)],widths=[2400]+[800]*10+[800,3900],size=7.5)
    else:
        K.p(doc,'De leerkracht vult het observatieblad bij het practicum in.',size=9,italic=True)
    K.portrait_section(doc)
    K.h1(doc,'Bijlage D – Zelfreflectie- en peer-evaluatiefiche')
    K.h3(doc,'D.1 Zelfreflectie (na labo 4, 9, 16 en 25)')
    K.tabel(doc,['Vraag','Mijn antwoord'],[
        ['Scoor jezelf op de 10 thema’s van Bijlage C (1 / 0,8 / 0,6 / 0,4 / 0,2) en motiveer één sterk punt en één werkpunt.',''],
        ['Welke vaardigheid beheers je nu beter dan bij het vorige reflectiemoment?',''],
        ['Wat ga je bij het volgende labo concreet anders doen?',''],
        ['Welke feedback op je verslagen heb je toegepast?','']
    ],widths=[5200,4438],size=9)
    K.h3(doc,'D.2 Peer-evaluatie (alleen indien aangekondigd door de leerkracht)')
    K.p(doc,'Iedere leerling verdeelt per groep 100 punten per groepslid over zichzelf én de anderen: '
            'groep van 3 → 300; groep van 2 → 200. Iedereen evenveel gedaan? 100 per persoon. '
            'Motivatie moet gedrag en bijdrage benoemen, niet sympathie. Vul individueel en vertrouwelijk in.')
    K.p(doc,'Peerfactor = (gemiddeld ontvangen punten, jezelf inbegrepen) / 100. Individueel productpunt '
            '= groepspunt × peerfactor (maximum 10/10). Bijvoorbeeld: groepspunt 7,5; ontvangen '
            '105, 105, 90 → gemiddeld 100 → factor 1,00 → 7,5. Bij 80, 85, 90 → factor 0,85 → 6,4. '
            'De leerkracht kan bijsturen als de verdeling strijdig is met de observaties.',size=9.5)
    K.p(doc,'Labo nr.: ……   Groep: ………………………   Ingevuld door: …………………………    Totaal: 300 / 200',size=9)
    K.tabel(doc,['Groepslid (naam)','Punten','Korte motivatie (wat deed deze persoon concreet?)'],[
        ['Ikzelf:','',''],['2:','',''],['3 (indien van toepassing):','',''],['Totaal:','300 / 200','']
    ],widths=[2800,1400,5438],size=9)

    _start_appendix(doc,'Bijlage E – Naslag: begrippen en formuleoverzicht')
    gloss={
        'ERB':'Eenparige rechtlijnige beweging: gelijke afstanden in gelijke tijden.',
        'EVRB':'Eenparig versnelde rechtlijnige beweging: snelheid verandert per seconde evenveel.',
        'Tijdtikker':'Toestel dat op een papierband op vaste tijdsintervallen stippen zet.',
        'Ogenblikkelijke snelheid':'Snelheid op een bepaald tijdstip, benaderd over een heel kort tijdsvenster.',
        'Richtingscoëfficiënt':'Stijging gedeeld door horizontale verandering in een grafiek.',
        'Tracker':'Programma voor positie-tijdmetingen uit een video, beeld voor beeld.',
        'Parallax':'Schijnbare verschuiving doordat camera en meetlat niet in hetzelfde vlak staan.',
        'Nettokracht / resultante':'Vectoriële som van alle krachten op één voorwerp.',
        'Centripetale kracht':'Nettokracht naar het middelpunt van een cirkelbaan.',
        'Hoeksnelheid':'Afgelegde hoek per seconde (rad/s).',
        'Amplitude':'Grootste uitwijking vanuit de evenwichtsstand.',
        'Eigenfrequentie':'Frequentie van vrije trilling zonder voortdurende aandrijving.',
        'Demping':'Afname van amplitude door energieverlies.',
        'Resonantie':'Sterke respons bij aandrijving nabij de eigenfrequentie.',
        'Golflengte':'Afstand tussen opeenvolgende toppen (m).',
        'Knoop / buik':'Stil punt / punt met grootste uitwijking van een staande golf.',
        'Buiging':'Een golf waaiert uit achter een opening of hindernis.',
        'Interferentie':'Golven samen zorgen voor versterking of verzwakking.',
        'Superpositie':'Momentane optelling van de uitwijkingen van meerdere golven.',
        'Tegenfase':'Top van ene golf valt samen met dal van andere.',
        'Dopplereffect':'Waargenomen frequentie verandert bij relatieve beweging bron/waarnemer.',
        'Roosterconstante':'Afstand tussen opeenvolgende roosterlijnen (m).',
        'Brekingsindex':'Maat voor richtingsverandering van licht tussen twee middenstoffen.',
        'SMART':'Specifiek, Meetbaar, Aanvaardbaar, Realistisch, Tijdsgebonden.',
        'Peerfactor':'Gemiddeld ontvangen peerevaluatiepunten gedeeld door 100.'}
    K.tabel(doc,['Begrip','Betekenis in eenvoudige woorden'],[[k,v] for k,v in gloss.items()],widths=[3000,6638],size=9)
    K.h3(doc,'E.1 Constantes en nuttige formules')
    K.tabel(doc,['Grootheid','Formule / waarde / eenheid'],[
        ['Valversnelling nabij aardoppervlak','g ≈ 9,81 m/s²'],
        ['Snelheid en versnelling','v = Δx/Δt (m/s); a = Δv/Δt (m/s²)'],
        ['Tweede wet','Fᵣ = ma (N)'],
        ['ECB','v = 2πr/T, ω = 2π/T, F_cp = mv²/r'],
        ['Veer / slinger','T_veer = 2π√(m/k); T_slinger = 2π√(l/g) (kleine hoek)'],
        ['Golf / lichtrooster','v = λf; a sin θ = nλ; a = 1/(lijnen per m)'],
        ['Breking','n = sin α/sin β (lucht naar kunststof)'],
    ],widths=[3200,6438],size=9)
    _start_appendix(doc,'Bijlage F – Tracker en tijdtikker: een startgids')
    K.h3(doc,'F.1 Tracker voor videoanalyse (eerste gebruik: labo 6)')
    K.numbered(doc,[
        'Film zijdelings met een vaste camera; houd een meetlat in het vlak van de beweging. Bewaar het fragment.',
        'Open Tracker op de schoollaptop. Importeer het videofragment (Bestand → Openen).',
        'Plaats kalibratiestok op de meetlat; geef de echte lengte in meter op.',
        'Zet de oorsprong (bij verticale worp: vloer of bal op vloer) en kies omhoog positief.',
        'Maak een spoor/point mass en markeer het midden van de bal op opeenvolgende frames.',
        'Controleer een paar punten op fout gekozen frames en pas ze aan; kopieer t en y naar Excel.',
        'Maak spreidingsgrafiek met losse punten, benoemde assen en gepaste trendlijn. Sla schermafbeelding met titel en uitleg op.'
    ],size=9.5)
    K.kader(doc,'PROBLEMEN OPLOSSEN',['Geen beeld? Gebruik een ander lokaal videobestand of schoollaptop.',
             'Vreemde snelheden? Controleer schaal, oorsprong en framefrequentie.',
             'Beeld springt? Markeer frames handmatig; meetlat in hetzelfde vlak.',
             'Bij ontbreken van Tracker: analyseer het filmpje frame voor frame met tijdstempels en meetlat.'],soort='uitleg',size=9.5)
    K.h3(doc,'F.2 Tijdtikker (eerste gebruik: labo 1)')
    K.numbered(doc,[
        'Lees de toegestane voedingsspanning en frequentie op het toestel; de leerkracht controleert de juiste lage voeding.',
        'Bevestig carbonlint en papieren bandje; proef kort met het wagentje veilig in een vangbak.',
        'Bij 50 Hz ligt tussen twee opeenvolgende stippen 0,020 s. Twee intervallen = 0,040 s.',
        'Meet plaatsen vanaf één gekozen nulstip, bereken Δx tussen stippen, en koppel elke snelheid aan de middentijd.',
        'Plak het originele bandje of een duidelijke foto ervan bij je ruwe data; zet voeding uit na de meting.'
    ],size=9.5)
    K.kader(doc,'VEILIGHEID / CONTROLE',['Gebruik nooit netspanning direct op de tijdtikker.',
           'Houd vingers, haren en kleding weg van de bewegende band.',
           'Bij onleesbare stippen: carbonlint corrigeren met voeding UIT, niet de data achteraf verzinnen.'],soort='veilig',size=9.5)
    if teacher:
        K.teacher_note(doc,['De werking van Tracker moet vóór de eerste meting op de schoollaptop getest worden. '
                  'Controleer de actuele schoolversie en voeg echte screenshots van het lokale menu toe vóór verspreiding.',
                  'Gebruik de geteste laagspanningsvoeding bij de tijdtikker; de werkelijke typeplaat en schoolvoeding zijn leidend.'])


    _start_appendix(doc,'Bijlage G – STEM-doelkaart: bewijs, feedback en volgende stap')
    K.p(doc,'Naam leerling: ………………………  Groep: ……………  Klas: ………  Periode: ………………  Leerkracht: ………………………',size=9.5)
    K.p(doc,'De zes STEM-doelen zijn leerplandoelen, geen zes bijkomende punten. Schrijf per doel '
            'waar het bewijs in je werk staat. De leerkracht noteert nog niet / op weg / aangetoond '
            'en één concrete volgende stap. Maak dit blad per leerling: gebruik groepsproduct én de eigen '
            'toelichting/individuele observatie. Een doel is niet automatisch behaald omdat het op een blad staat.',size=9.5)
    evidence={
        1:'Onderzoeksvraag, hypothese, ruwe data, onderbouwd besluit (o.a. 04, 07, 15, 25).',
        2:'Symbool, SI, resolutie, beduidende cijfers, machten van tien (o.a. 02, 09, 21).',
        3:'Veiligheidscontrole, juist meetinstrument, duurzaam opruimen en brondata (o.a. 05, 12, 21).',
        4:'Labo 07: twee opvangvarianten, formule/model, videotoets, bijsturing en hertoets.',
        5:'Labo 20: geluidsadvies met dB-getallen, techniek, twee betrokkenen en beperking.',
        6:'Labo 25: zeven fasen, passend goedgekeurd F-LPD, schoolafspraak, ruwe data en poster.',
    }
    K.tabel(doc,['LPD','Verplicht zichtbaar bewijs','Vindplaats in mijn werk','Status + datum','Feedforward'],[
        [f'{k} S',evidence[k],'','',''] for k in STEM
    ],widths=[590,3910,1920,1530,1688],size=8.2)
    K.p(doc,'Terugblik leerling: wat kan ik aantonen met getallen, en wat moet ik volgende keer oefenen?')
    K.invul(doc,regels=3)
    if teacher:
        K.teacher_note(doc,['Noteer een vindplaats in het origineel (werkblad/Excel/video/poster) en '
                            'een observeerbaar sterk punt en verbeteractie. Status is bewijsgericht, '
                            'geen nieuw cijfer buiten product 60 % / proces 40 %.',
                            '4 S vereist een ontwikkellus, 5 S een maatschappelijke afweging en '
                            '6 S een volledige cyclus plus vooraf bevestigde F-inhoud en schoolafspraak over de onderzoekscompetentie (#). Ontbrekend werk uit andere wetenschapsvakken '
                            'niet automatisch als behaald aftekenen.'])


def order_list():
    doc=K.new_document('Bestellijst nieuw materiaal Toegepaste fysica 6BCW')
    K.h1(doc,'Bestellijst nieuw materiaal – 6BCW')
    K.p(doc,'Voorlopige checklist voor 8 groepen van 2–3. Alleen niet-vanzelfsprekend materiaal; '
            'controleer eerst de voorraad. Prijzen zijn **niet geverifieerd** en dienen enkel voor budgettering; '
            'geen bestelling plaatsen zonder offertes en veiligheidscontrole.',size=10)
    rows=[
      ['Glazen buisje met afgeronde randen + stevige nylondraad + rubberstop','8 sets','€10–25/set','schoolleverancier fysicalabo','☐'],
      ['Roosters 80, 100, 300, 600 lijnen/mm','8 sets van 4','€30–80/set','optical/educational supplier','☐'],
      ['Gekeurde lageklasse-laserpen met bundelstop','8','€15–40/stuk','schoolleverancier optica','☐'],
      ['Overhead-golfbak of gelijkwaardig camerasysteem','1–2','offerte','schoolleverancier fysicalabo','☐'],
      ['Laagtoerige regelbare motor met excenter (resonantie)','2','offerte','schoolleverancier STEM','☐'],
      ['Statieven + zachte valmat/opvangbak voor werpproeven','8 sets','€10–25/set','schoolvoorraad / sporthandel','☐'],
      ['Twee stabiele smartphonehouders + twee verticale meetlatten per groep (handmatige verticale worp)','8 sets','offerte / voorraad','schoolvoorraad / schoolleverancier','☐'],
      ['Plexiglazen balkjes + spelden (optica)','8 sets','€10–30/set','schoolleverancier optica','☐'],
      ['Papieren tijdtikkerbandjes + carbonlint','8 × verbruiksset','€10–20/set','schoolleverancier fysicalabo','☐'],
      ['Veiligheidsbrillen voor ECB-rotatie','24','€5–12/stuk','schoolleverancier PBM','☐'],
    ]
    K.tabel(doc,['Item','Aantal voor 8 groepen','Richtprijs (niet geverifieerd)','Waar te koop','Al aanwezig?'],rows,
            widths=[3100,1350,1550,2500,1138],size=9)
    K.p(doc,'Gewone fysica-uitrusting (meetlat, massa’s, statief, chronometer, dynamometer, balans, '
            'laptop) staat bewust niet op de bestellijst. Koppel de bestelling aan de werkelijke groepsgrootte.',size=9)
    out=ROOT/'Bestellijst_nieuw_materiaal_6BCW.docx';doc.save(out)
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--teacher',action='store_true')
    ap.add_argument('--list-only',action='store_true')
    args=ap.parse_args()
    if args.list_only:
        print(order_list());return
    T=args.teacher
    from course_sheets import build as build_course
    doc=K.new_document()
    build_course(doc,T)
    appendices(doc,T)
    name=f'Labocursus_6BCW_{"LEERKRACHT" if T else "LEERLING"}.docx'
    path=ROOT/name;doc.save(path)
    print(path)
    if not T: print(order_list())

if __name__=='__main__': main()
