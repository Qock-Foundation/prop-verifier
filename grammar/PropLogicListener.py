# Generated from PropLogic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PropLogicParser import PropLogicParser
else:
    from PropLogicParser import PropLogicParser

# This class defines a complete listener for a parse tree produced by PropLogicParser.
class PropLogicListener(ParseTreeListener):

    # Enter a parse tree produced by PropLogicParser#genericExpr.
    def enterGenericExpr(self, ctx:PropLogicParser.GenericExprContext):
        pass

    # Exit a parse tree produced by PropLogicParser#genericExpr.
    def exitGenericExpr(self, ctx:PropLogicParser.GenericExprContext):
        pass


    # Enter a parse tree produced by PropLogicParser#equivalenceExpr.
    def enterEquivalenceExpr(self, ctx:PropLogicParser.EquivalenceExprContext):
        pass

    # Exit a parse tree produced by PropLogicParser#equivalenceExpr.
    def exitEquivalenceExpr(self, ctx:PropLogicParser.EquivalenceExprContext):
        pass


    # Enter a parse tree produced by PropLogicParser#implicationExpr.
    def enterImplicationExpr(self, ctx:PropLogicParser.ImplicationExprContext):
        pass

    # Exit a parse tree produced by PropLogicParser#implicationExpr.
    def exitImplicationExpr(self, ctx:PropLogicParser.ImplicationExprContext):
        pass


    # Enter a parse tree produced by PropLogicParser#disjunctionExpr.
    def enterDisjunctionExpr(self, ctx:PropLogicParser.DisjunctionExprContext):
        pass

    # Exit a parse tree produced by PropLogicParser#disjunctionExpr.
    def exitDisjunctionExpr(self, ctx:PropLogicParser.DisjunctionExprContext):
        pass


    # Enter a parse tree produced by PropLogicParser#conjunctionExpr.
    def enterConjunctionExpr(self, ctx:PropLogicParser.ConjunctionExprContext):
        pass

    # Exit a parse tree produced by PropLogicParser#conjunctionExpr.
    def exitConjunctionExpr(self, ctx:PropLogicParser.ConjunctionExprContext):
        pass


    # Enter a parse tree produced by PropLogicParser#negationExpr.
    def enterNegationExpr(self, ctx:PropLogicParser.NegationExprContext):
        pass

    # Exit a parse tree produced by PropLogicParser#negationExpr.
    def exitNegationExpr(self, ctx:PropLogicParser.NegationExprContext):
        pass


    # Enter a parse tree produced by PropLogicParser#atom.
    def enterAtom(self, ctx:PropLogicParser.AtomContext):
        pass

    # Exit a parse tree produced by PropLogicParser#atom.
    def exitAtom(self, ctx:PropLogicParser.AtomContext):
        pass



del PropLogicParser