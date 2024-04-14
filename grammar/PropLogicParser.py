# Generated from PropLogic.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,1,2,3,2,
        29,8,2,1,3,1,3,1,3,1,3,1,3,3,3,36,8,3,1,4,1,4,1,4,1,4,1,4,1,4,5,
        4,44,8,4,10,4,12,4,47,9,4,1,5,1,5,1,5,3,5,52,8,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,64,8,6,1,6,0,1,8,7,0,2,4,6,8,10,12,0,
        0,66,0,14,1,0,0,0,2,21,1,0,0,0,4,28,1,0,0,0,6,35,1,0,0,0,8,37,1,
        0,0,0,10,51,1,0,0,0,12,63,1,0,0,0,14,15,3,2,1,0,15,1,1,0,0,0,16,
        22,3,4,2,0,17,18,3,4,2,0,18,19,5,1,0,0,19,20,3,4,2,0,20,22,1,0,0,
        0,21,16,1,0,0,0,21,17,1,0,0,0,22,3,1,0,0,0,23,29,3,6,3,0,24,25,3,
        6,3,0,25,26,5,2,0,0,26,27,3,4,2,0,27,29,1,0,0,0,28,23,1,0,0,0,28,
        24,1,0,0,0,29,5,1,0,0,0,30,36,3,8,4,0,31,32,3,8,4,0,32,33,5,3,0,
        0,33,34,3,6,3,0,34,36,1,0,0,0,35,30,1,0,0,0,35,31,1,0,0,0,36,7,1,
        0,0,0,37,38,6,4,-1,0,38,39,3,10,5,0,39,45,1,0,0,0,40,41,10,1,0,0,
        41,42,5,4,0,0,42,44,3,10,5,0,43,40,1,0,0,0,44,47,1,0,0,0,45,43,1,
        0,0,0,45,46,1,0,0,0,46,9,1,0,0,0,47,45,1,0,0,0,48,52,3,12,6,0,49,
        50,5,5,0,0,50,52,3,10,5,0,51,48,1,0,0,0,51,49,1,0,0,0,52,11,1,0,
        0,0,53,64,5,6,0,0,54,64,5,11,0,0,55,56,5,7,0,0,56,57,3,0,0,0,57,
        58,5,8,0,0,58,64,1,0,0,0,59,60,5,9,0,0,60,61,3,0,0,0,61,62,5,10,
        0,0,62,64,1,0,0,0,63,53,1,0,0,0,63,54,1,0,0,0,63,55,1,0,0,0,63,59,
        1,0,0,0,64,13,1,0,0,0,6,21,28,35,45,51,63
    ]

