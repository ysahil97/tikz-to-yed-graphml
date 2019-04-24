# Generated from grammar/Tikz.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("U\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\7\2\27\n\2\f\2\16\2\32\13")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5/\n\5\3\5\3\5\5\5\63\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6:\n\6\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("A\n\7\3\b\3\b\3\b\3\b\5\bG\n\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\5\nQ\n\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20")
        buf.write("\22\2\3\3\2\16\17\2S\2\24\3\2\2\2\4\"\3\2\2\2\6$\3\2\2")
        buf.write("\2\b\62\3\2\2\2\n9\3\2\2\2\f@\3\2\2\2\16F\3\2\2\2\20H")
        buf.write("\3\2\2\2\22N\3\2\2\2\24\30\7\6\2\2\25\27\5\4\3\2\26\25")
        buf.write("\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\33\3\2\2\2\32\30\3\2\2\2\33\34\7\7\2\2\34\35\7\2\2\3")
        buf.write("\35\3\3\2\2\2\36\37\5\6\4\2\37 \5\4\3\2 #\3\2\2\2!#\5")
        buf.write("\6\4\2\"\36\3\2\2\2\"!\3\2\2\2#\5\3\2\2\2$%\7\b\2\2%&")
        buf.write("\5\b\5\2&\'\5\n\6\2\'(\7\t\2\2()\5\20\t\2)*\5\22\n\2*")
        buf.write("+\7\20\2\2+\7\3\2\2\2,.\7\n\2\2-/\7\22\2\2.-\3\2\2\2.")
        buf.write("/\3\2\2\2/\60\3\2\2\2\60\63\7\13\2\2\61\63\3\2\2\2\62")
        buf.write(",\3\2\2\2\62\61\3\2\2\2\63\t\3\2\2\2\64\65\7\3\2\2\65")
        buf.write("\66\5\f\7\2\66\67\7\4\2\2\67:\3\2\2\28:\3\2\2\29\64\3")
        buf.write("\2\2\298\3\2\2\2:\13\3\2\2\2;<\5\16\b\2<=\7\16\2\2=>\5")
        buf.write("\f\7\2>A\3\2\2\2?A\5\16\b\2@;\3\2\2\2@?\3\2\2\2A\r\3\2")
        buf.write("\2\2BC\7\22\2\2CD\7\5\2\2DG\7\22\2\2EG\7\22\2\2FB\3\2")
        buf.write("\2\2FE\3\2\2\2G\17\3\2\2\2HI\7\n\2\2IJ\7\21\2\2JK\t\2")
        buf.write("\2\2KL\7\21\2\2LM\7\13\2\2M\21\3\2\2\2NP\7\f\2\2OQ\7\22")
        buf.write("\2\2PO\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\7\r\2\2S\23\3\2\2")
        buf.write("\2\n\30\".\629@FP")
        return buf.getvalue()


class TikzParser ( Parser ):

    grammarFileName = "Tikz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'='", "'\\begin{tikzpicture}'", 
                     "'\\end{tikzpicture}'", "'\\node'", "'at'", "'('", 
                     "')'", "'{'", "'}'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BEGINTIKZPICTURE", "ENDTIKZPICTURE", "NODE", "AT", 
                      "OPEN_PARANTHESES", "CLOSE_PARANTHESES", "OPEN_CURLY_BRACKETS", 
                      "CLOSE_CURLY_BRACKETS", "COMMA", "COLON", "SEMICOLON", 
                      "DIGIT", "VARIABLE", "COMMENT", "WS" ]

    RULE_begin = 0
    RULE_instructions = 1
    RULE_node = 2
    RULE_nodeId = 3
    RULE_nodeProperties = 4
    RULE_properties = 5
    RULE_individualProperty = 6
    RULE_coordinates = 7
    RULE_label = 8

    ruleNames =  [ "begin", "instructions", "node", "nodeId", "nodeProperties", 
                   "properties", "individualProperty", "coordinates", "label" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    BEGINTIKZPICTURE=4
    ENDTIKZPICTURE=5
    NODE=6
    AT=7
    OPEN_PARANTHESES=8
    CLOSE_PARANTHESES=9
    OPEN_CURLY_BRACKETS=10
    CLOSE_CURLY_BRACKETS=11
    COMMA=12
    COLON=13
    SEMICOLON=14
    DIGIT=15
    VARIABLE=16
    COMMENT=17
    WS=18

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
            self.state = 18
            self.match(TikzParser.BEGINTIKZPICTURE)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TikzParser.NODE:
                self.state = 19
                self.instructions()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.match(TikzParser.ENDTIKZPICTURE)
            self.state = 26
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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.node()
                self.state = 29
                self.instructions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.node()
                pass


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
        self.enterRule(localctx, 4, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(TikzParser.NODE)
            self.state = 35
            self.nodeId()
            self.state = 36
            self.nodeProperties()
            self.state = 37
            self.match(TikzParser.AT)
            self.state = 38
            self.coordinates()
            self.state = 39
            self.label()
            self.state = 40
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
        self.enterRule(localctx, 6, self.RULE_nodeId)
        self._la = 0 # Token type
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.OPEN_PARANTHESES]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(TikzParser.OPEN_PARANTHESES)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TikzParser.VARIABLE:
                    self.state = 43
                    self.match(TikzParser.VARIABLE)


                self.state = 46
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
        self.enterRule(localctx, 8, self.RULE_nodeProperties)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TikzParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(TikzParser.T__0)
                self.state = 51
                self.properties()
                self.state = 52
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
        self.enterRule(localctx, 10, self.RULE_properties)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.individualProperty()
                self.state = 58
                self.match(TikzParser.COMMA)
                self.state = 59
                self.properties()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
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
        self.enterRule(localctx, 12, self.RULE_individualProperty)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(TikzParser.VARIABLE)
                self.state = 65
                self.match(TikzParser.T__2)
                self.state = 66
                self.match(TikzParser.VARIABLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(TikzParser.VARIABLE)
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
        self.enterRule(localctx, 14, self.RULE_coordinates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(TikzParser.OPEN_PARANTHESES)
            self.state = 71
            self.match(TikzParser.DIGIT)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==TikzParser.COMMA or _la==TikzParser.COLON):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 73
            self.match(TikzParser.DIGIT)
            self.state = 74
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
        self.enterRule(localctx, 16, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(TikzParser.OPEN_CURLY_BRACKETS)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TikzParser.VARIABLE:
                self.state = 77
                self.match(TikzParser.VARIABLE)


            self.state = 80
            self.match(TikzParser.CLOSE_CURLY_BRACKETS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





