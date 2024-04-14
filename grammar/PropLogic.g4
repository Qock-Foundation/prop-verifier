grammar PropLogic;

genericExpr : equivalenceExpr;
equivalenceExpr : implicationExpr | implicationExpr EquivStr implicationExpr;
implicationExpr : disjunctionExpr | disjunctionExpr ImpliesStr implicationExpr;
disjunctionExpr : conjunctionExpr | conjunctionExpr OrStr disjunctionExpr;
conjunctionExpr : negationExpr | conjunctionExpr AndStr negationExpr;
negationExpr : atomicExpr | NotStr negationExpr;
atomicExpr : FalseStr | Name | LParenStr genericExpr RParenStr | LBracketStr genericExpr RBracketStr;

EquivStr : 'equiv' | 'Equiv' | 'EQUIV' | 'equivalent' | '<->' | '<=>' | '<-->' | '<==> ';
ImpliesStr : 'implies' | 'IMPLIES' | '->' | '=>';
OrStr : 'or' | 'OR' | '||' | '\\/';
AndStr : 'and' | 'AND' | '&&' | '/\\';
NotStr : 'not' | 'NOT' | '!' | '~';
FalseStr : 'false' | 'False' | 'FALSE' | '0' | 'null' | 'nil';
LParenStr : '(';
RParenStr : ')';
LBracketStr : '[';
RBracketStr : ']';

Name : [a-zA-Z_][a-zA-Z_0-9]*;
WS : [ \t\r\n]+ -> skip;  // Skip whitespaces
