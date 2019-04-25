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
    : NODE nodeId nodeProperties AT coordinates label SEMICOLON
    ;

nodeId
    : OPEN_PARANTHESES (VARIABLE)? CLOSE_PARANTHESES
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
    : VARIABLE+ EQUAL_TO (VARIABLE)+
    | VARIABLE+
    ;

coordinates
    : OPEN_PARANTHESES VARIABLE COMMA VARIABLE ('cm'|'pt')? CLOSE_PARANTHESES #cartesianCoordinates
    | OPEN_PARANTHESES VARIABLE COLON VARIABLE ('cm'|'pt')? CLOSE_PARANTHESES #polarCoordinates
    ;

// ACTION : '{' ( ACTION | ~[{}] )* '}' ;

label
    // -    : OPEN_CURLY_BRACKETS ( label | (VARIABLE))* CLOSE_CURLY_BRACKETS
    : OPEN_CURLY_BRACKETS (VARIABLE)? CLOSE_CURLY_BRACKETS
    ;

// label
//     : '{' ( '{' | '}' | . )*? '}'
//     ;

BEGINTIKZPICTURE: '\\begin{tikzpicture}';
ENDTIKZPICTURE: '\\end{tikzpicture}';

NODE: '\\node';
DRAW: '\\draw';
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

VARIABLE: [-a-zA-Z0-9_!$.><|\\+*]+;
COMMENT : '%' ~[\n]* -> skip ;
WS : [ \r\t\n]+ -> skip ;
