grammar PropLogic;

genericExpr : equivalenceExpr;
equivalenceExpr : implicationExpr | implicationExpr EquivStr implicationExpr;
implicationExpr : disjunctionExpr | disjunctionExpr ImpliesStr implicationExpr;
disjunctionExpr : xorExpr | disjunctionExpr OrStr xorExpr;
xorExpr : conjunctionExpr | xorExpr XorStr conjunctionExpr;
conjunctionExpr : negationExpr | conjunctionExpr AndStr negationExpr;
negationExpr : atomicExpr | NotStr negationExpr;
atomicExpr : FalseStr | Name | LParenStr genericExpr RParenStr | LBracketStr genericExpr RBracketStr;

EquivStr : 'equiv' | 'Equiv' | 'EQUIV' | 'equivalent' | '<->' | '<=>' | '<-->' | '<==>' | '⇔' | '↔';
ImpliesStr : 'implies' | 'IMPLIES' | '->' | '=>' | '⇒' | '→';
OrStr : 'or' | 'OR' | '||' | '\\/' | '∨';
XorStr : 'xor' | 'XOR' | '+' | '⊕';
AndStr : 'and' | 'AND' | '&&' | '*' | '/\\' | '∧';
NotStr : 'not' | 'NOT' | '!' | '~' | '¬';
FalseStr : 'false' | 'False' | 'FALSE' | '0' | 'null' | 'nil' | '⊥' | 'o_O';
LParenStr : '(';
RParenStr : ')';
LBracketStr : '[';
RBracketStr : ']';

Name : [a-zA-Z_][a-zA-Z_0-9]*;
WS : [ \t\r\n]+ -> skip;  // Skip whitespaces
