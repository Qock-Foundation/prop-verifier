grammar PropLogic;

implicationExpr : disjunctionExpr | disjunctionExpr 'implies' implicationExpr | disjunctionExpr 'IMPLIES' implicationExpr | disjunctionExpr '->' implicationExpr | disjunctionExpr '=>' implicationExpr;
disjunctionExpr : conjunctionExpr | disjunctionExpr 'or' conjunctionExpr | disjunctionExpr 'OR' conjunctionExpr | disjunctionExpr '||' conjunctionExpr | disjunctionExpr '\\/' conjunctionExpr;
conjunctionExpr : atom | atom 'and' conjunctionExpr | atom 'AND' conjunctionExpr | atom '&&' conjunctionExpr | atom '/\\' conjunctionExpr;
atom : Name | 'false' | '(' implicationExpr ')' | '[' implicationExpr ']';
Name : [a-zA-Z_][a-zA-Z_0-9]*;

WS : [ \t\r\n]+ -> skip;  // Skip whitespaces
