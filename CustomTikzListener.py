import sys
from antlr4 import *
from grammar.TikzListener import TikzListener
from grammar.TikzParser import TikzParser

class CustomTikzListener(TikzListener) :
    def __init__(self):
        self.nodes = []
    
    def exitNode(self, ctx:TikzParser.NodeContext):
        print("NodeID: ", ctx.nodeID().text)
        print("coordinates: ", ctx.coordinates().x, ctx.coordinates().y)
        print("label: ", ctx.label())

    def exitNodeID(self, ctx:TikzParser.NodeIDContext):
        id = ctx.ID().getText()
        ctx.text = id

    def exitCoordinates(self, ctx:TikzParser.CoordinatesContext):
        x = ctx.DIGIT(0).getText()
        y = ctx.DIGIT(1).getText()
        ctx.x = x
        ctx.y = y