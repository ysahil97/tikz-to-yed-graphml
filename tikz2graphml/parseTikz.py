# from tikz2graphml import grammar
# from tikz2graphml import pyyed

import os
import antlr4
import logging
from tikz2graphml.grammar.TikzLexer import TikzLexer
from tikz2graphml.grammar.TikzParser import TikzParser
from tikz2graphml.TikzErrorListener import TikzErrorListener
from tikz2graphml.CustomTikzListener import CustomTikzListener
from tikz2graphml.extradeCodeInsideTikzAndUnrollForeach import getCodeInsideTIKZAfterUnrolling

logging.basicConfig(format='%(levelname)-1s : [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class ParseTikz:
    def printContents(self, value):
        print("===================================\n")
        for i, line in enumerate(value.split('\n')):
            print(i+1, ": ", line)
        print("===================================\n")

    def run(self, scalingFactor: float, logLevel: int, inputFilename: str, prefix: str, directory: str):

        if not prefix:
            prefix = os.path.basename(inputFilename)

        if not os.path.exists(directory):
            os.makedirs(directory)

        for value in getCodeInsideTIKZAfterUnrolling(inputFilename):
            self.printContents(value)
            input_stream = antlr4.InputStream(value)
            lexer = TikzLexer(input_stream)
            stream = antlr4.CommonTokenStream(lexer)
            parser = TikzParser(stream)
            parser.addErrorListener(TikzErrorListener())
            tree = parser.begin()

            # we save file as filename_t_{n}_graph.graphml
            # Getting next available output file path
            j = 0
            while(os.path.exists(directory + "/" + prefix + "_" + str(j) + "_graph.graphml")):
                j += 1
            outputFilename = directory + "/" + prefix + "_" + str(j) + "_graph.graphml"
            htmlChat = CustomTikzListener(inputFilename, outputFilename, scalingFactor)
            walker = antlr4.ParseTreeWalker()
            walker.walk(htmlChat, tree)
