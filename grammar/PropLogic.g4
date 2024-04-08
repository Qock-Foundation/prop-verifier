grammar PropLogic;

implicationExpr : disjunctionExpr ('implies' implicationExpr)?;
disjunctionExpr : conjunctionExpr | disjunctionExpr 'or' conjunctionExpr;
conjunctionExpr : atom ('and' conjunctionExpr)?;
atom : Name | 'false' | '(' implicationExpr ')';
Name : [a-zA-Z_][a-zA-Z_0-9]*;

WS : [ \t\r\n]+ -> skip;  // Skip whitespaces
