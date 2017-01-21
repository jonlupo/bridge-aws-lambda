#!/usr/bin/python
from pyparsing import *


lit = lambda x: Suppress(Literal(x))

expr = Dict( Group( lit('[') + Word(alphas) + lit('"') + Group(ZeroOrMore(Word(printables, excludeChars='"]['))) + lit('"') + lit(']')))

line_comment = Literal(';') + restOfLine
block_comment = nestedExpr("{", "}")

grammar = OneOrMore(expr)

grammar.ignore(line_comment)
grammar.ignore(block_comment)

if __name__ == '__main__':
    expr.parseString('[Event "A bunch of stuff"]')
    r = expr.parseString('[Event "A bunch of stuff"]')
    print r['Event']

    print grammar.parseString(
   """
    [Event "##11.14 Ansley Aces"]\r\n
    [Site "##"]\r\n
    [Date ""]\r\n
    [Board "21"]\r\n
    [West ""]\r\n
    [North ""]\r\n
    [East ""]\r\n
    [South ""]\r\n
    [Dealer "N"]\r\n
    [Vulnerable "NS"]\r\n
    [Deal "N:K96.AT84.A64.T85 8432.J.T75.AQJ43 AQ7.KQ965.KQ92.9
    JT5.732.J83.K762"]\r\n
    [Scoring ""]\r\n
    [Declarer ""]\r\n
    [Contract ""]\r\n
    [Result ""]
    {
      something to ignore
      #$% something to ignore
      234 something to ignore
    }
    """)

    r=  grammar.parseString(
   """
    [Event "##11.14 Ansley Aces"]\r\n
    [Site "##"]\r\n
    [Date ""]\r\n
    [Board "21"]\r\n
    [West ""]\r\n
    [North ""]\r\n
    [East ""]\r\n
    [South ""]\r\n
    [Dealer "N"]\r\n
    [Vulnerable "NS"]\r\n
    [Deal "N:K96.AT84.A64.T85 8432.J.T75.AQJ43 AQ7.KQ965.KQ92.9
    JT5.732.J83.K762"]\r\n
    [Scoring ""]\r\n
    [Declarer ""]\r\n
    [Contract ""]\r\n
    [Result ""]
    {
      something to ignore
      #$% something to ignore
      234 something to ignore
    }\r\n
    ;test line comment""")


