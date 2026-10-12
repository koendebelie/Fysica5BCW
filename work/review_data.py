# -*- coding: utf-8 -*-
"""Eindcontrole: gerichte reflectie voor vroeger onderbelichte deelproeven.
Sleutel: (themalabo 1-based, deelproef 1-based); vraag en docentantwoord
worden bewust als paar beheerd, zodat geen vraag zonder correctiesleutel verschijnt.
"""
REFLECTIE = {
 (5,1): [('De klas vindt bij verdubbeling van F niet exact een dubbele a. Vergelijk twee klasrijen met dezelfde totale massa: welk verband ondersteunen ze en welke wrijving of meetspreiding zie je?',
           'Bij dezelfde totale massa is a ongeveer recht evenredig met de nettokracht F. Vergelijk werkelijk de twee a- en F-waarden; wrijving en meetspreiding verstoren de ideale verhouding.')],
 (5,2): [('Wat gebeurt er volgens de klasgegevens met a als m_tot stijgt terwijl F gelijk blijft? Waarom is a tegen 1/m_tot nuttiger dan a tegen m_tot?',
           'a≈F_net/m_tot: bij gelijkblijvende F daalt a als m stijgt. De grafiek a(1/m_tot) is bij benadering lineair; controleer of F werkelijk constant bleef.')],
 (5,3): [('Vergelijk de getekende resultante met de gemeten resultante: wanneer is de afwijking groter dan je teken-/afleesnauwkeurigheid? Waarom mag je de groottes F₁ en F₂ niet altijd zomaar optellen?',
           'Krachten zijn vectoren; alleen bij gelijke richting tel je de groottes op. Vergelijk |F_r,tekening−F_r,gemeten| met de afleesnauwkeurigheid van gradenboog, schaal en dynamometers.')],
 (9,2): [('Wat betekent het snijpunt van T²(m_toegevoegd) met de massa-as? Welke veronderstelling over de veer maakt de berekende onbekende massa systematisch te groot?',
           'Het snijpunt is −m_onbekend in het ideaalmodel; een effectief meetrillende veermassa verschuift het snijpunt, zodat de geschatte onbekende massa te groot kan worden. Extrapolatie is geen meting.')],
 (10,1): [('Verschilt T bij 5° en 10° meer dan de spreiding van je drie herhalingen? Wat mag je over de onafhankelijkheid van amplitude besluiten?',
            'Bij kleine hoeken hoort T binnen de meetspreiding ongeveer gelijk te blijven; vergelijk de concrete herhalingen en claim geen exact nuleffect.')],
 (10,2): [('Verschilt T voor hout en metaal meer dan je meetspreiding als de lengte gelijk blijft? Welke voorwaarde zou een massa-effect kunnen veinzen?',
            'Bij gelijke effectieve lengte en kleine hoek is T massa-onafhankelijk. Een andere lengte tot het massamiddelpunt of luchtweerstand kan verschillen veroorzaken.')],
 (11,1): [('Waarom is de gemeten eigenfrequentie uit de vrije trilling een betere referentie voor deel 2 dan alleen de berekende ideale waarde?',
            'De vrije meting houdt rekening met de werkelijke massa, veer en demping; de berekening vereenvoudigt o.a. de effectieve veermassa. Vergelijk spreiding en f_e=1/T_e.')],
 (12,2): [('Hoe verandert de afstand tussen knopen als je bij dezelfde snaarlengte een hoger aantal buiken n meet? Past de berekende golfsnelheid bij dezelfde snaarspanning ongeveer bij één waarde?',
            'L=nλ/2: bij groter n wordt de knoopafstand λ/2 kleiner. Bij vaste spanning en massa per lengteeenheid is v=f_n·2L/n ongeveer constant binnen de onzekerheid.')],
 (14,1): [('Welke maximumorde verdwijnt het eerst bij grotere golflengte of dichter rooster? Controleer met jouw metingen de grens |sin θ|≤1 en leg de symmetrie van links/rechts uit.',
            'nλ=a sin θ, dus een orde bestaat alleen als nλ≤a; kleinere a of grotere λ beperkt het aantal ordes. Links/rechts is ongeveer symmetrisch rond de nulde orde, verschillen tonen uitlijnfouten.')],
 (14,2): [('Waarom is de schatting van de totale spoorlengte met middelomtrek niet exact? Bespreek de gevoeligheid voor een kleine fout in de gevonden sporenafstand a.',
            'Een CD heeft één spiraal, geen losse concentrische cirkels; ook de spiraalstraal verandert. N≈Δr/a en L≈N·2πr_midden: onderschat/overschat a om een factor geeft de tegengestelde relatieve fout in N en L.')],
 (14,3): [('Welke kleur ligt in de eerste orde bij hetzelfde rooster verder van het centrale wit: rood of violet? Waarom kan de kleurgrens geen exacte golflengte opleveren, en wat toont een kwiklijnenspectrum anders?',
            'Voor n en a gelijk geeft rood (grotere λ) grotere |θ| en |y| dan violet. Kleurgrenzen zijn onscherp en de bron heeft een spectrum; kwik geeft afzonderlijke heldere lijnen i.p.v. een continue kleurenband.')],
 (15,1): [('Waarom moet je bij iedere speldenpositie langs dezelfde kijklijn peilen? Wat gebeurt met de geconstrueerde straal wanneer je oog opzij beweegt?',
            'Een veranderde kijklijn veroorzaakt parallax; de schijnbare uitlijning verschuift en daardoor de geconstrueerde straal en inval-/brekingshoek.')],
 (15,2): [('Vergelijk de zes waarden van sin α/sin β: welke spreiding zie je? Welke gemeenschappelijke fout zou niet verdwijnen door het gemiddelde te nemen?',
            'Voor dezelfde twee stoffen is de verhouding ongeveer constant; vergelijk eigen minimum, maximum en gemiddelde. Een foutieve normaal of nulstand is systematisch en wordt niet uitgemiddeld.')],
 (16,1): [('Welke waarneming in je proefopzet zou je hypothese weerleggen? Welke variabele zou je dan alsnog onder controle moeten houden?',
            'Docentcontrole per gekozen onderzoek: noem een concreet tegengesteld datapatroon en een meetbare storende variabele met een haalbare controle.')],
 (16,2): [('Beantwoordt het patroon van alle herhalingen jouw eigen SMART-vraag? Noem één afwijkende meting, controleer het ruwe bewijs en stel een volgende test voor zonder gegevens weg te laten.',
            'Docentcontrole per gekozen onderzoek: koppel fit/spreiding aan de geformuleerde vraag, bespreek een afwijking met ruwe gegevens en voorstel voor herhaalbare controle; geen achteraf gefingeerde data.')],
}

