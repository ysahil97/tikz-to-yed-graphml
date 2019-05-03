# Tikz2GraphML: P2 File conversion
[![CircleCI](https://circleci.com/gh/ysahil97/tikz-to-yed-graphml/tree/master.svg?style=svg)](https://circleci.com/gh/ysahil97/tikz-to-yed-graphml/tree/master)


This README is about the description of our graph conversion software, what all constructs it can support and the current status of this software


## Aim

Develop an efficient software which can convert every possible Tikz Graph present in Latex code in GraphML format.

## Requirements

This software supportes Python>=3.7.0

## Installation

```
sudo apt-get install python3-tk python3-pip
pip3 install tikz2graphml
```

## Tikz Constructs Supported

We have handled these Tikz Constructs
* Node
	* Shapes: Circle, Ellipse, Rectangle, Diamond
	* Size
	* Color
	* NodeID
	* Label
	* Edge Color
* Edge
	* Width
	* Edge arrows: `->`, `<->`,`<-`,`-!-`
* Coordinates
	* Polar: (Angle, r (in cm))
	* Cartesian: (a,b)
* Rotation of the Entire Graph
* Handling Loop constructs(Foreach)
* Global properties(applied to each tikz construct)

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
