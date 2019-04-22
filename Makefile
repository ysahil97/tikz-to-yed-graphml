CLASSPATH ?= /usr/local/lib/antlr-4.7.2-complete.jar
antlr4=java -Xmx500M -cp "/usr/local/lib/antlr-4.7.2-complete.jar:${CLASSPATH}" org.antlr.v4.Tool

all: grammar test

grammar:
	${antlr4} -Dlanguage=Python3 grammar/Tikz.g4

test:
	python3 parseTikz.py

clean:
	cd grammar; ls | grep -vE '*.g4|__pycache__' | xargs rm;

.PHONY: test clean grammar