class PropLogicParser ( Parser ):

    grammarFileName = "PropLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "EquivStr", "ImpliesStr", "OrStr", "AndStr", 
                      "NotStr", "FalseStr", "LParenStr", "RParenStr", "LBracketStr", 
                      "RBracketStr", "Name", "WS" ]

    RULE_genericExpr = 0
    RULE_equivalenceExpr = 1
    RULE_implicationExpr = 2
    RULE_disjunctionExpr = 3
    RULE_conjunctionExpr = 4
    RULE_negationExpr = 5
    RULE_atomicExpr = 6

    ruleNames =  [ "genericExpr", "equivalenceExpr", "implicationExpr", 
                   "disjunctionExpr", "conjunctionExpr", "negationExpr", 
                   "atomicExpr" ]

    EOF = Token.EOF
    EquivStr=1
    ImpliesStr=2
    OrStr=3
    AndStr=4
    NotStr=5
    FalseStr=6
    LParenStr=7
    RParenStr=8
    LBracketStr=9
    RBracketStr=10
    Name=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GenericExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equivalenceExpr(self):
            return self.getTypedRuleContext(PropLogicParser.EquivalenceExprContext,0)


        def getRuleIndex(self):
            return PropLogicParser.RULE_genericExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericExpr" ):
                listener.enterGenericExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericExpr" ):
                listener.exitGenericExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenericExpr" ):
                return visitor.visitGenericExpr(self)
            else:
                return visitor.visitChildren(self)




    def genericExpr(self):

        localctx = PropLogicParser.GenericExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_genericExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.equivalenceExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EquivalenceExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicationExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropLogicParser.ImplicationExprContext)
            else:
                return self.getTypedRuleContext(PropLogicParser.ImplicationExprContext,i)


        def EquivStr(self):
            return self.getToken(PropLogicParser.EquivStr, 0)

        def getRuleIndex(self):
            return PropLogicParser.RULE_equivalenceExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquivalenceExpr" ):
                listener.enterEquivalenceExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquivalenceExpr" ):
                listener.exitEquivalenceExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquivalenceExpr" ):
                return visitor.visitEquivalenceExpr(self)
            else:
                return visitor.visitChildren(self)




    def equivalenceExpr(self):

        localctx = PropLogicParser.EquivalenceExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_equivalenceExpr)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.implicationExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.implicationExpr()
                self.state = 18
                self.match(PropLogicParser.EquivStr)
                self.state = 19
                self.implicationExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplicationExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disjunctionExpr(self):
            return self.getTypedRuleContext(PropLogicParser.DisjunctionExprContext,0)


        def ImpliesStr(self):
            return self.getToken(PropLogicParser.ImpliesStr, 0)

        def implicationExpr(self):
            return self.getTypedRuleContext(PropLogicParser.ImplicationExprContext,0)


        def getRuleIndex(self):
            return PropLogicParser.RULE_implicationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicationExpr" ):
                listener.enterImplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicationExpr" ):
                listener.exitImplicationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicationExpr" ):
                return visitor.visitImplicationExpr(self)
            else:
                return visitor.visitChildren(self)




    def implicationExpr(self):

        localctx = PropLogicParser.ImplicationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_implicationExpr)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.disjunctionExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.disjunctionExpr()
                self.state = 25
                self.match(PropLogicParser.ImpliesStr)
                self.state = 26
                self.implicationExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisjunctionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjunctionExpr(self):
            return self.getTypedRuleContext(PropLogicParser.ConjunctionExprContext,0)


        def OrStr(self):
            return self.getToken(PropLogicParser.OrStr, 0)

        def disjunctionExpr(self):
            return self.getTypedRuleContext(PropLogicParser.DisjunctionExprContext,0)


        def getRuleIndex(self):
            return PropLogicParser.RULE_disjunctionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunctionExpr" ):
                listener.enterDisjunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunctionExpr" ):
                listener.exitDisjunctionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunctionExpr" ):
                return visitor.visitDisjunctionExpr(self)
            else:
                return visitor.visitChildren(self)




    def disjunctionExpr(self):

        localctx = PropLogicParser.DisjunctionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_disjunctionExpr)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.conjunctionExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.conjunctionExpr(0)
                self.state = 32
                self.match(PropLogicParser.OrStr)
                self.state = 33
                self.disjunctionExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConjunctionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negationExpr(self):
            return self.getTypedRuleContext(PropLogicParser.NegationExprContext,0)


        def conjunctionExpr(self):
            return self.getTypedRuleContext(PropLogicParser.ConjunctionExprContext,0)


        def AndStr(self):
            return self.getToken(PropLogicParser.AndStr, 0)

        def getRuleIndex(self):
            return PropLogicParser.RULE_conjunctionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunctionExpr" ):
                listener.enterConjunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunctionExpr" ):
                listener.exitConjunctionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunctionExpr" ):
                return visitor.visitConjunctionExpr(self)
            else:
                return visitor.visitChildren(self)



    def conjunctionExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PropLogicParser.ConjunctionExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_conjunctionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.negationExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PropLogicParser.ConjunctionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conjunctionExpr)
                    self.state = 40
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 41
                    self.match(PropLogicParser.AndStr)
                    self.state = 42
                    self.negationExpr() 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NegationExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomicExpr(self):
            return self.getTypedRuleContext(PropLogicParser.AtomicExprContext,0)


        def NotStr(self):
            return self.getToken(PropLogicParser.NotStr, 0)

        def negationExpr(self):
            return self.getTypedRuleContext(PropLogicParser.NegationExprContext,0)


        def getRuleIndex(self):
            return PropLogicParser.RULE_negationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegationExpr" ):
                listener.enterNegationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegationExpr" ):
                listener.exitNegationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegationExpr" ):
                return visitor.visitNegationExpr(self)
            else:
                return visitor.visitChildren(self)




    def negationExpr(self):

        localctx = PropLogicParser.NegationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_negationExpr)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 9, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.atomicExpr()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(PropLogicParser.NotStr)
                self.state = 50
                self.negationExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomicExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FalseStr(self):
            return self.getToken(PropLogicParser.FalseStr, 0)

        def Name(self):
            return self.getToken(PropLogicParser.Name, 0)

        def LParenStr(self):
            return self.getToken(PropLogicParser.LParenStr, 0)

        def genericExpr(self):
            return self.getTypedRuleContext(PropLogicParser.GenericExprContext,0)


        def RParenStr(self):
            return self.getToken(PropLogicParser.RParenStr, 0)

        def LBracketStr(self):
            return self.getToken(PropLogicParser.LBracketStr, 0)

        def RBracketStr(self):
            return self.getToken(PropLogicParser.RBracketStr, 0)

        def getRuleIndex(self):
            return PropLogicParser.RULE_atomicExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomicExpr" ):
                listener.enterAtomicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomicExpr" ):
                listener.exitAtomicExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicExpr" ):
                return visitor.visitAtomicExpr(self)
            else:
                return visitor.visitChildren(self)




    def atomicExpr(self):

        localctx = PropLogicParser.AtomicExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atomicExpr)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(PropLogicParser.FalseStr)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(PropLogicParser.Name)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(PropLogicParser.LParenStr)
                self.state = 56
                self.genericExpr()
                self.state = 57
                self.match(PropLogicParser.RParenStr)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.match(PropLogicParser.LBracketStr)
                self.state = 60
                self.genericExpr()
                self.state = 61
                self.match(PropLogicParser.RBracketStr)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.conjunctionExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def conjunctionExpr_sempred(self, localctx:ConjunctionExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




