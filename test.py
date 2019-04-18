import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colors
import sys
import math
from mpl_toolkits.mplot3d import axes3d

# \begin{center}
# \begin{tikzpicture}[scale=.8,rotate=18,auto=center,every node/.style={circle,inner sep=3pt}]
# \draw (0*360/5: 2.5cm) node[fill=blue!90]{};
# \draw (1*360/5: 2.5cm) node[fill=red!90]{};
# \draw (2*360/5: 2.5cm) node[fill=green!90]{};
# \draw (3*360/5: 2.5cm) node[fill=black!90]{};
# \draw (4*360/5: 2.5cm) node[fill=black!90]{};

# \foreach \a/\b in {0/144,0/216,72/216, 72/288,144/288}{
# \draw (\a: 2.5cm) -- (\b: 2.5cm);}

# \draw (0*360/5: 3.5cm) node[fill=green!90]{};
# \draw (1*360/5: 3.5cm) node[fill=blue!90]{};
# \draw (2*360/5: 3.5cm) node[fill=red!90]{};
# \draw (3*360/5: 3.5cm) node[fill=green!90]{};
# \draw (4*360/5: 3.5cm) node[fill=blue!90]{};

# \foreach \a/\b in {0/72,72/144,144/216,216/288,288/0}{
# \draw (\a: 3.5cm) -- (\b: 3.5cm);}


# \foreach \a in {0,72,144,216,288}{
# \draw (\a: 2.5cm) -- (\a: 3.5cm);}

# \end{tikzpicture}
# \end{center}




positions=[]
color=[]
color_alpha=[]
size=[]
n_shape=[]
innerSep=[]
# scale = []

G=nx.Graph()
serial=0
rotate_Angle = 18
pos_to_node = {}


angle = 0*360/5.0 + rotate_Angle
x0 = 2.5 * round(math.cos(math.radians(angle)), 10)
y0 = 2.5 * round(math.sin(math.radians(angle)), 10)
pos_to_node[(x0,y0)]=0
G.add_node(0, shape='o', x=x0, y=y0, fill=True, color=colors.to_hex(colors.to_rgba('blue', alpha=90/256.0), keep_alpha=True), innerSep="3", scale="0.8", size=0.8*25)

angle = 1*360/5.0 + rotate_Angle
x1 = 2.5 * round(math.cos(math.radians(angle)), 10)
y1 = 2.5 * round(math.sin(math.radians(angle)), 10)
pos_to_node[(x1,y1)]=1
G.add_node(1, shape='o', x=x1, y=y1, fill=True, color=colors.to_hex(colors.to_rgba('red', alpha=90/256.0), keep_alpha=True), innerSep="3", scale="0.8", size=0.8*25)

angle = 2*360/5.0 + rotate_Angle
x2 = 2.5 * round(math.cos(math.radians(angle)), 10)
y2 = 2.5 * round(math.sin(math.radians(angle)), 10)
pos_to_node[(x2,y2)]=2
G.add_node(2, shape='o', x=x2, y=y2, fill=True, color=colors.to_hex(colors.to_rgba('green', alpha=90/256.0), keep_alpha=True), innerSep="3", scale="0.8", size=0.8*25)

angle = 3*360/5.0 + rotate_Angle
x3 = 2.5 * round(math.cos(math.radians(angle)), 10)
y3 = 2.5 * round(math.sin(math.radians(angle)), 10)
pos_to_node[(x3,y3)]=3
G.add_node(3, shape='o', x=x3, y=y3, fill=True, color=colors.to_hex(colors.to_rgba('black', alpha=90/256.0), keep_alpha=True), innerSep="3", scale="0.8", size=0.8*25)

angle = 4*360/5.0 + rotate_Angle
x4 = 2.5 * round(math.cos(math.radians(angle)), 10)
y4 = 2.5 * round(math.sin(math.radians(angle)), 10)
pos_to_node[(x4,y4)]=4
G.add_node(4, shape='o', x=x4, y=y4, fill=True, color=colors.to_hex(colors.to_rgba('black', alpha=90/256.0), keep_alpha=True), innerSep="3", scale="0.8", size=0.8*25)

print pos_to_node
for a,b in [(0,144),(0,216),(72,216),(72,288),(144,288)]:
	angle_u = a + rotate_Angle
	angle_v = b + rotate_Angle
	dist_origin = 2.5
	print (dist_origin * round(math.cos(math.radians(angle_u)), 10), dist_origin * round(math.sin(math.radians(angle_u)), 10))
	u = pos_to_node[(dist_origin * round(math.cos(math.radians(angle_u)), 10), dist_origin * round(math.sin(math.radians(angle_u)), 10))]
	v = pos_to_node[(dist_origin * round(math.cos(math.radians(angle_v)), 10), dist_origin * round(math.sin(math.radians(angle_v)), 10))]
	print u, v
	G.add_edge(u,v)


# positions=list(zip(nx.get_node_attributes(G, 'x'), nx.get_node_attributes(G, 'y')))
for g in G.nodes(data=True):
	print "NodeID=", g[0], ", Attributes=", g[1]
	n_shape.append(g[1]['shape'])
	innerSep.append(g[1]['innerSep'])
	positions.append((g[1]['x'], g[1]['y']))

print positions
# sys.exit(0)
nodeShapes = set((aShape[1]["shape"] for aShape in G.nodes(data = True)))

# print n_shape
# print nodeShapes

for aShape in nodeShapes:
	nodelist=[]
	color = []
	size = []
	for x in G.nodes(data=True):
		if(x[1]["shape"]==aShape):
			nodelist.append(x[0])
			color.append(x[1]['color'])
			size.append(x[1]['size'])
	# print (len(positions),len(color),len(size),len(nodelist))
	nx.draw_networkx_nodes(G,positions,node_color=color, node_size=size, node_shape = aShape, nodelist=nodelist)

nx.draw_networkx_edges(G,positions)

plt.axis('off')

plt.show()

# nx.write_graphml(G, "star.graphml")
