# Generated from PropLogic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PropLogicParser import PropLogicParser
else:
    from PropLogicParser import PropLogicParser

# This class defines a complete generic visitor for a parse tree produced by PropLogicParser.

class PropLogicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PropLogicParser#genericExpr.
    def visitGenericExpr(self, ctx:PropLogicParser.GenericExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PropLogicParser#equivalenceExpr.
    def visitEquivalenceExpr(self, ctx:PropLogicParser.EquivalenceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PropLogicParser#implicationExpr.
    def visitImplicationExpr(self, ctx:PropLogicParser.ImplicationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PropLogicParser#disjunctionExpr.
    def visitDisjunctionExpr(self, ctx:PropLogicParser.DisjunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PropLogicParser#conjunctionExpr.
    def visitConjunctionExpr(self, ctx:PropLogicParser.ConjunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PropLogicParser#negationExpr.
    def visitNegationExpr(self, ctx:PropLogicParser.NegationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PropLogicParser#atomicExpr.
    def visitAtomicExpr(self, ctx:PropLogicParser.AtomicExprContext):
        return self.visitChildren(ctx)



del PropLogicParser