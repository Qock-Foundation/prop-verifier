grammar PropLogic;

genericExpr : equivalenceExpr;
equivalenceExpr : implicationExpr | implicationExpr 'equiv' implicationExpr | implicationExpr 'EQUIV' implicationExpr | implicationExpr 'equivalent' implicationExpr | implicationExpr 'EQUIVALENT' implicationExpr | implicationExpr '<->' implicationExpr | implicationExpr '<=>' implicationExpr | implicationExpr '<-->' implicationExpr | implicationExpr '<==>' implicationExpr;
implicationExpr : disjunctionExpr | disjunctionExpr 'implies' implicationExpr | disjunctionExpr 'IMPLIES' implicationExpr | disjunctionExpr '->' implicationExpr | disjunctionExpr '=>' implicationExpr;
disjunctionExpr : conjunctionExpr | disjunctionExpr 'or' conjunctionExpr | disjunctionExpr 'OR' conjunctionExpr | disjunctionExpr '||' conjunctionExpr | disjunctionExpr '\\/' conjunctionExpr;
conjunctionExpr : negationExpr | negationExpr 'and' conjunctionExpr | negationExpr 'AND' conjunctionExpr | negationExpr '&&' conjunctionExpr | negationExpr '/\\' conjunctionExpr;
negationExpr : atom | 'not' negationExpr | 'NOT' negationExpr | '!' negationExpr | '~' negationExpr;
atom : Name | 'false' | '(' genericExpr ')' | '[' genericExpr ']';

Name : [a-zA-Z_][a-zA-Z_0-9]*;
WS : [ \t\r\n]+ -> skip;  // Skip whitespaces
