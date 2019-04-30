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

logging.basicConfig(format='%(levelname)-1s : [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def printContents(value):
    print ("===================================\n")
    for i, line in enumerate(value.split('\n')):
        print(i+1, ": ", line)
    print ("===================================\n")

def main(scalingFactor, logLevel, inputFilename, prefix, directory):
    if not prefix:
        prefix = inputFilename
    logging.debug("Unrolling For loops")
    for value in getCodeInsideTIKZAfterUnrolling(inputFilename):
        logging.debug("Unrolling Done")
        printContents(value)
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("-h", "--help", type=int, help="Print this menu")
    parser.add_argument("-D", "--debug", help="debug output", action="store_const", const=logging.DEBUG, default=logging.INFO)
    parser.add_argument("-s", "--scale", type=float, help="Scaling Factor", default=100)
    parser.add_argument("-i", "--input", type=str, help="Input file path")
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

    if args.input is None:
        logger.error("Please provide Input file")
        sys.exit(1)

    main(scalingFactor, logLevel, inputFileName, prefix, directory)

