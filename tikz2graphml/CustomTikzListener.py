import copy
import math
import logging
import tikz2graphml.parsingUtils as parsingUtils
from tikz2graphml.grammar.TikzListener import TikzListener
from tikz2graphml.grammar.TikzParser import TikzParser
from tikz2graphml.generateGraphml import Graph

logger = logging.getLogger()

# Custom Tikz Listener to augment Tikz Parsing with appropriate custiom actions
class CustomTikzListener(TikzListener):
    def __init__(self, inputFileName: str, outputFileName: str, scalingFactor: float):
        logger.debug("Parsing Tikz Code")
        self.globalProperties = {}
        self.currentNode = {}
        self.currentEdgeList = []
        self.currentEdgeProperty = {}
        self.latestCoordinateX = 0
        self.latestCoordinateY = 0
        self.lastSeenRadius = 1     # Default radius of \draw circle
        self.shapeNodesCoordinates = []
        self.G = Graph(scalingFactor)
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName
        self.nodeIds = {}
        self.numNodeIds = {}

    def exitBegin(self, ctx: TikzParser.BeginContext):
        """
        The exit of begin rule signals the end of graph creation
        Hence, creating the GraphML file here and saving it
        """
        try:
            logger.debug("GlobalProperties : {}".format(self.globalProperties))
            self.G.globalProperties = copy.copy(self.globalProperties)
            graphml = self.G.get_graph().encode("utf-8")
            with open(self.outputFileName, 'wb') as outFile:
                outFile.write(graphml)
            logger.info("Converted Tikz Graph to GraphML")
            logger.info("GraphML File Location: {}\n\n".format(self.outputFileName))
        except Warning as e:
            logger.warn("Error in converting {} - {}".format(self.inputFileName, e))

    def exitGlobalProperties(self, ctx: TikzParser.GlobalPropertiesContext):
        # globalProperties: EVERY (VARIABLE|EXPRESSION) '/.' 'style' '=' '{' properties '}'
        if len(ctx.getTokens(TikzParser.EVERY)) == 1:
            entityForEveryProperty = ctx.getChild(1).getText()
            assert entityForEveryProperty == "node" or \
                entityForEveryProperty == "edge" or \
                entityForEveryProperty == "draw", "Error in parsing {}. Only support \"node,edge,draw\" as ENTITY in \"every <ENTITY>/.style{{}}\"".format(ctx.getText())
            properties = parsingUtils.handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.globalProperties.update({entityForEveryProperty: properties})

        # globalProperties: properties
        elif len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            properties = parsingUtils.handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.globalProperties.update(properties)

    def enterNode(self, ctx: TikzParser.NodeContext):
        """
        Flushing out all node related data before analyzing it
        """
        self.currentNode = {}           # Emptying values before handling a new node
        logger.debug("Parsing Node {}".format(ctx.getText()))
        for k, v in self.globalProperties.items():
            if k == "node":
                self.currentNode.update(v)

    def exitNode(self, ctx: TikzParser.NodeContext):
        """
        Exit of Node rule signals no more node properties
        Hence, storing all those properties in the node dict
        """
        self.currentNode["X"] = self.latestCoordinateX
        self.currentNode["Y"] = self.latestCoordinateY
        if "edge_color" not in self.currentNode:
            self.currentNode["edge_color"] = "black"
        
        # Only send those attributes which are supported
        parsingUtils.filterOutNotSupportedNodeTags(self.currentNode)
        logger.debug("Got Node: {} in input {}".format(self.currentNode, ctx.getText()))
        self.G.addNode(**self.currentNode)

    def exitNodeId(self, ctx: TikzParser.NodeIdContext):
        # nodeID: OPEN_PARANTHESES (VARIABLE|EXPRESSION)? CLOSE_PARANTHESES
        if ctx.getChildCount() == 3:
            """
            Repeated nodeID checking done here
            """
            nodeId = ctx.getChild(1).getText()
            if nodeId in self.nodeIds:
                logger.debug("Got repeated nodeId : {}".format(ctx.getText()))
                self.numNodeIds[nodeId] += 1
                newNodeId = nodeId + "_" + str(self.numNodeIds[nodeId])
                self.currentNode["nodeID"] = newNodeId
                self.nodeIds[nodeId] = newNodeId
            else:
                logger.debug("Got new nodeId : {}".format(ctx.getText()))
                self.nodeIds[nodeId] = nodeId
                self.numNodeIds[nodeId] = 0
                self.currentNode["nodeID"] = nodeId
        else:
            logger.debug("No NodeId present : {}".format(ctx.getText()))
            self.currentNode["nodeID"] = None

    def exitCartesianCoordinates(self, ctx: TikzParser.CartesianCoordinatesContext):
        logger.debug("Cartesian Coordinates {}".format(ctx.getText()))
        self.latestCoordinateX = parsingUtils.handleNumbers(ctx.getChild(1).getText())
        self.latestCoordinateY = parsingUtils.handleNumbers(ctx.getChild(3).getText())
        self.shapeNodesCoordinates.append((self.latestCoordinateX, self.latestCoordinateY))

    def exitPolarCoordinates(self, ctx: TikzParser.PolarCoordinatesContext):
        logger.debug("Polar Coordinates {}".format(ctx.getText()))
        angle = parsingUtils.handleNumbers(ctx.getChild(1).getText())
        r = parsingUtils.handleNumbers(ctx.getChild(3).getText())
        cosA = round(math.cos(math.radians(angle)), 10)
        sinA = round(math.sin(math.radians(angle)), 10)
        self.latestCoordinateX = r * cosA
        self.latestCoordinateY = r * sinA
        logger.debug("Polar Coordinates translated {}".format(self.latestCoordinateX, self.latestCoordinateY))
        self.shapeNodesCoordinates.append((self.latestCoordinateX, self.latestCoordinateY))

    def exitLabel(self, ctx: TikzParser.LabelContext):
        if ctx.LABEL_VARIABLE() is not None:
            label_value = ctx.LABEL_VARIABLE().getText()
            # Stripping off $ at both the ends of the obtained label string in
            # order to get real data contained by the label
            self.currentNode["label"] = parsingUtils.parseLabelValue(label_value)

    def exitRadius(self, ctx: TikzParser.RadiusContext):
        logger.debug("Radius {}".format(ctx.getText()))
        self.lastSeenRadius = ctx.getChild(1).getText()
        self.lastSeenRadius = float(parsingUtils.handleNumbers(self.lastSeenRadius))

    def exitEdgeNode(self, ctx: TikzParser.EdgeNodeContext):
        # edgeNode: OPEN_PARANTHESES (VARIABLE|EXPRESSION) CLOSE_PARANTHESES
        if ctx.getChildCount() == 3:
            if ctx.getChild(1).getText() not in self.nodeIds:
                raise Exception("Node Id in draw operation does not exist : {}".format(ctx.getText()))

            logger.debug("EdgeNode, Original Nodeid: current id -- {}:{}".format(ctx.getChild(1).getText(), self.nodeIds[ctx.getChild(1).getText()]))
            self.currentEdgeList.append(self.nodeIds[ctx.getChild(1).getText()])
        else:
            # edgeNode: coordinates
            coord_x = self.latestCoordinateX
            coord_y = self.latestCoordinateY

            edgeNode = {}
            for k, v in self.globalProperties.items():
                if k == "node":
                    edgeNode.update(v)

            edgeNode["X"] = coord_x
            edgeNode["Y"] = coord_y
            edgeNode["transparent"] = "true"
            # Only send those attributes which are supported
            parsingUtils.filterOutNotSupportedNodeTags(edgeNode)

            newNodeId = self.G.addNode(**edgeNode)
            self.currentEdgeList.append(newNodeId)

    def exitEdgeProperties(self, ctx: TikzParser.EdgePropertiesContext):
        # Inclusion of current edge property into the set of all
        # edge properties for that edge
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            edgeProperties = parsingUtils.handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentEdgeProperty.update(edgeProperties)     # Merging the properties together

    def enterDraw(self, ctx: TikzParser.DrawContext):
        # Emptying data structures before handling a new node/edge
        self.currentEdgeList = []
        self.currentEdgeProperty = {}
        self.currentNode = {}
        self.shapeNodesCoordinates = []
        self.lastSeenRadius = 1     # Default radius of \draw circle

        for k, v in self.globalProperties.items():
            if k == "edge" or k == "draw":
                self.currentEdgeProperty.update(v)

        for k, v in self.globalProperties.items():
            if k == "node" or k == "draw":
                self.currentNode.update(v)

    def exitDraw(self, ctx: TikzParser.DrawContext):
        # \draw shape commands
        if len(ctx.getTypedRuleContexts(TikzParser.CoordinatesContext)) >= 1:

            # \draw[] () node {}
            if len(ctx.getTypedRuleContexts(TikzParser.NodePropertiesContext)) == 1:
                logger.debug("Draw Node Instruction {}".format(ctx.getText()))
                self.currentNode["X"] = self.latestCoordinateX
                self.currentNode["Y"] = self.latestCoordinateY
                logger.debug("NodeProperties : {}".format(self.currentNode))

                # Only send those attributes which are supported
                parsingUtils.filterOutNotSupportedNodeTags(self.currentNode)
                self.G.addNode(**self.currentNode)
            else:
                logger.debug("Draw Shape Instruction {}".format(ctx.getText()))
                node_shape = ctx.getChild(3).getText()
                # handle logic for rectangle drawing
                X = 0
                Y = 0
                height = 0
                width = 0

                if node_shape == 'rectangle':
                    assert len(self.shapeNodesCoordinates) == 2, "Error in parsing {}. Draw shape command has incorrect number of coordinates (!=2)".format(ctx.getText())
                    for i in self.shapeNodesCoordinates:
                        X += i[0]
                        Y += i[1]
                    X /= 2.0
                    Y /= 2.0
                    height = float(abs(int(self.shapeNodesCoordinates[1][1]) - float(self.shapeNodesCoordinates[0][1])))
                    height = 1 if height == 0.0 else height

                    width = float(abs(int(self.shapeNodesCoordinates[1][0]) - float(self.shapeNodesCoordinates[0][0])))
                    width = 1 if width == 0.0 else width

                elif node_shape == 'ellipse':
                    assert len(self.shapeNodesCoordinates) == 2, "Error in parsing {}. Draw shape command has incorrect number of coordinates (!=2)".format(ctx.getText())
                    X = self.shapeNodesCoordinates[0][0]
                    Y = self.shapeNodesCoordinates[0][1]
                    width = float(self.shapeNodesCoordinates[1][0]) * 2
                    height = float(self.shapeNodesCoordinates[1][1]) * 2
                    height = 1 if height == 0.0 else height
                    width = 1 if width == 0.0 else width

                elif node_shape == 'circle':
                    assert len(self.shapeNodesCoordinates) == 1, "Error in parsing {}. Draw circle shape command has incorrect number of coordinates(!=1)".format(ctx.getText())
                    height = float(float(self.lastSeenRadius) * 2)
                    width = float(float(self.lastSeenRadius) * 2)
                    X = float(self.shapeNodesCoordinates[0][0])
                    Y = float(self.shapeNodesCoordinates[0][1])
                    

                else:
                    raise Exception("Error in parsing {}. Currently only support rectangle/circle/ellipse in \draw command".format(ctx.getText()))

                self.G.addNode(X=X, Y=Y, height=height, width=width, shape=node_shape, edge_color="black")

        # \draw line commands
        else:
            logger.debug("Draw Edge(line) Instruction {}".format(ctx.getText()))
            sz = len(self.currentEdgeList)
            arrowFoot = False
            arrowHead = False
            color = "black"
            label = ""
            width = "1"
            line_type = "line"
            if "direction" in self.currentEdgeProperty:
                if self.currentEdgeProperty['direction'] == '->':
                    arrowHead = True
                # For left directed edges, adding the edge nodes in reverse
                elif self.currentEdgeProperty['direction'] == '<-':
                    self.currentEdgeList.reverse()
                    arrowHead = True
                elif self.currentEdgeProperty['direction'] == '-!-':
                    arrowHead = False
                # Only first and last edge should be directed
                elif self.currentEdgeProperty['direction'] == '<->':
                    arrowFoot = True
                    arrowHead = True

            if "fill" in self.currentEdgeProperty:
                color = self.currentEdgeProperty["fill"]

            if "width" in self.currentEdgeProperty:
                width = str(float(self.currentEdgeProperty["width"]) * 0.0352778)

            if "label" in self.currentEdgeProperty:
                label = self.currentEdgeProperty["label"]

            if "line_type" in self.currentEdgeProperty:
                line_type = self.currentEdgeProperty["line_type"]

            for i in range(1, sz, 1):
                nodeX, nodeY = self.currentEdgeList[i-1], self.currentEdgeList[i]
                logger.debug("Adding Edge: {nodeX} {nodeY} {arrowHead} {arrowFoot} {color} {width} {label} {line_type}".format(nodeX=nodeX, nodeY=nodeY, arrowHead=arrowHead, arrowFoot=arrowFoot, color=color, width=width, label=label, line_type=line_type))
                self.G.addEdge(nodeX=nodeX, nodeY=nodeY, arrowHead=arrowHead, arrowFoot=arrowFoot, color=color, width=width, label=label, line_type=line_type)


    def exitNodeProperties(self, ctx: TikzParser.NodePropertiesContext):
        # Inclusion of current node property into the set of all
        # node properties for that node
        if len(ctx.getTypedRuleContexts(TikzParser.PropertiesContext)) == 1:
            nodeProperties = parsingUtils.handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))
            self.currentNode.update(nodeProperties)
