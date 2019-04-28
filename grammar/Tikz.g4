grammar Tikz;
// import TikzLex;


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
    | DRAW edgeProperties coordinates (VARIABLE|EXPRESSION) coordinates SEMICOLON
    | DRAW edgeProperties coordinates (VARIABLE|EXPRESSION) radius SEMICOLON
    | DRAW edgeProperties coordinates (VARIABLE|EXPRESSION) nodeProperties label SEMICOLON
    ;

radius
    : OPEN_PARANTHESES (VARIABLE|EXPRESSION) CLOSE_PARANTHESES
    ;

nodeList
    : edgeNode '--' nodeList
    | edgeNode
    ;

edgeNode
    : coordinates
    | OPEN_PARANTHESES (VARIABLE|EXPRESSION) CLOSE_PARANTHESES
    ;

edgeProperties
    : '[' (properties)? ']'
    |
    ;

node
    : NODE nodeProperties nodeId nodeProperties AT coordinates nodeProperties label SEMICOLON
    ;

nodeId
    : OPEN_PARANTHESES (VARIABLE|EXPRESSION)? CLOSE_PARANTHESES
    |
    ;

allGlobalProperties
    : '[' (globalProperties)? ']'
    |
    ;

globalProperties
    : globalProperties ',' globalProperties
    | EVERY (VARIABLE|EXPRESSION) '/.' 'style' '=' '{' properties '}'
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
    : (VARIABLE|EXPRESSION)+ EQUAL_TO (VARIABLE|EXPRESSION)+
    | (VARIABLE|EXPRESSION)+
    ;

coordinates
    : OPEN_PARANTHESES (VARIABLE|EXPRESSION) (COMMA|AND) (VARIABLE|EXPRESSION) CLOSE_PARANTHESES #cartesianCoordinates
    | OPEN_PARANTHESES (VARIABLE|EXPRESSION) COLON (VARIABLE|EXPRESSION) CLOSE_PARANTHESES #polarCoordinates
    ;

label
    : OPEN_CURLY_BRACKETS (VARIABLE|EXPRESSION)? CLOSE_CURLY_BRACKETS
    ;

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

// EXPRESSION should be above VARIABLE for higher precedence
EXPRESSION: [0-9/*-+.]+;
// VARIABLE: ~[ \r\t\n;()]+?;
VARIABLE: [-a-zA-Z0-9_!$.><|\\+]+;
COMMENT : '%' ~[\n]* -> skip ;
WS : [ \r\t\n]+ -> skip ;