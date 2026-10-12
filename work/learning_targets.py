# -*- coding: utf-8 -*-
"""Leerplan III-BCSW-d (2024), pp. 17–21, 58–65: doelen per 6BCW-werkblad.

LPD 1–6 S zijn doelen van de HELE richting. Deze fysicacursus levert expliciet
bewijs voor elk ervan; dat is niet hetzelfde als een aftekening voor alle
biologie-, chemie- of informaticadoelen van de volledige studierichting.
Geen 16 F claimen voor alleen g uit val/slinger (16 F omvat gravitatieveld en
analogie met elektrisch veld). 22 F alleen bij staande golven, niet golfbak.
S4 vraagt ontwerp + geïntegreerd model + test/bijsturing, niet enkel meten.
S5 vraagt een maatschappelijke afweging, niet een los toepassingsvoorbeeld.
"""
from dataclasses import dataclass

STEM = {
 1:'Een afgebakende vraag en beredeneerde hypothese toetsen met waarnemingen; de methode en conclusie kritisch communiceren.',
 2:'Metingen noteren met symbool, SI-eenheid, meetnauwkeurigheid, beduidende cijfers en waar zinvol machten van tien.',
 3:'Meetinstrumenten en technische systemen nauwkeurig, veilig en duurzaam inzetten; ruwe data controleerbaar bewaren.',
 4:'Voor een concreet probleem een oplossing ontwikkelen met een fysisch én wiskundig model, technische keuzes, test en bijsturing.',
 5:'Bij een maatschappelijke uitdaging wetenschap, technologie en wiskunde én gevolgen voor verschillende betrokkenen afwegen.',
 6:'Een volledige onderzoekscyclus uitvoeren: oriëntatie, vraag, methode, data, analyse, conclusie en rapportering.',
}

@dataclass(frozen=True)
class Target:
    physics: str                 # correcte fysica-LPD, met begrenzing waar nodig
    physics_meaning: str
    stem: tuple[int,...]          # wat hier daadwerkelijk geoefend en beoordeeld wordt
    additions: tuple[str,str]    # naast twee concrete bestaande G.goals
    checks: tuple[str,str]       # bewijsbaar door leerlingen; geen abstracte afvinkcodes
    checkpoint: str              # formatieve ingreep door docent / peer tijdens het labo

