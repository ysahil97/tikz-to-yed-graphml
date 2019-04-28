import os
import sys
import antlr4
import logging
import argparse
from grammar.TikzLexer import TikzLexer
from grammar.TikzParser import TikzParser
from grammar.TikzListener import TikzListener
from TikzErrorListener import TikzErrorListener
from CustomTikzListener import CustomTikzListener
from extradeCodeInsideTikzAndUnrollForeach import getCodeInsideTIKZAfterUnrolling

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-1s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)

class ParseTikz:
    def printContents(self,value):
        for i, line in enumerate(value.split('\n')):
            print(i+1, ": ", line)

    def run(self,scalingFactor, logLevel, inputFilename, prefix, directory):

        if not prefix:
            prefix = inputFilename

        for value in getCodeInsideTIKZAfterUnrolling(inputFilename):
            logger.info("\n\n===================================\n\n")
            self.printContents(value)
            logger.info("\n\n===================================\n\n")
            input_stream = antlr4.InputStream(value)
            lexer = TikzLexer(input_stream)
            stream = antlr4.CommonTokenStream(lexer)
            parser = TikzParser(stream)
            parser.addErrorListener(TikzErrorListener())
            tree = parser.begin()

            # we save file as filename_t_{n}_graph.graphml
            j = 0
            while(os.path.exists(directory +"/" + prefix + "_" + str(j) + "_graph.graphml")):
                j += 1
            outputFilename = directory +"/" + prefix + "_" + str(j) + "_graph.graphml"
            htmlChat = CustomTikzListener(inputFilename, outputFilename, scalingFactor)
            walker = antlr4.ParseTreeWalker()
            walker.walk(htmlChat, tree)
