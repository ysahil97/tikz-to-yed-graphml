import re
import math
import logging
import numpy as np
import networkx as nx
import xml.dom.minidom
from matplotlib import colors
import tikz2graphml.pyyed as pyyed
from pylatexenc.latex2text import LatexNodes2Text

logger = logging.getLogger()

"""
Main Graph class storing all the properties of the edges and nodes of the graph
for a single TikZ graph code at a time
"""
class Graph:

	def __init__(self, scalingFactor: float):
		self.scalingFactor = scalingFactor
		self.G = pyyed.Graph()
		self.numNodes = 0
		self.numEdges = 0
		self.maxScaleFactor = 1.0
		self.nodes = []
		self.edges = []
		self.globalProperties = {}
		self.default_fontSize = str(int(0.20 * self.scalingFactor))
		self.defaultNodeSide = "10"

	# Rotate coordinates by a given angle(in Degrees)
	def rotateCoordinates(self, coordinates, angle):
		cosA = round(math.cos(math.radians(float(angle))), 10)
		sinA = round(math.sin(math.radians(float(angle))), 10)
		for index, val in enumerate(coordinates):
			x, y = val[0], val[1]
			coordinates[index][0] =      x * cosA + y * sinA
			coordinates[index][1] =  1 * x * sinA - y * cosA

	# Rescale coordinates by a given scale
	def rescaleCoordinates(self, coordinates, scale):
		for index, val in enumerate(coordinates):
			coordinates[index] = [float(val[0]) * scale, float(val[1]) * scale]

	# Rescale a coordinate tuple by a given scale
	def rescaleCoordinate(self, X, Y, scale):
		coordinates = np.array([[X, Y]])
		return (nx.rescale_layout(coordinates, scale))

	# Obtain scaling factor  for a given min distance
	# The formula used here is emperically tested so that it
	# works for most tikz code
	def getScalingFactor(self, minDistance):
		return self.maxScaleFactor * (3 - 2 * minDistance) * self.scalingFactor

	# Given a color string name, output it's corresponding hex-code
	def getColor(self, fill):
		if fill is None or fill == "none":
			return None
		m = re.search('^\s*([a-zA-Z]+)(?:!(\d+))?\s*$', fill)
		if not m:
			clr = None 	# stands for no color / transparent
		else:
			if m.group(2) is not None:
				alpha = float(m.group(2))
				clr = colors.to_hex(colors.to_rgba(m.group(1), alpha=alpha/256.0), keep_alpha=True)
			elif m.group(1) is not None:
				clr = colors.to_hex(colors.to_rgba(m.group(1)), keep_alpha=False)
			else:
				clr = None
		return clr

	# Helper function to add a node with its properties into the graph object
	def addNode(self, nodeID:str = None, X:str = "0", Y:str = "0", label:str = None,
		height:str = "-", width:str = "-", inner_sep:str = "", fill:str = "1", edge_color:str = None,
		scale:str = "1", shape:str = "rectangle", regular_polygon_sides:str="0", rotate:str="0", auto:str="center", transparent:bool="false"):
		if inner_sep == "":
			inner_sep = self.defaultNodeSide

		# This rotate is rotation of shape of node
		if rotate != "0":
			logger.warning("Rotation of each node cannot be done in graphml")

		fillClr = self.getColor(fill)
		edgeClr = self.getColor(edge_color)

		# When nodeID is unassigned for a given node, then the ID is generated
		# internally by incrementing the numNodes counter variable
		if nodeID is None:
			nodeID = str(self.numNodes)

		self.numNodes += 1

		# Given a label string, we convert it to text format
		# to be used in GraphML generation
		if label is not None:
			label = LatexNodes2Text().latex_to_text(label)

        # Currently the distance values for cm & pt  is handled together
		# and those without any units are handled separately
		if inner_sep.__contains__("cm"):
			m = re.search('^\s*([0-9/*-+.]+)\s*(?:pt|cm)?\s*$', inner_sep)
			if m and len(m.group(1)) > 0 and m.group(1) != ".":
				inner_sep = float(m.group(1))
		else:
			m = re.search('^\s*([0-9/*-+.]+)\s*(?:pt|cm)?\s*$', inner_sep)
			if m and len(m.group(1)) > 0 and m.group(1) != ".":
				inner_sep = max(float(m.group(1)), float(self.defaultNodeSide)) * 0.0352778

		if shape == "circle":
			shape = "ellipse"

		if shape is None:
			shape = "rectangle"

		# Creating a node dict for storing all its properties
		node = {
			"nodeID": nodeID,
			"shape": shape,
			"label": label,
			"X": float(X),
			"Y": float(Y),
			"shape_fill": fillClr,
			"edge_color": edgeClr,
			"height": height if height != '-' else inner_sep ,
			"width": width if width != '-' else inner_sep,
			"edge_width": "1.0",
			"transparent": transparent
		}
		logger.debug("Adding Node to Graph : \n{}".format(node))
		self.nodes.append(node)
		return nodeID

	# TODO: Add exception handling when NodeID is referenced without declaring it
	# Helper function to add a edge with its properties into the graph object
	def addEdge(self, nodeX:str=None, nodeY:str=None, arrowHead:bool=False, arrowFoot:bool=False, color:str="black", width:str="1", label:str="", line_type:str="line"):

		if line_type is not None and line_type == "solid":
			line_type="line"
		elif line_type is not None and line_type == "dash":
			line_type="dashed"

		# Creating a edge dict for storing all its properties
		self.edges.append({
			"x": nodeX,
			"y": nodeY,
			"arrowhead": "standard" if arrowHead==True else "none",
			"arrowfoot": "standard" if arrowFoot==True else "none",
			"color" : self.getColor(color),
			"width" : width,
			"label" : label,
			"line_type" : line_type
		})

	# Obtain a GraphML xml snippet for the existing graph object
	def get_graph(self):
		sz = len(self.nodes)
		if sz == 0:
			logger.warn("No Nodes are present in the graph. Printing Empty GraphML graph.")
			return ""
		positions = np.empty((0,2))

		for node in self.nodes:
			positions = np.append(positions, [[node["X"], node["Y"]]], axis=0)

		# Rotation handled before examining the node objects
		if "rotate" in self.globalProperties:
			logger.debug("Rotating Coordinates by {}".format(self.globalProperties["rotate"]))
			self.rotateCoordinates(positions, self.globalProperties["rotate"])


		for i, node in enumerate(self.nodes):
			"""
				addNode default Properties
				(node_name, label=None, shape="rectangle", font_family="Dialog",
                 underlined_text="false", font_style="plain", font_size="12",
                 shape_fill="#FF0000", transparent="false", edge_color="#000000",
                 edge_type="line", edge_width="1.0", height=False, width=False, x=False,
                 y=False, node_type="ShapeNode", UML=False):
			"""

			# Handling Shapes of nodes
			if node["shape"] in ["rectangle", "ellipse", "diamond"] :
				positions[i][0] = positions[i][0] - node["width"]/2.0
				# yed has axis inverted to TiKZ
				# So the formula for y is bit different than standard rotate for cartessian coordinates
				positions[i][1] = -1 * positions[i][1] - node["height"]/2.0

            # Adding all the nodes obtained from CustomTikzListener
			# into graph object
			self.G.add_node(
				node["nodeID"],
				shape=node["shape"],
				label=node["label"],
				x=str(positions[i][0]* self.scalingFactor),
				y=str(positions[i][1]* self.scalingFactor),
				shape_fill=node["shape_fill"],
				edge_color=node["edge_color"],
				height=str(node["height"]* self.scalingFactor ),
				width=str(node["width"]* self.scalingFactor),
				font_size=self.default_fontSize,
				edge_width=node["edge_width"],
				transparent=node["transparent"]
			)

        # Adding all the edge data obtained from CustomTikzListener
		# into graph object
		for edge in self.edges:
			"""
			node1, node2,
			label="", arrowhead="convex", arrowfoot="none",
            color="#000000", line_type="line", width="1.0"
			"""
			self.G.add_edge(
				edge["x"],
				edge["y"],
				arrowhead=edge["arrowhead"],
				arrowfoot=edge["arrowfoot"],
				color=edge["color"],
				width=edge["width"],
				label=edge["label"],
				line_type=edge["line_type"]
			)

		dom = xml.dom.minidom.parseString(self.G.get_graph())
		return dom.toprettyxml()
