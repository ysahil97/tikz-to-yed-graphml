# Generated from grammar/Tikz.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TikzParser import TikzParser
else:
    from TikzParser import TikzParser

# This class defines a complete listener for a parse tree produced by TikzParser.
class TikzListener(ParseTreeListener):

    # Enter a parse tree produced by TikzParser#begin.
    def enterBegin(self, ctx:TikzParser.BeginContext):
        pass

    # Exit a parse tree produced by TikzParser#begin.
    def exitBegin(self, ctx:TikzParser.BeginContext):
        pass


    # Enter a parse tree produced by TikzParser#globalProperties.
    def enterGlobalProperties(self, ctx:TikzParser.GlobalPropertiesContext):
        pass

    # Exit a parse tree produced by TikzParser#globalProperties.
    def exitGlobalProperties(self, ctx:TikzParser.GlobalPropertiesContext):
        pass


    # Enter a parse tree produced by TikzParser#globalProperty.
    def enterGlobalProperty(self, ctx:TikzParser.GlobalPropertyContext):
        pass

    # Exit a parse tree produced by TikzParser#globalProperty.
    def exitGlobalProperty(self, ctx:TikzParser.GlobalPropertyContext):
        pass


    # Enter a parse tree produced by TikzParser#instructions.
    def enterInstructions(self, ctx:TikzParser.InstructionsContext):
        pass

    # Exit a parse tree produced by TikzParser#instructions.
    def exitInstructions(self, ctx:TikzParser.InstructionsContext):
        pass


    # Enter a parse tree produced by TikzParser#node.
    def enterNode(self, ctx:TikzParser.NodeContext):
        pass

    # Exit a parse tree produced by TikzParser#node.
    def exitNode(self, ctx:TikzParser.NodeContext):
        pass


    # Enter a parse tree produced by TikzParser#nodeId.
    def enterNodeId(self, ctx:TikzParser.NodeIdContext):
        pass

    # Exit a parse tree produced by TikzParser#nodeId.
    def exitNodeId(self, ctx:TikzParser.NodeIdContext):
        pass


    # Enter a parse tree produced by TikzParser#nodeProperties.
    def enterNodeProperties(self, ctx:TikzParser.NodePropertiesContext):
        pass

    # Exit a parse tree produced by TikzParser#nodeProperties.
    def exitNodeProperties(self, ctx:TikzParser.NodePropertiesContext):
        pass


    # Enter a parse tree produced by TikzParser#properties.
    def enterProperties(self, ctx:TikzParser.PropertiesContext):
        pass

    # Exit a parse tree produced by TikzParser#properties.
    def exitProperties(self, ctx:TikzParser.PropertiesContext):
        pass


    # Enter a parse tree produced by TikzParser#individualProperty.
    def enterIndividualProperty(self, ctx:TikzParser.IndividualPropertyContext):
        pass

    # Exit a parse tree produced by TikzParser#individualProperty.
    def exitIndividualProperty(self, ctx:TikzParser.IndividualPropertyContext):
        pass


    # Enter a parse tree produced by TikzParser#coordinates.
    def enterCoordinates(self, ctx:TikzParser.CoordinatesContext):
        pass

    # Exit a parse tree produced by TikzParser#coordinates.
    def exitCoordinates(self, ctx:TikzParser.CoordinatesContext):
        pass


    # Enter a parse tree produced by TikzParser#label.
    def enterLabel(self, ctx:TikzParser.LabelContext):
        pass

    # Exit a parse tree produced by TikzParser#label.
    def exitLabel(self, ctx:TikzParser.LabelContext):
        pass


