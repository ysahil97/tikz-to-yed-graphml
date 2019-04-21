import sys
import antlr4
from grammar.TikzLexer import TikzLexer
from grammar.TikzListener import TikzListener
from grammar.TikzParser import TikzParser
from CustomTikzListener import CustomTikzListener

def main():
    fileName = './TestCases/graph.tex'
    input_stream = antlr4.FileStream(fileName)
    lexer = TikzLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = TikzParser(stream)
    tree = parser.begin()

    htmlChat = CustomTikzListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(htmlChat, tree)


if __name__ == '__main__':
    main()

