#!/usr/bin/python3

import sys, re
from antlr4 import InputStream, CommonTokenStream
from grammar.PropLogicLexer import PropLogicLexer
from grammar.PropLogicParser import PropLogicParser

s = 'a implies b'
parser = PropLogicParser(CommonTokenStream(PropLogicLexer(InputStream(s))))
print(parser.implicationExpr())

#author = input('author ')
#assert re.search('^[a-zA-Z0-9_]*$', author) is not None, f'author name should be alphanumeric without spaces etc, your author name is "{author}"'
#print(f'Hello, {author}!!!')
#for i, s in enumerate(sys.stdin):
#  s = s[:-1]
#  #proposition_parsed = formula_t.parseString(s)[0]
#  parser = PropLogicParser(CommonTokenStream(PropLogicLexer(InputStream(s))))
#  print(str(parser), s)
#  proposition_parsed = parser.implicationExpr()
#  print('parsed as', proposition_parsed)
