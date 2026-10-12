# -*- coding: utf-8 -*-
"""Mini-LaTeX -> OMML (Office Math ML) omzetter voor de labocursus.

Ondersteunde invoer:
  \\frac{a}{b}   \\sqrt{a}   x^{2}   x_{1}   \\text{met }   \\cdot  \\times  \\pm
  Griekse letters en een reeks symbolen (zie SYMBOLS).
Geeft een XML-string terug die als <m:oMathPara> in een paragraaf geplakt kan worden.
"""
import re
import html

SYMBOLS = {
    "cdot": "\u00b7", "times": "\u00d7", "pm": "\u00b1", "mp": "\u2213",
    "div": "\u00f7", "approx": "\u2248", "ne": "\u2260", "le": "\u2264",
    "ge": "\u2265", "ll": "\u226a", "gg": "\u226b",
    "alpha": "\u03b1", "beta": "\u03b2", "gamma": "\u03b3", "delta": "\u03b4",
    "Delta": "\u0394", "epsilon": "\u03b5", "varepsilon": "\u03b5", "theta": "\u03b8",
    "vartheta": "\u03d1", "lambda": "\u03bb", "mu": "\u03bc", "nu": "\u03bd",
    "pi": "\u03c0", "rho": "\u03c1", "sigma": "\u03c3", "Sigma": "\u03a3",
    "tau": "\u03c4", "phi": "\u03c6", "varphi": "\u03c6", "chi": "\u03c7",
    "psi": "\u03c8", "omega": "\u03c9", "Omega": "\u03a9", "kappa": "\u03ba",
    "eta": "\u03b7", "zeta": "\u03b6", "xi": "\u03be", "Xi": "\u039e",
    "infty": "\u221e", "sum": "\u2211", "prod": "\u220f", "int": "\u222b",
    "partial": "\u2202", "nabla": "\u2207", "deg": "\u00b0",
    "rightarrow": "\u2192", "leftarrow": "\u2190", "Rightarrow": "\u21d2",
    "leftrightarrow": "\u2194", "to": "\u2192",
    "sin": "sin", "cos": "cos", "tan": "tan", "log": "log", "ln": "ln",
    "half": "\u00bd", "quad": "   ", "hspace": " ",
    "degC": "\u00b0C", "per": "/",
}


def esc(t):
    return html.escape(str(t), quote=False)


def mrun(text, style=None):
    if text == "":
        return ""
    sty = '<m:rPr><m:sty m:val="p"/></m:rPr>' if style == "p" else ""
    return "<m:r>%s<m:t xml:space=\"preserve\">%s</m:t></m:r>" % (sty, esc(text))


