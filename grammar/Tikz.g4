grammar Tikz;

begin   : '\\begin{tikzpicture}' instructions* '\\end{tikzpicture}';

instructions    : node instructions
                | node
                ;

node
    : '\\node' nodeID 'at' coordinates label DELIMITER
    ;

nodeID
    : '(' ID ')'
    | '(' ')'       // Node ID can be empty
    |
    ;

coordinates
    : '(' DIGIT ',' DIGIT ')'
    | '(' DIGIT ':' DIGIT ')'
    ;

label   
    : '{' ID '}'
    | '{' '}'    // Label can be empty
    ;

ID : [a-zA-Z] [a-zA-Z0-9]* ;
DIGIT: [0-9]+;
DELIMITER: ';';
WS : [ \r\t\n]+ -> skip ;