import sys
import logging
import antlr4
from filterGraphml import *
from grammar.TikzListener import TikzListener
from grammar.TikzParser import TikzParser
from generateGraphml import Graph

class CustomTikzListener(TikzListener) :
    def __init__(self, inputFileName:str, outputFileName:str):
        self.currentNode = {}
        self.G = Graph()
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName

    def exitBegin(self, ctx:TikzParser.BeginContext):
        try:
            logging.info("Trying to convert Tikz into GraphML")
            graphml = self.G.get_graph().encode("utf-8")
            with open(self.outputFileName, 'wb') as outFile:
                outFile.write(graphml)
            logging.info("Converted Tikz Graph to GraphML.\n\n\t\tGraphML File Location: {}\n\n".format(self.outputFileName))
        except Warning as e:
            logging.warn("Error in converting {} - {}".format(self.inputFileName, e))

    def exitNode(self, ctx:TikzParser.NodeContext):
        if len(self.currentNode) > 0:
            self.G.addNode(**self.currentNode)

    def exitNodeId(self, ctx:TikzParser.NodeIdContext):
        if ctx.VARIABLE() is not None:
            self.currentNode["nodeID"] = ctx.VARIABLE().getText()
        else:
            self.currentNode["nodeID"] = None

    def exitCoordinates(self, ctx:TikzParser.CoordinatesContext):
        self.currentNode["X"] = ctx.DIGIT(0).getText()
        self.currentNode["Y"] = ctx.DIGIT(1).getText()

    def exitLabel(self, ctx:TikzParser.LabelContext):
        if ctx.VARIABLE() is not None and ctx.VARIABLE().getText() is not None:
            self.currentNode["label"] = ctx.VARIABLE().getText()
        else:
            self.currentNode["label"] = None
    
    def exitIndividualProperty(self, ctx:TikzParser.IndividualPropertyContext):
        key = ""
        value = ""
        currentValue = ""
        for child in ctx.children:
            if child.getText() != "=":
                currentValue += child.getText() + " "
            else:
                key = currentValue
                currentValue = ""
        value = currentValue
        # property of Key Value of format "x = y"
        if len(key) > 0:
            k, v = identifyKeyValueProperty(key, value)
        # individual property of format "x"
        else:
            k, v = identifyIndividualProperty(value)

        self.currentNode[k] = v