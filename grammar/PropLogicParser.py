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
        4,1,8,38,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,3,0,12,8,0,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,2,1,2,1,2,
        3,2,28,8,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,36,8,3,1,3,0,1,2,4,0,2,4,
        6,0,0,38,0,8,1,0,0,0,2,13,1,0,0,0,4,24,1,0,0,0,6,35,1,0,0,0,8,11,
        3,2,1,0,9,10,5,1,0,0,10,12,3,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,
        1,1,0,0,0,13,14,6,1,-1,0,14,15,3,4,2,0,15,21,1,0,0,0,16,17,10,1,
        0,0,17,18,5,2,0,0,18,20,3,4,2,0,19,16,1,0,0,0,20,23,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,3,1,0,0,0,23,21,1,0,0,0,24,27,3,6,3,0,25,
        26,5,3,0,0,26,28,3,4,2,0,27,25,1,0,0,0,27,28,1,0,0,0,28,5,1,0,0,
        0,29,36,5,7,0,0,30,36,5,4,0,0,31,32,5,5,0,0,32,33,3,0,0,0,33,34,
        5,6,0,0,34,36,1,0,0,0,35,29,1,0,0,0,35,30,1,0,0,0,35,31,1,0,0,0,
        36,7,1,0,0,0,4,11,21,27,35
    ]

class PropLogicParser ( Parser ):

    grammarFileName = "PropLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'implies'", "'or'", "'and'", "'false'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Name", "WS" ]

    RULE_implicationExpr = 0
    RULE_disjunctionExpr = 1
    RULE_conjunctionExpr = 2
    RULE_atom = 3

    ruleNames =  [ "implicationExpr", "disjunctionExpr", "conjunctionExpr", 
                   "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    Name=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ImplicationExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disjunctionExpr(self):
            return self.getTypedRuleContext(PropLogicParser.DisjunctionExprContext,0)


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




    def implicationExpr(self):

        localctx = PropLogicParser.ImplicationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_implicationExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.disjunctionExpr(0)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 9
                self.match(PropLogicParser.T__0)
                self.state = 10
                self.implicationExpr()


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



    def disjunctionExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PropLogicParser.DisjunctionExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_disjunctionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.conjunctionExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PropLogicParser.DisjunctionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_disjunctionExpr)
                    self.state = 16
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 17
                    self.match(PropLogicParser.T__1)
                    self.state = 18
                    self.conjunctionExpr() 
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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

        def atom(self):
            return self.getTypedRuleContext(PropLogicParser.AtomContext,0)


        def conjunctionExpr(self):
            return self.getTypedRuleContext(PropLogicParser.ConjunctionExprContext,0)


        def getRuleIndex(self):
            return PropLogicParser.RULE_conjunctionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunctionExpr" ):
                listener.enterConjunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunctionExpr" ):
                listener.exitConjunctionExpr(self)




    def conjunctionExpr(self):

        localctx = PropLogicParser.ConjunctionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conjunctionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.atom()
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 25
                self.match(PropLogicParser.T__2)
                self.state = 26
                self.conjunctionExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(PropLogicParser.Name, 0)

        def implicationExpr(self):
            return self.getTypedRuleContext(PropLogicParser.ImplicationExprContext,0)


        def getRuleIndex(self):
            return PropLogicParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = PropLogicParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(PropLogicParser.Name)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(PropLogicParser.T__3)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(PropLogicParser.T__4)
                self.state = 32
                self.implicationExpr()
                self.state = 33
                self.match(PropLogicParser.T__5)
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
        self._predicates[1] = self.disjunctionExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def disjunctionExpr_sempred(self, localctx:DisjunctionExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




