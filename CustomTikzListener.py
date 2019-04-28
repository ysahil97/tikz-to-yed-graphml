import sys
import math
import antlr4
import logging
from grammar.TikzListener import TikzListener
from grammar.TikzParser import TikzParser
from generateGraphml import Graph
from parsingUtils import *
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
        self.lastSeenRadius = 1     #Default radius of \draw circle
        self.shapeNodesCoordinates = []

        self.G = Graph(scalingFactor)
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName
        self.nodeIds = {}
        self.numNodeIds = {}

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

        #globalProperties: EVERY (VARIABLE|EXPRESSION) '/.' 'style' '=' '{' properties '}'
        if len(ctx.getTokens(TikzParser.EVERY)) == 1:

            entityForEveryProperty = ctx.getChild(1).getText() 
            assert entityForEveryProperty == "node" or \
                entityForEveryProperty == "edge" or \
                entityForEveryProperty == "draw", "Error in parsing {}. Only support \"node,edge,draw\" as ENTITY in \"every <ENTITY>/.style{{}}\"".format(ctx.getText())
            properties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.globalProperties.update({ entityForEveryProperty : properties })

        #globalProperties: properties
        elif len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            properties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.globalProperties.update(properties)

    def enterNode(self, ctx:TikzParser.NodeContext):
        self.currentNode = {}           #Emptying values before handling a new node
        for k,v in self.globalProperties.items():
            if k == "node":
                self.currentNode.update(v)

    def exitNode(self, ctx:TikzParser.NodeContext):
        self.currentNode["X"] = self.latestCoordinateX
        self.currentNode["Y"] = self.latestCoordinateY

        # Only send those attributes which are supported
        filterOutNotSupportedNodeTags(self.currentNode)

        self.G.addNode(**self.currentNode)

    def exitNodeId(self, ctx:TikzParser.NodeIdContext):
        #nodeID: OPEN_PARANTHESES (VARIABLE|EXPRESSION)? CLOSE_PARANTHESES
        if ctx.getChildCount() == 3:
            if ctx.getChild(1).getText() in self.nodeIds:
                self.numNodeIds[ctx.getChild(1).getText()] += 1
                newNodeId = ctx.getChild(1).getText() + "_" + str(self.numNodeIds[ctx.getChild(1).getText()])
                self.currentNode["nodeID"] = newNodeId
                self.nodeIds[ctx.getChild(1).getText()] = newNodeId
            else:
                self.nodeIds[ctx.getChild(1).getText()] = ctx.getChild(1).getText()
                self.numNodeIds[ctx.getChild(1).getText()] = 0
                self.currentNode["nodeID"] = ctx.getChild(1).getText()

        else:
            self.currentNode["nodeID"] = None

    def exitCartesianCoordinates(self, ctx:TikzParser.CartesianCoordinatesContext):
        try:
            self.latestCoordinateX = eval(handleNumbers(ctx.getChild(1).getText()))
            self.latestCoordinateY = eval(handleNumbers(ctx.getChild(3).getText()))
            self.shapeNodesCoordinates.append((self.latestCoordinateX, self.latestCoordinateY))
        except:
            raise Exception("Cannot Evaluate Math Expression {}".format(ctx.getText()))

    def exitPolarCoordinates(self, ctx:TikzParser.PolarCoordinatesContext):
        try:
            angle = eval(handleNumbers(ctx.getChild(1).getText()))
            r = eval(handleNumbers(ctx.getChild(3).getText()))
            cosA = round(math.cos(math.radians(angle)), 10)
            sinA = round(math.sin(math.radians(angle)), 10)
            self.latestCoordinateX = r * cosA
            self.latestCoordinateY = r * sinA
            self.shapeNodesCoordinates.append((self.latestCoordinateX, self.latestCoordinateY))
        except:
            raise Exception("Cannot Evaluate Math Expression {}".format(ctx.getText()))

    def exitLabel(self, ctx:TikzParser.LabelContext):
        if ctx.getChildCount() == 3:
            self.currentNode["label"] = ctx.getChild(1).getText()
        else:
            self.currentNode["label"] = None

    def exitRadius(self,ctx:TikzParser.RadiusContext):
        self.lastSeenRadius = ctx.getChild(1).getText()
        self.lastSeenRadius = float(handleNumbers(self.lastSeenRadius)) * 2

    def exitEdgeNode(self, ctx:TikzParser.EdgeNodeContext):
        #edgeNode: OPEN_PARANTHESES (VARIABLE|EXPRESSION) CLOSE_PARANTHESES
        if ctx.getChildCount() == 3:
            print ("-------------",self.nodeIds[ctx.getChild(1).getText()])
            self.currentEdgeList.append(self.nodeIds[ctx.getChild(1).getText()])
        else:
        #edgeNode: coordinates
            coord_x = self.latestCoordinateX
            coord_y = self.latestCoordinateY

            edgeNode = {}
            for k,v in self.globalProperties.items():
                if k == "node":
                    edgeNode.update(v)

            edgeNode["X"] = coord_x
            edgeNode["Y"] = coord_y

            # Only send those attributes which are supported
            filterOutNotSupportedNodeTags(edgeNode)

            newNodeId = self.G.addNode(**edgeNode)
            self.currentEdgeList.append(newNodeId)

    def exitEdgeProperties(self, ctx:TikzParser.EdgePropertiesContext):
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            edgeProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentEdgeProperty.update(edgeProperties)     #Merging the properties together

    def enterDraw(self,ctx:TikzParser.DrawContext):
        #Emptying data structures before handling a new node/edge
        self.currentEdgeList = []
        self.currentEdgeProperty = {}
        self.currentNode = {}
        self.shapeNodesCoordinates = []
        self.lastSeenRadius = 1     #Default radius of \draw circle
        
        for k,v in self.globalProperties.items():
            if k == "edge" or k == "draw":
                self.currentEdgeProperty.update(v)

        for k,v in self.globalProperties.items():
            if k == "node" or k == "draw":
                self.currentNode.update(v)

    def exitDraw(self,ctx:TikzParser.DrawContext):
        # \draw shape commands
        if len(ctx.getTypedRuleContexts(TikzParser.CoordinatesContext)) >= 1:

            #\draw[] () node {}
            if len(ctx.getTypedRuleContexts(TikzParser.NodePropertiesContext)) == 1:
                self.currentNode["X"] = self.latestCoordinateX
                self.currentNode["Y"] = self.latestCoordinateY
                logger.info("NodeProperties : {}".format(self.currentNode))

                # Only send those attributes which are supported
                filterOutNotSupportedNodeTags(self.currentNode)

                self.G.addNode(**self.currentNode)
            else:
                node_shape = ctx.getChild(3).getText()
                # handle logic for rectangle drawing
                total_x = 0
                total_y = 0
                height = 0
                width = 0
                if node_shape == 'rectangle' or  node_shape == 'ellipse':

                    assert len(self.shapeNodesCoordinates) == 2, "Error in parsing {}. Draw shape command has incorrect number of coordinates (!=2)".format(ctx.getText())

                    for i in self.shapeNodesCoordinates:
                        total_x += float(i[0])
                        total_y += float(i[1])

                    total_x = str(total_x / 2)
                    total_y = str(total_y / 2)
                    height = float(abs(int(self.shapeNodesCoordinates[1][1]) - float(self.shapeNodesCoordinates[0][1])))
                    width = float(abs(int(self.shapeNodesCoordinates[1][0]) - float(self.shapeNodesCoordinates[0][0])))
                elif node_shape == 'circle':

                    assert len(self.shapeNodesCoordinates) == 1, "Error in parsing {}. Draw circle shape command has incorrect number of coordinates(!=1)".format(ctx.getText())

                    total_x = float(self.shapeNodesCoordinates[0][0])
                    total_y = float(self.shapeNodesCoordinates[0][1])
                    height = float(float(self.lastSeenRadius) * 2)
                    width = float(float(self.lastSeenRadius) * 2)
                else:
                    raise Exception("Error in parsing {}. Currently only support rectangle/circle/ellipse in \draw command".format(ctx.getText()))

                self.G.addNode(X=total_x, Y=total_y, height=height, width=width, shape=node_shape)
        # \draw line commands
        else:
            sz = len(self.currentEdgeList)
            pointed = [False] * sz
            color = "black"
            label = ""
            width = "1"
            line_type = "line"
            a, b = False, False
            if "direction" in self.currentEdgeProperty:
                if self.currentEdgeProperty['direction'] == '->':
                    pointed = [True] * sz
                #For left directed edges, adding the edge nodes in reverse
                elif self.currentEdgeProperty['direction'] == '<-':
                    self.currentEdgeList.reverse()
                    pointed = [True] * sz
                elif self.currentEdgeProperty['direction'] == '-!-':
                    pointed = [False] * sz
                #Only first and last edge should be directed
                elif self.currentEdgeProperty['direction'] == '<->':
                    pointed = [False] * sz
                    pointed[0] = True
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
