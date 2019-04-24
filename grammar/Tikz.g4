grammar Tikz;
// import TikzLex;

begin   : BEGINTIKZPICTURE (globalProperties)? instructions* ENDTIKZPICTURE EOF;


globalProperties
    : '[' globalProperty ']'
    |
    ;

globalProperty
    : .
    ;

instructions    : node instructions
                | node
                ;

node
    : NODE nodeId nodeProperties AT coordinates label SEMICOLON
    ;

nodeId
    : OPEN_PARANTHESES (VARIABLE)? CLOSE_PARANTHESES
    |
;

nodeProperties
    : '[' properties ']'
    |
    ;

properties
    : individualProperty ',' properties
    | individualProperty
    ;

individualProperty
    : VARIABLE+ '=' VARIABLE+
    | VARIABLE+
    ;

coordinates
    : OPEN_PARANTHESES DIGIT (COMMA|COLON) DIGIT CLOSE_PARANTHESES
    ;

label
    : OPEN_CURLY_BRACKETS (VARIABLE)? CLOSE_CURLY_BRACKETS
    ;

// label
//     : '{' ( '{' | '}' | . )*? '}'
//     ;

BEGINTIKZPICTURE: '\\begin{tikzpicture}';
ENDTIKZPICTURE: '\\end{tikzpicture}';

NODE: '\\node';
AT: 'at';

OPEN_PARANTHESES: '(';
CLOSE_PARANTHESES: ')';
OPEN_CURLY_BRACKETS: '{';
CLOSE_CURLY_BRACKETS: '}';

COMMA: ',';
COLON: ':';
SEMICOLON: ';';

// DIGIT should be above VARIABLE for higher precedence
DIGIT: [0-9]+;
VARIABLE: [a-zA-Z0-9_!$.]+;

COMMENT : '%' ~[\n]* -> skip ;
WS : [ \r\t\n]+ -> skip ;
