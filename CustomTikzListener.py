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
        self.currentEdgeNode = {}
        self.G = Graph()
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName
        self.edgesNodesList = []
        self.uniquecounter = 0

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

    def exitEdgeNode(self, ctx:TikzParser.EdgeNodeContext):
        if ctx.VARIABLE() is not None:
            coord_x = -1*self.uniquecounter
            coord_y = -1*self.uniquecounter
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
        for k in self.currentEdgeNode.keys():
            if first_node_seen:
                node1 = self.currentEdgeNode[k]
                x1 = k[0]
                y1 = k[1]
                first_node_seen = False
                continue
            node2 = self.currentEdgeNode[k]
            x2 = k[0]
            y2 = k[1]
            self.G.addEdge(node1,node2,x1,y1,x2,y2)
            node1,x1,y1 = node2,x2,y2

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