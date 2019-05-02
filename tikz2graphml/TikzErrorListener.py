from antlr4.error.ErrorListener import ErrorListener


class TikzErrorListener(ErrorListener):

    def __init__(self):
        super(TikzErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("""\n\nSyntax Error in/around the following line. :
            \n\tLine Number : {}
            \n\tColumn : {}
            \n\tOffending Symbol : {}
            \n\tMessage : {}
            \n\tP.S. Look at text just before the offending symbol.\n\n""".format(line, column, offendingSymbol.text, msg))