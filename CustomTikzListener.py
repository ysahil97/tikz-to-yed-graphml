import sys
import logging
import antlr4
from filterGraphml import *
from grammar.TikzListener import TikzListener
from grammar.TikzParser import TikzParser
from generateGraphml import Graph
import math
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

    def enterNode(self, ctx:TikzParser.NodeContext):
        self.currentNode = {}

    def exitNode(self, ctx:TikzParser.NodeContext):
        if len(self.currentNode) > 0:
            self.G.addNode(**self.currentNode)

    def exitNodeId(self, ctx:TikzParser.NodeIdContext):
        if ctx.VARIABLE() is not None:
            self.currentNode["nodeID"] = ctx.VARIABLE().getText()
        else:
            self.currentNode["nodeID"] = None

    def exitCartesianCoordinates(self, ctx:TikzParser.CoordinatesContext):
        self.currentNode["X"] = eval(ctx.DIGIT(0).getText())
        self.currentNode["Y"] = eval(ctx.DIGIT(1).getText())

    def exitPolarCoordinates(self, ctx:TikzParser.CoordinatesContext):
        try:
            r = eval(ctx.DIGIT(1).getText())
            angle = eval(ctx.DIGIT(0).getText())
            cosA = round(math.cos(math.radians(angle)), 10)
            sinA = round(math.sin(math.radians(angle)), 10)
            print (r, angle, cosA, sinA)
            self.currentNode["X"] = r * cosA
            self.currentNode["Y"] = r * sinA
        except:
            logger.error("Cannot Parse ", ctx.getText())



    def exitLabel(self, ctx:TikzParser.LabelContext):
        if ctx.VARIABLE() is not None and ctx.VARIABLE().getText() is not None:
            if("label" in self.currentNode):
                self.currentNode["label"] = self.currentNode["label"] + "\n" + ctx.VARIABLE().getText()
            else:
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
        
        if k is not None:
            self.currentNode[k] = v