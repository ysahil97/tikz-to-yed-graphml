import sys
import math
import antlr4
import logging
from grammar.TikzListener import TikzListener
from grammar.TikzParser import TikzParser
from generateGraphml import Graph
from handleProperties import *
import copy 

logger = logging.getLogger(__name__)

class CustomTikzListener(TikzListener) :
    def __init__(self, inputFileName:str, outputFileName:str):
        self.globalProperties = {}
        self.currentNode = {}
        self.G = Graph()
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName

    def exitBegin(self, ctx:TikzParser.BeginContext):
        try:
            logger.info("Trying to convert Tikz into GraphML")
            logger.info("GlobalProperties : {}".format(self.globalProperties))
            # graphml = self.G.get_graph().encode("utf-8")
            # with open(self.outputFileName, 'wb') as outFile:
            #     outFile.write(graphml)
            # logging.info("Converted Tikz Graph to GraphML.\n\n\t\tGraphML File Location: {}\n\n".format(self.outputFileName))
        except Warning as e:
            logging.warn("Error in converting {} - {}".format(self.inputFileName, e))

    def exitGlobalProperties(self, ctx:TikzParser.GlobalPropertiesContext):

        #globalProperties: EVERY VARIABLE '/.' 'style' '=' '{' properties '}'
        if len(ctx.getTokens(TikzParser.EVERY)) == 1:

            entityForEveryProperty = ctx.getToken(TikzParser.VARIABLE, 0).getText()
            assert entityForEveryProperty == "node" or \
                entityForEveryProperty == "label" or \
                entityForEveryProperty == "edge" or \
                entityForEveryProperty == "draw", "Error in parsing {}. Only support \"node,label,edge,draw\" as ENTITY in \"every <ENTITY> /.style{{}}\"".format(ctx.getText())
            properties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.globalProperties.update({ entityForEveryProperty : properties })

        #globalProperties: properties
        elif ctx.getChildCount() == 1 and len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            properties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.globalProperties.update(properties)

    def enterNode(self, ctx:TikzParser.NodeContext):
        if "node" in  self.globalProperties:
            self.currentNode =  copy.copy(self.globalProperties["node"])
        else:
            self.currentNode = {}

    def exitNode(self, ctx:TikzParser.NodeContext):
        if len(self.currentNode) > 0:
            logger.info("NodeProperties : {}".format(self.currentNode))
            self.G.addNode(**self.currentNode)

    def exitNodeId(self, ctx:TikzParser.NodeIdContext):
        if ctx.VARIABLE() is not None:
            self.currentNode["nodeID"] = ctx.VARIABLE().getText()
        elif ctx.DIGIT() is not None:
            self.currentNode["nodeID"] = ctx.DIGIT().getText()
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

    def exitNodeProperties(self, ctx:TikzParser.NodePropertiesContext):
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            nodeProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentNode.update(nodeProperties)     #Merging the properties together
