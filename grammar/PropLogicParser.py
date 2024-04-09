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
        4,1,19,79,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,26,8,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,43,8,1,10,
        1,12,1,46,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,3,2,65,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,77,8,3,1,3,0,1,2,4,0,2,4,6,0,0,89,0,25,1,0,0,0,2,27,1,0,
        0,0,4,64,1,0,0,0,6,76,1,0,0,0,8,26,3,2,1,0,9,10,3,2,1,0,10,11,5,
        1,0,0,11,12,3,0,0,0,12,26,1,0,0,0,13,14,3,2,1,0,14,15,5,2,0,0,15,
        16,3,0,0,0,16,26,1,0,0,0,17,18,3,2,1,0,18,19,5,3,0,0,19,20,3,0,0,
        0,20,26,1,0,0,0,21,22,3,2,1,0,22,23,5,4,0,0,23,24,3,0,0,0,24,26,
        1,0,0,0,25,8,1,0,0,0,25,9,1,0,0,0,25,13,1,0,0,0,25,17,1,0,0,0,25,
        21,1,0,0,0,26,1,1,0,0,0,27,28,6,1,-1,0,28,29,3,4,2,0,29,44,1,0,0,
        0,30,31,10,4,0,0,31,32,5,5,0,0,32,43,3,4,2,0,33,34,10,3,0,0,34,35,
        5,6,0,0,35,43,3,4,2,0,36,37,10,2,0,0,37,38,5,7,0,0,38,43,3,4,2,0,
        39,40,10,1,0,0,40,41,5,8,0,0,41,43,3,4,2,0,42,30,1,0,0,0,42,33,1,
        0,0,0,42,36,1,0,0,0,42,39,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,
        45,1,0,0,0,45,3,1,0,0,0,46,44,1,0,0,0,47,65,3,6,3,0,48,49,3,6,3,
        0,49,50,5,9,0,0,50,51,3,4,2,0,51,65,1,0,0,0,52,53,3,6,3,0,53,54,
        5,10,0,0,54,55,3,4,2,0,55,65,1,0,0,0,56,57,3,6,3,0,57,58,5,11,0,
        0,58,59,3,4,2,0,59,65,1,0,0,0,60,61,3,6,3,0,61,62,5,12,0,0,62,63,
        3,4,2,0,63,65,1,0,0,0,64,47,1,0,0,0,64,48,1,0,0,0,64,52,1,0,0,0,
        64,56,1,0,0,0,64,60,1,0,0,0,65,5,1,0,0,0,66,77,5,18,0,0,67,77,5,
        13,0,0,68,69,5,14,0,0,69,70,3,0,0,0,70,71,5,15,0,0,71,77,1,0,0,0,
        72,73,5,16,0,0,73,74,3,0,0,0,74,75,5,17,0,0,75,77,1,0,0,0,76,66,
        1,0,0,0,76,67,1,0,0,0,76,68,1,0,0,0,76,72,1,0,0,0,77,7,1,0,0,0,5,
        25,42,44,64,76
    ]

class PropLogicParser ( Parser ):

    grammarFileName = "PropLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'implies'", "'IMPLIES'", "'->'", "'=>'", 
                     "'or'", "'OR'", "'||'", "'\\/'", "'and'", "'AND'", 
                     "'&&'", "'/\\'", "'false'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Name", "WS" ]

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
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    Name=18
    WS=19

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicationExpr" ):
                return visitor.visitImplicationExpr(self)
            else:
                return visitor.visitChildren(self)




    def implicationExpr(self):

        localctx = PropLogicParser.ImplicationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_implicationExpr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.disjunctionExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.disjunctionExpr(0)
                self.state = 10
                self.match(PropLogicParser.T__0)
                self.state = 11
                self.implicationExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                self.disjunctionExpr(0)
                self.state = 14
                self.match(PropLogicParser.T__1)
                self.state = 15
                self.implicationExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.disjunctionExpr(0)
                self.state = 18
                self.match(PropLogicParser.T__2)
                self.state = 19
                self.implicationExpr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 21
                self.disjunctionExpr(0)
                self.state = 22
                self.match(PropLogicParser.T__3)
                self.state = 23
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



    def disjunctionExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PropLogicParser.DisjunctionExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_disjunctionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.conjunctionExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = PropLogicParser.DisjunctionExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_disjunctionExpr)
                        self.state = 30
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 31
                        self.match(PropLogicParser.T__4)
                        self.state = 32
                        self.conjunctionExpr()
                        pass

                    elif la_ == 2:
                        localctx = PropLogicParser.DisjunctionExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_disjunctionExpr)
                        self.state = 33
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 34
                        self.match(PropLogicParser.T__5)
                        self.state = 35
                        self.conjunctionExpr()
                        pass

                    elif la_ == 3:
                        localctx = PropLogicParser.DisjunctionExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_disjunctionExpr)
                        self.state = 36
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 37
                        self.match(PropLogicParser.T__6)
                        self.state = 38
                        self.conjunctionExpr()
                        pass

                    elif la_ == 4:
                        localctx = PropLogicParser.DisjunctionExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_disjunctionExpr)
                        self.state = 39
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 40
                        self.match(PropLogicParser.T__7)
                        self.state = 41
                        self.conjunctionExpr()
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunctionExpr" ):
                return visitor.visitConjunctionExpr(self)
            else:
                return visitor.visitChildren(self)




    def conjunctionExpr(self):

        localctx = PropLogicParser.ConjunctionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conjunctionExpr)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.atom()
                self.state = 49
                self.match(PropLogicParser.T__8)
                self.state = 50
                self.conjunctionExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.atom()
                self.state = 53
                self.match(PropLogicParser.T__9)
                self.state = 54
                self.conjunctionExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.atom()
                self.state = 57
                self.match(PropLogicParser.T__10)
                self.state = 58
                self.conjunctionExpr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.atom()
                self.state = 61
                self.match(PropLogicParser.T__11)
                self.state = 62
                self.conjunctionExpr()
                pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = PropLogicParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(PropLogicParser.Name)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(PropLogicParser.T__12)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(PropLogicParser.T__13)
                self.state = 69
                self.implicationExpr()
                self.state = 70
                self.match(PropLogicParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(PropLogicParser.T__15)
                self.state = 73
                self.implicationExpr()
                self.state = 74
                self.match(PropLogicParser.T__16)
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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




