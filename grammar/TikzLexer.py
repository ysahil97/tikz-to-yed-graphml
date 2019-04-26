# Generated from grammar/Tikz.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35")
        buf.write("\u00c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\6\31\u00a9\n")
        buf.write("\31\r\31\16\31\u00aa\3\32\6\32\u00ae\n\32\r\32\16\32\u00af")
        buf.write("\3\33\3\33\7\33\u00b4\n\33\f\33\16\33\u00b7\13\33\3\33")
        buf.write("\3\33\3\34\6\34\u00bc\n\34\r\34\16\34\u00bd\3\34\3\34")
        buf.write("\2\2\35\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30/\31\61\32\63\33\65\34\67\35\3\2\6\4\2,-\60;\16\2")
        buf.write("##&&--/\60\62;>>@@C\\^^aac|~~\3\2\f\f\5\2\13\f\17\17\"")
        buf.write("\"\2\u00c4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\39\3\2\2\2\5<\3\2\2\2\7>\3\2\2\2")
        buf.write("\t@\3\2\2\2\13C\3\2\2\2\rI\3\2\2\2\17L\3\2\2\2\21O\3\2")
        buf.write("\2\2\23c\3\2\2\2\25u\3\2\2\2\27{\3\2\2\2\31\u0081\3\2")
        buf.write("\2\2\33\u0084\3\2\2\2\35\u0088\3\2\2\2\37\u008e\3\2\2")
        buf.write("\2!\u0090\3\2\2\2#\u0092\3\2\2\2%\u0094\3\2\2\2\'\u0096")
        buf.write("\3\2\2\2)\u0098\3\2\2\2+\u009a\3\2\2\2-\u009c\3\2\2\2")
        buf.write("/\u009e\3\2\2\2\61\u00a8\3\2\2\2\63\u00ad\3\2\2\2\65\u00b1")
        buf.write("\3\2\2\2\67\u00bb\3\2\2\29:\7/\2\2:;\7/\2\2;\4\3\2\2\2")
        buf.write("<=\7]\2\2=\6\3\2\2\2>?\7_\2\2?\b\3\2\2\2@A\7\61\2\2AB")
        buf.write("\7\60\2\2B\n\3\2\2\2CD\7u\2\2DE\7v\2\2EF\7{\2\2FG\7n\2")
        buf.write("\2GH\7g\2\2H\f\3\2\2\2IJ\7e\2\2JK\7o\2\2K\16\3\2\2\2L")
        buf.write("M\7r\2\2MN\7v\2\2N\20\3\2\2\2OP\7^\2\2PQ\7d\2\2QR\7g\2")
        buf.write("\2RS\7i\2\2ST\7k\2\2TU\7p\2\2UV\7}\2\2VW\7v\2\2WX\7k\2")
        buf.write("\2XY\7m\2\2YZ\7|\2\2Z[\7r\2\2[\\\7k\2\2\\]\7e\2\2]^\7")
        buf.write("v\2\2^_\7w\2\2_`\7t\2\2`a\7g\2\2ab\7\177\2\2b\22\3\2\2")
        buf.write("\2cd\7^\2\2de\7g\2\2ef\7p\2\2fg\7f\2\2gh\7}\2\2hi\7v\2")
        buf.write("\2ij\7k\2\2jk\7m\2\2kl\7|\2\2lm\7r\2\2mn\7k\2\2no\7e\2")
        buf.write("\2op\7v\2\2pq\7w\2\2qr\7t\2\2rs\7g\2\2st\7\177\2\2t\24")
        buf.write("\3\2\2\2uv\7^\2\2vw\7p\2\2wx\7q\2\2xy\7f\2\2yz\7g\2\2")
        buf.write("z\26\3\2\2\2{|\7^\2\2|}\7f\2\2}~\7t\2\2~\177\7c\2\2\177")
        buf.write("\u0080\7y\2\2\u0080\30\3\2\2\2\u0081\u0082\7c\2\2\u0082")
        buf.write("\u0083\7v\2\2\u0083\32\3\2\2\2\u0084\u0085\7c\2\2\u0085")
        buf.write("\u0086\7p\2\2\u0086\u0087\7f\2\2\u0087\34\3\2\2\2\u0088")
        buf.write("\u0089\7g\2\2\u0089\u008a\7x\2\2\u008a\u008b\7g\2\2\u008b")
        buf.write("\u008c\7t\2\2\u008c\u008d\7{\2\2\u008d\36\3\2\2\2\u008e")
        buf.write("\u008f\7*\2\2\u008f \3\2\2\2\u0090\u0091\7+\2\2\u0091")
        buf.write("\"\3\2\2\2\u0092\u0093\7}\2\2\u0093$\3\2\2\2\u0094\u0095")
        buf.write("\7\177\2\2\u0095&\3\2\2\2\u0096\u0097\7?\2\2\u0097(\3")
        buf.write("\2\2\2\u0098\u0099\7.\2\2\u0099*\3\2\2\2\u009a\u009b\7")
        buf.write("<\2\2\u009b,\3\2\2\2\u009c\u009d\7=\2\2\u009d.\3\2\2\2")
        buf.write("\u009e\u009f\7^\2\2\u009f\u00a0\7r\2\2\u00a0\u00a1\7c")
        buf.write("\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\b\30\2\2\u00a6")
        buf.write("\60\3\2\2\2\u00a7\u00a9\t\2\2\2\u00a8\u00a7\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\62\3\2\2\2\u00ac\u00ae\t\3\2\2\u00ad\u00ac\3\2")
        buf.write("\2\2\u00ae\u00af\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\64\3\2\2\2\u00b1\u00b5\7\'\2\2\u00b2\u00b4")
        buf.write("\n\4\2\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b8\u00b9\b\33\2\2\u00b9\66\3\2")
        buf.write("\2\2\u00ba\u00bc\t\5\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd")
        buf.write("\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c0\b\34\2\2\u00c08\3\2\2\2\7\2")
        buf.write("\u00aa\u00af\u00b5\u00bd\3\b\2\2")
        return buf.getvalue()


class TikzLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    BEGINTIKZPICTURE = 8
    ENDTIKZPICTURE = 9
    NODE = 10
    DRAW = 11
    AT = 12
    AND = 13
    EVERY = 14
    OPEN_PARANTHESES = 15
    CLOSE_PARANTHESES = 16
    OPEN_CURLY_BRACKETS = 17
    CLOSE_CURLY_BRACKETS = 18
    EQUAL_TO = 19
    COMMA = 20
    COLON = 21
    SEMICOLON = 22
    PAUSE = 23
    DIGIT = 24
    VARIABLE = 25
    COMMENT = 26
    WS = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'--'", "'['", "']'", "'/.'", "'style'", "'cm'", "'pt'", "'\\begin{tikzpicture}'", 
            "'\\end{tikzpicture}'", "'\\node'", "'\\draw'", "'at'", "'and'", 
            "'every'", "'('", "')'", "'{'", "'}'", "'='", "','", "':'", 
            "';'", "'\\pause'" ]

    symbolicNames = [ "<INVALID>",
            "BEGINTIKZPICTURE", "ENDTIKZPICTURE", "NODE", "DRAW", "AT", 
            "AND", "EVERY", "OPEN_PARANTHESES", "CLOSE_PARANTHESES", "OPEN_CURLY_BRACKETS", 
            "CLOSE_CURLY_BRACKETS", "EQUAL_TO", "COMMA", "COLON", "SEMICOLON", 
            "PAUSE", "DIGIT", "VARIABLE", "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "BEGINTIKZPICTURE", "ENDTIKZPICTURE", "NODE", "DRAW", 
                  "AT", "AND", "EVERY", "OPEN_PARANTHESES", "CLOSE_PARANTHESES", 
                  "OPEN_CURLY_BRACKETS", "CLOSE_CURLY_BRACKETS", "EQUAL_TO", 
                  "COMMA", "COLON", "SEMICOLON", "PAUSE", "DIGIT", "VARIABLE", 
                  "COMMENT", "WS" ]

    grammarFileName = "Tikz.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


