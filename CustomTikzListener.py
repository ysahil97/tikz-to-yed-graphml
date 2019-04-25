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
        self.currentEdgeList = []
        self.currentEdgeProperty = {}
        self.latestCoordinateX = 0
        self.latestCoordinateY = 0
        self.lastSeenRadius = None
        self.shapeNodes = []

        self.G = Graph()
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName

    def exitBegin(self, ctx:TikzParser.BeginContext):
        try:
            logger.info("Trying to convert Tikz into GraphML")
            logger.info("GlobalProperties : {}".format(self.globalProperties))
            self.G.globalProperties = copy.copy(self.globalProperties)
            graphml = self.G.get_graph().encode("utf-8")
            with open(self.outputFileName, 'wb') as outFile:
                outFile.write(graphml)
            logging.info("Converted Tikz Graph to GraphML.\n\n\t\tGraphML File Location: {}\n\n".format(self.outputFileName))
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
        self.shapeNodes = []

    def exitNode(self, ctx:TikzParser.NodeContext):
        if len(self.currentNode) > 0:
            self.currentNode["X"] = self.latestCoordinateX
            self.currentNode["Y"] = self.latestCoordinateY
            logger.info("NodeProperties : {}".format(self.currentNode))
            self.G.addNode(**self.currentNode)

    def exitNodeId(self, ctx:TikzParser.NodeIdContext):
        if ctx.VARIABLE() is not None and ctx.VARIABLE().getText() is not None:
            self.currentNode["nodeID"] = ctx.VARIABLE().getText()
        elif ctx.DIGIT() is not None and ctx.DIGIT().getText() is not None:
            self.currentNode["nodeID"] = ctx.DIGIT().getText()
        else:
            self.currentNode["nodeID"] = None

    def exitCartesianCoordinates(self, ctx:TikzParser.CartesianCoordinatesContext):
        self.latestCoordinateX = eval(ctx.DIGIT(0).getText())
        self.latestCoordinateY = eval(ctx.DIGIT(1).getText())
        self.shapeNodes.append((self.latestCoordinateX, self.latestCoordinateY))

    def exitPolarCoordinates(self, ctx:TikzParser.PolarCoordinatesContext):
        try:
            r = eval(ctx.DIGIT(1).getText())
            angle = eval(ctx.DIGIT(0).getText())
            cosA = round(math.cos(math.radians(angle)), 10)
            sinA = round(math.sin(math.radians(angle)), 10)
            print (r, angle, cosA, sinA)
            self.latestCoordinateX = r * cosA
            self.latestCoordinateY = r * sinA
            self.shapeNodes.append((self.latestCoordinateX, self.latestCoordinateY))

        except:
            raise Exception("Cannot Evaluate Math Expression {}".format(ctx.getText()))

    def exitLabel(self, ctx:TikzParser.LabelContext):
        if ctx.VARIABLE() is not None and ctx.VARIABLE().getText() is not None:
            self.currentNode["label"] = ctx.VARIABLE().getText()
        elif ctx.DIGIT() is not None and ctx.DIGIT().getText() is not None:
            self.currentNode["label"] = ctx.DIGIT().getText()
        else:
            self.currentNode["label"] = None

    def exitRadius(self,ctx:TikzParser.RadiusContext):
        self.lastSeenRadius = ctx.VARIABLE().getText()

    def exitEdgeNode(self, ctx:TikzParser.EdgeNodeContext):
        if ctx.VARIABLE() is not None:
            self.currentEdgeList.append(ctx.VARIABLE().getText())
        else:
            coord_x = self.latestCoordinateX
            coord_y = self.latestCoordinateY
            edgeNode = {}
            edgeNode["X"] = coord_x
            edgeNode["Y"] = coord_y
            edgeNode["inner_sep"] = "0.25pt"   #edge coordinates is of size 0
            newNodeId = self.G.addNode(**edgeNode)
            self.currentEdgeList.append(newNodeId)

    def exitEdgeProperties(self, ctx:TikzParser.EdgePropertiesContext):
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            edgeProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentEdgeProperty.update(edgeProperties)     #Merging the properties together

    def enterDraw(self,ctx:TikzParser.DrawContext):
        self.currentEdgeList = []
        self.currentEdgeProperty = {}

    def exitDraw(self,ctx:TikzParser.DrawContext):
        if ctx.VARIABLE():

            # handle logic for rectangle drawing for now
            total_x = 0
            total_y = 0
            height = 0
            width = 0
            if self.shape == 'rectangle':
                for i in self.shapeNodes:
                    total_x+=int(i[0])
                    total_y+=int(i[1])
                total_x = str(total_x/2)
                total_y = str(total_y/2)
                height = float(abs(int(self.shapeNodes[1][1])-int(self.shapeNodes[0][1])))
                width = float(abs(int(self.shapeNodes[1][0])-int(self.shapeNodes[0][0])))
            elif self.shape == 'circle':
                total_x = int(self.shapeNodes[0][0])
                total_y = int(self.shapeNodes[0][1])
                height = float(int(self.lastSeenRadius)*2)
                width = float(int(self.lastSeenRadius)*2)
            self.G.addNode(X=total_x,Y=total_y,height=height,width=width,shape=self.shape)
        else:
            pointed = False
            if "direction" in self.currentEdgeProperty:
                pointed = True
                #For left directed edges, adding the edge nodes in reverse
                if self.currentEdgeProperty['direction'] == '<-':
                    self.currentEdgeList.reverse()

            sz = len(self.currentEdgeList)
            for i in range(1, sz, 1):
                node1, node2 = self.currentEdgeList[i-1], self.currentEdgeList[i]
                self.G.addEdge(node1, node2, pointed)

    def exitNodeProperties(self, ctx:TikzParser.NodePropertiesContext):
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            nodeProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentNode.update(nodeProperties)     #Merging the properties together
