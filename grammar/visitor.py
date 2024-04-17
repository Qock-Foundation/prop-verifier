from antlr4 import CommonTokenStream, InputStream
from .PropLogicLexer import PropLogicLexer
from .PropLogicParser import PropLogicParser
from .PropLogicVisitor import PropLogicVisitor
from functools import reduce

def left_assoc_fold(op_name, list):
  return reduce(lambda a, b : [a, op_name, b] if a else b, list[::2])  # since there are extra Nones in-between
def right_assoc_fold(op_name, list):
  return reduce(lambda a, b : [b, op_name, a] if a else b, list[::-2])
#assert left_assoc_fold('and', ['a', 'b', 'c', 'd']) == [[['a', 'and', 'b'], 'and', 'c'], 'and', 'd']
#assert right_assoc_fold('implies', ['a', 'b', 'c', 'd']) == ['a', 'implies', ['b', 'implies', ['c', 'implies', 'd']]]

class KekVisitor(PropLogicVisitor):
  def visitEquivalenceExpr(self, ctx):
    if len(ctx.children) == 1:
      return self.visit(ctx.children[0])
    assert len(ctx.children) == 3  # [left_expr, 'equiv', right_expr]
    return [self.visit(ctx.children[0]), 'equiv', self.visit(ctx.children[2])]
  def visitImplicationExpr(self, ctx):
    return right_assoc_fold('implies', [self.visit(child) for child in ctx.children])
  def visitDisjunctionExpr(self, ctx):
    return left_assoc_fold('or', [self.visit(child) for child in ctx.children])
  def visitXorExpr(self, ctx):
    return left_assoc_fold('xor', [self.visit(child) for child in ctx.children])
  def visitConjunctionExpr(self, ctx):
    return left_assoc_fold('and', [self.visit(child) for child in ctx.children])
  def visitNegationExpr(self, ctx):
    if len(ctx.children) == 1:
      return self.visit(ctx.children[0])
    assert len(ctx.children) == 2  # ['not', expr]
    return ['not', self.visit(ctx.children[1])]
  def visitAtomicExpr(self, ctx):
    if len(ctx.children) == 1:
      return self.visit(ctx.children[0])
    assert len(ctx.children) == 3  # ['(', expr, ')']
    return self.visit(ctx.children[1])
  def visitTerminal(self, node):
    token = node.symbol
    if token.type is PropLogicLexer.FalseStr:
      return 'false'
    return token.text

def kek_conversion(s):
  tree = PropLogicParser(CommonTokenStream(PropLogicLexer(InputStream(s)))).genericExpr()
  return KekVisitor().visit(tree)

s = 'a implies b or c and d implies e'
#print(s)
converted = kek_conversion(s)
#print('CONVERTED:', converted)
assert converted == ['a', 'implies', [['b', 'or', ['c', 'and', 'd']], 'implies', 'e']]
#print()

s = r'a -> b \/ c /\ (d -> e)'
#print(s)
converted = kek_conversion(s)
#print('CONVERTED:', converted)
assert converted == ['a', 'implies', ['b', 'or', ['c', 'and', ['d', 'implies', 'e']]]]
#print()

s = r'a <-> not not a'
#print(s)
converted = kek_conversion(s)
#print('CONVERTED:', converted)
assert converted == ['a', 'equiv', ['not', ['not', 'a']]]

s = 'a -> 0'
#print(s)
converted = kek_conversion(s)
#print('CONVERTED:', converted)
assert converted == ['a', 'implies', 'false']

s = 'a ⇒ b ⇔ c ⊕ ¬d ∨ e ∧ ⊥ or o_O'
#print(s)
converted = kek_conversion(s)
#print('CONVERTED:', converted)
assert converted == [['a', 'implies', 'b'], 'equiv', [[['c', 'xor', ['not', 'd']], 'or', ['e', 'and', 'false']], 'or', 'false']]
