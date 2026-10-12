# -*- coding: utf-8 -*-
"""Rijke 6BCW-inleiding naar het didactische model van de 5BCW-cursus.

Bewust geen didactisch onjuiste 5BCW-elektriciteitsvoorbeelden of verouderde
16-labonummers overnemen. Voor de leerlingen geen herkomstpagina's of links.
"""
import kit as K
from course_guidance import G
from labs import LABOS
from learning_targets import T, STEM, STEM_BORGING


def build(doc,teacher,sheets):
    # Volwaardige titelpagina, net als bij de 5BCW-referentiecursus.
    for _ in range(3):K.p(doc,'')
    K.p(doc,'LABOCURSUS TOEGEPASTE FYSICA',size=24,bold=True,color='1F4E79',align='c',space_after=10)
    K.p(doc,'Beweging · krachten · trillingen · golven · licht',size=14,color='2E7D32',align='c',space_after=12)
    K.p(doc,'6BCW · 25 zelfstandige practica',size=13,align='c',space_after=20)
    K.p(doc,'Werkbladen volgens de OVUR-methode',size=12,bold=True,align='c')
    K.p(doc,'Oriënteren · Voorbereiden · Uitvoeren · Reflecteren',size=11,align='c',space_after=14)
    K.p(doc,'LEERKRACHTENVERSIE · met modelantwoorden en didactische aanwijzingen' if teacher else
          'LEERLINGENVERSIE · meten, redeneren en besluiten',size=11,
          color='B71C1C' if teacher else '1F4E79',align='c',space_after=26)
    for label in ('Naam leerling','Klas / nummer','Labogroep / partner(s)','Schooljaar'):
        K.p(doc,f'{label}: ………………………………………………………………………………',size=11,space_after=8)
    K.p(doc,'Leerplan III-BCSW-d (2024) · STEM- en fysicadoelen. In ieder labo staat de passende doelcode.',
        size=9,align='c',color='555555')
    K.pagebreak(doc)

    K.h1(doc,'Inhoud')
    K.p(doc,'De Word-inhoudsopgave kan op basis van de kopstijlen met F9 worden bijgewerkt. '
            'Onderstaand overzicht volgt de volgorde van de lessen; één proef is één zelfstandig werkblad.',
        size=9,italic=True)
    fallback=[(0,'Deel 1 · Werken en leren in het fysica-labo')]
    fallback += [(0,f'LABO {i:02d} · {title}') for i,(_,_,title) in enumerate(sheets,1)]
    fallback += [(0,f'Bijlage {letter} · {title}') for letter,title in zip('ABCDEFG',
       ('Verslagsjabloon: opbouw en checklist','Productevaluatie','Proces- en attituderubric',
        'Zelfreflectie en peer-evaluatie','Begrippen en formules','Tracker en tijdtikker',
        'STEM-doelkaart en feedforward'))]
    K.toc(doc,fallback,levels='1-2')
    K.pagebreak(doc)

    K.h1(doc,'Deel 1 · Werken en leren in het fysica-labo')
    K.h2(doc,'1.1 De OVUR-methode: van vraag tot beargumenteerd besluit')
    K.p(doc,'In het labo gaat het niet om een mooi resultaat dat van tevoren vaststaat. Je gebruikt een '
        'afgesproken of zelfgemaakt meetplan om een fysische vraag te beantwoorden. Elk werkblad volgt '
        'dezelfde vier fasen. Lees vóór het opbouwen de context, leerdoelen, veiligheidsafspraken en '
        'oriëntatievragen; kom na het meten met je eigen gegevens tot een besluit.')
    K.tabel(doc,['Fase','Wat doe je?','Wat lever je als bewijs?'],[
        ['O · Oriënteren','Verken de situatie, haal voorkennis op en formuleer een toetsbare vraag.',
         'Context, doelen, antwoorden op oriëntatievragen en SMART-vraag.'],
        ['V · Voorbereiden','Voorspel, kies variabelen en meetmethode, teken de opstelling en toets veiligheid.',
         'Hypothese, O/A/C-tabel, schets en zo nodig goedgekeurd eigen werkplan.'],
        ['U · Uitvoeren','Bouw en meet zoals gepland; bewaar ook onverwachte ruwe data.',
         'Bandje, video of foto, ingevulde tabel, berekening en XY-grafiek.'],
        ['R · Reflecteren','Verbind data met theorie, toets hypothese en bespreek onzekerheid en toepassing.',
         'Antwoord op de onderzoeksvraag, reflectievragen, meetfouten en verbeteridee.'],
    ],widths=[1600,4350,3688],size=9)
    K.h3(doc,'Leerlijn: sneller zelfstandig, maar niet zonder meetdiscipline')
    K.tabel(doc,['Stap','Wie bepaalt de vraag/werkwijze?','Wanneer?'],[
        ['Voorbeeld','Je krijgt één uitgewerkte SMART-vraag en beoordeelt haar letters; het protocol is gegeven.','Labo 01'],
        ['Kiezen','Je kiest één SMART-vraag uit vier voorstellen en verantwoordt waarom.','Labo 02'],
        ['Zelf formuleren','Je schrijft vanaf nu je eigen SMART-vraag. Bij de vaste proeven behoud je de afgesproken schoolopstelling en de meetreeksen.','Vanaf labo 03'],
        ['Open ontwerpen','Je bepaalt een uitvoerbaar plan binnen het bestaande materiaal; de leerkracht keurt risico’s en meetstrategie vooraf goed.','Labo 04, 07, 15, 25'],
    ],widths=[1600,5890,2148],size=9)
    K.p(doc,'Een SMART-vraag zegt wat je verandert (O), wat je meet (A), wat gelijk blijft (C), waarmee '
        'en binnen welke lescontext je meet. Een open werkblad betekent niet dat je ruwe gegevens '
        'of een gekende proefopstelling mag vervangen door een mooiere fictieve reeks.',size=9.8)
    K.tabel(doc,['Letter','Betekenis','Controlevraag bij jouw proef'],[
        ['S','Specifiek','Welke beweging, kracht of golf en welk verband onderzoek ik?'],
        ['M','Meetbaar','Welke grootheden, meetinstrumenten, eenheden en aantallen?'],
        ['A','Aanvaardbaar','Is mijn vraag fysisch zinvol en de proef veilig en ethisch?'],
        ['R','Realistisch','Is het haalbaar met het aanwezige schoolmateriaal?'],
        ['T','Tijdsgebonden','Welke meting en verwerking kunnen binnen dit labo gebeuren?'],
    ],widths=[650,1800,7188],size=9)

    K.h2(doc,'1.2 Veilig, zorgvuldig en als groep werken')
    K.p(doc,'De leerkracht controleert de eerste opstelling. Duid per les een veiligheidsverantwoordelijke '
        'aan en wissel de rol. Die persoon is het aanspreekpunt, niet de enige die verantwoordelijkheid draagt.')
    K.tabel(doc,['Moment','Afspraak'],[
        ['Voor de proef','Lees het veiligheidskader, controleer klemmen, baan en voeding en vraag akkoord vóór inschakelen of loslaten.'],
        ['Tijdens de proef','Houd omstanders uit val- en draaicirkel. Gebruik lage, passende voeding; houd water bij golfbak/motor van stekkers weg. Richt een laser nooit op ogen. Zet geluid zacht.'],
        ['Na de proef','Schakel voeding uit; berg massa’s, linten, spelden en laser op; meld schade, hergebruik veilig bruikbaar materiaal en ruim de werkplek op.'],
    ],widths=[1750,7888],size=9)
    K.p(doc,'Leg meetrollen vast: opsteller/veiligheidscontrole, meter en notulist/verwerker. Wissel bij '
        'een reeks van rol, zodat ieder de meting kan uitleggen. Eén groepsproduct betekent dat iedereen '
        'de gegevens, formules en het besluit controleert; meld problemen tijdig.',size=9.6)

    K.h2(doc,'1.3 Meten, grafieken maken en verschillen verklaren')
    K.tabel(doc,['Afspraak','Concreet bij deze cursus'],[
        ['Ruwe data','Noteer waarden onmiddellijk met symbool én eenheid. Verwijder een opvallend meetpunt niet zonder te onderzoeken waarom. Bewaar bandje, video of foto.'],
        ['Herhalingen','Volg het aantal uit het werkblad; bij perioden meet je vaak 10 of 20 omwentelingen tegelijk. Noteer afzonderlijke metingen vóór het gemiddelde.'],
        ['Grootheid en eenheid','Gebruik SI-eenheden bij formules; zet g→kg en cm→m om wanneer nodig. Schrijf bv. 0,020 s = 2,0×10⁻² s en 500 nm = 5,0×10⁻⁷ m; rond pas aan na de berekening.'],
        ['Beduidende cijfers','Noteer de resolutie/afleesnauwkeurigheid van ieder meettoestel. Rond berekende waarden niet nauwkeuriger af dan de meting toelaat.'],
        ['Excel-grafiek','Gebruik XY-spreiding met losse punten, benoemde assen en eenheden; trendlijn/vergelijking alleen als het model dat rechtvaardigt. Verbind ruwe punten niet zomaar.'],
        ['Rico en afsnede','Noem de eenheid én betekenis: v₀ is de y-asafsnede van v(t′), a de rico; bij T²(l) is de rico 4π²/g. Extrapolatie is geen meetpunt.'],
        ['Onzekerheid','Bespreek minstens één concrete bron: tikinterval, bandwrijving, reactietijd, schaal/parallax, scheve opstelling of meetspreiding. Zeg welke richting/omvang het effect heeft.'],
    ],widths=[2300,7338],size=9)
    K.p(doc,'Gebruik een externe bron uitsluitend waar een werkblad om bronnen vraagt (bijvoorbeeld bij de poster): '
        'noteer auteur/organisatie, titel en raadpleegdatum. Scheid broninformatie van de eigen meetgegevens. '
        'Laat geen AI-hulpmiddel meetwaarden, een berekening, grafiek, verklaring of eigen reflectie verzinnen of '
        'het antwoord in jouw plaats schrijven. Volg daarnaast de actuele schoolafspraken over bronnen en AI.',size=9.4)
    K.kader(doc,'TIJDTIKKER → EXCEL: t′ STAAT DIRECT LINKS VAN v',[
        'Bij 50 Hz ligt elke tik 0,020 s later. Kies je om de twee stippen een meetpunt, dan is het venster Δt=0,040 s.',
        'Een uit Δx/Δt berekende snelheid hoort bij het MIDDENTIJDSTIP t′=(t_begin+t_eind)/2. t′ is geen duur Δt en geen snelheidsverschil Δv.',
        'Selecteer voor v(t′) in Excel de aangrenzende kolommen t′ en v. Voor x(t) selecteer je t en x. Controleer vóór interpretatie je askeuze en eenheden.',
    ],soort='uitleg',size=9.3)

    K.h2(doc,'1.4 Het verslag, de samenwerking en de beoordeling')
    K.p(doc,'Bijlage A geeft het herkenbare verslagoverzicht en een checklist. De oorspronkelijke lege '
        '5BCW-Exceltemplate is niet meegeleverd; het beschikbare bestand '
        '“Blanco_verslag_6BCW_CONCEPT.xlsx” is nadrukkelijk een voorlopig invulblad. De leerkracht '
        'bevestigt vóór het eerste verslag de schooltemplate en Smartschool-uploadzone. Naar het '
        '5BCW-voorbeeld lever je één week na het labo uiterlijk om 23.59 u in; de leerkracht geeft '
        'de concrete datum en meldt vooraf eventuele schoolspecifieke afwijkingen. '
        'Bij een korte observatieproef kan het ingevulde werkblad volstaan; bij metingen en grafieken '
        'is een Excel-verslag passend. Het werkblad vermeldt het te verwachten product.')
    K.tabel(doc,['Verslagonderdeel','Wat komt erin?'],[
        ['Omschrijving','Doel, materiaal en herhaalbare werkwijze in je eigen woorden.'],
        ['Vraag en hypothese','Eén SMART-vraag; een beargumenteerde verwachting, vóór de meting geschreven.'],
        ['Opstelling en tabel','Gelabeld schema/foto; ALLE ruwe metingen met kolomsymbool en eenheid.'],
        ['Berekening en grafiek','Voorbeelden met eenheid; formules in Excel; losse punten en passende fit.'],
        ['Besluit','Beantwoord je vraag met getallen, toets hypothese, bespreek afwijking en reflectievragen.'],
        ['Feedback','Laat de ruimte voor opmerkingen van de leerkracht staan.'],
    ],widths=[2650,6988],size=9)
    K.p(doc,'Werk met één gedeeld groepsbestand, maak taakafspraken en lees ELKAARS resultaat na. '
        'Houd ieder een kopie van de ruwe meetgegevens. De leerkracht beoordeelt het product als '
        'groepswerk (60 %) en het eigen proces/attitude (40 %) met de ongewijzigde 5BCW-rubric '
        'in Bijlage C; criteria en voorbeeldfeedback staan in Bijlage B. Het product (/10) telt '
        'voor 60 %, het individueel geobserveerde proces (/10) voor 40 %: bv. product 8 en '
        'proces 7 geven samen 0,6 × 8 + 0,4 × 7 = 7,6/10. De 2 productpunten voor '
        'verzorging en tijdig indienen meten NIET nogmaals je houding tijdens het labo. '
        'Bijlage D geeft zelfreflectie en een peerfiche indien die vooraf is aangekondigd.')
    K.kader(doc,'MINICHECK VÓÓR INDIENEN',[
        'Kan een andere leerling met jouw beschrijving de proef veilig herhalen?',
        'Staan de ruwe gegevens, eenheden, twee voorbeeldberekeningen en de gevraagde grafiek erbij?',
        'Beantwoordt het besluit de eigen vraag met data, theorie, meetfouten en een verbeteridee?',
        'Heeft ieder groepslid het geheel nagelezen en is de juiste bestandsvorm bevestigd?',
    ],soort='eval',size=9)

    K.h2(doc,'1.5 Lesdoelen en alle zes STEM-doelen: bewijs en feedback')
    K.p(doc,'De lesdoelen bovenaan ieder blad zeggen wat je na dat labo aantoonbaar moet kunnen. '
        'Daaronder staan de betrokken Fysica- en STEM-leerplandoelen en twee concrete controlepunten: '
        'bewijs is een meetwaarde, ontwerp, grafiek, verklaring of besluit, niet alleen een afgevinkt nummer. '
        'Een F-doel kan slechts gedeeltelijk in één proef aan bod komen; de beperking staat dan expliciet op het blad. '
        'De zes STEM-doelen uit het leerplan (III-BCSW-d, blz. 17–21) zijn over de HELE cursus gespreid:',size=9.3)
    K.tabel(doc,['STEM-LPD','Wat leer je doen?','Waar is verplicht, toetsbaar bewijs?'],[
        [f'{k} S',STEM[k],('Labo '+', '.join(f'{i:02d}' for i in STEM_BORGING[k])+
                        (': beide opvangontwerpen, model, videotoets en bijsturing.' if k==4 else
                         ': dB-vergelijking en afweging van geluidstechniek voor betrokkenen.' if k==5 else
                         ': zeven fasen in goedgekeurd plan, data en wetenschappelijke poster.' if k==6 else
                         '; zie ook de concrete doelen op ieder werkblad.'))]
        for k in STEM
    ],widths=[900,4170,4568],size=8.2)
    K.p(doc,'Bij labo 07, 20 en 25 geeft elk groepslid onder de STEM-opdracht een korte eigen toelichting '
        'met een getal of meetrij. De leerkracht gebruikt die en de individuele labo-observatie bij de '
        'doelstatus; het groepsproduct alleen bewijst geen individuele beheersing. Bij “nog niet” of “op weg” '
        'volgt een gerichte verbeteropdracht, bijvoorbeeld een berekening opnieuw uitleggen of een '
        'meetrij opnieuw analyseren. De leerkracht beoordeelt vervolgens het nieuwe bewijs. Geen extra punten.',size=9.3)
    K.p(doc,'Onderzoek is GEEN star recept: een observatie kan een nieuwe vraag opleveren; je mag een '
        'hypothese eerlijk herzien als je het originele bewijs bewaart. Labo 07 vereist naast de eigen '
        'horizontale-worpmeting een kleine veilige ontwerp-/testlus (4 S), labo 20 een maatschappelijke '
        'afweging (5 S); labo 25 doorloopt aantoonbaar alle zeven onderzoeksfasen (6 S). '
        'Dit fysicabewijs vervangt niet de andere inhoudelijke doelen van Biologie, Chemie en Informatica '
        'in de volledige studierichting. Behaald betekent: je laat het bewijs werkelijk zien, niet: de code staat op papier.',size=9.2)
    K.h3(doc,'Hoe beoordeelt de leerkracht lesdoelen en STEM zonder extra punten?')
    K.tabel(doc,['Moment','Doelbewijs','Hoe krijg je feedback / punten?'],[
        ['Vooraf, formatief','Vraag, hypothese, variabelen, veiligheids- en ontwerpplan; bij labo 07 beide opvangvarianten.','De leerkracht geeft gerichte feedback en keurt risico’s goed vóór meten. Een fout verbeteren is hier leren, nog geen apart cijfer.'],
        ['Tijdens, formatief + observatie','Ruwe data, meetresolutie, SI, machten van tien, veilige samenwerking; één tussentijds meetpunt controleren.','Bijsturen met een volgende actie; individueel geobserveerd proces volgens de ONGEWIJZIGDE rubric C (/10, 40 %).'],
        ['Na afloop, product','Onderzoeksvraag/plan; tabellen/grafiek/ontwerptest; conclusie/maatschappelijke keuze of postercyclus.','Groepsproduct /10: verkennen 2, uitvoeren 3, concluderen 3, verzorging/indienen 2 (Bijlage B); dit telt voor 60 %. 4 S, 5 S en 6 S zitten IN deze punten.'],
        ['Feedforward','Gebruik de vier genummerde bewijscriteria in je doelcheck en de individuele toelichting bij 07/20/25.','Schriftelijke productfeedback en individuele procesfeedback: benoem een sterk punt, een tekort én een haalbare volgende stap; peerfiche alleen indien aangekondigd.'],
    ],widths=[1750,3990,3898],size=8.4)
    K.p(doc,'Differentiatie: gebruik bij een moeilijkere opgave het voorbeeld van een tabel, een '
        'rekenstap of gerichte docentfeedback; wie sneller werkt onderzoekt een extra onzekerheid of '
        'alternatief. De vereiste doelen en veiligheidsgrenzen blijven voor iedereen gelijk. '
        'Een hogere orde in een rooster of een onverwacht meetpunt hoeft geen extra cijfer te geven; '
        'de argumentatie met eigen data bepaalt de kwaliteit.',size=9.3)

    K.h2(doc,'1.6 Overzicht van de 25 labo’s en leerplandoelen')
    K.p(doc,'Elk nummer hieronder is een zelfstandig werkblad. Fysica-codes met “deelvaardigheid” '
        'of “ondersteuning” betekenen niet dat die hele leerplandoelen in dit ene practicum afgetekend zijn.',size=9)
    K.tabel(doc,['Nr.','Practicum','Sturing','Fysica-LPD','STEM-LPD'],[
        [f'{i:02d}',title,G[i-1].steering,T[i-1].physics,', '.join(f'{k} S' for k in T[i-1].stem)]
        for i,(_,_,title) in enumerate(sheets,1)
    ],widths=[490,3400,1800,2050,1898],size=7.8)
    K.pagebreak(doc)
