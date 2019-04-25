import sys
import math
import antlr4
import logging
from grammar.TikzListener import TikzListener
from grammar.TikzParser import TikzParser
from generateGraphml import Graph
from handleProperties import *

logger = logging.getLogger(__name__)

class CustomTikzListener(TikzListener) :
    def __init__(self, inputFileName:str, outputFileName:str):
        self.globalProperties = {}
        self.currentNode = {}
        self.currentEdgeNode = {}
        self.G = Graph()
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName
        self.edgesNodesList = []
        self.uniquecounter = 0
        self.currentEdgeProperty = {}

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
        self.currentNode = {}

    def exitNode(self, ctx:TikzParser.NodeContext):
        if len(self.currentNode) > 0:
            logger.info("NodeProperties : {}".format(self.currentNode))
            self.G.addNode(**self.currentNode)

    def exitNodeId(self, ctx:TikzParser.NodeIdContext):
        if ctx.VARIABLE() is not None and ctx.VARIABLE().getText() is not None:
            self.currentNode["nodeID"] = ctx.VARIABLE().getText()
        elif ctx.DIGIT() is not None and ctx.DIGIT().getText() is not None:
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
            logger.error("Cannot Parse {}".format(ctx.getText()))


    def exitLabel(self, ctx:TikzParser.LabelContext):
        if ctx.VARIABLE() is not None and ctx.VARIABLE().getText() is not None:
            self.currentNode["label"] = ctx.VARIABLE().getText()
        elif ctx.DIGIT() is not None and ctx.DIGIT().getText() is not None:
            self.currentNode["label"] = ctx.DIGIT().getText()
        else:
            self.currentNode["label"] = None

    def exitEdgeNode(self, ctx:TikzParser.EdgeNodeContext):
        if ctx.VARIABLE() is not None:
            coord_x = -1 * self.uniquecounter
            coord_y = -1 * self.uniquecounter
            self.currentEdgeNode[(coord_x,coord_y)] = ctx.VARIABLE().getText()
            self.uniquecounter-=1
        else:
            coord_x = ctx.DIGIT(0).getText()
            coord_y = ctx.DIGIT(1).getText()
            node_insert = {}
            node_insert["X"] = coord_x
            node_insert["Y"] = coord_y
            self.G.addNode(**node_insert)
            self.currentEdgeNode[(coord_x,coord_y)] = None

    def exitDraw(self,ctx:TikzParser.DrawContext):
        first_node_seen = True
        node1 = None
        node2 = None
        x1 = "0"
        y1 = "0"
        x2 = "0"
        y2 = "0"
        key_list = list(self.currentEdgeNode.keys())
        # print(key_list)
        pointed = False
        if self.currentEdgeProperty['dir']:
            pointed = True
        if self.currentEdgeProperty['dir'] == 'left':
            key_list.reverse()
        for k in key_list:
            if first_node_seen:
                node1 = self.currentEdgeNode[k]
                x1 = k[0]
                y1 = k[1]
                first_node_seen = False
                continue
            node2 = self.currentEdgeNode[k]
            x2 = k[0]
            y2 = k[1]
            self.G.addEdge(node1,node2,pointed,str(x1),str(y1),str(x2),str(y2))
            node1,x1,y1 = node2,x2,y2
        self.currentEdgeProperty = {}
        self.currentEdgeNode = {}


    def exitNodeProperties(self, ctx:TikzParser.NodePropertiesContext):
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            nodeProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentNode.update(nodeProperties)     #Merging the properties together
