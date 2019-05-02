# Generated from tikz2graphml/grammar/Tikz.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("\u00ca\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\7\2&\n")
        buf.write("\2\f\2\16\2)\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\66\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4R\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6]\n\6\3\7\3\7\3\7\3\7\5\7c\n\7\3\b\3\b\5\b")
        buf.write("g\n\b\3\b\3\b\5\bk\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\5\nx\n\n\3\n\3\n\5\n|\n\n\3\13\3\13\5\13")
        buf.write("\u0080\n\13\3\13\3\13\5\13\u0084\n\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0091\n\f\3\f\3\f\3\f")
        buf.write("\7\f\u0096\n\f\f\f\16\f\u0099\13\f\3\r\3\r\5\r\u009d\n")
        buf.write("\r\3\r\3\r\5\r\u00a1\n\r\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00a8\n\16\3\17\6\17\u00ab\n\17\r\17\16\17\u00ac\3\17")
        buf.write("\3\17\6\17\u00b1\n\17\r\17\16\17\u00b2\3\17\6\17\u00b6")
        buf.write("\n\17\r\17\16\17\u00b7\5\17\u00ba\n\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00c6\n\20\3")
        buf.write("\21\3\21\3\21\2\3\26\22\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \2\4\3\2\31\32\4\2\17\17\24\24\2\u00d2\2\"\3")
        buf.write("\2\2\2\4\65\3\2\2\2\6Q\3\2\2\2\bS\3\2\2\2\n\\\3\2\2\2")
        buf.write("\fb\3\2\2\2\16j\3\2\2\2\20l\3\2\2\2\22{\3\2\2\2\24\u0083")
        buf.write("\3\2\2\2\26\u0090\3\2\2\2\30\u00a0\3\2\2\2\32\u00a7\3")
        buf.write("\2\2\2\34\u00b9\3\2\2\2\36\u00c5\3\2\2\2 \u00c7\3\2\2")
        buf.write("\2\"#\7\n\2\2#\'\5\24\13\2$&\5\4\3\2%$\3\2\2\2&)\3\2\2")
        buf.write("\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2\2\2*+\7\13\2")
        buf.write("\2+,\7\2\2\3,\3\3\2\2\2-.\5\20\t\2./\5\4\3\2/\66\3\2\2")
        buf.write("\2\60\61\5\6\4\2\61\62\5\4\3\2\62\66\3\2\2\2\63\66\5\6")
        buf.write("\4\2\64\66\5\20\t\2\65-\3\2\2\2\65\60\3\2\2\2\65\63\3")
        buf.write("\2\2\2\65\64\3\2\2\2\66\5\3\2\2\2\678\7\r\2\289\5\16\b")
        buf.write("\29:\5\n\6\2:;\7\26\2\2;R\3\2\2\2<=\7\r\2\2=>\5\16\b\2")
        buf.write(">?\5\36\20\2?@\t\2\2\2@A\5\36\20\2AB\7\26\2\2BR\3\2\2")
        buf.write("\2CD\7\r\2\2DE\5\16\b\2EF\5\36\20\2FG\t\2\2\2GH\5\b\5")
        buf.write("\2HI\7\26\2\2IR\3\2\2\2JK\7\r\2\2KL\5\16\b\2LM\5\36\20")
        buf.write("\2MN\t\2\2\2NO\5\30\r\2OP\5 \21\2PR\3\2\2\2Q\67\3\2\2")
        buf.write("\2Q<\3\2\2\2QC\3\2\2\2QJ\3\2\2\2R\7\3\2\2\2ST\7\21\2\2")
        buf.write("TU\t\2\2\2UV\7\22\2\2V\t\3\2\2\2WX\5\f\7\2XY\7\3\2\2Y")
        buf.write("Z\5\n\6\2Z]\3\2\2\2[]\5\f\7\2\\W\3\2\2\2\\[\3\2\2\2]\13")
        buf.write("\3\2\2\2^c\5\36\20\2_`\7\21\2\2`a\t\2\2\2ac\7\22\2\2b")
        buf.write("^\3\2\2\2b_\3\2\2\2c\r\3\2\2\2df\7\4\2\2eg\5\32\16\2f")
        buf.write("e\3\2\2\2fg\3\2\2\2gh\3\2\2\2hk\7\5\2\2ik\3\2\2\2jd\3")
        buf.write("\2\2\2ji\3\2\2\2k\17\3\2\2\2lm\7\f\2\2mn\5\30\r\2no\5")
        buf.write("\22\n\2op\5\30\r\2pq\7\16\2\2qr\5\36\20\2rs\5\30\r\2s")
        buf.write("t\5 \21\2t\21\3\2\2\2uw\7\21\2\2vx\t\2\2\2wv\3\2\2\2w")
        buf.write("x\3\2\2\2xy\3\2\2\2y|\7\22\2\2z|\3\2\2\2{u\3\2\2\2{z\3")
        buf.write("\2\2\2|\23\3\2\2\2}\177\7\4\2\2~\u0080\5\26\f\2\177~\3")
        buf.write("\2\2\2\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0084")
        buf.write("\7\5\2\2\u0082\u0084\3\2\2\2\u0083}\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\25\3\2\2\2\u0085\u0086\b\f\1\2\u0086\u0087")
        buf.write("\7\20\2\2\u0087\u0088\t\2\2\2\u0088\u0089\7\6\2\2\u0089")
        buf.write("\u008a\7\7\2\2\u008a\u008b\7\23\2\2\u008b\u008c\7\b\2")
        buf.write("\2\u008c\u008d\5\32\16\2\u008d\u008e\7\t\2\2\u008e\u0091")
        buf.write("\3\2\2\2\u008f\u0091\5\32\16\2\u0090\u0085\3\2\2\2\u0090")
        buf.write("\u008f\3\2\2\2\u0091\u0097\3\2\2\2\u0092\u0093\f\5\2\2")
        buf.write("\u0093\u0094\7\24\2\2\u0094\u0096\5\26\f\6\u0095\u0092")
        buf.write("\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\27\3\2\2\2\u0099\u0097\3\2\2\2\u009a")
        buf.write("\u009c\7\4\2\2\u009b\u009d\5\32\16\2\u009c\u009b\3\2\2")
        buf.write("\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a1")
        buf.write("\7\5\2\2\u009f\u00a1\3\2\2\2\u00a0\u009a\3\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\31\3\2\2\2\u00a2\u00a3\5\34\17\2")
        buf.write("\u00a3\u00a4\7\24\2\2\u00a4\u00a5\5\32\16\2\u00a5\u00a8")
        buf.write("\3\2\2\2\u00a6\u00a8\5\34\17\2\u00a7\u00a2\3\2\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\33\3\2\2\2\u00a9\u00ab\t\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\7")
        buf.write("\23\2\2\u00af\u00b1\t\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00ba\3\2\2\2\u00b4\u00b6\t\2\2\2\u00b5\u00b4\3")
        buf.write("\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00aa\3\2\2\2\u00b9")
        buf.write("\u00b5\3\2\2\2\u00ba\35\3\2\2\2\u00bb\u00bc\7\21\2\2\u00bc")
        buf.write("\u00bd\t\2\2\2\u00bd\u00be\t\3\2\2\u00be\u00bf\t\2\2\2")
        buf.write("\u00bf\u00c6\7\22\2\2\u00c0\u00c1\7\21\2\2\u00c1\u00c2")
        buf.write("\t\2\2\2\u00c2\u00c3\7\25\2\2\u00c3\u00c4\t\2\2\2\u00c4")
        buf.write("\u00c6\7\22\2\2\u00c5\u00bb\3\2\2\2\u00c5\u00c0\3\2\2")
        buf.write("\2\u00c6\37\3\2\2\2\u00c7\u00c8\7\30\2\2\u00c8!\3\2\2")
        buf.write("\2\27\'\65Q\\bfjw{\177\u0083\u0090\u0097\u009c\u00a0\u00a7")
        buf.write("\u00ac\u00b2\u00b7\u00b9\u00c5")
        return buf.getvalue()