class Parser:
    def __init__(self, src):
        self.s = src
        self.i = 0

    def eof(self):
        return self.i >= len(self.s)

    def peek(self):
        return self.s[self.i] if not self.eof() else ""

    def take(self):
        c = self.s[self.i]
        self.i += 1
        return c

    def read_group(self):
        """Lees { ... } of één token, geef lijst van elementen terug."""
        if self.eof():
            return []
        if self.peek() == "{":
            self.take()
            out = []
            depth = 1
            start = self.i
            # zoek de bijhorende sluitende accolade
            while not self.eof():
                c = self.take()
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
            inner = self.s[start:self.i - 1]
            return Parser(inner).parse_all()
        # enkel token
        c = self.take()
        return [mrun(c)]

    def parse_all(self):
        elems = []
        buf = ""
        while not self.eof():
            c = self.peek()
            if c == "\\":
                self.take()
                m = re.match(r"[A-Za-z]+", self.s[self.i:])
                if not m:
                    buf += "\\"
                    continue
                cmd = m.group(0)
                self.i += len(cmd)
                if buf:
                    elems.append(mrun(buf))
                    buf = ""
                if cmd == "frac":
                    num = self.read_group()
                    den = self.read_group()
                    elems.append("<m:f><m:fPr/>%s%s</m:f>" % (
                        "<m:num>%s</m:num>" % "".join(num),
                        "<m:den>%s</m:den>" % "".join(den)))
                elif cmd == "sqrt":
                    inner = self.read_group()
                    elems.append("<m:rad><m:radPr><m:degHide m:val=\"1\"/></m:radPr>"
                                 "<m:deg/><m:e>%s</m:e></m:rad>" % "".join(inner))
                elif cmd == "nthroot":
                    idx = self.read_group()
                    inner = self.read_group()
                    elems.append("<m:rad><m:radPr/><m:deg>%s</m:deg>"
                                 "<m:e>%s</m:e></m:rad>" % ("".join(idx), "".join(inner)))
                elif cmd == "text":
                    inner = self.read_group()
                    txt = "".join(inner)
                    txt = re.sub(r"<m:r>(<m:rPr>.*?</m:rPr>)?<m:t[^>]*>", "", txt)
                    txt = txt.replace("</m:t></m:r>", "")
                    elems.append(mrun(txt, style="p"))
                elif cmd == "hat":
                    inner = self.read_group()
                    elems.append("<m:acc><m:accPr><m:chr m:val=\"^\"/></m:accPr>"
                                 "<m:e>%s</m:e></m:acc>" % "".join(inner))
                elif cmd == "bar":
                    inner = self.read_group()
                    elems.append("<m:bar><m:barPr><m:pos m:val=\"top\"/></m:barPr>"
                                 "<m:e>%s</m:e></m:bar>" % "".join(inner))
                elif cmd == "vec":
                    inner = self.read_group()
                    elems.append("<m:acc><m:accPr><m:chr m:val=\"\u2192\"/></m:accPr>"
                                 "<m:e>%s</m:e></m:acc>" % "".join(inner))
                elif cmd == "abs":
                    inner = self.read_group()
                    elems.append("<m:d><m:dPr><m:begChr m:val=\"|\"/><m:endChr m:val=\"|\"/></m:dPr>"
                                 "<m:e>%s</m:e></m:d>" % "".join(inner))
                elif cmd in SYMBOLS:
                    elems.append(mrun(SYMBOLS[cmd]))
                else:
                    elems.append(mrun(cmd))
            elif c in "^_":
                self.take()
                grp = self.read_group()
                if buf:
                    elems.append(mrun(buf))
                    buf = ""
                if not elems:
                    base = mrun("")
                else:
                    base = elems.pop()
                if c == "^":
                    elems.append("<m:sSup><m:e>%s</m:e><m:sup>%s</m:sup></m:sSup>"
                                 % (base, "".join(grp)))
                else:
                    elems.append("<m:sSub><m:e>%s</m:e><m:sub>%s</m:sub></m:sSub>"
                                 % (base, "".join(grp)))
            elif c == "{":
                grp = self.read_group()
                if buf:
                    elems.append(mrun(buf))
                    buf = ""
                elems.extend(grp)
            elif c in "\u00b7\u00d7\u00b1":
                self.take()
                buf += c
            else:
                self.take()
                buf += c
        if buf:
            elems.append(mrun(buf))
        return elems


def omml(src):
    """Geeft <m:oMathPara>...</m:oMathPara> als string."""
    inner = "".join(Parser(src).parse_all())
    return ('<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
            '<m:oMath>%s</m:oMath></m:oMathPara>') % inner


def omml_inline(src):
    """Geeft <m:oMath>...</m:oMath> als string (binnen een lopende paragraaf)."""
    return ('<m:oMath xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
            '%s</m:oMath>') % "".join(Parser(src).parse_all())


if __name__ == "__main__":
    print(omml("F = m \\cdot a"))
    print(omml("v = \\frac{\\Delta x}{\\Delta t}"))
    print(omml("T = 2\\pi\\sqrt{\\frac{l}{g}}"))
    print(omml("E_{k} = \\frac{1}{2} m v^{2}"))
