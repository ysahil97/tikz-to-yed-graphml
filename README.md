
# Tikz2GraphML: P2 File conversion

[![CircleCI](https://circleci.com/gh/ysahil97/tikz-to-yed-graphml/tree/master.svg?style=svg)](https://circleci.com/gh/ysahil97/tikz-to-yed-graphml/tree/master)

**tikz2graphml** is TikZ (tex) to Graphml convertor which can be viewed in yEd software. It allows you to select the tex file (with TikZ code) and writes corresponding graphml file in the output directory. For the sake of cleanliness, each Tikz Block is analyzed separately to generate different GraphML files. tikz2graphml works on Linux and Windows. It can be used from commandline as well as GUI. tikz2graphml is very simple to use, powerful and supports many TikZ constructs. It also lets you scale the coordinates in graphml for better visualization of graphml in yEd.


## Requirements
> Python Version 3.7.0

This software requires following Python packages
* colour==0.1.5
* numpy==1.16.2
* networkx==2.3
* matplotlib==3.0.3
* pylatexenc==1.4
* antlr4-python3-runtime==4.7.2


## Installation

### Ubuntu
```bash
> sudo apt-get install python3-tk python3-pip
> (sudo) pip3 install tikz2graphml
> tikz2graphml
```
### Windows

* [Python3 Installation](docs/Python3_windows.md)
* [Pip Installation](docs/Pip_windows.md)
* Open Command Line from Windows
* Use this command


```
pip install tikz2graphml  
tikz2graphml
```

## GUI

![GUI Screenshot][GUI]

[GUI]: https://github.com/ysahil97/tikz-to-yed-graphml/blob/master/GUI.png "GUI-Image"



## Tikz Constructs Supported

We have handled these Tikz Constructs
* Node
* Shapes: Circle, Ellipse, Rectangle, Diamond
* Size
* Color
* NodeID
* Label
* Edge Color
* Lable
* Edge
* Width
* Edge arrows: `->`, `<->`,`<-`,`-!-`
* Coordinates
* Polar: (Angle, r (in cm))
* Cartesian: (x,y)
* Rotation of the Entire Graph
* Handling Loop constructs(Foreach)
* Global properties(applied to each tikz construct)

## Examples

Sample TikZ code

```
\begin{tikzpicture}
    \draw (6,6) ellipse (3cm and 6cm);
    \draw (6,6) ellipse (2.5cm and 5cm);
    \draw (6,6) ellipse (2cm and 4cm);
    \draw (6,6) ellipse (1.5cm and 3cm);
    \draw (6,6) ellipse (1cm and 2cm);
    \draw (0,12) rectangle (12,0);
    \node (a) [fill=green, shape=diamond] at (0,6) {};
    \node (b) [fill=blue] at (12,6) {};
    \node (c) [fill=red] at (6,0) {};
    \node (d) [fill=black] at (6,12) {};
    \draw (6,6) circle (6cm);
    \draw [<->] (a) -- (b);
    \draw [->] (d) -- (c);
    \draw (6,6) ellipse (6cm and 2cm);
    \draw (6,6) ellipse (6cm and 6cm);
    \draw (6,6) ellipse (6cm and 5cm);
    \draw (6,6) ellipse (6cm and 4cm);
    \draw (6,6) ellipse (6cm and 3cm);
\end{tikzpicture}
```
GraphML output in yEd

![Sample Output][Sample Output]

[Sample Output]: https://github.com/ysahil97/tikz-to-yed-graphml/blob/master/SampleOutput.png "Sample Output"

## Generation of GraphML file (Design)


Conversion Process

* Read Input (tex file)
* Detect TikZ code in File. If multiple TikZ block found, store them in list.
* For each TikZ block detected above, do following
	* Detect Foreach Instruction and [Unroll](https://www.geeksforgeeks.org/loop-unrolling/) it.
	* Parse File using [this grammar](https://github.com/ysahil97/tikz-to-yed-graphml/blob/master/tikz2graphml/grammar/Tikz.g4) with Antlr4 tool
	* For each rule in Antlr grammar, we add corresponding rules which detects and store the properties of instruction in either of node or edge list [TikZAntlrListener](https://github.com/ysahil97/tikz-to-yed-graphml/blob/master/tikz2graphml/CustomTikzListener.py)
	* Once parsing is done. We call get_graph which first rotates the graph (if rotate property is there) and then add the nodes and edges to pyyed graph.
	* We get the XML output from pyyed (using pyyed.graph.get_graph()) and write it in *.graphml file.


## Current Status of the software

* All the possible Tikz constructs are handled efficiently with the consideration of all the possible test-cases(invalid and valid test cases included)
* The tool has been installed as a [pip library](https://pypi.org/project/tikz2graphml/)
* It works cross-platform(both Linux and Windows)
* The original aim was to make it a command line tool. But in addition to this, we have also added a GUI interface which can take in input file and scaling parameter and output the corresponding GraphML file.