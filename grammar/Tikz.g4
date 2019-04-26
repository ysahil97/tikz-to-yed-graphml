grammar Tikz;
// import TikzLex;

// TODO see if empty rule can be replace with ?

begin
    : BEGINTIKZPICTURE allGlobalProperties instructions* ENDTIKZPICTURE EOF
    ;

instructions
    : node instructions
    | draw instructions
    | draw
    | node
    ;

draw
    : DRAW edgeProperties nodeList SEMICOLON
    | DRAW edgeProperties coordinates VARIABLE coordinates SEMICOLON
    | DRAW edgeProperties coordinates VARIABLE radius SEMICOLON
    | DRAW edgeProperties coordinates VARIABLE nodeProperties label SEMICOLON
    ;

radius
    : OPEN_PARANTHESES VARIABLE CLOSE_PARANTHESES
    ;

nodeList
    : edgeNode '--' nodeList
    | edgeNode
    ;

edgeNode
    : coordinates
    | OPEN_PARANTHESES VARIABLE CLOSE_PARANTHESES
    ;

edgeProperties
    : '[' (properties)? ']'
    |
    ;

node
    : NODE nodeProperties nodeId nodeProperties AT coordinates nodeProperties label SEMICOLON
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
    : OPEN_PARANTHESES (VARIABLE|DIGIT) (COMMA|AND) (VARIABLE|DIGIT) CLOSE_PARANTHESES #cartesianCoordinates
    | OPEN_PARANTHESES (VARIABLE|DIGIT) COLON (VARIABLE|DIGIT) CLOSE_PARANTHESES #polarCoordinates
    ;

// ACTION : '{' ( ACTION | ~[{}] )* '}' ;

label
    // -    : OPEN_CURLY_BRACKETS ( label | (VARIABLE|DIGIT))* CLOSE_CURLY_BRACKETS
    : OPEN_CURLY_BRACKETS (VARIABLE|DIGIT)? CLOSE_CURLY_BRACKETS
    ;

// label
//     : '{' ( '{' | '}' | . )*? '}'
//     ;

BEGINTIKZPICTURE: '\\begin{tikzpicture}';
ENDTIKZPICTURE: '\\end{tikzpicture}';

NODE: '\\node';
DRAW: '\\draw';
AT: 'at';
AND: 'and';
EVERY: 'every';

OPEN_PARANTHESES: '(';
CLOSE_PARANTHESES: ')';
OPEN_CURLY_BRACKETS: '{';
CLOSE_CURLY_BRACKETS: '}';
EQUAL_TO: '=';


COMMA: ',';
COLON: ':';
SEMICOLON: ';';

PAUSE : '\\pause' -> skip;

// DIGIT should be above VARIABLE for higher precedence
DIGIT: [0-9/*-+.]+;
VARIABLE: [-a-zA-Z0-9_!$.><|\\+]+;
COMMENT : '%' ~[\n]* -> skip ;
WS : [ \r\t\n]+ -> skip ;
