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
    ;

coordinates
    : '(' DIGIT ',' DIGIT ')'
    | '(' DIGIT ':' DIGIT ')'
    ;

label   
    : '{' ID '}'
    ;

ID : [a-zA-Z] [a-zA-Z0-9]* ; // match usual identifier spec
DIGIT: [0-9]+;
DELIMITER: ';';
WS : [ \r\t\n]+ -> skip ;