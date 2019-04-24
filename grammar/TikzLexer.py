# Generated from grammar/Tikz.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("\u0084\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\6\20l\n\20\r\20\16\20m\3\21\6\21q\n\21")
        buf.write("\r\21\16\21r\3\22\3\22\7\22w\n\22\f\22\16\22z\13\22\3")
        buf.write("\22\3\22\3\23\6\23\177\n\23\r\23\16\23\u0080\3\23\3\23")
        buf.write("\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\3\2\6\3\2\62")
        buf.write(";\t\2##&&\60\60\62;C\\aac|\3\2\f\f\5\2\13\f\17\17\"\"")
        buf.write("\2\u0087\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5)\3\2\2\2\7+\3\2\2\2\t")
        buf.write("-\3\2\2\2\13A\3\2\2\2\rS\3\2\2\2\17Y\3\2\2\2\21\\\3\2")
        buf.write("\2\2\23^\3\2\2\2\25`\3\2\2\2\27b\3\2\2\2\31d\3\2\2\2\33")
        buf.write("f\3\2\2\2\35h\3\2\2\2\37k\3\2\2\2!p\3\2\2\2#t\3\2\2\2")
        buf.write("%~\3\2\2\2\'(\7]\2\2(\4\3\2\2\2)*\7_\2\2*\6\3\2\2\2+,")
        buf.write("\7?\2\2,\b\3\2\2\2-.\7^\2\2./\7d\2\2/\60\7g\2\2\60\61")
        buf.write("\7i\2\2\61\62\7k\2\2\62\63\7p\2\2\63\64\7}\2\2\64\65\7")
        buf.write("v\2\2\65\66\7k\2\2\66\67\7m\2\2\678\7|\2\289\7r\2\29:")
        buf.write("\7k\2\2:;\7e\2\2;<\7v\2\2<=\7w\2\2=>\7t\2\2>?\7g\2\2?")
        buf.write("@\7\177\2\2@\n\3\2\2\2AB\7^\2\2BC\7g\2\2CD\7p\2\2DE\7")
        buf.write("f\2\2EF\7}\2\2FG\7v\2\2GH\7k\2\2HI\7m\2\2IJ\7|\2\2JK\7")
        buf.write("r\2\2KL\7k\2\2LM\7e\2\2MN\7v\2\2NO\7w\2\2OP\7t\2\2PQ\7")
        buf.write("g\2\2QR\7\177\2\2R\f\3\2\2\2ST\7^\2\2TU\7p\2\2UV\7q\2")
        buf.write("\2VW\7f\2\2WX\7g\2\2X\16\3\2\2\2YZ\7c\2\2Z[\7v\2\2[\20")
        buf.write("\3\2\2\2\\]\7*\2\2]\22\3\2\2\2^_\7+\2\2_\24\3\2\2\2`a")
        buf.write("\7}\2\2a\26\3\2\2\2bc\7\177\2\2c\30\3\2\2\2de\7.\2\2e")
        buf.write("\32\3\2\2\2fg\7<\2\2g\34\3\2\2\2hi\7=\2\2i\36\3\2\2\2")
        buf.write("jl\t\2\2\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2n \3")
        buf.write("\2\2\2oq\t\3\2\2po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3\2\2")
        buf.write("\2s\"\3\2\2\2tx\7\'\2\2uw\n\4\2\2vu\3\2\2\2wz\3\2\2\2")
        buf.write("xv\3\2\2\2xy\3\2\2\2y{\3\2\2\2zx\3\2\2\2{|\b\22\2\2|$")
        buf.write("\3\2\2\2}\177\t\5\2\2~}\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0083\b\23\2\2\u0083&\3\2\2\2\7\2mrx\u0080\3\b\2\2")
        return buf.getvalue()


class TikzLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    BEGINTIKZPICTURE = 4
    ENDTIKZPICTURE = 5
    NODE = 6
    AT = 7
    OPEN_PARANTHESES = 8
    CLOSE_PARANTHESES = 9
    OPEN_CURLY_BRACKETS = 10
    CLOSE_CURLY_BRACKETS = 11
    COMMA = 12
    COLON = 13
    SEMICOLON = 14
    DIGIT = 15
    VARIABLE = 16
    COMMENT = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'='", "'\\begin{tikzpicture}'", "'\\end{tikzpicture}'", 
            "'\\node'", "'at'", "'('", "')'", "'{'", "'}'", "','", "':'", 
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "BEGINTIKZPICTURE", "ENDTIKZPICTURE", "NODE", "AT", "OPEN_PARANTHESES", 
            "CLOSE_PARANTHESES", "OPEN_CURLY_BRACKETS", "CLOSE_CURLY_BRACKETS", 
            "COMMA", "COLON", "SEMICOLON", "DIGIT", "VARIABLE", "COMMENT", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BEGINTIKZPICTURE", "ENDTIKZPICTURE", 
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


