# Generated from PropLogic.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,56,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,5,6,45,
        8,6,10,6,12,6,48,9,6,1,7,4,7,51,8,7,11,7,12,7,52,1,7,1,7,0,0,8,1,
        1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,3,3,0,65,90,95,95,97,122,4,
        0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,57,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,25,1,0,0,0,5,28,1,0,0,0,7,32,
        1,0,0,0,9,38,1,0,0,0,11,40,1,0,0,0,13,42,1,0,0,0,15,50,1,0,0,0,17,
        18,5,105,0,0,18,19,5,109,0,0,19,20,5,112,0,0,20,21,5,108,0,0,21,
        22,5,105,0,0,22,23,5,101,0,0,23,24,5,115,0,0,24,2,1,0,0,0,25,26,
        5,111,0,0,26,27,5,114,0,0,27,4,1,0,0,0,28,29,5,97,0,0,29,30,5,110,
        0,0,30,31,5,100,0,0,31,6,1,0,0,0,32,33,5,102,0,0,33,34,5,97,0,0,
        34,35,5,108,0,0,35,36,5,115,0,0,36,37,5,101,0,0,37,8,1,0,0,0,38,
        39,5,40,0,0,39,10,1,0,0,0,40,41,5,41,0,0,41,12,1,0,0,0,42,46,7,0,
        0,0,43,45,7,1,0,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,14,1,0,0,0,48,46,1,0,0,0,49,51,7,2,0,0,50,49,1,0,0,0,
        51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,6,
        7,0,0,55,16,1,0,0,0,3,0,46,52,1,6,0,0
    ]

class PropLogicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    Name = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'implies'", "'or'", "'and'", "'false'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "Name", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "Name", 
                  "WS" ]

    grammarFileName = "PropLogic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


