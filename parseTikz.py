import sys
import antlr4
import logging
import os
from grammar.TikzLexer import TikzLexer
from grammar.TikzParser import TikzParser
from grammar.TikzListener import TikzListener
from CustomTikzListener import CustomTikzListener
from extradeCodeInsideTikzAndUnrollForeach import getCodeInsideTIKZAfterUnrolling
import argparse

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-1s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main(scalingFactor, logLevel, inputFilename, prefix, directory):
    
    if not prefix:
        prefix = inputFilename

    for value in getCodeInsideTIKZAfterUnrolling(directory, inputFilename):
        logger.info("===================================")
        logger.info("\n\n" + value + "\n\n")
        logger.info("===================================")
        input_stream = antlr4.InputStream(value)
        lexer = TikzLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = TikzParser(stream)
        tree = parser.begin()

        # we save file as filename_t_{n}_graph.graphml
        j = 0
        while(os.path.exists(directory +"/" + prefix + "_" + str(j) + "_graph.graphml")):
            j+=1
        outputFilename = directory +"/" + prefix + "_" + str(j) + "_graph.graphml"
        htmlChat = CustomTikzListener(inputFilename, outputFilename, scalingFactor)
        walker = antlr4.ParseTreeWalker()
        walker.walk(htmlChat, tree)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("-h", "--help", type=int, help="Print this menu")
    parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity", default=0)
    parser.add_argument("-s", "--scale", type=float, help="Scaling Factor", default=200)
    parser.add_argument("-i", "--input", type=str, help="Input file name")
    parser.add_argument("-p", "--prefix", type=str, help="Output file Prefix")
    parser.add_argument("-d", "--directory", type=str, help="Output file directory")

    args = parser.parse_args()

    scalingFactor = args.scale
    logLevel = args.scale
    inputFileName = args.input
    prefix = args.prefix
    directory = "./"
    if args.directory:
        directory=args.directory

    main(scalingFactor, logLevel, inputFileName, prefix, directory)

