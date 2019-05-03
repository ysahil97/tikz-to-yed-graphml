
# Tikz2GraphML: P2 File conversion

[![CircleCI](https://circleci.com/gh/ysahil97/tikz-to-yed-graphml/tree/master.svg?style=svg)](https://circleci.com/gh/ysahil97/tikz-to-yed-graphml/tree/master)

This README is about the description of our graph conversion software, what all constructs it can support and the current status of this software

## Aim

Develop an efficient software which can convert most of Tikz Graph present in Latex code in GraphML format.

## Requirements

This software requires following pyhton packages
- colour==0.1.5
- numpy==1.16.2
- networkx==2.3
- matplotlib==3.0.3
- pylatexenc==1.4
- antlr4-python3-runtime==4.7.2

Python Version 3.7.0

## Installation

```bash
 sudo apt-get install python3-tk python3-pip
(sudo) pip3 install tikz2graphml
```
## GUI

![alt text][GUI]

[GUI]: https://github.com/ysahil97/tikz-to-yed-graphml/blob/master/Screenshots/GUI.png "GUI-Image"



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

```TeX
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

![alt text][Sample Output]

[Sample Output]: https://github.com/ysahil97/tikz-to-yed-graphml/blob/master/Screenshots/SampleOutput.png "Sample Output"

## Generation of GraphML file

For the sake of cleanliness, each Tikz Block is analyzed separately to generate different GraphML files pertaining to each Tikz Block.

In addition to this, proper scaling of nodes is introduced in the software automatically in order to show graphs properly in GraphML. Nevertheless, the user does have a control in scaling by providing a scaling parameter

## Current Status of the software

* All the possible Tikz constructs are handled efficiently with the consideration of all the possible test-cases(invalid and valid test cases included)
* The tool has been installed as a [pip library](https://pypi.org/project/tikz2graphml/)
* It works cross-platform(both Linux and Windows)
* The original aim was to make it a command line tool. But in addition to this, we have also added a GUI interface which can take in input file and scaling parameter and output the corresponding GraphML file.

-------

###### Part of our CS4443: Software Engineering Project component offered in Spring 2019
