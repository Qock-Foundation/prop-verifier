from antlr4 import CommonTokenStream, InputStream
from PropLogicLexer import PropLogicLexer
from PropLogicParser import PropLogicParser

s = 'a implies b or c and d implies e'
tree = PropLogicParser(CommonTokenStream(PropLogicLexer(InputStream(s)))).implicationExpr()
print(s)
print(tree.children)