T = [
 Target('13 F (deelvaardigheid)','Plaats en tijd verbinden met gemiddelde snelheid; eenparige beweging is de opstap naar EVRB.',(1,2,3),
 ('een onderzoekbare vraag en hypothese formuleren over dezelfde bel bij twee hoeken.','de spreiding en afleesnauwkeurigheid van de klokmetingen verklaren.'),
 ('mijn twee reeksen hebben dezelfde nulpositie, eenheden en minstens één herhaling.','ik kan twee rico’s met getallen vergelijken en één concrete onzekerheid noemen.'),
 'Controleer vóór de eerste meting het referentiepunt en geef feedback op de hypothese.'),
 Target('13 F (deelvaardigheid)','Plaats, tijdstip en snelheid op een echt bandje interpreteren; EVRB volgt in labo 03.',(1,2,3),
 ('de stipafstand met de tijdstap 0,020 s onderscheiden van een 0,040 s-venster.','uitleggen waarom t′ midden in het venster staat en naast v hoort.'),
 ('ik markeer op het originele bandje de optrek-, ERB- en remfase.','mijn x(t)-rico en tabelsnelheid staan met m/s en worden vergeleken.'),
 'Bekijk het geselecteerde banddeel en corrigeer de Excel-askeuze vóór het maken van de fit.'),
 Target('13 F','Positie, tijdstip, snelheid en versnelling in een EVRB met beginsnelheid kwantificeren.',(1,2,3),
 ('met gegevens aantonen waarom de gekozen nulstip niet stilstand betekent.','de y-afsnede, rico en geëxtrapoleerde x-asafsnede fysisch beoordelen.'),
 ('ik toon bandje, t′ direct links van v en een v(t′)-fit met m/s en m/s².','ik leg uit welke asafsnede gemeten is en welke slechts geëxtrapoleerd.'),
 'Laat de leerling vóór de fit voorspellen of v₀ nul is; vraag eenheden bij beide fitparameters.'),
 Target('13 F; 6 S (oefencyclus)','EVRB met negatieve versnelling onderzoeken; de open cyclus bereidt het sluitstuk in labo 25 voor.',(1,2,3),
 ('een meetbare eigen vraag en toetsbare hypothese opschrijven vóór het duwen.','het meetplan, de keuze na loslaten en de onzekerheid achteraf verantwoorden.'),
 ('mijn goedgekeurde plan begint pas NA handcontact en omvat een veilige stop.','mijn v(t′)-grafiek onderbouwt teken van a en de grenzen van het stopmoment.'),
 'Keurt nulstip, risico’s en bereik goed vóór de eerste band; laat twijfel over het keerpunt bespreken.'),
 Target('13 F','Vrije val als benadering van een eenparig versnelde beweging kwantificeren.',(1,2,3),
 ('g uit de rico van v(t′) met eenheid bepalen zonder v/t te verwarren met a.','een numeriek verschil met 9,81 m/s² koppelen aan een plausibele meetfout.'),
 ('mijn bandje en tabel bewijzen het gebruikte 0,020 s-interval.','ik vergelijk mijn gemeten g en de referentiewaarde met een berekening.'),
 'Check opvangzone en getekende tijdrichting; bespreek bandwrijving vóór de fit.'),
 Target('13 F (toepassing)','Snelheid en versnelling bij een verticale EVRB met twee meetmethoden analyseren.',(1,2,3),
 ('beide camera’s en de Tracker-schaal ten opzichte van hetzelfde y=0 instellen.','het verschil tussen voorspelde en uit video bepaalde toppunthoogte evalueren.'),
 ('ik lever de twee ruwe metingen én een Tracker-reeks met correcte schaal.','ik benoem een verschil tussen methoden en een toetsbare oorzaak.'),
 'Vraag na kalibratie het beeld van bal en meetlat in hetzelfde vlak te tonen.'),
 Target('14 F; 13 F (componenten)','Horizontale worp in x- en y-componenten kwantificeren en een veilige opvangpositie ontwerpen.',(1,2,3,4),
 ('twee haalbare posities/marges voor de bestaande zachte opvangbak te ontwerpen met x≈v₀√(2h/g).','één ontwerp tegen de bestaande videodata te toetsen, een tekort vast te stellen en een betere versie te evalueren.'),
 ('mijn schets vergelijkt twee posities en vermeldt h, v₀, berekende landingsplaats en marge.','ik toets vóór/na-beslissing aan videometing en onzekerheid, zonder een onveilige extra worp.'),
 'Keur eerst video-opstelling en beide opvangvarianten goed; geef tussentijdse feedback op het model. Beoordeel de ontwerpwijziging, niet alleen een mooie baan.'),
 Target('14 F (2D-ondersteuning)','Een gebogen spoor modelleren met x/y-coördinaten; geen bewijs voor alle horizontale-worpinhouden.',(1,2,3),
 ('het nulpunt en de assen voor alle drie hellingen consequent te bewaren.','y(x²) met de drie originele sporen te toetsen zonder afwijkende punten te verbergen.'),
 ('mijn drie sporen en de vooraf bepaalde meetafstanden zijn controleerbaar.','ik vergelijk mijn drie fits en verantwoord een afwijkende stip.'),
 'Controleer beschermpapier, schaal en nulpunten vóór de tweede spoorreeks.'),
 Target('12 F; 13 F','Newtons tweede wet met variërende kracht/massa onderzoeken; v(t′) gebruiken voor a.',(1,2,3),
 ('de nettokracht en totale bewegende massa in beide klassikale vergelijkingen expliciet te houden.','de twee gezamenlijke fits inclusief spreiding en wrijvingsinvloed uit te leggen.'),
 ('beide eigen bandjes én twee volledige klassentabellen zijn terug te vinden.','ik beschrijf het verschil tussen a(F) en a(1/m) met eenheden.'),
 'Controleer één ruwe rit per groep en laat groepen elkaar massa- en krachteenheden controleren.'),
 Target('12 F (vectoriële kracht)','Krachten als vectoren samenstellen en de resultante in een dynamisch model toetsen.',(1,2,3),
 ('een schaal/hoek te kiezen vóór de constructie van het parallellogram.','te bepalen of het verschil tussen constructie en dynamometer binnen afleesfout past.'),
 ('mijn tekening bevat schaal, richting, zin en alle drie de krachtwaarden.','ik kan uitleggen waarom twee groottes niet zonder meer optellen.'),
 'Controleer een getekende hoek vóór het meten; geef directe feedback op pijlrichting.'),
 Target('15 F','Hoeksnelheid, baansnelheid en centripetale beweging bij twee echte systemen vergelijken.',(1,2,3),
 ('twee plaatstralen bij éénzelfde T en ω met verschillende v te verbinden.','de onzekerheid van de gemeten omlooptijd met minstens één herhaling te schatten.'),
 ('de trein is gestabiliseerd en beide plaatmarkeringen zijn gemeten.','ik kan r, T, f, ω en v met de juiste eenheid berekenen.'),
 'Laat vóór het meten voorspellen welke van ω en v per plaatstraal verandert.'),
 Target('15 F','De naar het middelpunt gerichte kracht met metingen aan een rubberstop kwantificeren.',(1,2,3),
 ('het effect van een wisselende straal op de berekende centripetale kracht te voorspellen.','F_cp met m′g voor vijf hangmassa’s inclusief procentuele afwijking te vergelijken.'),
 ('mijn veiligheidscontrole en vijf gelabelde rijen zijn volledig.','ik motiveer wanneer m′g geen exacte waarde voor F_cp is.'),
 'Check bril, buis en draaimarkeringen vóór starten; laat een meetpunt samen narekenen.'),
 Target('18 F','Periode en veerconstante vergelijken met het model van een harmonische trilling.',(1,2,3),
 ('k voor elke veer uit statische rek apart te bepalen.','het verschil tussen T_berek en T_gem bij de lichtste massa te verklaren.'),
 ('beide oorspronkelijke massareeksen hebben aparte k-waarden en t₂₀.','ik laat formule, eenheid en twee concrete foutbronnen bij een afwijking zien.'),
 'Vergelijk vóór de tweede veer de gekozen nulstand en de 20 volledige cycli.'),
 Target('18 F','Een halve trilling met getekende y(t) en v(t′) aan een model toetsen.',(1,2,3),
 ('de evenwichtspositie en positieve/negatieve uitwijkingen op het carbonlint vast te leggen.','v_max uit A en T met de gemeten maximale |v| te vergelijken.'),
 ('mijn bandje en tabel gebruiken y(t) en t′ direct links van v.','ik herken op de grafiek waarom v maximaal is nabij y=0.'),
 'Controleer de evenwichtsmarkering en het teken van y vóór de leerling Excel opent.'),
 Target('18 F; 6 S (oefencyclus)','De trilling van een onbekende massa binnen een eigen goedgekeurd onderzoeksplan analyseren.',(1,2,3),
 ('een methode zonder balans vooraf te kiezen en te onderbouwen met T²(m).','de negatieve asafsnede en invloed van de meebewegende veermassa kritisch te bespreken.'),
 ('mijn eigen plan houdt de onbekende massa op dezelfde veer.','ik geef een geschatte massa met eenheid én onderbouwde onzekerheid.'),
 'Keur massa-/veerbelasting en variabelen goed vóór meten; bespreek extrapolatie tijdens verwerking.'),
 Target('18 F','De slinger met variaties in hoek, bolmassa en lengte aan T=2π√(l/g) toetsen.',(1,2,3),
 ('bij kleine hoek de rol van amplitude en massa met spreiding te vergelijken.','g uit de rico van T²(l), niet van T(l), met eenheid te berekenen.'),
 ('drie delen en herhalingen staan in de oorspronkelijke tabellen.','ik kan de lineaire T²(l)-fit en g=4π²/rico toelichten.'),
 'Controleer de lengte tot het massamiddelpunt en de kleine hoek vóór klokmetingen.'),
 Target('18 F (resonantie)','De vrije eigenfrequentie en gedwongen resonantiecurve analyseren.',(1,2,3),
 ('dezelfde gedempte opstelling bij acht frequenties met dichtere punten rond piek te meten.','het verschil tussen modelpiek en gemeten piek met demping te verklaren.'),
 ('mijn tabel houdt waterdiepte constant en meet f en A op hetzelfde moment.','ik vergelijk resonantiepiek en eigenfrequentie met een getal.'),
 'Laat groepen voor de motormeting formuleren wat de constante waterdiepte doet.'),
 Target('19 F; 21 F (buiging/interferentie)','Lopende golven met v=λf en grafische interferentie/buiging verklaren; geen 22 F-claim.',(1,2,3),
 ('appletbeelden en vijf fysieke experimenten met dezelfde schetsconventie te vergelijken.','een verschil tussen twee bronnen als modelbeperking te benoemen.'),
 ('ik bewaar tien beelden én bewijs per fysiek experiment.','ik onderscheid buiging bij een smalle/brede opening met eigen waarneming.'),
 'Toon eerst aan hoe de projectieschaal werkt; vraag naar coherentie bij proef 5.'),
 Target('22 F; 19 F (achtergrond)','Staande golven uit voortplanting/terugkaatsing met knopen en buiken verklaren.',(1,2,3),
 ('bij n=1…4 het aantal buiken, λ=2L/n en v=fλ te bepalen.','de benadering van constante golfsnelheid kritisch met vier rijen te toetsen.'),
 ('mijn foto of schets markeert knopen en buiken per modus.','ik laat voor één rij een berekening en passende eenheid zien.'),
 'Laat voor het verhogen van f eerst een knoop en buik aanwijzen.'),
 Target('20 F; 21 F (geluid als golf)','Zweving, Doppler en klankkleur verklaren en de decibelschaal verantwoord interpreteren.',(1,2,3,5),
 ('uit 437 en 443 Hz de zwevingsfrequentie te berekenen en ΔL=10 dB als tienvoudige intensiteit te herkennen.','voor een concrete geluidsuitdaging twee maatregelen vanuit akoestiek, technologie en sociale gevolgen af te wegen.'),
 ('ik documenteer veilige geluidsinstelling, schermafbeeldingen en een dB-berekening.','mijn maatschappelijk advies noemt twee betrokkenen, cijfers, afweging en een beperking.'),
 'Bespreek eerst luidheid versus intensiteit en laat bij het advies een andere betrokkene tegenargumenten formuleren.'),
 Target('21 F; 23 F (EM-golf)','Interferentie aan roosters van laserlicht met hoeken en golflengtes kwantificeren.',(1,2,3),
 ('verschillende ordes aan vier roosters links en rechts met het centrale maximum te vergelijken.','onzichtbare hogere ordes en asymmetrie uit nλ=a sin θ te verklaren.'),
 ('mijn maxima staan met n, l, y en a genoteerd.','ik vergelijk de vier gevonden λ-waarden en motiveer onzekerheid.'),
 'Laat een laserbundelstop controleren en één hoekberekening vóór de reeks narekenen.'),
 Target('21 F; 23 F (EM-golf)','CD-sporen als rooster met een bekend golflengtemodel kwantificeren.',(1,2,3),
 ('a uit veilige CD-maxima zonder beschadiging van de CD te berekenen.','aantal en lengte van sporen met een onderbouwde spiraalbenadering te schatten.'),
 ('ik noteer twee ringstralen, maxima, berekening en eenheid.','ik bespreek waarom de cirkelbenadering niet exact is.'),
 'Check intacte CD en richting van de reflectie vóór het inschakelen van de laser.'),
 Target('21 F (diffractie); 23 F (EM-golf)','Witlichtdiffractie en verschillen tussen continu en lijnenspectrum verklaren.',(1,2,3),
 ('twee roosterreeksen met kleurgrenzen op gelijke wijze te registreren.','de resolutie van de kleurrand van een gasontladingslijn te onderscheiden.'),
 ('mijn acht kleurvelden en schets van beide spectra zijn aanwezig.','ik kan met nλ=a sin θ voorspellen waarom rood verder ligt.'),
 'Leg vooraf uit dat de eventuele kwiklamp uitsluitend een afgeschermde docentdemonstratie is.'),
 Target('21 F (breking); 23 F (EM-context)','Lichtbreking via stralendiagram en sin α/sin β in een EM-context verklaren.',(1,2,3),
 ('uit zes hoekparen de brekingsindex met spreiding te bepalen.','een gedeelde systematische nul-/speldfout van toevallige afwijking te onderscheiden.'),
 ('mijn tekening bevat normaal, grensvlak en twee kijkposities.','ik kan n met eenhedenloos resultaat en meetonzekerheid verantwoorden.'),
 'Controleer de normaal en twee speldenbeelden voordat de zes hoeken worden gemeten.'),
 Target('6 S (#); F-LPD volgens gekozen vraag','De volledige OVUR-onderzoekscyclus met een inhoud uit dit leerplan zelfstandig doorlopen.',(1,2,3,6),
 ('een eigen relevante fysicavraag en herhaalbaar plan met vijf meetwaarden en drie herhalingen vooraf te laten toetsen.','op een poster alle zeven onderzoeksfasen, databetrouwbaarheid, reflectie en bronnen traceerbaar te maken.'),
 ('vraag, hypothese, goedkeuring, ruwe data, analyse en poster zijn terug te vinden.','mijn poster beantwoordt de eigen vraag met data, onzekerheid en een volgende test.'),
 'Geef schriftelijk groen licht vóór uitvoering, een tussentijds datagesprek en na de poster feedforward per leerling.'),
]
assert len(T)==25
assert set().union(*(set(t.stem) for t in T))==set(STEM)
STEM_BORGING={1:(4,7,15,25),2:(2,3,9,16,25),3:(5,12,21,25),4:(7,),5:(20,),6:(25,)}
