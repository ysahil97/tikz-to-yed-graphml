# Generated from tikz2graphml/grammar/Tikz.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\34")
        buf.write("\u00c9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\7\27\u00a2\n\27\f\27\16\27\u00a5\13\27\3\27")
        buf.write("\3\27\7\27\u00a9\n\27\f\27\16\27\u00ac\13\27\3\27\3\27")
        buf.write("\3\30\6\30\u00b1\n\30\r\30\16\30\u00b2\3\31\6\31\u00b6")
        buf.write("\n\31\r\31\16\31\u00b7\3\32\3\32\7\32\u00bc\n\32\f\32")
        buf.write("\16\32\u00bf\13\32\3\32\3\32\3\33\6\33\u00c4\n\33\r\33")
        buf.write("\16\33\u00c5\3\33\3\33\3\u00a3\2\34\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\3\2\7\3\2\f\f\5\2\13\13\17\17\"\"\4\2,-\60;\16\2##&&")
        buf.write("--/\60\62;>>@@C\\^^aac|~~\5\2\13\f\17\17\"\"\2\u00ce\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\3\67")
        buf.write("\3\2\2\2\5:\3\2\2\2\7<\3\2\2\2\t>\3\2\2\2\13A\3\2\2\2")
        buf.write("\rG\3\2\2\2\17I\3\2\2\2\21K\3\2\2\2\23_\3\2\2\2\25q\3")
        buf.write("\2\2\2\27w\3\2\2\2\31}\3\2\2\2\33\u0080\3\2\2\2\35\u0084")
        buf.write("\3\2\2\2\37\u008a\3\2\2\2!\u008c\3\2\2\2#\u008e\3\2\2")
        buf.write("\2%\u0090\3\2\2\2\'\u0092\3\2\2\2)\u0094\3\2\2\2+\u0096")
        buf.write("\3\2\2\2-\u009f\3\2\2\2/\u00b0\3\2\2\2\61\u00b5\3\2\2")
        buf.write("\2\63\u00b9\3\2\2\2\65\u00c3\3\2\2\2\678\7/\2\289\7/\2")
        buf.write("\29\4\3\2\2\2:;\7]\2\2;\6\3\2\2\2<=\7_\2\2=\b\3\2\2\2")
        buf.write(">?\7\61\2\2?@\7\60\2\2@\n\3\2\2\2AB\7u\2\2BC\7v\2\2CD")
        buf.write("\7{\2\2DE\7n\2\2EF\7g\2\2F\f\3\2\2\2GH\7}\2\2H\16\3\2")
        buf.write("\2\2IJ\7\177\2\2J\20\3\2\2\2KL\7^\2\2LM\7d\2\2MN\7g\2")
        buf.write("\2NO\7i\2\2OP\7k\2\2PQ\7p\2\2QR\7}\2\2RS\7v\2\2ST\7k\2")
        buf.write("\2TU\7m\2\2UV\7|\2\2VW\7r\2\2WX\7k\2\2XY\7e\2\2YZ\7v\2")
        buf.write("\2Z[\7w\2\2[\\\7t\2\2\\]\7g\2\2]^\7\177\2\2^\22\3\2\2")
        buf.write("\2_`\7^\2\2`a\7g\2\2ab\7p\2\2bc\7f\2\2cd\7}\2\2de\7v\2")
        buf.write("\2ef\7k\2\2fg\7m\2\2gh\7|\2\2hi\7r\2\2ij\7k\2\2jk\7e\2")
        buf.write("\2kl\7v\2\2lm\7w\2\2mn\7t\2\2no\7g\2\2op\7\177\2\2p\24")
        buf.write("\3\2\2\2qr\7^\2\2rs\7p\2\2st\7q\2\2tu\7f\2\2uv\7g\2\2")
        buf.write("v\26\3\2\2\2wx\7^\2\2xy\7f\2\2yz\7t\2\2z{\7c\2\2{|\7y")
        buf.write("\2\2|\30\3\2\2\2}~\7c\2\2~\177\7v\2\2\177\32\3\2\2\2\u0080")
        buf.write("\u0081\7c\2\2\u0081\u0082\7p\2\2\u0082\u0083\7f\2\2\u0083")
        buf.write("\34\3\2\2\2\u0084\u0085\7g\2\2\u0085\u0086\7x\2\2\u0086")
        buf.write("\u0087\7g\2\2\u0087\u0088\7t\2\2\u0088\u0089\7{\2\2\u0089")
        buf.write("\36\3\2\2\2\u008a\u008b\7*\2\2\u008b \3\2\2\2\u008c\u008d")
        buf.write("\7+\2\2\u008d\"\3\2\2\2\u008e\u008f\7?\2\2\u008f$\3\2")
        buf.write("\2\2\u0090\u0091\7.\2\2\u0091&\3\2\2\2\u0092\u0093\7<")
        buf.write("\2\2\u0093(\3\2\2\2\u0094\u0095\7=\2\2\u0095*\3\2\2\2")
        buf.write("\u0096\u0097\7^\2\2\u0097\u0098\7r\2\2\u0098\u0099\7c")
        buf.write("\2\2\u0099\u009a\7w\2\2\u009a\u009b\7u\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\3\2\2\2\u009d\u009e\b\26\2\2\u009e")
        buf.write(",\3\2\2\2\u009f\u00a3\7}\2\2\u00a0\u00a2\n\2\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a6\u00aa\7\177\2\2\u00a7\u00a9\t\3\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2")
        buf.write("\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3\2\2\2\u00ac\u00aa\3")
        buf.write("\2\2\2\u00ad\u00ae\7=\2\2\u00ae.\3\2\2\2\u00af\u00b1\t")
        buf.write("\4\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\60\3\2\2\2\u00b4\u00b6")
        buf.write("\t\5\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\62\3\2\2\2\u00b9")
        buf.write("\u00bd\7\'\2\2\u00ba\u00bc\n\2\2\2\u00bb\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3")
        buf.write("\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c1")
        buf.write("\b\32\2\2\u00c1\64\3\2\2\2\u00c2\u00c4\t\6\2\2\u00c3\u00c2")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\b\33\2")
        buf.write("\2\u00c8\66\3\2\2\2\t\2\u00a3\u00aa\u00b2\u00b7\u00bd")
        buf.write("\u00c5\3\b\2\2")
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
    EQUAL_TO = 17
    COMMA = 18
    COLON = 19
    SEMICOLON = 20
    PAUSE = 21
    LABEL_VARIABLE = 22
    EXPRESSION = 23
    VARIABLE = 24
    COMMENT = 25
    WS = 26

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'--'", "'['", "']'", "'/.'", "'style'", "'{'", "'}'", "'\\begin{tikzpicture}'", 
            "'\\end{tikzpicture}'", "'\\node'", "'\\draw'", "'at'", "'and'", 
            "'every'", "'('", "')'", "'='", "','", "':'", "';'", "'\\pause'" ]

    symbolicNames = [ "<INVALID>",
            "BEGINTIKZPICTURE", "ENDTIKZPICTURE", "NODE", "DRAW", "AT", 
            "AND", "EVERY", "OPEN_PARANTHESES", "CLOSE_PARANTHESES", "EQUAL_TO", 
            "COMMA", "COLON", "SEMICOLON", "PAUSE", "LABEL_VARIABLE", "EXPRESSION", 
            "VARIABLE", "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "BEGINTIKZPICTURE", "ENDTIKZPICTURE", "NODE", "DRAW", 
                  "AT", "AND", "EVERY", "OPEN_PARANTHESES", "CLOSE_PARANTHESES", 
                  "EQUAL_TO", "COMMA", "COLON", "SEMICOLON", "PAUSE", "LABEL_VARIABLE", 
                  "EXPRESSION", "VARIABLE", "COMMENT", "WS" ]

    grammarFileName = "Tikz.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