# Wat specifiek per zelfstandig werkblad als GROEPSPRODUCT wordt verwacht.
PRODUCTBEWIJS = [
 'Tabel voor beide hellingen, x(t)-grafieken en vergelijking van de snelheden.',
 'Origineel bandje, x(t)- en v(t′)-grafiek voor het gelijkmatige baandeel.',
 'Bandje en v(t′)-fit met v₀, versnelling en interpretatie van de asafsneden.',
 'Goedgekeurd open plan, bandje en v(t′)-fit met stopmoment en geldigheidsgebied.',
 'Valbandje, v(t′)-fit en vergelijking van g met de verwachte waarde.',
 'Handmatige meetreeks én Tracker-baan, met vergelijking en videomeetbewijs.',
 'Goedgekeurd meetplan en Tracker-metingen met x(t) en y(t) en grafieken.',
 'Sporen op papier voor drie hellingen, meettabel en toets van y tegen x².',
 'Eigen ritten én gemeenschappelijke a(F)- en a(1/m)-klastabellen met twee grafieken.',
 'Krachtenconstructie op schaal, dynamometermeting en vergelijking met onzekerheid.',
 'Trein én platenspeler: omlooptijden, twee stralen en vergelijking van ω en v.',
 'Rubberstop en vijf hangmassa’s: meetreeks en vergelijking F_cp met F_z.',
 'Twee veren: afzonderlijke k-bepaling, t₂₀ en gemeten/berekende perioden.',
 'Origineel carbonlint van halve trilling, y(t)- en v(t′)-grafiek en v_max.',
 'Eigen goedgekeurde aanpak, T²(m)-grafiek en schatting van onbekende massa zonder balans.',
 'Drie slingerdeelproeven, herhalingen en T²(l)-grafiek met g uit de rico.',
 'Vrije eigenfrequentie en gedwongen A(f)-resonantiecurve met uitleg.',
 'Appletbeelden én foto’s/metingen van de vijf fysieke golfbakexperimenten.',
 'Schets/foto van knopen en buiken voor vier standen met berekening λ en v.',
 'Beelden van tonen/zwevingen, Dopplerschets en vergelijking van harmonischen/klankkleur.',
 'Vier roosterreeksen met maxima links/rechts, λ per rooster en onzekerheid.',
 'CD-maxima, ringstralen, sporenafstand, aantal sporen en spoorlengte.',
 'Twee roosterreeksen met kleurgrenzen én schets van continu en lijnenspectrum.',
 'Schetsen van de speldenlijnen, zes hoekparen en vergelijking van brekingsindexen.',
 'Goedgekeurd plan, originele meettabel/grafiek, wetenschappelijke poster en taakbijdragen.',
]
assert len(PRODUCTBEWIJS)==25
WERKBLAD_PDF={10,18,19,20}
