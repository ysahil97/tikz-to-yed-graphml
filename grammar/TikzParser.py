# Generated from grammar/Tikz.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("\u00a9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\5\2\'\n\2\3\2\7\2*\n\2\f\2\16\2-\13\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\67\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5C\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7O\n\7\3\b\3\b\3\b\3\b\3\b\5\bV\n\b\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\5\n_\n\n\3\13\3\13\3\13\5\13d\n")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\5\13k\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\5\rw\n\r\3\r\3\r\5\r{\n\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\5\16\u0082\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u0089\n\17\3\20\6\20\u008c\n\20\r\20\16")
        buf.write("\20\u008d\3\20\3\20\6\20\u0092\n\20\r\20\16\20\u0093\3")
        buf.write("\20\6\20\u0097\n\20\r\20\16\20\u0098\5\20\u009b\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\5\22\u00a5\n\22")
        buf.write("\3\22\3\22\3\22\2\2\23\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"\2\3\3\2\20\21\2\u00ab\2$\3\2\2\2\4\66\3\2\2")
        buf.write("\2\68\3\2\2\2\bB\3\2\2\2\nD\3\2\2\2\fN\3\2\2\2\16U\3\2")
        buf.write("\2\2\20W\3\2\2\2\22^\3\2\2\2\24c\3\2\2\2\26l\3\2\2\2\30")
        buf.write("z\3\2\2\2\32\u0081\3\2\2\2\34\u0088\3\2\2\2\36\u009a\3")
        buf.write("\2\2\2 \u009c\3\2\2\2\"\u00a2\3\2\2\2$&\7\7\2\2%\'\5\4")
        buf.write("\3\2&%\3\2\2\2&\'\3\2\2\2\'+\3\2\2\2(*\5\b\5\2)(\3\2\2")
        buf.write("\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2\2.")
        buf.write("/\7\b\2\2/\60\7\2\2\3\60\3\3\2\2\2\61\62\7\3\2\2\62\63")
        buf.write("\5\6\4\2\63\64\7\4\2\2\64\67\3\2\2\2\65\67\3\2\2\2\66")
        buf.write("\61\3\2\2\2\66\65\3\2\2\2\67\5\3\2\2\289\13\2\2\29\7\3")
        buf.write("\2\2\2:;\5\26\f\2;<\5\b\5\2<C\3\2\2\2=>\5\n\6\2>?\5\b")
        buf.write("\5\2?C\3\2\2\2@C\5\n\6\2AC\5\26\f\2B:\3\2\2\2B=\3\2\2")
        buf.write("\2B@\3\2\2\2BA\3\2\2\2C\t\3\2\2\2DE\7\n\2\2EF\5\f\7\2")
        buf.write("FG\5\22\n\2GH\7\22\2\2H\13\3\2\2\2IJ\7\3\2\2JK\5\16\b")
        buf.write("\2KL\7\4\2\2LO\3\2\2\2MO\3\2\2\2NI\3\2\2\2NM\3\2\2\2O")
        buf.write("\r\3\2\2\2PQ\5\20\t\2QR\7\20\2\2RS\5\16\b\2SV\3\2\2\2")
        buf.write("TV\5\20\t\2UP\3\2\2\2UT\3\2\2\2V\17\3\2\2\2WX\7\25\2\2")
        buf.write("X\21\3\2\2\2YZ\5\24\13\2Z[\7\5\2\2[\\\5\22\n\2\\_\3\2")
        buf.write("\2\2]_\5\24\13\2^Y\3\2\2\2^]\3\2\2\2_\23\3\2\2\2`a\7\f")
        buf.write("\2\2ab\7\24\2\2bd\7\r\2\2c`\3\2\2\2cd\3\2\2\2dj\3\2\2")
        buf.write("\2ef\7\f\2\2fg\7\23\2\2gh\t\2\2\2hi\7\23\2\2ik\7\r\2\2")
        buf.write("je\3\2\2\2jk\3\2\2\2k\25\3\2\2\2lm\7\t\2\2mn\5\30\r\2")
        buf.write("no\5\32\16\2op\7\13\2\2pq\5 \21\2qr\5\"\22\2rs\7\22\2")
        buf.write("\2s\27\3\2\2\2tv\7\f\2\2uw\7\24\2\2vu\3\2\2\2vw\3\2\2")
        buf.write("\2wx\3\2\2\2x{\7\r\2\2y{\3\2\2\2zt\3\2\2\2zy\3\2\2\2{")
        buf.write("\31\3\2\2\2|}\7\3\2\2}~\5\34\17\2~\177\7\4\2\2\177\u0082")
        buf.write("\3\2\2\2\u0080\u0082\3\2\2\2\u0081|\3\2\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\33\3\2\2\2\u0083\u0084\5\36\20\2\u0084")
        buf.write("\u0085\7\20\2\2\u0085\u0086\5\34\17\2\u0086\u0089\3\2")
        buf.write("\2\2\u0087\u0089\5\36\20\2\u0088\u0083\3\2\2\2\u0088\u0087")
        buf.write("\3\2\2\2\u0089\35\3\2\2\2\u008a\u008c\7\24\2\2\u008b\u008a")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\7\6\2\2")
        buf.write("\u0090\u0092\7\24\2\2\u0091\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u009b\3\2\2\2\u0095\u0097\7\24\2\2\u0096\u0095\3\2\2")
        buf.write("\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u008b\3\2\2\2\u009a")
        buf.write("\u0096\3\2\2\2\u009b\37\3\2\2\2\u009c\u009d\7\f\2\2\u009d")
        buf.write("\u009e\7\23\2\2\u009e\u009f\t\2\2\2\u009f\u00a0\7\23\2")
        buf.write("\2\u00a0\u00a1\7\r\2\2\u00a1!\3\2\2\2\u00a2\u00a4\7\16")
        buf.write("\2\2\u00a3\u00a5\7\24\2\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\7\17\2\2\u00a7")
        buf.write("#\3\2\2\2\24&+\66BNU^cjvz\u0081\u0088\u008d\u0093\u0098")
        buf.write("\u009a\u00a4")
        return buf.getvalue()


class TikzParser ( Parser ):

    grammarFileName = "Tikz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'--'", "'='", "'\\begin{tikzpicture}'", 
                     "'\\end{tikzpicture}'", "'\\node'", "'\\draw'", "'at'", 
                     "'('", "')'", "'{'", "'}'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BEGINTIKZPICTURE", "ENDTIKZPICTURE", 
                      "NODE", "DRAW", "AT", "OPEN_PARANTHESES", "CLOSE_PARANTHESES", 
                      "OPEN_CURLY_BRACKETS", "CLOSE_CURLY_BRACKETS", "COMMA", 
                      "COLON", "SEMICOLON", "DIGIT", "VARIABLE", "LINE_SHAPE", 
                      "COMMENT", "WS" ]

    RULE_begin = 0
    RULE_globalProperties = 1
    RULE_globalProperty = 2
    RULE_instructions = 3
    RULE_draw = 4
    RULE_edgeProperties = 5
    RULE_eProperties = 6
    RULE_singleProperty = 7
    RULE_nodeList = 8
    RULE_edgeNode = 9
    RULE_node = 10
    RULE_nodeId = 11
    RULE_nodeProperties = 12
    RULE_properties = 13
    RULE_individualProperty = 14
    RULE_coordinates = 15
    RULE_label = 16

    ruleNames =  [ "begin", "globalProperties", "globalProperty", "instructions", 
                   "draw", "edgeProperties", "eProperties", "singleProperty", 
                   "nodeList", "edgeNode", "node", "nodeId", "nodeProperties", 
                   "properties", "individualProperty", "coordinates", "label" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    BEGINTIKZPICTURE=5
    ENDTIKZPICTURE=6
    NODE=7
    DRAW=8
    AT=9
    OPEN_PARANTHESES=10
    CLOSE_PARANTHESES=11
    OPEN_CURLY_BRACKETS=12
    CLOSE_CURLY_BRACKETS=13
    COMMA=14
    COLON=15
    SEMICOLON=16
    DIGIT=17
    VARIABLE=18
    LINE_SHAPE=19
    COMMENT=20
    WS=21

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

        def ENDTIKZPICTURE(self):
            return self.getToken(TikzParser.ENDTIKZPICTURE, 0)

        def EOF(self):
            return self.getToken(TikzParser.EOF, 0)

        def globalProperties(self):
            return self.getTypedRuleContext(TikzParser.GlobalPropertiesContext,0)


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
            self.state = 34
            self.match(TikzParser.BEGINTIKZPICTURE)
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 35
                self.globalProperties()


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TikzParser.NODE or _la==TikzParser.DRAW:
                self.state = 38
                self.instructions()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(TikzParser.ENDTIKZPICTURE)
            self.state = 45
            self.match(TikzParser.EOF)
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

        def globalProperty(self):
            return self.getTypedRuleContext(TikzParser.GlobalPropertyContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_globalProperties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalProperties" ):
                listener.enterGlobalProperties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalProperties" ):
                listener.exitGlobalProperties(self)




    def globalProperties(self):

        localctx = TikzParser.GlobalPropertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_globalProperties)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(TikzParser.T__0)
                self.state = 48
                self.globalProperty()
                self.state = 49
                self.match(TikzParser.T__1)
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


    class GlobalPropertyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TikzParser.RULE_globalProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalProperty" ):
                listener.enterGlobalProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalProperty" ):
                listener.exitGlobalProperty(self)




    def globalProperty(self):

        localctx = TikzParser.GlobalPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_globalProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.matchWildcard()
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
        self.enterRule(localctx, 6, self.RULE_instructions)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.node()
                self.state = 57
                self.instructions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.draw()
                self.state = 60
                self.instructions()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.draw()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
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
        self.enterRule(localctx, 8, self.RULE_draw)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(TikzParser.DRAW)
            self.state = 67
            self.edgeProperties()
            self.state = 68
            self.nodeList()
            self.state = 69
            self.match(TikzParser.SEMICOLON)
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

        def eProperties(self):
            return self.getTypedRuleContext(TikzParser.EPropertiesContext,0)


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
        self.enterRule(localctx, 10, self.RULE_edgeProperties)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(TikzParser.T__0)
                self.state = 72
                self.eProperties()
                self.state = 73
                self.match(TikzParser.T__1)
                pass
            elif token in [TikzParser.T__2, TikzParser.OPEN_PARANTHESES, TikzParser.SEMICOLON]:
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


    class EPropertiesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleProperty(self):
            return self.getTypedRuleContext(TikzParser.SinglePropertyContext,0)


        def COMMA(self):
            return self.getToken(TikzParser.COMMA, 0)

        def eProperties(self):
            return self.getTypedRuleContext(TikzParser.EPropertiesContext,0)


        def getRuleIndex(self):
            return TikzParser.RULE_eProperties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEProperties" ):
                listener.enterEProperties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEProperties" ):
                listener.exitEProperties(self)




    def eProperties(self):

        localctx = TikzParser.EPropertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_eProperties)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.singleProperty()
                self.state = 79
                self.match(TikzParser.COMMA)
                self.state = 80
                self.eProperties()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.singleProperty()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinglePropertyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_SHAPE(self):
            return self.getToken(TikzParser.LINE_SHAPE, 0)

        def getRuleIndex(self):
            return TikzParser.RULE_singleProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleProperty" ):
                listener.enterSingleProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleProperty" ):
                listener.exitSingleProperty(self)




    def singleProperty(self):

        localctx = TikzParser.SinglePropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_singleProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(TikzParser.LINE_SHAPE)
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
        self.enterRule(localctx, 16, self.RULE_nodeList)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.edgeNode()
                self.state = 88
                self.match(TikzParser.T__2)
                self.state = 89
                self.nodeList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
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

        def OPEN_PARANTHESES(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.OPEN_PARANTHESES)
            else:
                return self.getToken(TikzParser.OPEN_PARANTHESES, i)

        def VARIABLE(self):
            return self.getToken(TikzParser.VARIABLE, 0)

        def CLOSE_PARANTHESES(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.CLOSE_PARANTHESES)
            else:
                return self.getToken(TikzParser.CLOSE_PARANTHESES, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.DIGIT)
            else:
                return self.getToken(TikzParser.DIGIT, i)

        def COMMA(self):
            return self.getToken(TikzParser.COMMA, 0)

        def COLON(self):
            return self.getToken(TikzParser.COLON, 0)

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
        self.enterRule(localctx, 18, self.RULE_edgeNode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 94
                self.match(TikzParser.OPEN_PARANTHESES)
                self.state = 95
                self.match(TikzParser.VARIABLE)
                self.state = 96
                self.match(TikzParser.CLOSE_PARANTHESES)


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TikzParser.OPEN_PARANTHESES:
                self.state = 99
                self.match(TikzParser.OPEN_PARANTHESES)
                self.state = 100
                self.match(TikzParser.DIGIT)
                self.state = 101
                _la = self._input.LA(1)
                if not(_la==TikzParser.COMMA or _la==TikzParser.COLON):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 102
                self.match(TikzParser.DIGIT)
                self.state = 103
                self.match(TikzParser.CLOSE_PARANTHESES)


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

        def nodeId(self):
            return self.getTypedRuleContext(TikzParser.NodeIdContext,0)


        def nodeProperties(self):
            return self.getTypedRuleContext(TikzParser.NodePropertiesContext,0)


        def AT(self):
            return self.getToken(TikzParser.AT, 0)

        def coordinates(self):
            return self.getTypedRuleContext(TikzParser.CoordinatesContext,0)


        def label(self):
            return self.getTypedRuleContext(TikzParser.LabelContext,0)


        def SEMICOLON(self):
            return self.getToken(TikzParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 20, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(TikzParser.NODE)
            self.state = 107
            self.nodeId()
            self.state = 108
            self.nodeProperties()
            self.state = 109
            self.match(TikzParser.AT)
            self.state = 110
            self.coordinates()
            self.state = 111
            self.label()
            self.state = 112
            self.match(TikzParser.SEMICOLON)
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
        self.enterRule(localctx, 22, self.RULE_nodeId)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.OPEN_PARANTHESES]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(TikzParser.OPEN_PARANTHESES)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TikzParser.VARIABLE:
                    self.state = 115
                    self.match(TikzParser.VARIABLE)


                self.state = 118
                self.match(TikzParser.CLOSE_PARANTHESES)
                pass
            elif token in [TikzParser.T__0, TikzParser.AT]:
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
        self.enterRule(localctx, 24, self.RULE_nodeProperties)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(TikzParser.T__0)
                self.state = 123
                self.properties()
                self.state = 124
                self.match(TikzParser.T__1)
                pass
            elif token in [TikzParser.AT]:
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
        self.enterRule(localctx, 26, self.RULE_properties)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.individualProperty()
                self.state = 130
                self.match(TikzParser.COMMA)
                self.state = 131
                self.properties()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
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

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.VARIABLE)
            else:
                return self.getToken(TikzParser.VARIABLE, i)

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
        self.enterRule(localctx, 28, self.RULE_individualProperty)
        self._la = 0 # Token type
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 136
                    self.match(TikzParser.VARIABLE)
                    self.state = 139 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==TikzParser.VARIABLE):
                        break

                self.state = 141
                self.match(TikzParser.T__3)
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 142
                    self.match(TikzParser.VARIABLE)
                    self.state = 145 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==TikzParser.VARIABLE):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 147
                    self.match(TikzParser.VARIABLE)
                    self.state = 150 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==TikzParser.VARIABLE):
                        break

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

        def OPEN_PARANTHESES(self):
            return self.getToken(TikzParser.OPEN_PARANTHESES, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.DIGIT)
            else:
                return self.getToken(TikzParser.DIGIT, i)

        def CLOSE_PARANTHESES(self):
            return self.getToken(TikzParser.CLOSE_PARANTHESES, 0)

        def COMMA(self):
            return self.getToken(TikzParser.COMMA, 0)

        def COLON(self):
            return self.getToken(TikzParser.COLON, 0)

        def getRuleIndex(self):
            return TikzParser.RULE_coordinates

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordinates" ):
                listener.enterCoordinates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordinates" ):
                listener.exitCoordinates(self)




    def coordinates(self):

        localctx = TikzParser.CoordinatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_coordinates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(TikzParser.OPEN_PARANTHESES)
            self.state = 155
            self.match(TikzParser.DIGIT)
            self.state = 156
            _la = self._input.LA(1)
            if not(_la==TikzParser.COMMA or _la==TikzParser.COLON):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 157
            self.match(TikzParser.DIGIT)
            self.state = 158
            self.match(TikzParser.CLOSE_PARANTHESES)
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

        def OPEN_CURLY_BRACKETS(self):
            return self.getToken(TikzParser.OPEN_CURLY_BRACKETS, 0)

        def CLOSE_CURLY_BRACKETS(self):
            return self.getToken(TikzParser.CLOSE_CURLY_BRACKETS, 0)

        def VARIABLE(self):
            return self.getToken(TikzParser.VARIABLE, 0)

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
        self.enterRule(localctx, 32, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(TikzParser.OPEN_CURLY_BRACKETS)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TikzParser.VARIABLE:
                self.state = 161
                self.match(TikzParser.VARIABLE)


            self.state = 164
            self.match(TikzParser.CLOSE_CURLY_BRACKETS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





