import re
import pyyed
import numpy as np
import networkx as nx
import xml.dom.minidom
from matplotlib import colors
from pylatexenc.latex2text import LatexNodes2Text

class Graph:
	def __init__(self):
		self.G = pyyed.Graph()
		self.numNodes = 0
		self.numEdges = 0
		self.scalingFactor = 1.0
		self.nodes = []

	def rescaleCoordinates(self, coordinates, scale):
		return nx.rescale_layout(coordinates, scale)

	def rescaleCoordinate(self, X, Y, scale):
		coordinates = np.array([[X, Y]])
		print(nx.rescale_layout(coordinates, scale))

	def getScalingFactor(self, scale=".8", inner_sep="1pt"):
		scalingFactor = 1.0
		m = re.search('^\s*(\d*[.]?\d*)\s*(?:pt)?\s*$', inner_sep)
		if m and len(m.group(1)) > 0 and m.group(1) != ".":
			scalingFactor *= float(m.group(1))

		scalingFactor *= float(scale) * 50 * 2
		return scalingFactor

	def addNode(self, nodeID, X, Y, label=None, inner_sep="1pt", fill="none", scale=".8", shape="ellipse"):
		m = re.search('^\s*([a-zA-Z]+)(?:!(\d+))?\s*$', fill)
		if fill == "none" or not m:
			clr = colors.to_hex(colors.to_rgba('black', alpha=80/256.0), keep_alpha=True)
		else:
			if m.group(2) is not None:
				alpha = float(m.group(2))
				clr = colors.to_hex(colors.to_rgba(m.group(1), alpha=alpha/256.0), keep_alpha=True)
			else:
				clr = colors.to_hex(colors.to_rgba(m.group(1)), keep_alpha=False)

		self.scalingFactor = max(self.scalingFactor, self.getScalingFactor(scale, inner_sep))

		if nodeID is None:
			nodeID = str(self.numNodes)

		self.numNodes += 1

		if shape == "circle":
			shape = "ellipse"

		if label is not None:
			label = LatexNodes2Text().latex_to_text(label)

		self.nodes.append({
			"nodeID": nodeID,
			"shape": shape,
			"label": label,
			"X": float(X),
			"Y": float(Y),
			"shape_fill": clr,
			"edge_color": clr,
			"height": float(scale),
			"width": float(scale),
			"edge_width": "1.0"
		})

	def get_graph(self):
		positions = np.empty((0,2))
		for node in self.nodes:
			positions = np.append(positions, [[node["X"], node["Y"]]], axis=0)

		pos = self.rescaleCoordinates(positions, self.scalingFactor)
		for i, node in enumerate(self.nodes):
			self.G.add_node(
				node["nodeID"],
				shape=node["shape"],
				label=node["label"],
				x=str(pos[i][0]),
				y=str(pos[i][1]),
				shape_fill=node["shape_fill"],
				edge_color=node["edge_color"],
				height=str(node["height"] * 20),
				width=str(node["width"] * 20),
				font_size=str(int(node["height"]*10)),
				edge_width=node["edge_width"]
			)

		dom = xml.dom.minidom.parseString(self.G.get_graph())
		return dom.toprettyxml()