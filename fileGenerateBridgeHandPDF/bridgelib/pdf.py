#!/usr/bin/python

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from pbn import grammar
import collections
from types import *
from reportlab.lib.colors import ColorType

#utf shapes
SPADE = u'\u2660'
HEART = u'\u2665'
DIAMOND = u'\u2666'
CLUB = u'\u2663'

#rgb colors
RED = (255, 0, 0)
BLACK = (0, 0 , 0)

#defaults
DEFAULT_FONT = "Helvetica-Oblique"
DEFAULT_SIZE = 12

##colors can be either rgb or a color from reportlab.lib.colors
DEFAULT_COLOR =  BLACK
DEFAULT_ORIGIN = (0, 0)

#constants
RGB = "rgb"
COLOR_TYPE = "colortype"

def check_values(sequence, Type):
    for i in sequence:
        if not type(i) is Type:
            raise Exception("sequence can only contain %s values" %
                    (Type.__name__))

def check_color(color):
    colortype = type(color) == ColorType
    rgbvalues = isinstance(color, collections.Sequence) and len(color) == 3
    if not (colortype or rgbvalues):
        raise Exception("color must either of type ColorType or be a sequence with 3 values")
    if(rgbvalues):
        check_values(color, IntType)
        return RGB
    else:
        return COLOR_TYPE

def check_origin(origin):
    sequence = isinstance(origin, collections.Sequence) and len(origin) == 2
    if not sequence:
       raise Exception("origin must be a sequence containing x value and y value")
    check_values(origin, IntType)

def set_origin(textobject, origin):
    check_origin(origin)
    textobject.setTextOrigin(origin[0], origin[1])

def fill_color(textobject, color):
    Type = check_color(color)
    if(Type == RGB):
        textobject.setFillColorRGB(color[0], color[1], color[2])
    elif(Type == COLOR_TYPE):
        textobject.setFillColor(color)
    else:
        raise Exception("Color is invalid")

def draw_color(textobject, text, color):
    fill_color(textobject, color)
    textobject.textOut(text)

    #reset to default color
    fill_color(textobject, DEFAULT_COLOR)

def draw_text(**kwargs):
    if not "canvas" in kwargs:
        raise Exception("canvas is required")
    if not "text" in kwargs:
        raise Exception("text is required")

    canvas = kwargs["canvas"]
    textobject = canvas.beginText()
    text = kwargs["text"]
    font = DEFAULT_FONT
    size = DEFAULT_SIZE
    origin = DEFAULT_ORIGIN
    color = DEFAULT_COLOR

    if "origin" in kwargs:
        origin = kwargs["origin"]
    if "font" in kwargs:
        font = kwargs["font"]
    if "size" in kwargs:
        size = kwargs["size"]
    if("color" in kwargs):
        color = kwargs["color"]

    set_origin(textobject, origin)
    fill_color(textobject, color)
    textobject.setFont(font, size)
    textobject.textOut(text)

    canvas.drawText(textobject)

def draw_hand(canvas, hand, x, y):
    textobject = canvas.beginText()
    textobject.setTextOrigin(x, y)
    textobject.setFont(DEFAULT_FONT, DEFAULT_SIZE)
    fill_color(textobject, DEFAULT_COLOR)

    #transform hand to list
    hand = hand.split('.')

    #spade
    draw_color(textobject, SPADE, BLACK)
    textobject.textOut(hand[0])

    #heart
    textobject.moveCursor(0,14)
    draw_color(textobject, HEART, RED)
    textobject.textOut(hand[1])

    #diamond
    textobject.moveCursor(0,14)
    draw_color(textobject, DIAMOND, RED)
    textobject.textOut(hand[2])

    #club
    textobject.moveCursor(0,14)
    draw_color(textobject, CLUB, BLACK)
    textobject.textOut(hand[3])

    canvas.drawText(textobject)

def createPDF():
    g = grammar.parseFile("test.pbn");
    buffer = StringIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setLineWidth(.3)

    dealer = " ".join(g["Dealer"]) + " Deals"
    vulnerable = " ".join(g["Vulnerable"]) + " Vul"
    board = " ".join(g["Board"])
    deal = g["Deal"]

    north = deal[0].split(':')[1]
    east = deal[1]
    south = deal[2]
    west = deal[3]

    draw_text(canvas = p,
              text   = dealer,
              origin = (60,750),
              size   = 14)

    draw_text(canvas = p,
              text   = vulnerable,
              origin = (60,735),
              size   = 14)

    draw_text(canvas = p,
              text   = board,
              origin = (360,750),
              size   = 20)

    draw_hand(p, north, 3*inch, 9*inch)
    draw_hand(p, east, 2*inch, 8*inch)
    draw_hand(p, south, 3*inch, 7*inch)
    draw_hand(p, west, 4*inch, 8*inch)

    p.save()
    buffer.reset()
    pdf = buffer.read()

    buffer.close()
    return pdf


