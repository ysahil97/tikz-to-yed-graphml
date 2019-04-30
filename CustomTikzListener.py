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
        logger.debug("Parsing Tikz Code")
        self.globalProperties = {}
        self.currentNode = {}
        self.currentEdgeList = []
        self.currentEdgeProperty = {}
        self.latestCoordinateX = 0
        self.latestCoordinateY = 0
        self.lastSeenRadius = 1  #Default radius of \draw circle
        self.shapeNodesCoordinates = []
        self.G = Graph(scalingFactor)
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName
        self.nodeIds = {}
        self.numNodeIds = {}

    def exitBegin(self, ctx:TikzParser.BeginContext):
        try:
            logger.debug("GlobalProperties : {}".format(self.globalProperties))
            self.G.globalProperties = copy.copy(self.globalProperties)
            graphml = self.G.get_graph().encode("utf-8")
            with open(self.outputFileName, 'wb') as outFile:
                outFile.write(graphml)
            logging.debug("Converted Tikz Graph to GraphML")
            logging.info("GraphML File Location: {}\n\n".format(self.outputFileName))
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
        logging.debug("Parsing Node {}".format(ctx.getText()))
        for k,v in self.globalProperties.items():
            if k == "node":
                self.currentNode.update(v)

    def exitNode(self, ctx:TikzParser.NodeContext):
        self.currentNode["X"] = self.latestCoordinateX
        self.currentNode["Y"] = self.latestCoordinateY
        # Only send those attributes which are supported
        filterOutNotSupportedNodeTags(self.currentNode)
        logging.debug("Got Node: {}".format(self.currentNode))
        self.G.addNode(**self.currentNode)

    def exitNodeId(self, ctx:TikzParser.NodeIdContext):
        #nodeID: OPEN_PARANTHESES (VARIABLE|EXPRESSION)? CLOSE_PARANTHESES
        if ctx.getChildCount() == 3:
            if ctx.getChild(1).getText() in self.nodeIds:
                logging.debug("Got repeated nodeId")
                self.numNodeIds[ctx.getChild(1).getText()] += 1
                newNodeId = ctx.getChild(1).getText() + "_" + str(self.numNodeIds[ctx.getChild(1).getText()])
                self.currentNode["nodeID"] = newNodeId
                self.nodeIds[ctx.getChild(1).getText()] = newNodeId
            else:
                logging.debug("Got new nodeId")
                self.nodeIds[ctx.getChild(1).getText()] = ctx.getChild(1).getText()
                self.numNodeIds[ctx.getChild(1).getText()] = 0
                self.currentNode["nodeID"] = ctx.getChild(1).getText()
        else:
            logging.debug("No NodeId present")
            self.currentNode["nodeID"] = None

    def exitCartesianCoordinates(self, ctx:TikzParser.CartesianCoordinatesContext):
        logging.debug("Cartesian Coordinates {}".format(ctx.getText()))
        self.latestCoordinateX = handleNumbers(ctx.getChild(1).getText())
        self.latestCoordinateY = handleNumbers(ctx.getChild(3).getText())
        self.shapeNodesCoordinates.append((self.latestCoordinateX, self.latestCoordinateY))

    def exitPolarCoordinates(self, ctx:TikzParser.PolarCoordinatesContext):
        logging.debug("Polar Coordinates {}".format(ctx.getText()))
        angle = handleNumbers(ctx.getChild(1).getText())
        r = handleNumbers(ctx.getChild(3).getText())
        cosA = round(math.cos(math.radians(angle)), 10)
        sinA = round(math.sin(math.radians(angle)), 10)
        self.latestCoordinateX = r * cosA
        self.latestCoordinateY = r * sinA
        self.shapeNodesCoordinates.append((self.latestCoordinateX, self.latestCoordinateY))
        
    def exitLabel(self, ctx:TikzParser.LabelContext):
        if ctx.LABEL_VARIABLE() is not None:
            label_value = ctx.LABEL_VARIABLE().getText()
            self.currentNode["label"] = parseLabelValue(label_value)

    def exitRadius(self,ctx:TikzParser.RadiusContext):
        logging.debug("Radius {}".format(ctx.getText()))
        self.lastSeenRadius = ctx.getChild(1).getText()
        self.lastSeenRadius = float(handleNumbers(self.lastSeenRadius))

    def exitEdgeNode(self, ctx:TikzParser.EdgeNodeContext):
        #edgeNode: OPEN_PARANTHESES (VARIABLE|EXPRESSION) CLOSE_PARANTHESES
        if ctx.getChildCount() == 3:
            logging.debug("EdgeNode, Orinial Nodeid: current id -- {}:{}".format(ctx.getChild(1).getText(), self.nodeIds[ctx.getChild(1).getText()]))
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
            edgeNode["transparent"] = "true"
            
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
                logging.debug("Draw Node Instruction {}".format(ctx.getText()))
                self.currentNode["X"] = self.latestCoordinateX
                self.currentNode["Y"] = self.latestCoordinateY
                logger.debug("NodeProperties : {}".format(self.currentNode))

                # Only send those attributes which are supported
                filterOutNotSupportedNodeTags(self.currentNode)
                self.G.addNode(**self.currentNode)
            else:
                logging.debug("Draw Shape Instruction {}".format(ctx.getText()))
                node_shape = ctx.getChild(3).getText()
                # handle logic for rectangle drawing
                X = 0
                Y = 0
                height = 0
                width = 0

                if node_shape == 'rectangle':
                    assert len(self.shapeNodesCoordinates) == 2, "Error in parsing {}. Draw shape command has incorrect number of coordinates (!=2)".format(ctx.getText())

                    minx = sys.float_info.max
                    miny = sys.float_info.min
                    for i in self.shapeNodesCoordinates:
                        X += i[0]
                        Y += i[1]
                    X /= 2.0
                    Y /= 2.0
                    height = float(abs(int(self.shapeNodesCoordinates[1][1]) - float(self.shapeNodesCoordinates[0][1])))
                    width = float(abs(int(self.shapeNodesCoordinates[1][0]) - float(self.shapeNodesCoordinates[0][0])))
                
                elif node_shape == 'ellipse':
                    assert len(self.shapeNodesCoordinates) == 2, "Error in parsing {}. Draw shape command has incorrect number of coordinates (!=2)".format(ctx.getText())
                    X = self.shapeNodesCoordinates[0][0]
                    Y = self.shapeNodesCoordinates[0][1]
                    width = float(self.shapeNodesCoordinates[1][0]) * 2
                    height = float(self.shapeNodesCoordinates[1][1]) * 2

                elif node_shape == 'circle':
                    assert len(self.shapeNodesCoordinates) == 1, "Error in parsing {}. Draw circle shape command has incorrect number of coordinates(!=1)".format(ctx.getText())
                    height  = float(float(self.lastSeenRadius) * 2)
                    width   = float(float(self.lastSeenRadius) * 2)
                    X = float(self.shapeNodesCoordinates[0][0])
                    Y = float(self.shapeNodesCoordinates[0][1])

                else:
                    raise Exception("Error in parsing {}. Currently only support rectangle/circle/ellipse in \draw command".format(ctx.getText()))
                
                self.G.addNode(X=X, Y=Y, height=height, width=width, shape=node_shape, edge_color="black")

        # \draw line commands
        else:
            logging.debug("Draw Edge(line) Instruction {}".format(ctx.getText()))
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
                width = str(float(self.currentEdgeProperty["width"])* 0.0352778)

            if "label" in self.currentEdgeProperty:
                label = self.currentEdgeProperty["label"]

            if "line_type" in self.currentEdgeProperty:
                line_type = self.currentEdgeProperty["line_type"]

            for i in range(1, sz, 1):
                nodeX, nodeY = self.currentEdgeList[i-1], self.currentEdgeList[i]
                logging.debug("Adding Edge: {nodeX} {nodeY} {pointed} {color} {width} {label} {line_type}".format(nodeX=nodeX, nodeY=nodeY, pointed=pointed[i], color=color, width=width, label=label, line_type=line_type))
                self.G.addEdge(nodeX=nodeX, nodeY=nodeY, pointed=pointed[i], color=color, width=width, label=label, line_type=line_type)

    def exitNodeProperties(self, ctx:TikzParser.NodePropertiesContext):
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            nodeProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentNode.update(nodeProperties)
