#!/usr/bin/python
from generatepdf import parsepbn as pbn

string_withcomments =  """
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
    ;test line comment
    """


string_tags =  """
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
    """



def test_single_tag():
    pbn.expr.parseString('[Event "A bunch of stuff"]')
    r = pbn.expr.parseString('[Event "A bunch of stuff"]')
    return r


def test_mult_tag():
    r = pbn.grammar.parseString(string_tags)
    return r


def test_mult_tag_wcomments():
    r = pbn.grammar.parseString(string_withcomments)
    return r
