import re
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
    def __init__(self, inputFileName:str, outputFileName:str, scalingFactor:float):
        self.globalProperties = {}
        self.currentNode = {}
        self.currentEdgeList = []
        self.currentEdgeProperty = {}
        self.latestCoordinateX = 0
        self.latestCoordinateY = 0
        self.lastSeenRadius = None
        self.shapeNodesCoordinates = []

        self.G = Graph(scalingFactor)
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
        self.currentNode = {}
        for k,v in self.globalProperties.items():
            if k == "node":
                self.currentNode.update(v)
            # elif not (k == "edge" or k == "label" or k == "draw"):
            #     self.currentNode[k] = v

    def exitNode(self, ctx:TikzParser.NodeContext):
        self.currentNode["X"] = self.latestCoordinateX
        self.currentNode["Y"] = self.latestCoordinateY
        self.G.addNode(**self.currentNode)

    def exitNodeId(self, ctx:TikzParser.NodeIdContext):
        if ctx.VARIABLE() is not None and ctx.VARIABLE().getText() is not None:
            self.currentNode["nodeID"] = ctx.VARIABLE().getText()
        elif ctx.DIGIT() is not None and ctx.DIGIT().getText() is not None:
            self.currentNode["nodeID"] = ctx.DIGIT().getText()
        else:
            self.currentNode["nodeID"] = None

    def exitCartesianCoordinates(self, ctx:TikzParser.CartesianCoordinatesContext):
        try:
            self.latestCoordinateX = eval(self.handleNumbers(ctx.getChild(1).getText()))
            self.latestCoordinateY = eval(self.handleNumbers(ctx.getChild(3).getText()))
            self.shapeNodesCoordinates.append((self.latestCoordinateX, self.latestCoordinateY))
        except:
            raise Exception("Cannot Evaluate Math Expression {}".format(ctx.getText()))

    def exitPolarCoordinates(self, ctx:TikzParser.PolarCoordinatesContext):
        try:
            angle = eval(self.handleNumbers(ctx.getChild(1).getText()))
            r = eval(self.handleNumbers(ctx.getChild(3).getText()))
            cosA = round(math.cos(math.radians(angle)), 10)
            sinA = round(math.sin(math.radians(angle)), 10)
            self.latestCoordinateX = r * cosA
            self.latestCoordinateY = r * sinA
            self.shapeNodesCoordinates.append((self.latestCoordinateX, self.latestCoordinateY))
        except:
            raise Exception("Cannot Evaluate Math Expression {}".format(ctx.getText()))

    def exitLabel(self, ctx:TikzParser.LabelContext):
        if ctx.VARIABLE() is not None and ctx.VARIABLE().getText() is not None:
            self.currentNode["label"] = ctx.VARIABLE().getText()
        elif ctx.DIGIT() is not None and ctx.DIGIT().getText() is not None:
            self.currentNode["label"] = ctx.DIGIT().getText()
        else:
            self.currentNode["label"] = None

    def handleNumbers(self, input):
        m = re.search('^\s*([0-9/*-+.]+)\s*(?:pt|cm)?\s*$', input)
        if m and len(m.group(1)) > 0 and m.group(1) != ".":
            return m.group(1)
       
        raise Exception("Could not parse coordinates individual coordinates")

    def exitRadius(self,ctx:TikzParser.RadiusContext):
        self.lastSeenRadius = ctx.VARIABLE().getText()
        self.lastSeenRadius = float(self.handleNumbers(self.lastSeenRadius)) * 2

    def exitEdgeNode(self, ctx:TikzParser.EdgeNodeContext):
        if ctx.VARIABLE() is not None:
            self.currentEdgeList.append(ctx.VARIABLE().getText())
        else:
            coord_x = self.latestCoordinateX
            coord_y = self.latestCoordinateY
            edgeNode = {}
            edgeNode["X"] = coord_x
            edgeNode["Y"] = coord_y
            edgeNode["inner_sep"] = "2.5pt"   #edge coordinates is of size 0
            newNodeId = self.G.addNode(**edgeNode)
            self.currentEdgeList.append(newNodeId)

    def exitEdgeProperties(self, ctx:TikzParser.EdgePropertiesContext):
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            edgeProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentEdgeProperty.update(edgeProperties)     #Merging the properties together

    def enterDraw(self,ctx:TikzParser.DrawContext):
        self.currentEdgeList = []
        self.currentEdgeProperty = {}
        self.currentNode = {}

        for k,v in self.globalProperties.items():
            # print("k, v : ", k, v)
            if k == "edge":
                self.currentNode.update(v)
        #     elif not (k == "node" or k == "label" or k == "draw"):
        #         self.currentNode[k] = v

        for k,v in self.globalProperties.items():
            if k == "node":
                self.currentNode.update(v)
            # elif not (k == "edge" or k == "label" or k == "draw"):
            #     self.currentNode[k] = v


    def exitDraw(self,ctx:TikzParser.DrawContext):
        if ctx.VARIABLE() is not None:

            if len(ctx.getTypedRuleContexts(TikzParser.NodePropertiesContext)) == 1:
                self.currentNode["X"] = self.latestCoordinateX
                self.currentNode["Y"] = self.latestCoordinateY
                logger.info("NodeProperties : {}".format(self.currentNode))
                self.G.addNode(**self.currentNode)
            else:
                node_shape = ctx.VARIABLE().getText()
                # handle logic for rectangle drawing for now
                total_x = 0
                total_y = 0
                height = 0
                width = 0
                if node_shape == 'rectangle' or  node_shape == 'ellipse':
                    for i in self.shapeNodesCoordinates:
                        total_x += float(i[0])
                        total_y += float(i[1])
                    total_x = str(total_x/2)
                    total_y = str(total_y/2)
                    height = float(abs(int(self.shapeNodesCoordinates[1][1]) - float(self.shapeNodesCoordinates[0][1])))
                    width = float(abs(int(self.shapeNodesCoordinates[1][0]) - float(self.shapeNodesCoordinates[0][0])))
                elif node_shape == 'circle':
                    total_x = float(self.shapeNodesCoordinates[0][0])
                    total_y = float(self.shapeNodesCoordinates[0][1])
                    height = float(float(self.lastSeenRadius)*2)
                    width = float(float(self.lastSeenRadius)*2)
                self.G.addNode(X=total_x, Y=total_y, height=height, width=width, shape=node_shape)
        else:
            sz = len(self.currentEdgeList)
            pointed = [False] * sz
            color = "black"
            label = ""
            width = "1"
            line_type = "line"
            a, b = False, False
            if "direction" in self.currentEdgeProperty:
                #For left directed edges, adding the edge nodes in reverse
                if self.currentEdgeProperty['direction'] == '->':
                    pointed = [True] * sz
                elif self.currentEdgeProperty['direction'] == '<-':
                    self.currentEdgeList.reverse()
                    pointed = [True] * sz
                elif self.currentEdgeProperty['direction'] == '-!-':
                    pointed = [False] * sz
                elif self.currentEdgeProperty['direction'] == '<->':
                    pointed = [False] * sz
                    pointed[1] = True
                    pointed[-1] = True
            
            if "fill" in self.currentEdgeProperty:
                color = self.currentEdgeProperty["fill"]
            
            if "width" in self.currentEdgeProperty:
                width = self.currentEdgeProperty["width"]
            
            if "label" in self.currentEdgeProperty:
                label = self.currentEdgeProperty["label"]
            
            if "line_type" in self.currentEdgeProperty:
                line_type = self.currentEdgeProperty["line_type"]
            
            for i in range(1, sz, 1):
                nodeX, nodeY = self.currentEdgeList[i-1], self.currentEdgeList[i]
                self.G.addEdge(nodeX=nodeX, nodeY=nodeY, pointed=pointed[i], color=color, width=width, label=label, line_type=line_type)

    def exitNodeProperties(self, ctx:TikzParser.NodePropertiesContext):
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            nodeProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentNode.update(nodeProperties) 
