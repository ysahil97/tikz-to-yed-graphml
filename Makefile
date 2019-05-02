CLASSPATH	?=	/usr/local/lib/antlr-4.7.2-complete.jar
antlr4		:= java -Xmx500M -cp "/usr/local/lib/antlr-4.7.2-complete.jar:${CLASSPATH}" org.antlr.v4.Tool

all: clean grammar test

grammar:
	${antlr4} -Dlanguage=Python3 tikz2graphml/grammar/Tikz.g4

test:
	rm -f output/*.graphml
	python3 -m unittest discover test

sample-test:
	python3 tikz2graphml/__main__.py -i TestCases/valid-graphs/tex/TestCaseForShape.tex -s 200 -d ./TestCases

clean:
	cd tikz2graphml/grammar; ls | grep -vE '*.g4|__pycache__' | xargs rm -f;
	rm -f TestCases/*.graphml
	rm -f output/*.graphml

removeGraphs:
	rm -f TestCases/*.graphml
	rm -f output/*.graphml

.PHONY: test clean grammar
