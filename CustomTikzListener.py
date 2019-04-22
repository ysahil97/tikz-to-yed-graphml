import sys
import logging
from antlr4 import *
from grammar.TikzListener import TikzListener
from grammar.TikzParser import TikzParser
from generateGraphml import Graph

class CustomTikzListener(TikzListener) :
    def __init__(self, inputFileName:str, outputFileName:str):
        self.nodes = []
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
        self.G.addNode(
            ctx.nodeID().id,
            ctx.coordinates().x,
            ctx.coordinates().y,
            label=ctx.label().label
        )

    def exitNodeID(self, ctx:TikzParser.NodeIDContext):
        if ctx.ID() is not None:
            ctx.id = ctx.ID().getText()
        else:
            ctx.id = None

    def exitCoordinates(self, ctx:TikzParser.CoordinatesContext):
        x = ctx.DIGIT(0).getText()
        y = ctx.DIGIT(1).getText()
        ctx.x = x
        ctx.y = y

    def exitLabel(self, ctx:TikzParser.LabelContext):
        if ctx.ID() is not None:
            ctx.label = ctx.ID().getText()
        else:
            ctx.label = ""