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
        4,1,13,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,1,2,1,2,
        1,2,3,2,31,8,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,39,8,3,10,3,12,3,42,9,
        3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,50,8,4,10,4,12,4,53,9,4,1,5,1,5,1,
        5,1,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,1,6,1,6,1,6,3,6,69,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,81,8,7,1,7,0,3,6,8,10,
        8,0,2,4,6,8,10,12,14,0,0,83,0,16,1,0,0,0,2,23,1,0,0,0,4,30,1,0,0,
        0,6,32,1,0,0,0,8,43,1,0,0,0,10,54,1,0,0,0,12,68,1,0,0,0,14,80,1,
        0,0,0,16,17,3,2,1,0,17,1,1,0,0,0,18,24,3,4,2,0,19,20,3,4,2,0,20,
        21,5,1,0,0,21,22,3,4,2,0,22,24,1,0,0,0,23,18,1,0,0,0,23,19,1,0,0,
        0,24,3,1,0,0,0,25,31,3,6,3,0,26,27,3,6,3,0,27,28,5,2,0,0,28,29,3,
        4,2,0,29,31,1,0,0,0,30,25,1,0,0,0,30,26,1,0,0,0,31,5,1,0,0,0,32,
        33,6,3,-1,0,33,34,3,8,4,0,34,40,1,0,0,0,35,36,10,1,0,0,36,37,5,3,
        0,0,37,39,3,8,4,0,38,35,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,
        1,0,0,0,41,7,1,0,0,0,42,40,1,0,0,0,43,44,6,4,-1,0,44,45,3,10,5,0,
        45,51,1,0,0,0,46,47,10,1,0,0,47,48,5,4,0,0,48,50,3,10,5,0,49,46,
        1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,9,1,0,0,0,53,
        51,1,0,0,0,54,55,6,5,-1,0,55,56,3,12,6,0,56,62,1,0,0,0,57,58,10,
        1,0,0,58,59,5,5,0,0,59,61,3,12,6,0,60,57,1,0,0,0,61,64,1,0,0,0,62,
        60,1,0,0,0,62,63,1,0,0,0,63,11,1,0,0,0,64,62,1,0,0,0,65,69,3,14,
        7,0,66,67,5,6,0,0,67,69,3,12,6,0,68,65,1,0,0,0,68,66,1,0,0,0,69,
        13,1,0,0,0,70,81,5,7,0,0,71,81,5,12,0,0,72,73,5,8,0,0,73,74,3,0,
        0,0,74,75,5,9,0,0,75,81,1,0,0,0,76,77,5,10,0,0,77,78,3,0,0,0,78,
        79,5,11,0,0,79,81,1,0,0,0,80,70,1,0,0,0,80,71,1,0,0,0,80,72,1,0,
        0,0,80,76,1,0,0,0,81,15,1,0,0,0,7,23,30,40,51,62,68,80
    ]

class PropLogicParser ( Parser ):

    grammarFileName = "PropLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "EquivStr", "ImpliesStr", "OrStr", "XorStr", 
                      "AndStr", "NotStr", "FalseStr", "LParenStr", "RParenStr", 
                      "LBracketStr", "RBracketStr", "Name", "WS" ]

    RULE_genericExpr = 0
    RULE_equivalenceExpr = 1
    RULE_implicationExpr = 2
    RULE_disjunctionExpr = 3
    RULE_xorExpr = 4
    RULE_conjunctionExpr = 5
    RULE_negationExpr = 6
    RULE_atomicExpr = 7

    ruleNames =  [ "genericExpr", "equivalenceExpr", "implicationExpr", 
                   "disjunctionExpr", "xorExpr", "conjunctionExpr", "negationExpr", 
                   "atomicExpr" ]

    EOF = Token.EOF
    EquivStr=1
    ImpliesStr=2
    OrStr=3
    XorStr=4
    AndStr=5
    NotStr=6
    FalseStr=7
    LParenStr=8
    RParenStr=9
    LBracketStr=10
    RBracketStr=11
    Name=12
    WS=13

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
            self.state = 16
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
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.implicationExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.implicationExpr()
                self.state = 20
                self.match(PropLogicParser.EquivStr)
                self.state = 21
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
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.disjunctionExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.disjunctionExpr(0)
                self.state = 27
                self.match(PropLogicParser.ImpliesStr)
                self.state = 28
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

        def xorExpr(self):
            return self.getTypedRuleContext(PropLogicParser.XorExprContext,0)


        def disjunctionExpr(self):
            return self.getTypedRuleContext(PropLogicParser.DisjunctionExprContext,0)


        def OrStr(self):
            return self.getToken(PropLogicParser.OrStr, 0)

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



    def disjunctionExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PropLogicParser.DisjunctionExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_disjunctionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.xorExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PropLogicParser.DisjunctionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_disjunctionExpr)
                    self.state = 35
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 36
                    self.match(PropLogicParser.OrStr)
                    self.state = 37
                    self.xorExpr(0) 
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class XorExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjunctionExpr(self):
            return self.getTypedRuleContext(PropLogicParser.ConjunctionExprContext,0)


        def xorExpr(self):
            return self.getTypedRuleContext(PropLogicParser.XorExprContext,0)


        def XorStr(self):
            return self.getToken(PropLogicParser.XorStr, 0)

        def getRuleIndex(self):
            return PropLogicParser.RULE_xorExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXorExpr" ):
                listener.enterXorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXorExpr" ):
                listener.exitXorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXorExpr" ):
                return visitor.visitXorExpr(self)
            else:
                return visitor.visitChildren(self)



    def xorExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PropLogicParser.XorExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_xorExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.conjunctionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PropLogicParser.XorExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_xorExpr)
                    self.state = 46
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 47
                    self.match(PropLogicParser.XorStr)
                    self.state = 48
                    self.conjunctionExpr(0) 
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_conjunctionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.negationExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PropLogicParser.ConjunctionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conjunctionExpr)
                    self.state = 57
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 58
                    self.match(PropLogicParser.AndStr)
                    self.state = 59
                    self.negationExpr() 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_negationExpr)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 10, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.atomicExpr()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(PropLogicParser.NotStr)
                self.state = 67
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
        self.enterRule(localctx, 14, self.RULE_atomicExpr)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(PropLogicParser.FalseStr)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(PropLogicParser.Name)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(PropLogicParser.LParenStr)
                self.state = 73
                self.genericExpr()
                self.state = 74
                self.match(PropLogicParser.RParenStr)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.match(PropLogicParser.LBracketStr)
                self.state = 77
                self.genericExpr()
                self.state = 78
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
        self._predicates[3] = self.disjunctionExpr_sempred
        self._predicates[4] = self.xorExpr_sempred
        self._predicates[5] = self.conjunctionExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def disjunctionExpr_sempred(self, localctx:DisjunctionExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def xorExpr_sempred(self, localctx:XorExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def conjunctionExpr_sempred(self, localctx:ConjunctionExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




