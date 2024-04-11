grammar PropLogic;

genericExpr : equivalenceExpr;
equivalenceExpr : implicationExpr | implicationExpr EquivStr implicationExpr;
implicationExpr : disjunctionExpr | disjunctionExpr ImpliesStr implicationExpr;
disjunctionExpr : conjunctionExpr | disjunctionExpr OrStr conjunctionExpr;
conjunctionExpr : negationExpr | negationExpr AndStr conjunctionExpr;
negationExpr : atomicExpr | NotStr negationExpr;
atomicExpr : NameStr | FalseStr | '(' genericExpr ')' | '[' genericExpr ']';

NameStr : [a-zA-Z_][a-zA-Z_0-9]*;
EquivStr : 'equiv' | 'Equiv' | 'EQUIV' | 'equivalent' | 'Equivalent' | 'EQUIVALENT' | '<->' | '<=>' | '<-->' | '<==>';
ImpliesStr : 'implies' | 'Implies' | 'IMPLIES' | '->' | '=>';
OrStr : 'or' | 'Or' | 'OR' | '||' | '\\/';
AndStr : 'and' | 'And' | 'AND' | '&&' | '/\\';
NotStr : 'not' | 'Not' | 'NOT' | '!' | '~';
FalseStr : 'false' | 'False' | 'FALSE' | '0';

WS : [ \t\r\n]+ -> skip;  // Skip whitespaces
