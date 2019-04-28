CLASSPATH	?=	/usr/local/lib/antlr-4.7.2-complete.jar
antlr4		:= java -Xmx500M -cp "/usr/local/lib/antlr-4.7.2-complete.jar:${CLASSPATH}" org.antlr.v4.Tool

all: clean grammar test

grammar:
	${antlr4} -Dlanguage=Python3 grammar/Tikz.g4

test:
	python3 parseTikz.py -i draw.tex -s 300 -d ./TestCases/

clean:
	cd grammar; ls | grep -vE '*.g4|__pycache__' | xargs rm;
	rm -rf TestCases/*.graphml

.PHONY: test clean grammar
