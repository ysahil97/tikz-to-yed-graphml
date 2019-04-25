# Generated from grammar/Tikz.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("\u0089\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r")
        buf.write("\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\6\21q\n\21\r\21")
        buf.write("\16\21r\3\22\6\22v\n\22\r\22\16\22w\3\23\3\23\7\23|\n")
        buf.write("\23\f\23\16\23\177\13\23\3\23\3\23\3\24\6\24\u0084\n\24")
        buf.write("\r\24\16\24\u0085\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25\3\2\6\4\2,-\61;\t\2##&&\60\60\62")
        buf.write(";C\\aac|\3\2\f\f\5\2\13\f\17\17\"\"\2\u008c\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2\7-\3\2\2\2\t/\3\2\2\2")
        buf.write("\13\62\3\2\2\2\rF\3\2\2\2\17X\3\2\2\2\21^\3\2\2\2\23a")
        buf.write("\3\2\2\2\25c\3\2\2\2\27e\3\2\2\2\31g\3\2\2\2\33i\3\2\2")
        buf.write("\2\35k\3\2\2\2\37m\3\2\2\2!p\3\2\2\2#u\3\2\2\2%y\3\2\2")
        buf.write("\2\'\u0083\3\2\2\2)*\7]\2\2*\4\3\2\2\2+,\7_\2\2,\6\3\2")
        buf.write("\2\2-.\7?\2\2.\b\3\2\2\2/\60\7e\2\2\60\61\7o\2\2\61\n")
        buf.write("\3\2\2\2\62\63\7^\2\2\63\64\7d\2\2\64\65\7g\2\2\65\66")
        buf.write("\7i\2\2\66\67\7k\2\2\678\7p\2\289\7}\2\29:\7v\2\2:;\7")
        buf.write("k\2\2;<\7m\2\2<=\7|\2\2=>\7r\2\2>?\7k\2\2?@\7e\2\2@A\7")
        buf.write("v\2\2AB\7w\2\2BC\7t\2\2CD\7g\2\2DE\7\177\2\2E\f\3\2\2")
        buf.write("\2FG\7^\2\2GH\7g\2\2HI\7p\2\2IJ\7f\2\2JK\7}\2\2KL\7v\2")
        buf.write("\2LM\7k\2\2MN\7m\2\2NO\7|\2\2OP\7r\2\2PQ\7k\2\2QR\7e\2")
        buf.write("\2RS\7v\2\2ST\7w\2\2TU\7t\2\2UV\7g\2\2VW\7\177\2\2W\16")
        buf.write("\3\2\2\2XY\7^\2\2YZ\7p\2\2Z[\7q\2\2[\\\7f\2\2\\]\7g\2")
        buf.write("\2]\20\3\2\2\2^_\7c\2\2_`\7v\2\2`\22\3\2\2\2ab\7*\2\2")
        buf.write("b\24\3\2\2\2cd\7+\2\2d\26\3\2\2\2ef\7}\2\2f\30\3\2\2\2")
        buf.write("gh\7\177\2\2h\32\3\2\2\2ij\7.\2\2j\34\3\2\2\2kl\7<\2\2")
        buf.write("l\36\3\2\2\2mn\7=\2\2n \3\2\2\2oq\t\2\2\2po\3\2\2\2qr")
        buf.write("\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\"\3\2\2\2tv\t\3\2\2ut\3")
        buf.write("\2\2\2vw\3\2\2\2wu\3\2\2\2wx\3\2\2\2x$\3\2\2\2y}\7\'\2")
        buf.write("\2z|\n\4\2\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2")
        buf.write("\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0081\b\23\2\2\u0081")
        buf.write("&\3\2\2\2\u0082\u0084\t\5\2\2\u0083\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u0088\b\24\2\2\u0088(\3\2\2")
        buf.write("\2\7\2rw}\u0085\3\b\2\2")
        return buf.getvalue()


class TikzLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    BEGINTIKZPICTURE = 5
    ENDTIKZPICTURE = 6
    NODE = 7
    AT = 8
    OPEN_PARANTHESES = 9
    CLOSE_PARANTHESES = 10
    OPEN_CURLY_BRACKETS = 11
    CLOSE_CURLY_BRACKETS = 12
    COMMA = 13
    COLON = 14
    SEMICOLON = 15
    DIGIT = 16
    VARIABLE = 17
    COMMENT = 18
    WS = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'='", "'cm'", "'\\begin{tikzpicture}'", "'\\end{tikzpicture}'", 
            "'\\node'", "'at'", "'('", "')'", "'{'", "'}'", "','", "':'", 
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "BEGINTIKZPICTURE", "ENDTIKZPICTURE", "NODE", "AT", "OPEN_PARANTHESES", 
            "CLOSE_PARANTHESES", "OPEN_CURLY_BRACKETS", "CLOSE_CURLY_BRACKETS", 
            "COMMA", "COLON", "SEMICOLON", "DIGIT", "VARIABLE", "COMMENT", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "BEGINTIKZPICTURE", "ENDTIKZPICTURE", 
                  "NODE", "AT", "OPEN_PARANTHESES", "CLOSE_PARANTHESES", 
                  "OPEN_CURLY_BRACKETS", "CLOSE_CURLY_BRACKETS", "COMMA", 
                  "COLON", "SEMICOLON", "DIGIT", "VARIABLE", "COMMENT", 
                  "WS" ]

    grammarFileName = "Tikz.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


