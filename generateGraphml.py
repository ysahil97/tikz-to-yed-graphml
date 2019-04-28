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
		self.default_fontSize = str(int(2.5*self.scalingFactor))

	def rotateCoordinates(self, coordinates, angle):
		cosA = round(math.cos(math.radians(float(angle))), 10)
		sinA = round(math.sin(math.radians(float(angle))), 10)
		for index, val in enumerate(coordinates):
			x, y = val[0], val[1]
			coordinates[index][0] =  x * cosA + y * sinA
			coordinates[index][1] =  (-1 * x * sinA + y * cosA)*-1

	def rescaleCoordinates(self, coordinates, scale):
		for index, val in enumerate(coordinates):
			coordinates[index] = [float(val[0]) * scale, float(val[1]) * scale]

	def rescaleCoordinate(self, X, Y, scale):
		coordinates = np.array([[X, Y]])
		return (nx.rescale_layout(coordinates, scale))

	def getScalingFactor(self, minDistance):
		# return self.maxScaleFactor * minDistance * self.scalingFactor
		return self.maxScaleFactor * (3 - 2 * minDistance) * self.scalingFactor

	def getColor(self, fill):
		if fill is None or fill == "none":
			return None

		m = re.search('^\s*([a-zA-Z]+)(?:!(\d+))?\s*$', fill)
		if not m:
			clr = None 	#stands for no color / transparent
		else:
			if m.group(2) is not None:
				alpha = float(m.group(2))
				clr = colors.to_hex(colors.to_rgba(m.group(1), alpha=alpha/256.0), keep_alpha=True)
			else:
				clr = colors.to_hex(colors.to_rgba(m.group(1)), keep_alpha=False)

		return clr

	def addNode(self, nodeID:str = None, X:str = "0", Y:str = "0", label:str = None,
		height:str = "-", width:str = "-", inner_sep:str = "3.3333pt", fill:str = "none", edge_color:str = None,
		scale:str = "1", shape:str = "ellipse", regular_polygon_sides:str="0", rotate:str="0", auto:str="center"):


		if rotate != "0":
			pass
			rotate = float(rotate)
			x = float(X)
			y = float(Y)
			cosA = round(math.cos(math.radians(rotate)), 10)
			sinA = round(math.sin(math.radians(rotate)), 10)
			X = x * cosA + y * sinA
			Y = (-1 * x * sinA + y * cosA) * -1

		fillClr = self.getColor(fill)
		edgeClr = self.getColor(edge_color)
		

		if nodeID is None:
			nodeID = str(self.numNodes)

		self.numNodes += 1

		if label is not None:
			label = LatexNodes2Text().latex_to_text(label)

		# self.maxScaleFactor = max(self.maxScaleFactor, float(scale)*100)
		# if scale != "1":
		# 	self.rescaleCoordinate(X, Y, float(scale))

		if inner_sep.__contains__("cm"):
			inner_sep *= 28.3465
			pass
		else:
			m = re.search('^\s*([0-9/*-+.]+)\s*(?:pt|cm)?\s*$', inner_sep)
			if m and len(m.group(1)) > 0 and m.group(1) != ".":
				inner_sep = float(m.group(1))

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
			"X": float(X) * 28.3465, # Converting Xpt to Xcm so factor of 28.3465 involved
			"Y": float(Y) * 28.3465, # Converting Xpt to Xcm so factor of 28.3465 involved
			"shape_fill": fillClr,
			"edge_color": edgeClr,
			"height": height if height != '-' else inner_sep ,
			"width": width if width != '-' else inner_sep,
			"edge_width": "1.0",
		}

		logger.debug("Adding Node to Graph : \n{}".format(pformat(node)))
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

		sz = len(self.nodes)

		if sz == 0:
			logger.warn("No Nodes are present in the graph. Printing Empty GraphML graph.")
			return ""

		positions = np.empty((0,2))

		# minDis = sys.float_info.max
		# rescaleFactor = sys.float_info.max
		# maxDistance = 0
		# for i in range(0, sz-1, 1):
		# 	for j in range(i+1, sz, 1):
		# 		aa = 0
		# 		dis = (self.nodes[i]["X"]-self.nodes[j]["X"])**2 + (self.nodes[i]["Y"]-self.nodes[j]["Y"])**2 
		# 		if dis == 0.0:
		# 			continue
		# 		sumofNodeSized = max(float(self.nodes[i]["height"]), float(self.nodes[i]["width"])) + max(float(self.nodes[j]["height"]), float(self.nodes[j]["width"]))
		# 		maxDistance = max(maxDistance, dis)
		# 		rescaleFactor = min(rescaleFactor, (2*float(sumofNodeSized)/0.0352778) / float(math.sqrt(dis)))

		
		for node in self.nodes:
			positions = np.append(positions, [[node["X"], node["Y"]]], axis=0)

		
		if "rotate" in self.globalProperties:
			logger.debug("Rotating Coordinates by {}".format(self.globalProperties["rotate"]))
			self.rotateCoordinates(positions, self.globalProperties["rotate"])

		nx.rescale_layout(positions, 23.4) # 23.4 is width of PDF

		for i, node in enumerate(self.nodes):
			self.G.add_node(
				node["nodeID"],
				shape=node["shape"],
				label=node["label"],
				# yed hax axis inverted to TiKZ
				# We need to reflect coordinates across X axis to get correct graph
				x=str(positions[i][0] * 4*self.scalingFactor),
				y=str(positions[i][1] * -4*self.scalingFactor),
				shape_fill=node["shape_fill"],
				edge_color=node["edge_color"],
				height=str(node["height"] * self.scalingFactor),
				width=str(node["width"]* self.scalingFactor),
				font_size=self.default_fontSize,
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
