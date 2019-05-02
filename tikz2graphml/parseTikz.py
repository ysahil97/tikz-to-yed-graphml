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

logger = logging.getLogger()

"""
Higher level class to handle conversion of Tikz graph to GraphML format
"""
class ParseTikz:
    def printContents(self, value):
        print("===================================\n")
        for i, line in enumerate(value.split('\n')):
            print(i+1, ": ", line)
        print("===================================\n")

    """
    Main conversion function
    Arguments:-
    scalingFactor:  scale value provided by the user to make graph look reasonable
    logLevel: Toggle verbosity
    inputFilename: path of the input Tikz File
    directory: path of the output directory to save the generated GraphML file
    """
    def run(self, scalingFactor: float, inputFilename: str, prefix: str, directory: str):

        if not prefix:
            prefix = os.path.basename(os.path.splitext(prefix)[0])

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
