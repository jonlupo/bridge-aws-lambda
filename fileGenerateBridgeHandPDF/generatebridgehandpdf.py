#!/usr/bin/python

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch

from parsepbn import grammar

SPADE = u'\u2660'
HEART = u'\u2665'
DIAMOND = u'\u2666'
CLUB = u'\u2663'


def drawRed(textobject, text):
    textobject.setFillColorRGB(255, 0, 0)
    textobject.textOut(text)
    textobject.setFillColorRGB(0, 0, 0)

def drawHand(canvas, hand, x, y):
    textobject = canvas.beginText()
    textobject.setTextOrigin(x, y)
    hand = hand.split('.')

    #spade
    textobject.setFillColorRGB(0, 0, 0)
    textobject.textOut(SPADE)
    textobject.textOut(hand[0])

    #heart
    textobject.moveCursor(0,14)
    drawRed(textobject, HEART)
    textobject.textOut(hand[1])

    #diamond
    textobject.moveCursor(0,14)
    drawRed(textobject, DIAMOND)
    textobject.textOut(hand[2])

    #club
    textobject.setFillColorRGB(0, 0, 0)
    textobject.moveCursor(0,14)
    textobject.textOut(CLUB)
    textobject.textOut(hand[3])

    canvas.drawText(textobject)

def createPDF():
    g = grammar.parseFile("test.pbn");
    buffer = StringIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setLineWidth(.3)

    dealer = " ".join(g["Dealer"])
    vulnerable = " ".join(g["Vulnerable"])
    board = " ".join(g["Board"])
    deal = g["Deal"]
    print deal
    print deal[0]
    print deal[1]
    print deal[2]
    print deal[3]

    p.drawString(60, 750,  dealer + " Deals")
    p.drawString(60, 735, vulnerable + " Vul")
    p.drawString(360, 750, board)

    drawHand(p, deal[0], 3*inch, 9*inch)
    drawHand(p, deal[1], 2*inch, 8*inch)
    drawHand(p, deal[2], 3*inch, 7*inch)
    drawHand(p, deal[3], 4*inch, 8*inch)

    p.save()
    buffer.reset()
    pdf = buffer.read()

    buffer.close()
    return pdf




def test_createPDF():
    f = open('test.pdf', 'wb')
    pdf = createPDF()
    f.write(pdf)
    f.close()



if __name__ == '__main__':
    test_createPDF()
