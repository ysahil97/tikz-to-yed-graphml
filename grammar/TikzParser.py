# Generated from Tikz.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\63\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2\65\2\16")
        buf.write("\3\2\2\2\4\33\3\2\2\2\6\35\3\2\2\2\b$\3\2\2\2\n\62\3\2")
        buf.write("\2\2\f\64\3\2\2\2\16\22\7\3\2\2\17\21\5\4\3\2\20\17\3")
        buf.write("\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\25")
        buf.write("\3\2\2\2\24\22\3\2\2\2\25\26\7\4\2\2\26\3\3\2\2\2\27\30")
        buf.write("\5\6\4\2\30\31\5\4\3\2\31\34\3\2\2\2\32\34\5\6\4\2\33")
        buf.write("\27\3\2\2\2\33\32\3\2\2\2\34\5\3\2\2\2\35\36\7\5\2\2\36")
        buf.write("\37\5\b\5\2\37 \7\6\2\2 !\5\n\6\2!\"\5\f\7\2\"#\7\17\2")
        buf.write("\2#\7\3\2\2\2$%\7\7\2\2%&\7\r\2\2&\'\7\b\2\2\'\t\3\2\2")
        buf.write("\2()\7\7\2\2)*\7\16\2\2*+\7\t\2\2+,\7\16\2\2,\63\7\b\2")
        buf.write("\2-.\7\7\2\2./\7\16\2\2/\60\7\n\2\2\60\61\7\16\2\2\61")
        buf.write("\63\7\b\2\2\62(\3\2\2\2\62-\3\2\2\2\63\13\3\2\2\2\64\65")
        buf.write("\7\13\2\2\65\66\7\r\2\2\66\67\7\f\2\2\67\r\3\2\2\2\5\22")
        buf.write("\33\62")
        return buf.getvalue()


class TikzParser ( Parser ):

    grammarFileName = "Tikz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\begin{tikzpicture}'", "'\\end{tikzpicture}'", 
                     "'\\node'", "'at'", "'('", "')'", "','", "':'", "'{'", 
                     "'}'", "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "DIGIT", 
                      "DELIMITER", "WS" ]

    RULE_begin = 0
    RULE_instructions = 1
    RULE_node = 2
    RULE_nodeID = 3
    RULE_coordinates = 4
    RULE_label = 5

    ruleNames =  [ "begin", "instructions", "node", "nodeID", "coordinates", 
                   "label" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ID=11
    DIGIT=12
    DELIMITER=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BeginContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            self.state = 12
            self.match(TikzParser.T__0)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TikzParser.T__2:
                self.state = 13
                self.instructions()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(TikzParser.T__1)
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
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.node()
                self.state = 22
                self.instructions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
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

        def nodeID(self):
            return self.getTypedRuleContext(TikzParser.NodeIDContext,0)


        def coordinates(self):
            return self.getTypedRuleContext(TikzParser.CoordinatesContext,0)


        def label(self):
            return self.getTypedRuleContext(TikzParser.LabelContext,0)


        def DELIMITER(self):
            return self.getToken(TikzParser.DELIMITER, 0)

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
            self.state = 27
            self.match(TikzParser.T__2)
            self.state = 28
            self.nodeID()
            self.state = 29
            self.match(TikzParser.T__3)
            self.state = 30
            self.coordinates()
            self.state = 31
            self.label()
            self.state = 32
            self.match(TikzParser.DELIMITER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TikzParser.ID, 0)

        def getRuleIndex(self):
            return TikzParser.RULE_nodeID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeID" ):
                listener.enterNodeID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeID" ):
                listener.exitNodeID(self)




    def nodeID(self):

        localctx = TikzParser.NodeIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nodeID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(TikzParser.T__4)
            self.state = 35
            self.match(TikzParser.ID)
            self.state = 36
            self.match(TikzParser.T__5)
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

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(TikzParser.DIGIT)
            else:
                return self.getToken(TikzParser.DIGIT, i)

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
        self.enterRule(localctx, 8, self.RULE_coordinates)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(TikzParser.T__4)
                self.state = 39
                self.match(TikzParser.DIGIT)
                self.state = 40
                self.match(TikzParser.T__6)
                self.state = 41
                self.match(TikzParser.DIGIT)
                self.state = 42
                self.match(TikzParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(TikzParser.T__4)
                self.state = 44
                self.match(TikzParser.DIGIT)
                self.state = 45
                self.match(TikzParser.T__7)
                self.state = 46
                self.match(TikzParser.DIGIT)
                self.state = 47
                self.match(TikzParser.T__5)
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

        def ID(self):
            return self.getToken(TikzParser.ID, 0)

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
        self.enterRule(localctx, 10, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(TikzParser.T__8)
            self.state = 51
            self.match(TikzParser.ID)
            self.state = 52
            self.match(TikzParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





