# Generated from Tikz.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("o\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\7\f]\n")
        buf.write("\f\f\f\16\f`\13\f\3\r\6\rc\n\r\r\r\16\rd\3\16\3\16\3\17")
        buf.write("\6\17j\n\17\r\17\16\17k\3\17\3\17\2\2\20\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2\62;\5\2\13\f\17\17\"")
        buf.write("\"\2q\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5\63\3\2\2\2\7E\3\2")
        buf.write("\2\2\tK\3\2\2\2\13N\3\2\2\2\rP\3\2\2\2\17R\3\2\2\2\21")
        buf.write("T\3\2\2\2\23V\3\2\2\2\25X\3\2\2\2\27Z\3\2\2\2\31b\3\2")
        buf.write("\2\2\33f\3\2\2\2\35i\3\2\2\2\37 \7^\2\2 !\7d\2\2!\"\7")
        buf.write("g\2\2\"#\7i\2\2#$\7k\2\2$%\7p\2\2%&\7}\2\2&\'\7v\2\2\'")
        buf.write("(\7k\2\2()\7m\2\2)*\7|\2\2*+\7r\2\2+,\7k\2\2,-\7e\2\2")
        buf.write("-.\7v\2\2./\7w\2\2/\60\7t\2\2\60\61\7g\2\2\61\62\7\177")
        buf.write("\2\2\62\4\3\2\2\2\63\64\7^\2\2\64\65\7g\2\2\65\66\7p\2")
        buf.write("\2\66\67\7f\2\2\678\7}\2\289\7v\2\29:\7k\2\2:;\7m\2\2")
        buf.write(";<\7|\2\2<=\7r\2\2=>\7k\2\2>?\7e\2\2?@\7v\2\2@A\7w\2\2")
        buf.write("AB\7t\2\2BC\7g\2\2CD\7\177\2\2D\6\3\2\2\2EF\7^\2\2FG\7")
        buf.write("p\2\2GH\7q\2\2HI\7f\2\2IJ\7g\2\2J\b\3\2\2\2KL\7c\2\2L")
        buf.write("M\7v\2\2M\n\3\2\2\2NO\7*\2\2O\f\3\2\2\2PQ\7+\2\2Q\16\3")
        buf.write("\2\2\2RS\7.\2\2S\20\3\2\2\2TU\7<\2\2U\22\3\2\2\2VW\7}")
        buf.write("\2\2W\24\3\2\2\2XY\7\177\2\2Y\26\3\2\2\2Z^\t\2\2\2[]\t")
        buf.write("\3\2\2\\[\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\30\3")
        buf.write("\2\2\2`^\3\2\2\2ac\t\4\2\2ba\3\2\2\2cd\3\2\2\2db\3\2\2")
        buf.write("\2de\3\2\2\2e\32\3\2\2\2fg\7=\2\2g\34\3\2\2\2hj\t\5\2")
        buf.write("\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2lm\3\2\2\2m")
        buf.write("n\b\17\2\2n\36\3\2\2\2\6\2^dk\3\b\2\2")
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
    T__7 = 8
    T__8 = 9
    T__9 = 10
    ID = 11
    DIGIT = 12
    DELIMITER = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\begin{tikzpicture}'", "'\\end{tikzpicture}'", "'\\node'", 
            "'at'", "'('", "')'", "','", "':'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "DIGIT", "DELIMITER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "ID", "DIGIT", "DELIMITER", "WS" ]

    grammarFileName = "Tikz.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