class TikzParser ( Parser ):

    grammarFileName = "Tikz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'--'", "'['", "']'", "'/.'", "'style'", 
                     "'{'", "'}'", "'\\begin{tikzpicture}'", "'\\end{tikzpicture}'", 
                     "'\\node'", "'\\draw'", "'at'", "'and'", "'every'", 
                     "'('", "')'", "'='", "','", "':'", "';'", "'\\pause'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BEGINTIKZPICTURE", "ENDTIKZPICTURE", "NODE", "DRAW", 
                      "AT", "AND", "EVERY", "OPEN_PARANTHESES", "CLOSE_PARANTHESES", 
                      "EQUAL_TO", "COMMA", "COLON", "SEMICOLON", "PAUSE", 
                      "LABEL_VARIABLE", "EXPRESSION", "VARIABLE", "COMMENT", 
                      "WS" ]

    RULE_begin = 0
    RULE_instructions = 1
    RULE_draw = 2
    RULE_radius = 3
    RULE_nodeList = 4
    RULE_edgeNode = 5
    RULE_edgeProperties = 6
    RULE_node = 7
    RULE_nodeId = 8
    RULE_allGlobalProperties = 9
    RULE_globalProperties = 10
    RULE_nodeProperties = 11
    RULE_properties = 12
    RULE_individualProperty = 13
    RULE_coordinates = 14
    RULE_label = 15

    ruleNames =  [ "begin", "instructions", "draw", "radius", "nodeList", 
                   "edgeNode", "edgeProperties", "node", "nodeId", "allGlobalProperties", 
                   "globalProperties", "nodeProperties", "properties", "individualProperty", 
                   "coordinates", "label" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    BEGINTIKZPICTURE=8
    ENDTIKZPICTURE=9
    NODE=10
    DRAW=11
    AT=12
    AND=13
    EVERY=14
    OPEN_PARANTHESES=15
    CLOSE_PARANTHESES=16
    EQUAL_TO=17
    COMMA=18
    COLON=19
    SEMICOLON=20
    PAUSE=21
    LABEL_VARIABLE=22
    EXPRESSION=23
    VARIABLE=24
    COMMENT=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BeginContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGINTIKZPICTURE(self):
            return self.getToken(TikzParser.BEGINTIKZPICTURE, 0)

        def allGlobalProperties(self):
            return self.getTypedRuleContext(TikzParser.AllGlobalPropertiesContext,0)


        def ENDTIKZPICTURE(self):
            return self.getToken(TikzParser.ENDTIKZPICTURE, 0)

        def EOF(self):
            return self.getToken(TikzParser.EOF, 0)

        def instructions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TikzParser.InstructionsContext)
            else:
                return self.getTypedRuleContext(TikzParser.InstructionsContext,i)


        def getRuleIndex(self):
            return TikzParser.RULE_begin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBegin" ):
                listener.enterBegin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBegin" ):
                listener.exitBegin(self)




    def begin(self):

        localctx = TikzParser.BeginContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_begin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(TikzParser.BEGINTIKZPICTURE)
            self.state = 33
            self.allGlobalProperties()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TikzParser.NODE or _la==TikzParser.DRAW:
                self.state = 34
                self.instructions()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(TikzParser.ENDTIKZPICTURE)
            self.state = 41
            self.match(TikzParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node(self):
            return self.getTypedRuleContext(TikzParser.NodeContext,0)


        def instructions(self):
            return self.getTypedRuleContext(TikzParser.InstructionsContext,0)


        def draw(self):
            return self.getTypedRuleContext(TikzParser.DrawContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_instructions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstructions" ):
                listener.enterInstructions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstructions" ):
                listener.exitInstructions(self)




    def instructions(self):

        localctx = TikzParser.InstructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instructions)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.node()
                self.state = 44
                self.instructions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.draw()
                self.state = 47
                self.instructions()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.draw()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.node()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DrawContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DRAW(self):
            return self.getToken(TikzParser.DRAW, 0)

        def edgeProperties(self):
            return self.getTypedRuleContext(TikzParser.EdgePropertiesContext,0)


        def nodeList(self):
            return self.getTypedRuleContext(TikzParser.NodeListContext,0)


        def SEMICOLON(self):
            return self.getToken(TikzParser.SEMICOLON, 0)

        def coordinates(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TikzParser.CoordinatesContext)
            else:
                return self.getTypedRuleContext(TikzParser.CoordinatesContext,i)


        def VARIABLE(self):
            return self.getToken(TikzParser.VARIABLE, 0)

        def EXPRESSION(self):
            return self.getToken(TikzParser.EXPRESSION, 0)

        def radius(self):
            return self.getTypedRuleContext(TikzParser.RadiusContext,0)


        def nodeProperties(self):
            return self.getTypedRuleContext(TikzParser.NodePropertiesContext,0)


        def label(self):
            return self.getTypedRuleContext(TikzParser.LabelContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_draw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDraw" ):
                listener.enterDraw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDraw" ):
                listener.exitDraw(self)




    def draw(self):

        localctx = TikzParser.DrawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_draw)
        self._la = 0 # Token type
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(TikzParser.DRAW)
                self.state = 54
                self.edgeProperties()
                self.state = 55
                self.nodeList()
                self.state = 56
                self.match(TikzParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(TikzParser.DRAW)
                self.state = 59
                self.edgeProperties()
                self.state = 60
                self.coordinates()
                self.state = 61
                _la = self._input.LA(1)
                if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 62
                self.coordinates()
                self.state = 63
                self.match(TikzParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(TikzParser.DRAW)
                self.state = 66
                self.edgeProperties()
                self.state = 67
                self.coordinates()
                self.state = 68
                _la = self._input.LA(1)
                if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 69
                self.radius()
                self.state = 70
                self.match(TikzParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(TikzParser.DRAW)
                self.state = 73
                self.edgeProperties()
                self.state = 74
                self.coordinates()
                self.state = 75
                _la = self._input.LA(1)
                if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 76
                self.nodeProperties()
                self.state = 77
                self.label()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RadiusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARANTHESES(self):
            return self.getToken(TikzParser.OPEN_PARANTHESES, 0)

        def CLOSE_PARANTHESES(self):
            return self.getToken(TikzParser.CLOSE_PARANTHESES, 0)

        def VARIABLE(self):
            return self.getToken(TikzParser.VARIABLE, 0)

        def EXPRESSION(self):
            return self.getToken(TikzParser.EXPRESSION, 0)

        def getRuleIndex(self):
            return TikzParser.RULE_radius

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRadius" ):
                listener.enterRadius(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRadius" ):
                listener.exitRadius(self)




    def radius(self):

        localctx = TikzParser.RadiusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_radius)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(TikzParser.OPEN_PARANTHESES)
            self.state = 82
            _la = self._input.LA(1)
            if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 83
            self.match(TikzParser.CLOSE_PARANTHESES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edgeNode(self):
            return self.getTypedRuleContext(TikzParser.EdgeNodeContext,0)


        def nodeList(self):
            return self.getTypedRuleContext(TikzParser.NodeListContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_nodeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeList" ):
                listener.enterNodeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeList" ):
                listener.exitNodeList(self)




    def nodeList(self):

        localctx = TikzParser.NodeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nodeList)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.edgeNode()
                self.state = 86
                self.match(TikzParser.T__0)
                self.state = 87
                self.nodeList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.edgeNode()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeNodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordinates(self):
            return self.getTypedRuleContext(TikzParser.CoordinatesContext,0)


        def OPEN_PARANTHESES(self):
            return self.getToken(TikzParser.OPEN_PARANTHESES, 0)

        def CLOSE_PARANTHESES(self):
            return self.getToken(TikzParser.CLOSE_PARANTHESES, 0)

        def VARIABLE(self):
            return self.getToken(TikzParser.VARIABLE, 0)

        def EXPRESSION(self):
            return self.getToken(TikzParser.EXPRESSION, 0)

        def getRuleIndex(self):
            return TikzParser.RULE_edgeNode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdgeNode" ):
                listener.enterEdgeNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdgeNode" ):
                listener.exitEdgeNode(self)




    def edgeNode(self):

        localctx = TikzParser.EdgeNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_edgeNode)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.coordinates()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(TikzParser.OPEN_PARANTHESES)
                self.state = 94
                _la = self._input.LA(1)
                if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 95
                self.match(TikzParser.CLOSE_PARANTHESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgePropertiesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def properties(self):
            return self.getTypedRuleContext(TikzParser.PropertiesContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_edgeProperties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdgeProperties" ):
                listener.enterEdgeProperties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdgeProperties" ):
                listener.exitEdgeProperties(self)




    def edgeProperties(self):

        localctx = TikzParser.EdgePropertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_edgeProperties)
        self._la = 0 # Token type
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(TikzParser.T__1)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE:
                    self.state = 99
                    self.properties()


                self.state = 102
                self.match(TikzParser.T__2)
                pass
            elif token in [TikzParser.OPEN_PARANTHESES]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NODE(self):
            return self.getToken(TikzParser.NODE, 0)

        def nodeProperties(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TikzParser.NodePropertiesContext)
            else:
                return self.getTypedRuleContext(TikzParser.NodePropertiesContext,i)


        def nodeId(self):
            return self.getTypedRuleContext(TikzParser.NodeIdContext,0)


        def AT(self):
            return self.getToken(TikzParser.AT, 0)

        def coordinates(self):
            return self.getTypedRuleContext(TikzParser.CoordinatesContext,0)


        def label(self):
            return self.getTypedRuleContext(TikzParser.LabelContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)




    def node(self):

        localctx = TikzParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(TikzParser.NODE)
            self.state = 107
            self.nodeProperties()
            self.state = 108
            self.nodeId()
            self.state = 109
            self.nodeProperties()
            self.state = 110
            self.match(TikzParser.AT)
            self.state = 111
            self.coordinates()
            self.state = 112
            self.nodeProperties()
            self.state = 113
            self.label()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARANTHESES(self):
            return self.getToken(TikzParser.OPEN_PARANTHESES, 0)

        def CLOSE_PARANTHESES(self):
            return self.getToken(TikzParser.CLOSE_PARANTHESES, 0)

        def VARIABLE(self):
            return self.getToken(TikzParser.VARIABLE, 0)

        def EXPRESSION(self):
            return self.getToken(TikzParser.EXPRESSION, 0)

        def getRuleIndex(self):
            return TikzParser.RULE_nodeId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeId" ):
                listener.enterNodeId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeId" ):
                listener.exitNodeId(self)




    def nodeId(self):

        localctx = TikzParser.NodeIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_nodeId)
        self._la = 0 # Token type
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.OPEN_PARANTHESES]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(TikzParser.OPEN_PARANTHESES)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE:
                    self.state = 116
                    _la = self._input.LA(1)
                    if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 119
                self.match(TikzParser.CLOSE_PARANTHESES)
                pass
            elif token in [TikzParser.T__1, TikzParser.AT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AllGlobalPropertiesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalProperties(self):
            return self.getTypedRuleContext(TikzParser.GlobalPropertiesContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_allGlobalProperties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllGlobalProperties" ):
                listener.enterAllGlobalProperties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllGlobalProperties" ):
                listener.exitAllGlobalProperties(self)




    def allGlobalProperties(self):

        localctx = TikzParser.AllGlobalPropertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_allGlobalProperties)
        self._la = 0 # Token type
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(TikzParser.T__1)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TikzParser.EVERY) | (1 << TikzParser.EXPRESSION) | (1 << TikzParser.VARIABLE))) != 0):
                    self.state = 124
                    self.globalProperties(0)


                self.state = 127
                self.match(TikzParser.T__2)
                pass
            elif token in [TikzParser.ENDTIKZPICTURE, TikzParser.NODE, TikzParser.DRAW]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalPropertiesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVERY(self):
            return self.getToken(TikzParser.EVERY, 0)

        def EQUAL_TO(self):
            return self.getToken(TikzParser.EQUAL_TO, 0)

        def properties(self):
            return self.getTypedRuleContext(TikzParser.PropertiesContext,0)


        def VARIABLE(self):
            return self.getToken(TikzParser.VARIABLE, 0)

        def EXPRESSION(self):
            return self.getToken(TikzParser.EXPRESSION, 0)

        def globalProperties(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TikzParser.GlobalPropertiesContext)
            else:
                return self.getTypedRuleContext(TikzParser.GlobalPropertiesContext,i)


        def COMMA(self):
            return self.getToken(TikzParser.COMMA, 0)

        def getRuleIndex(self):
            return TikzParser.RULE_globalProperties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalProperties" ):
                listener.enterGlobalProperties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalProperties" ):
                listener.exitGlobalProperties(self)



    def globalProperties(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TikzParser.GlobalPropertiesContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_globalProperties, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.EVERY]:
                self.state = 132
                self.match(TikzParser.EVERY)
                self.state = 133
                _la = self._input.LA(1)
                if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 134
                self.match(TikzParser.T__3)
                self.state = 135
                self.match(TikzParser.T__4)
                self.state = 136
                self.match(TikzParser.EQUAL_TO)
                self.state = 137
                self.match(TikzParser.T__5)
                self.state = 138
                self.properties()
                self.state = 139
                self.match(TikzParser.T__6)
                pass
            elif token in [TikzParser.EXPRESSION, TikzParser.VARIABLE]:
                self.state = 141
                self.properties()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TikzParser.GlobalPropertiesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_globalProperties)
                    self.state = 144
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 145
                    self.match(TikzParser.COMMA)
                    self.state = 146
                    self.globalProperties(4) 
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NodePropertiesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def properties(self):
            return self.getTypedRuleContext(TikzParser.PropertiesContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_nodeProperties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeProperties" ):
                listener.enterNodeProperties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeProperties" ):
                listener.exitNodeProperties(self)




    def nodeProperties(self):

        localctx = TikzParser.NodePropertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_nodeProperties)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(TikzParser.T__1)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE:
                    self.state = 153
                    self.properties()


                self.state = 156
                self.match(TikzParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertiesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def individualProperty(self):
            return self.getTypedRuleContext(TikzParser.IndividualPropertyContext,0)


        def COMMA(self):
            return self.getToken(TikzParser.COMMA, 0)

        def properties(self):
            return self.getTypedRuleContext(TikzParser.PropertiesContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_properties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProperties" ):
                listener.enterProperties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProperties" ):
                listener.exitProperties(self)




    def properties(self):

        localctx = TikzParser.PropertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_properties)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.individualProperty()
                self.state = 161
                self.match(TikzParser.COMMA)
                self.state = 162
                self.properties()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.individualProperty()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndividualPropertyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_TO(self):
            return self.getToken(TikzParser.EQUAL_TO, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.VARIABLE)
            else:
                return self.getToken(TikzParser.VARIABLE, i)

        def EXPRESSION(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.EXPRESSION)
            else:
                return self.getToken(TikzParser.EXPRESSION, i)

        def getRuleIndex(self):
            return TikzParser.RULE_individualProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndividualProperty" ):
                listener.enterIndividualProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndividualProperty" ):
                listener.exitIndividualProperty(self)




    def individualProperty(self):

        localctx = TikzParser.IndividualPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_individualProperty)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 167
                    _la = self._input.LA(1)
                    if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 170 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                        break

                self.state = 172
                self.match(TikzParser.EQUAL_TO)
                self.state = 174 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 173
                        _la = self._input.LA(1)
                        if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 176 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 178
                        _la = self._input.LA(1)
                        if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 181 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordinatesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TikzParser.RULE_coordinates

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CartesianCoordinatesContext(CoordinatesContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TikzParser.CoordinatesContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_PARANTHESES(self):
            return self.getToken(TikzParser.OPEN_PARANTHESES, 0)
        def CLOSE_PARANTHESES(self):
            return self.getToken(TikzParser.CLOSE_PARANTHESES, 0)
        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.VARIABLE)
            else:
                return self.getToken(TikzParser.VARIABLE, i)
        def EXPRESSION(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.EXPRESSION)
            else:
                return self.getToken(TikzParser.EXPRESSION, i)
        def COMMA(self):
            return self.getToken(TikzParser.COMMA, 0)
        def AND(self):
            return self.getToken(TikzParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCartesianCoordinates" ):
                listener.enterCartesianCoordinates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCartesianCoordinates" ):
                listener.exitCartesianCoordinates(self)


    class PolarCoordinatesContext(CoordinatesContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TikzParser.CoordinatesContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_PARANTHESES(self):
            return self.getToken(TikzParser.OPEN_PARANTHESES, 0)
        def COLON(self):
            return self.getToken(TikzParser.COLON, 0)
        def CLOSE_PARANTHESES(self):
            return self.getToken(TikzParser.CLOSE_PARANTHESES, 0)
        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.VARIABLE)
            else:
                return self.getToken(TikzParser.VARIABLE, i)
        def EXPRESSION(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.EXPRESSION)
            else:
                return self.getToken(TikzParser.EXPRESSION, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolarCoordinates" ):
                listener.enterPolarCoordinates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolarCoordinates" ):
                listener.exitPolarCoordinates(self)



    def coordinates(self):

        localctx = TikzParser.CoordinatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_coordinates)
        self._la = 0 # Token type
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = TikzParser.CartesianCoordinatesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(TikzParser.OPEN_PARANTHESES)
                self.state = 186
                _la = self._input.LA(1)
                if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 187
                _la = self._input.LA(1)
                if not(_la==TikzParser.AND or _la==TikzParser.COMMA):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 188
                _la = self._input.LA(1)
                if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                self.match(TikzParser.CLOSE_PARANTHESES)
                pass

            elif la_ == 2:
                localctx = TikzParser.PolarCoordinatesContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(TikzParser.OPEN_PARANTHESES)
                self.state = 191
                _la = self._input.LA(1)
                if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self.match(TikzParser.COLON)
                self.state = 193
                _la = self._input.LA(1)
                if not(_la==TikzParser.EXPRESSION or _la==TikzParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 194
                self.match(TikzParser.CLOSE_PARANTHESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL_VARIABLE(self):
            return self.getToken(TikzParser.LABEL_VARIABLE, 0)

        def getRuleIndex(self):
            return TikzParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = TikzParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(TikzParser.LABEL_VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.globalProperties_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def globalProperties_sempred(self, localctx:GlobalPropertiesContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




