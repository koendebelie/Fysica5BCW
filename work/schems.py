# -*- coding: utf-8 -*-
"""Eenvoudige schematische figuren (opstellingen) voor de labocursus 6BCW."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
W, H = 900, 460
BG = "#FFFFFF"
INK = "#1F1F1F"
ACC = "#1F4E79"
RED = "#C62828"
GREEN = "#2E7D32"
GREY = "#9E9E9E"


def _font(sz, bold=False):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else ""),
              "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


F = _font(17)
FB = _font(17, True)
FS = _font(14)


class Fig:
    def __init__(self, w=W, h=H):
        self.w, self.h = w, h
        self.im = Image.new("RGB", (w, h), BG)
        self.d = ImageDraw.Draw(self.im)

    def line(self, a, b, col=INK, w=2):
        self.d.line([a, b], fill=col, width=w)

    def dash(self, a, b, col=GREY, w=1, seg=9, gap=6):
        import math
        x1, y1 = a
        x2, y2 = b
        L = max(1.0, ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
        n = int(L // (seg + gap)) + 1
        for i in range(n):
            t0 = i * (seg + gap) / L
            t1 = min(1.0, t0 + seg / L)
            self.line((x1 + (x2 - x1) * t0, y1 + (y2 - y1) * t0),
                      (x1 + (x2 - x1) * t1, y1 + (y2 - y1) * t1), col, w)

    def arrow(self, a, b, col=ACC, w=2, head=9):
        import math
        self.line(a, b, col, w)
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        for s in (ang + 2.6, ang - 2.6):
            self.line(b, (b[0] + head * math.cos(s), b[1] + head * math.sin(s)), col, w)

    def rect(self, box, fill=None, outline=INK, w=2):
        self.d.rectangle(box, fill=fill, outline=outline, width=w)

    def ellipse(self, box, fill=None, outline=INK, w=2):
        self.d.ellipse(box, fill=fill, outline=outline, width=w)

    def poly(self, pts, fill=None, outline=INK, w=2):
        self.d.polygon(pts, fill=fill, outline=outline)

    def arc(self, box, start, end, fill=ACC, width=2):
        self.d.arc(box, start, end, fill=fill, width=width)

    def text(self, xy, t, font=None, col=INK, anchor="la"):
        self.d.text(xy, t, font=font or F, fill=col, anchor=anchor)

    def axis(self, org, xlen, ylen, xlab="t (s)", ylab="y", col=INK):
        x0, y0 = org
        self.arrow((x0, y0), (x0 + xlen, y0), col, 2)
        self.arrow((x0, y0), (x0, y0 - ylen), col, 2)
        self.text((x0 + xlen + 6, y0 + 2), xlab, FS, col)
        self.text((x0, y0 - ylen - 4), ylab, FS, col, anchor="lb")

    def save(self, name):
        p = os.path.join(OUT, name)
        self.im.save(p)
        return p


# ------------------------------------------------------------------ figuren
def helling_sensor():
    f = Fig()
    f.line((60, 380), (840, 380), INK, 3)                 # tafel
    f.poly([(120, 380), (760, 230), (760, 244), (120, 394)], fill="#DCE6F1", outline=INK)  # helling
    # wagentje
    f.rect((300, 268, 372, 306), fill="#FFF0C2", outline=INK)
    f.ellipse((306, 300, 320, 314), fill=INK)
    f.ellipse((352, 300, 366, 314), fill=INK)
    # sensor
    f.rect((92, 196, 176, 250), fill="#E8F1FA", outline=ACC, w=2)
    f.text((134, 223), "sensor", FS, ACC, anchor="mm")
    for dx in (0, 14, 28):
        f.arc((170 + dx, 206, 210 + dx, 246), 300, 60, fill=ACC, width=2)
    f.arrow((250, 320), (420, 320), GREEN, 2)
    f.text((335, 330), "v", FB, GREEN, anchor="mm")
    f.text((700, 214), "helling / luchtbaan", FS)
    f.text((150, 400), "bewegingssensor of gsm-camera", FS, GREY)
    f.save("sch_helling_sensor.png")


def worp():
    f = Fig()
    f.line((60, 150), (330, 150), INK, 3)                  # tafelblad
    f.line((60, 150), (60, 390), INK, 3)
    for y in range(160, 390, 26):                          # parabolische baan
        pass
    import math
    pts = []
    for i in range(0, 61):
        t = i / 60
        x = 330 + 480 * t
        y = 150 + 0.5 * 9.81 * (t * 0.62) ** 2 * 260
        pts.append((x, min(y, 385)))
    f.d.line(pts, fill=ACC, width=2, joint="curve")
    for i in range(1, 6):
        p = pts[i * 10]
        f.ellipse((p[0] - 5, p[1] - 5, p[0] + 5, p[1] + 5), fill=ACC)
    f.arrow((330, 150), (430, 150), GREEN, 2)
    f.text((380, 132), "v₀", FB, GREEN, anchor="mm")
    f.dash((330, 150), (330, 385), GREY)
    f.dash((810, 150), (810, 385), GREY)
    f.arrow((330, 368), (810, 368), RED, 2)
    f.text((570, 356), "reikwijdte x", FS, RED, anchor="mm")
    f.arrow((790, 150), (790, 385), RED, 2)
    f.text((800, 268), "h", FS, RED, anchor="lm")
    f.text((120, 140), "tafel", FS)
    f.save("sch_worp.png")


def kracht_wagentje():
    f = Fig()
    f.line((70, 340), (830, 340), INK, 3)
    f.rect((300, 292, 420, 336), fill="#FFF0C2", outline=INK)     # wagentje
    f.ellipse((310, 330, 326, 346), fill=INK)
    f.ellipse((394, 330, 410, 346), fill=INK)
    f.text((360, 312), "m", FS, anchor="mm")
    # katrol
    f.ellipse((770, 300, 812, 342), fill="#E8F1FA", outline=ACC, w=2)
    f.text((791, 321), "◦", FS, ACC, anchor="mm")
    f.line((812, 300), (812, 240), INK, 2)
    f.line((740, 240), (812, 240), INK, 2)
    f.line((420, 314), (770, 306), INK, 2)                        # draad
    f.rect((756, 342, 786, 402), fill="#E0E0E0", outline=INK)      # gewichtje
    f.text((771, 372), "mₕ", FS, anchor="mm")
    f.arrow((500, 306), (560, 306), GREEN, 2)
    f.text((530, 292), "F", FB, GREEN, anchor="mm")
    f.arrow((360, 400), (470, 400), ACC, 2)
    f.text((415, 414), "a", FB, ACC, anchor="mm")
    # fotopoorten
    for x in (500, 690):
        f.line((x, 240), (x, 340), RED, 3)
        f.line((x, 240), (x + 60, 240), RED, 3)
        f.line((x + 60, 240), (x + 60, 340), RED, 3)
    f.text((530, 224), "fotopoort 1", FS, RED)
    f.text((720, 224), "fotopoort 2", FS, RED)
    f.save("sch_kracht_wagentje.png")


def wrijving():
    f = Fig(860, 430)
    f.poly([(90, 340), (700, 130), (700, 148), (90, 358)], fill="#DCE6F1", outline=INK)
    f.rect((330, 176, 430, 226), fill="#FFF0C2", outline=INK)   # blok (schuin)
    f.text((380, 200), "m", FS, anchor="mm")
    f.arrow((430, 196), (560, 150), RED, 2)                    # dynamometer
    f.text((575, 140), "dynamometer", FS, RED, anchor="lm")
    # hoek
    f.arc((90 - 70, 340 - 70, 90 + 70, 340 + 70), 340, 360, fill=ACC, width=2)
    f.text((150, 330), "α", F, ACC, anchor="lm")
    f.dash((90, 340), (700, 340), GREY)
    f.arrow((380, 226), (380, 300), GREEN, 2)
    f.text((392, 268), "Fz = m·g", FS, GREEN, anchor="lm")
    f.arrow((380, 226), (300, 176), ACC, 2)
    f.text((300, 160), "Fw", FS, ACC, anchor="rm")
    f.arrow((380, 226), (330, 250), RED, 2)
    f.text((326, 262), "Fn", FS, RED, anchor="rm")
    f.save("sch_wrijving.png")


def val_fluïdum():
    f = Fig(760, 470)
    f.line((80, 60), (80, 420), INK, 3)
    f.line((300, 60), (300, 420), INK, 3)
    # maatcilinder
    f.rect((120, 90, 260, 400), outline=ACC, w=3)
    f.rect((120, 150, 260, 400), fill="#BBDEFB", outline=ACC)     # vloeistof
    for y in range(160, 400, 40):
        f.line((120, y), (145, y), ACC, 2)
        f.text((152, y), str((400 - y) // 4 * 5), FS, GREY, anchor="lm")
    # bollen
    for y, col in ((200, INK), (270, INK), (340, INK)):
        f.ellipse((175, y, 205, y + 30), fill=col)
    f.arrow((215, 215), (215, 265), RED, 2)
    f.text((228, 240), "v", FS, RED, anchor="lm")
    f.text((80, 40), "valbuizen / maatcilinder met glycerol", FS, GREY, anchor="lm")
    f.save("sch_val_fluidum.png")


def veerpistool():
    f = Fig(860, 380)
    f.line((70, 300), (800, 300), INK, 3)
    f.line((70, 300), (70, 250), INK, 6)                      # wand
    for x in range(90, 210, 14):                              # veer
        f.line((x, 250), (x + 8, 292), INK, 2)
        f.line((x + 8, 292), (x + 16, 250), INK, 2)
    f.text((150, 226), "veer, k", FS, anchor="mm")
    f.rect((230, 264, 330, 300), fill="#FFF0C2", outline=INK)   # wagentje/kogel
    f.ellipse((240, 294, 256, 310), fill=INK)
    f.ellipse((304, 294, 320, 310), fill=INK)
    f.arrow((340, 282), (470, 282), GREEN, 2)
    f.text((405, 266), "v", FB, GREEN, anchor="mm")
    f.dash((70, 282), (230, 282), RED)
    f.arrow((80, 328), (230, 328), RED, 2)
    f.arrow((230, 328), (80, 328), RED, 2)
    f.text((155, 344), "x (indrukking)", FS, RED, anchor="mm")
    f.save("sch_veerpistool.png")


def conische_slinger():
    f = Fig(700, 470)
    f.line((350, 40), (350, 130), INK, 3)                      # statief
    f.line((330, 130), (370, 130), INK, 3)
    f.line((350, 130), (500, 210), INK, 2)                     # draad
    f.ellipse((490, 200, 530, 240), fill="#FFF0C2", outline=INK)  # massa
    f.text((510, 220), "m", FS, anchor="mm")
    f.line((500, 240), (500, 300), INK, 2)                     # tweede draad
    f.rect((478, 300, 522, 352), fill="#E0E0E0", outline=INK)   # gewichtje
    f.text((500, 326), "M", FS, anchor="mm")
    f.dash((350, 130), (350, 300), GREY)
    f.dash((350, 300), (500, 300), GREY)
    f.text((420, 312), "r", FS, GREY, anchor="mm")
    f.ellipse((350, 210, 650, 330), outline=GREY)
    f.dash((350, 270), (350, 340), GREY)
    f.text((365, 352), "draai-as", FS, GREY)
    f.arrow((510, 260), (510, 300), GREEN, 2)
    f.text((526, 282), "v", FS, GREEN, anchor="lm")
    f.save("sch_conische_slinger.png")


def massa_veer():
    f = Fig(700, 470)
    f.line((120, 60), (120, 120), INK, 3)
    f.line((90, 120), (330, 120), INK, 5)
    for i in range(9):
        x = 150 + i * 20
        f.line((x, 120), (x + 10 if i % 2 == 0 else x - 10, 170), INK, 2)
        f.line((x + 10 if i % 2 == 0 else x - 10, 170), (x + 20, 220), INK, 2)
    f.rect((300, 220, 380, 272), fill="#FFF0C2", outline=INK)
    f.text((340, 246), "m", FS, anchor="mm")
    f.dash((120, 120), (120, 420), GREY)
    f.dash((340, 272), (340, 420), GREY)
    f.line((120, 400), (340, 400), GREY, 1)
    f.text((230, 412), "evenwichtsstand", FS, GREY, anchor="mm")
    f.arrow((340, 300), (340, 380), GREEN, 2)
    f.arrow((340, 380), (340, 300), GREEN, 2)
    f.text((352, 340), "A (amplitude)", FS, GREEN, anchor="lm")
    f.save("sch_massa_veer.png")


def slinger():
    f = Fig(700, 470)
    f.line((150, 40), (550, 40), INK, 5)
    f.line((350, 40), (350, 70), INK, 2)
    f.line((350, 70), (420, 300), INK, 2)
    f.ellipse((404, 290, 436, 322), fill="#FFF0C2", outline=INK)
    f.text((420, 306), "m", FS, anchor="mm")
    f.dash((350, 70), (350, 400), GREY)
    f.dash((420, 306), (420, 400), GREY)
    f.line((350, 380), (420, 380), GREY, 1)
    f.text((385, 392), "A", FS, GREY, anchor="mm")
    f.arc((330, 70, 400, 140), 0, 60, fill=ACC, width=2)
    f.text((400, 120), "θ", F, ACC, anchor="lm")
    f.line((350, 70), (350, 70), INK)
    f.dash((350, 70), (350, 306), GREY)
    f.text((300, 200), "l", F, GREEN, anchor="rm")
    f.arrow((330, 190), (352, 190), GREEN, 2)
    f.save("sch_slinger.png")


def golfbak():
    f = Fig(900, 420)
    f.rect((80, 120, 820, 300), outline=INK, w=3)
    f.rect((95, 200, 805, 300), fill="#BBDEFB", outline="#90CAF9")
    import math
    pts = [(95 + i * 4, 250 - 30 * math.sin(i * 0.25)) for i in range(178)]
    f.d.line(pts, fill=ACC, width=2)
    f.text((450, 160), "golfbak met water", FS)
    f.arrow((95, 100), (805, 100), RED, 2)
    f.arrow((805, 100), (95, 100), RED, 2)
    f.text((450, 82), "golflengte λ", FS, RED, anchor="mm")
    f.text((100, 330), "trilbron / golfwekker", FS, GREY)
    f.line((60, 120), (60, 300), INK, 3)
    f.save("sch_golfbak.png")


def melde():
    f = Fig(900, 380)
    f.line((60, 300), (840, 300), INK, 3)
    f.rect((90, 120, 130, 300), fill="#E8F1FA", outline=ACC, w=2)   # triller
    f.text((110, 200), "trilbron", FS, ACC)
    f.line((130, 200), (760, 200), INK, 2)
    f.ellipse((760, 180, 790, 220), fill="#E0E0E0", outline=INK)    # katrol
    f.line((790, 200), (790, 140), INK, 2)
    f.line((760, 140), (830, 140), INK, 2)
    f.rect((800, 140, 840, 190), fill="#E0E0E0", outline=INK)
    f.text((820, 165), "m", FS, anchor="mm")
    import math
    for k, (amp, col) in enumerate(((38, ACC), (0, GREY))):
        pts = [(130 + i * 3, 200 + amp * math.sin(i * 0.11)) for i in range(211)]
        f.d.line(pts, fill=col, width=2)
    f.text((450, 250), "staande golf: knopen (•) en buiken", FS)
    for x in (130, 325, 520, 715):
        f.ellipse((x - 4, 196, x + 4, 204), fill=RED)
    f.text((230, 120), "L", F, GREEN, anchor="mm")
    f.save("sch_melde.png")


def resonantie():
    f = Fig(900, 430)
    f.line((100, 60), (500, 60), INK, 5)
    f.line((300, 60), (300, 90), INK, 2)
    f.text((300, 40), "aandrijving (motor met excenter)", FS, GREY, anchor="mm")
    for i in range(7):
        x = 150 + i * 24
        f.line((x, 90), (x + 12 if i % 2 == 0 else x - 12, 150), INK, 2)
        f.line((x + 12 if i % 2 == 0 else x - 12, 150), (x + 24, 210), INK, 2)
    f.rect((280, 210, 360, 262), fill="#FFF0C2", outline=INK)
    f.text((320, 236), "m", FS, anchor="mm")
    f.dash((150, 90), (150, 380), GREY)
    f.arrow((320, 300), (320, 360), GREEN, 2)
    f.arrow((320, 360), (320, 300), GREEN, 2)
    f.text((336, 330), "A", FS, GREEN, anchor="lm")
    f.text((600, 120), "frequentie f instelbaar", FS, GREY)
    f.arrow((560, 140), (420, 190), GREY, 2)
    f.save("sch_resonantie.png")


def geluid_buis():
    f = Fig(880, 400)
    f.rect((120, 140, 420, 200), outline=INK, w=3)            # buis
    f.rect((540, 120, 600, 380), outline=INK, w=3)            # reservoir
    f.rect((545, 230, 595, 380), fill="#BBDEFB", outline="#90CAF9")
    f.line((420, 170), (540, 170), INK, 2)
    f.text((150, 122), "glazen buis", FS)
    f.ellipse((100, 130, 140, 210), fill="#FFF0C2", outline=INK)
    f.text((120, 100), "stemvork f", FS, anchor="mm")
    f.arrow((145, 170), (200, 170), ACC, 2)
    f.dash((120, 240), (420, 240), GREY)
    f.text((270, 256), "lengte l van de luchtkolom", FS, GREY, anchor="mm")
    f.text((620, 240), "waterreservoir: niveau verstelbaar", FS, GREY)
    f.save("sch_geluid_buis.png")


def rooster():
    f = Fig(900, 420)
    f.rect((70, 190, 110, 230), fill="#FFF0C2", outline=INK)   # laser
    f.text((90, 165), "laser", FS, anchor="mm")
    f.line((110, 210), (300, 210), RED, 2)
    f.line((300, 150), (300, 270), INK, 4)                    # rooster
    for y in range(150, 275, 12):
        f.ellipse((297, y, 303, y + 6), fill="#FFFFFF")
    f.text((300, 130), "rooster", FS, anchor="mm")
    f.line((300, 210), (830, 90), RED, 2)
    f.line((300, 210), (830, 210), RED, 2)
    f.line((300, 210), (830, 330), RED, 2)
    f.rect((760, 60, 790, 360), outline=INK, w=2)
    f.text((775, 40), "scherm", FS, anchor="mm")
    for y in (90, 210, 330):
        f.ellipse((y and 0 or 0, 0, 0, 0), fill=RED)
    for y in (90, 210, 330):
        f.rect((770, y - 4, 780, y + 4), fill=RED)
    f.text((600, 380), "L", F, GREEN, anchor="mm")
    f.save("sch_rooster.png")


def energie_achtbaan():
    f = Fig(900, 420)
    import math
    pts = []
    for i in range(0, 181):
        t = i / 180
        x = 70 + 760 * t
        y = 330 - 170 * (0.5 - 0.5 * math.cos(2 * math.pi * t)) ** 0.9
        pts.append((x, y))
    f.d.line(pts, fill=ACC, width=3, joint="curve")
    f.line((70, 340), (830, 340), INK, 2)
    f.ellipse((120, 140, 150, 170), fill="#FFF0C2", outline=INK)
    f.text((135, 118), "h₁", FS, anchor="mm")
    f.ellipse((430, 320, 460, 350), fill="#FFF0C2", outline=INK)
    f.text((445, 300), "h₂", FS, anchor="mm")
    f.dash((70, 340), (830, 340), GREY)
    f.text((450, 372), "referentiehoogte (h = 0)", FS, GREY, anchor="mm")
    f.save("sch_energie_achtbaan.png")


def valproef():
    f = Fig(760, 470)
    f.line((100, 40), (100, 430), INK, 3)
    f.ellipse((330, 60, 366, 96), fill="#FFF0C2", outline=INK)
    f.dash((348, 96), (348, 400), RED)
    for y, lab in ((130, "fotopoort 1"), (270, "fotopoort 2")):
        f.line((280, y), (280, y + 34), ACC, 3)
        f.line((280, y), (420, y), ACC, 3)
        f.line((420, y), (420, y + 34), ACC, 3)
        f.text((430, y + 8), lab, FS, ACC)
    f.arrow((300, 110), (300, 240), RED, 2)
    f.text((262, 175), "Δx", FS, RED, anchor="rm")
    f.text((120, 30), "valopstelling met twee fotopoorten", FS, GREY, anchor="lm")
    f.text((360, 430), "vloer / vangnet", FS, GREY, anchor="lm")
    f.save("sch_valproef.png")


def lichtbreking():
    f = Fig(800, 430)
    f.rect((290, 130, 560, 310), fill="#E8F1FA", outline=ACC)
    f.line((150, 65), (360, 130), RED, 3)
    f.line((360, 130), (440, 310), RED, 3)
    f.line((440, 310), (660, 375), RED, 3)
    f.dash((360, 40), (360, 370), GREY)
    f.text((315, 75), "α", FB, ACC);f.text((387, 165), "β", FB, ACC)
    f.text((300, 110), "lucht", FS);f.text((420, 220), "plexiglas", FS)
    f.text((555, 325), "uitgaande straal", FS)
    f.ellipse((192,73,204,85),fill=INK);f.ellipse((240,89,252,101),fill=INK)
    f.ellipse((595,351,607,363),fill=INK)
    f.text((160, 90), "speld 1", FS);f.text((240, 120), "speld 2", FS)
    f.text((595, 340), "speld 3", FS)
    f.save('sch_lichtbreking.png')


def hefboom():
    f=Fig(800,370)
    f.line((110,170),(690,170),INK,5)
    f.poly([(375,245),(425,245),(400,175)],fill="#E8F1FA",outline=INK)
    f.rect((140,170,195,220),fill="#FFF0C2",outline=INK)
    f.text((168,235),'last Fₗ',FS,anchor='mm')
    f.arrow((625,170),(625,240),GREEN,2)
    f.text((640,240),'macht Fₘ',FS)
    f.arrow((180,110),(400,110),ACC,2)
    f.text((290,90),'dₗ',FS,ACC,anchor='mm')
    f.arrow((400,110),(625,110),RED,2)
    f.text((512,90),'dₘ',FS,RED,anchor='mm')
    f.save('sch_hefboom.png')


def geluid():
    import math
    f=Fig(900,350)
    f.axis((80,180),740,120,'t (s)','uitwijking')
    pts1=[];pts2=[];pts3=[]
    for x in range(80,800,2):
        a=55*math.sin((x-80)/38)
        pts1.append((x,180-a));pts2.append((x,180+a));pts3.append((x,180))
    f.d.line(pts1,fill=ACC,width=2)
    f.d.line(pts2,fill=RED,width=2)
    f.d.line(pts3,fill=GREEN,width=3)
    f.text((130,275),'tegenfase: som bijna nul',FS,GREEN)
    f.save('sch_geluid.png')


def cd_sporen():
    """CD-spiraal als optisch rooster; zonder de onveilige krasinstructie op het oude bronplaatje."""
    f=Fig(800,360)
    cx,cy=225,175
    for r in (38,50,63,76,89,102,115,128):
        f.ellipse((cx-r,cy-r,cx+r,cy+r),outline=ACC if r%2 else GREEN,w=2)
    f.ellipse((cx-35,cy-35,cx+35,cy+35),fill=BG,outline=GREY,w=2)
    f.arrow((cx+42,cy),(cx+123,cy),RED,3)
    f.text((390,120),'r binnen',FS)
    f.text((390,165),'spoorafstand a (schematisch vergroot)',FS)
    f.text((390,212),'r buiten',FS)
    f.text((390,270),'N ≈ (r buiten − r binnen) / a',FB,ACC)
    f.save('sch_cd_sporen.png')


def verticale_worp_tweecamera():
    """Privacyvriendelijk overzicht van de ECHTE tweecamera-opstelling (bron p. 16–20)."""
    f=Fig(900,460)
    f.line((100,380),(800,380),INK,3)
    f.text((650,390),'vloer: y = 0',FS)
    f.line((560,75),(560,382),INK,3)
    for y,lab in [(355,'0,3 m'),(265,'0,6 m'),(175,'0,9 m'),(85,'1,2 m')]:
        f.line((548,y),(572,y),INK,2);f.text((577,y),lab,FS,anchor='lm')
    f.ellipse((425,340,451,366),fill='#FFF0C2',outline=INK)
    f.arrow((438,335),(438,85),GREEN,3)
    f.text((365,75),'top y_max',FB,ACC)
    f.text((400,373),'loslaatpositie y₀',FS,ACC,anchor='rb')
    f.rect((115,70,210,120),fill='#E8F1FA',outline=ACC)
    f.text((162,96),'camera 1',FS,ACC,anchor='mm')
    f.dash((212,96),(438,90),GREY)
    f.text((120,132),'hoogste punt filmen',FS)
    f.rect((115,285,210,335),fill='#E8F1FA',outline=ACC)
    f.text((162,311),'camera 2',FS,ACC,anchor='mm')
    f.dash((212,311),(438,352),GREY)
    f.text((120,347),'loslaten filmen',FS)
    f.text((495,415),'bal en meetlat even ver van camera',FS,GREEN,anchor='mb')
    f.save('sch_verticale_worp_tweecamera.png')


def luchtbel_twee_standen():
    f=Fig(780,400)
    f.line((205,335),(205,75),ACC,15)
    f.ellipse((198,173,212,188),fill='#E6F7FF',outline=INK)
    f.text((185,55),'90°',FB,ACC)
    f.line((450,335),(625,155),ACC,15)
    f.ellipse((510,267,525,282),fill='#E6F7FF',outline=INK)
    f.text((580,95),'45°',FB,ACC)
    for x,y in [(205,335),(205,95),(450,335),(617,160)]:
        f.ellipse((x-3,y-3,x+3,y+3),fill=RED,outline=RED)
    f.text((205,365),'0–100 cm',FS,anchor='mm')
    f.text((545,365),'dezelfde voorkant van de bel volgen',FS,anchor='mm')
    f.save('sch_luchtbel_twee_standen.png')


def tijdtikker_wagentje():
    f=Fig(800,340)
    f.line((75,270),(735,270),INK,4)
    f.rect((430,175,600,260),fill='#FFF0C2',outline=INK)
    f.ellipse((455,245,482,272),fill=INK)
    f.ellipse((555,245,582,272),fill=INK)
    f.text((515,165),'elektrisch wagentje',FS,ACC,anchor='mm')
    f.rect((95,188,245,258),fill='#E8F1FA',outline=ACC)
    f.text((170,213),'tijdtikker',FS,ACC,anchor='mm')
    f.text((170,241),'50 Hz / 6 V~',FS,ACC,anchor='mm')
    f.line((245,228),(432,228),GREY,7)
    for x in range(265,420,19): f.ellipse((x-2,225,x+2,229),fill=RED)
    f.text((327,200),'papierbandje met carbonlint',FS,ACC,anchor='mm')
    f.arrow((615,215),(690,215),GREEN,3)
    f.text((685,190),'rijrichting',FS,GREEN,anchor='mm')
    f.save('sch_tijdtikker_wagentje.png')


ALL = [helling_sensor, worp, kracht_wagentje, wrijving, val_fluïdum, veerpistool,
       conische_slinger, massa_veer, slinger, golfbak, melde, resonantie,
       geluid_buis, rooster, energie_achtbaan, valproef, lichtbreking, hefboom,
       geluid, cd_sporen, verticale_worp_tweecamera, luchtbel_twee_standen,
       tijdtikker_wagentje]

if __name__ == '__main__':
    for fn in ALL:
        print(fn.__name__, '->', fn())
