# coding: utf-8
import pyparsing as pp
g = "[" + pp.Word( pp.alphas ) + "]"
g.parseString("[Hello]")
g = "[" + pp.Word( pp.alphas ) + Word(pp.alphas) + "]"
g = "[" + pp.Word( pp.alphas ) + pp.Word(pp.alphas) + "]"
g.parseString("[Hello]")
g.parseString("[Hello You]")
g.parseString('[Hello You]')
g.parseString('[Hello "You"]')
g = "[" + pp.Word( pp.alphas ) + pp.Word(pp.printables) + "]"
g.parseString('[Hello "You"]')
g = "[" + pp.Word( pp.alphas ) + pp.Word(pp.printables, excludeChars="\"") + "]"
g.parseString('[Hello "You"]')
g.parseString('[Hello Y"ou]')
g.parseString('[Hello You]')
g = "[" + pp.Word( pp.alphas ) + pp.Word(pp.printables, excludeChars="\"]") + "]"
g.parseString('[Hello You]')
g.parseString('[Hello "You"]')
g = "[" + pp.Word( pp.alphas ) + "\"" + pp.Word(pp.printables, excludeChars="\"]") + "\"]"
g.parseString('[Hello "You"]')
g = "[" + pp.Word( pp.alphas ) + pp.Suppress("\"") + pp.Word(pp.printables, excludeChars="\"]") + pp.Suppress("\"") + "]"
g.parseString('[Hello "You"]')
g.parseString('[Hello "You Person"]')
help(pp.OneOrMore)
g = "[" + pp.Word( pp.alphas ) + pp.Suppress("\"") + pp.OneOrMore(pp.Word(pp.printables, excludeChars="\"]") ) + pp.Suppress("\"") + "]"
g.parseString('[Hello "You Person"]')
r = g.parseString('[Hello "You Person"]')
r[0]
r[1]
print r
g = "[" + pp.Word( pp.alphas ) + pp.Suppress("\"") + pp.OneOrMore(pp.Word(pp.printables, excludeChars="\"]") ) + pp.Suppress("\"") + "]"
g = pp.Suppress("[") + pp.Word( pp.alphas ) + pp.Suppress("\"") + pp.OneOrMore(pp.Word(pp.printables, excludeChars="\"]") ) + pp.Suppress("\"") + pp.Suppress("]")
r = g.parseString('[Hello "You Person"]')
r
attribute = pp.Group(pp.Suppress('[') + pp.OneOrMore(pp.Word(pp.alphas)) + pp.Suppress(']'))
attribute.parseString("[Event Some thing]")
attribute = pp.Group(pp.Suppress('[') + pp.OneOrMore(pp.Word(pp.alphas)) + pp.Suppress(']'))
member = pp.Group(pp.Word(pp.printables) + pp.Word(pp.printables.replace(';', '')) + pp.Suppress(';'))
msgHeader = pp.ZeroOrMore(attribute)
msgName = pp.Word(pp.printables)
msgContent = pp.Suppress('{') + pp.OneOrMore(member) + pp.Suppress('}')
msgWithContent = pp.Keyword("message").suppress() + msgName + msgContent
defaultMsg = pp.Keyword("default").suppress() + pp.Suppress(';')
protoStatement = msgHeader + pp.MatchFirst([msgWithContent, defaultMsg])
protoFileParser = pp.ZeroOrMore(protoStatement)
protoFileParser.parseString(fileContents, parseAll=True)
fileContents = open("~/testfile.t", r)
fileContents = open("~/testfile.t", "r")
fileContents = open("/home/jonathan/testfile.t", "r")
protoFileParser.parseString(fileContents, parseAll=True)
fileContents = fileContents.read()
protoFileParser.parseString(fileContents, parseAll=True)
g = pp.Dict(pp.Word( pp.alphas ) + " " + pp.Word( pp.alphas ) )
g.parseString("Hello World")
g = pp.Dict(pp.Word( pp.alphas ) + pp.Word( pp.alphas ) )
g.parseString("Hello World")
from pyparsing import *
wd = Word(alphas)
lbracket = Suppress(Literal('['))
rbracket = Suppress(Literal(']'))
expr = Dict(Group( lbracket + wd + Group(OneOrMore(wd)) ) )
expr.parseString("[Hello You person")
r = expr.parseString("[Hello You person")
r['Hello']
r['Hello'][1]
r['Hello']
quot = Suppress(Literal('"'))
expr = Dict(Group( lbracket + wd + quot + Group(OneOrMore(wd)) + quot + rbracket ) )
expr.parseString('[Event "A bunch of stuff"]')
r = expr.parseString('[Event "A bunch of stuff"]')
r['Event']
get_ipython().magic(u'save pyparsing_session_01 1 72')
