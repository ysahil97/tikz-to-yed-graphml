grammar Tikz;
// import TikzLex;

// TODO see if empty rule can be replace with ?

begin   : BEGINTIKZPICTURE allGlobalProperties instructions* ENDTIKZPICTURE EOF;

instructions    : node instructions
                | node
                ;

node
    : NODE nodeId nodeProperties AT coordinates label SEMICOLON
    ;

nodeId
    : OPEN_PARANTHESES (VARIABLE|DIGIT)? CLOSE_PARANTHESES
    |
    ;

allGlobalProperties
    : '[' (globalProperties)? ']'
    |
    ;

globalProperties
    : globalProperties ',' globalProperties
    | EVERY VARIABLE '/.' 'style' '=' '{' properties '}'
    | properties
    ;

nodeProperties
    : '[' (properties)? ']'
    |
    ;

properties
    : individualProperty ',' properties
    | individualProperty
    ;

individualProperty
    : VARIABLE+ EQUAL_TO (VARIABLE|DIGIT)+
    | VARIABLE+
    ;

coordinates
    : OPEN_PARANTHESES DIGIT (COMMA|COLON) DIGIT CLOSE_PARANTHESES
    ;

label
    : OPEN_CURLY_BRACKETS (VARIABLE|DIGIT)? CLOSE_CURLY_BRACKETS
    ;

// label
//     : '{' ( '{' | '}' | . )*? '}'
//     ;

BEGINTIKZPICTURE: '\\begin{tikzpicture}';
ENDTIKZPICTURE: '\\end{tikzpicture}';

NODE: '\\node';
AT: 'at';
EVERY: 'every';

OPEN_PARANTHESES: '(';
CLOSE_PARANTHESES: ')';
OPEN_CURLY_BRACKETS: '{';
CLOSE_CURLY_BRACKETS: '}';
EQUAL_TO: '=';

COMMA: ',';
COLON: ':';
SEMICOLON: ';';

// DIGIT should be above VARIABLE for higher precedence
DIGIT: [0-9]+;
VARIABLE: [a-zA-Z0-9_!$.]+;

COMMENT : '%' ~[\n]* -> skip ;
WS : [ \r\t\n]+ -> skip ;
