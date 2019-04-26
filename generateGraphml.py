import re
import sys
import math
import pyyed
import logging
import numpy as np
import networkx as nx
import xml.dom.minidom
from pprint import pformat
from matplotlib import colors
from pylatexenc.latex2text import LatexNodes2Text

logger = logging.getLogger(__name__)

class Graph:
	def __init__(self, scalingFactor:float):
		self.scalingFactor = scalingFactor
		self.G = pyyed.Graph()
		self.numNodes = 0
		self.numEdges = 0
		self.maxScaleFactor = 1.0
		self.nodes = []
		self.edges = []
		self.globalProperties = {}

	def rotateCoordinates(self, coordinates, angle):
		cosA = round(math.cos(math.radians(float(angle))), 10)
		sinA = round(math.sin(math.radians(float(angle))), 10)
		for index, val in enumerate(coordinates):
			x, y = val[0], val[1]
			coordinates[index][0] =  x * cosA + y * sinA
			coordinates[index][1] =  -1 * x * sinA + y * cosA

	def rescaleCoordinates(self, coordinates, scale):
		return nx.rescale_layout(coordinates, scale)

	def rescaleCoordinate(self, X, Y, scale):
		coordinates = np.array([[X, Y]])
		print(nx.rescale_layout(coordinates, scale))

	def getScalingFactor(self, minDistance):
		return self.maxScaleFactor * minDistance * self.scalingFactor
		# return self.maxScaleFactor * size * (3 - 2 * minDistance) * self.scalingFactor

	def getColor(self, fill):
		m = re.search('^\s*([a-zA-Z]+)(?:!(\d+))?\s*$', fill)
		if fill == "none" or not m:
			clr = colors.to_hex(colors.to_rgba('black', alpha=80/256.0), keep_alpha=True)
		else:
			if m.group(2) is not None:
				alpha = float(m.group(2))
				clr = colors.to_hex(colors.to_rgba(m.group(1), alpha=alpha/256.0), keep_alpha=True)
			else:
				clr = colors.to_hex(colors.to_rgba(m.group(1)), keep_alpha=False)

		return clr

	def addNode(self, nodeID:str = None, X:str = "0", Y:str = "0", label:str = None,
		height:str = "-", width:str = "-", inner_sep:str = "2.5pt", fill:str = "none", edge_color:str = "black",
		scale:str = ".8", shape:str = "ellipse", regular_polygon_sides:str="0", rotate:str="0"):

		if rotate != "0":
			pass
			rotate = float(rotate)
			x = float(X)
			y = float(Y)
			cosA = round(math.cos(math.radians(rotate)), 10)
			sinA = round(math.sin(math.radians(rotate)), 10)
			X = x * cosA + y * sinA
			Y = -1 * x * sinA + y * cosA

		clr = self.getColor(fill)

		if nodeID is None:
			nodeID = str(self.numNodes)

		self.numNodes += 1

		if label is not None:
			label = LatexNodes2Text().latex_to_text(label)

		self.maxScaleFactor = max(self.maxScaleFactor, float(scale))

		m = re.search('^\s*(\d*[.]?\d*)\s*(?:pt)?\s*$', inner_sep)
		if m and len(m.group(1)) > 0 and m.group(1) != ".":
			inner_sep = 2 * float(m.group(1))

		if shape == "circle" or shape is None:
			shape = "ellipse"

		if shape == "regular polygon":
			if float(regular_polygon_sides) not in [4, 6, 8]:
				shape = "ellipse"
			elif float(regular_polygon_sides) ==4:
				shape = "parallelogram"
			elif float(regular_polygon_sides) ==6:
				shape = "hexagon"
			elif float(regular_polygon_sides) ==8:
				shape = "octagon"

		node = {
			"nodeID": nodeID,
			"shape": shape,
			"label": label,
			"X": float(X),
			"Y": float(Y),
			"shape_fill": clr,
			"edge_color": clr,
			"height": height if height != '-' else inner_sep,
			"width": width if width != '-' else inner_sep,
			"edge_width": "1.0",
		}

		# logger.debug("Adding Node to Graph : \n{}".format(pformat(node)))
		self.nodes.append(node)
		return nodeID

	def addEdge(self, nodeX:str=None, nodeY:str=None, pointed:bool=False, color:str="black", width:str="1", label:str="", line_type:str="line"):
		# TODO: Add exception handling when NodeID is referenced without declaring it
		
		if line_type == "solid":
			line_type="line"
		if line_type == "dash":
			line_type="dashed"


		arrowDir = "none"
		if pointed:
			arrowDir = "standard"
		self.edges.append({
			"x": nodeX,
			"y": nodeY,
			"arrowhead": arrowDir,
			"color" : color,
			"width" : width,
			"label" : label,
			"line_type" : line_type
		})


	def get_graph(self):
		positions = np.empty((0,2))

		minDis = sys.float_info.max
		sz = len(self.nodes)

		for i in range(0, sz-1, 1):
			for j in range(i+1, sz, 1):
				dis = (self.nodes[i]["X"]-self.nodes[j]["X"])**2 + (self.nodes[i]["Y"]-self.nodes[j]["Y"])**2
				if dis == 0.0:
					continue
				minDis = min(minDis, dis)

		for node in self.nodes:
			positions = np.append(positions, [[node["X"], node["Y"]]], axis=0)

		if "rotate" in self.globalProperties:
			self.rotateCoordinates(positions, self.globalProperties["rotate"])

		#TODO find proper function to find scaling factor using inner_sep, min_distance, scale
		self.rescaleCoordinates(positions, self.getScalingFactor(minDis))


		for i, node in enumerate(self.nodes):
			self.G.add_node(
				node["nodeID"],
				shape=node["shape"],
				label=node["label"],
				# yed hax axis inverted to TiKZ
				# We need to reflect coordinates across X axis to get correct graph
				x=str(positions[i][0]),
				y=str(positions[i][1]*(-1)),
				shape_fill=node["shape_fill"],
				edge_color=node["edge_color"],
				height=str(node["height"] * 10),
				width=str(node["width"] * 10),
				font_size=str(int(node["height"]*9)),
				edge_width=node["edge_width"]
			)

		for edge in self.edges:
			self.G.add_edge(
				edge["x"],
				edge["y"],
				arrowhead=edge["arrowhead"],
				color=edge["color"],
				width=edge["width"],
				label=edge["label"],
				line_type=edge["line_type"]
			)

		dom = xml.dom.minidom.parseString(self.G.get_graph())
		return dom.toprettyxml()
