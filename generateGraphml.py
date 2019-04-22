import re
import sys
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
	def __init__(self):
		self.G = pyyed.Graph()
		self.numNodes = 0
		self.numEdges = 0
		self.maxScaleFactor = 1.0
		self.nodes = []
		self.edges = []

	def rescaleCoordinates(self, coordinates, scale):
		return nx.rescale_layout(coordinates, scale)

	def rescaleCoordinate(self, X, Y, scale):
		coordinates = np.array([[X, Y]])
		print(nx.rescale_layout(coordinates, scale))

	def getScalingFactor(self, size, minDistance):
		return self.maxScaleFactor * size * (3 - 2 * minDistance) * 5
	
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


	def addShape(self, nodeID, X, Y, height, width, label=None, fill="white", edge_color="black", shape="ellipse"):

		fill_clr = self.getColor(fill)
		edge_clr = self.getColor(edge_color)

		if nodeID is None:
			nodeID = str(self.numNodes)

		self.numNodes += 1

		print("")

		self.nodes.append({
			"nodeID": nodeID,
			"shape": shape,
			"label": label,
			"X": X,
			"Y": Y,
			"shape_fill": fill_clr,
			"edge_color": edge_clr,
			"height": height,
			"width": width,
			"edge_width": "1.0"
		})

	def addNode(self, nodeID:str, X:str, Y:str, label:str = None, inner_sep:str = "2.5pt", fill:str = "none", scale:str = ".8", shape:str = "ellipse"):
		clr = self.getColor(fill)

		if nodeID is None:
			nodeID = str(self.numNodes)

		self.numNodes += 1

		if shape == "circle":
			shape = "ellipse"

		if label is not None:
			label = LatexNodes2Text().latex_to_text(label)

		self.maxScaleFactor = max(self.maxScaleFactor, float(scale))

		m = re.search('^\s*(\d*[.]?\d*)\s*(?:pt)?\s*$', inner_sep)
		if m and len(m.group(1)) > 0 and m.group(1) != ".":
			inner_sep = 2 * float(m.group(1))

		node = {
			"nodeID": nodeID,
			"shape": shape,
			"label": label,
			"X": float(X),
			"Y": float(Y),
			"shape_fill": clr,
			"edge_color": clr,
			"height": inner_sep,
			"width": inner_sep,
			"edge_width": "1.0"
		}

		logger.debug("Adding NODE to Graph : \n{}".format(pformat(node)))
		self.nodes.append(node)

	def addEdge(self, nodeX, nodeY):
		self.edges.append({
			"x": nodeX,
			"y": nodeY
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

		#TODO find proper function to find scaling factor using inner_sep, min_distance, scale
		self.rescaleCoordinates(positions, self.getScalingFactor(node["height"], minDis))
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
				edge["y"]
			)

		dom = xml.dom.minidom.parseString(self.G.get_graph())
		return dom.toprettyxml()
