import argparse
from parseTikz import ParseTikz

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("-h", "--help", type=int, help="Print this menu")
    parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity", default=0)
    parser.add_argument("-s", "--scale", type=float, help="Scaling Factor", default=200)
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

    Tikz_parse = ParseTikz()
    Tikz_parse.run(scalingFactor, logLevel, inputFileName, prefix, directory)