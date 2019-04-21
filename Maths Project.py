#Running Dijkstra's algorithm to find the shortest path in the network.    Dated (4/6/2019)
# The System runs on a GUI where the user has to specify the (Nodes),(Start and End Node) & (Weights of the edges)
# System plots a graph
# Also returns the possible paths along with the weights along with the shortest path.
#  Code developed by Adolf A D'costa (903538404) , Sannithi Vinod Kumar (903636939) , Lekha Ananthula (903872019)



from tkinter import *
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
from collections import defaultdict

node_box=[]
source_box=[]
destination_box=[]
weight_box=[]
COUNT = 0
COUNTEdge =0



class Graph:
    def __init__(self, start, end):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.start = start
        self.end = end

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

def printThis():
    int_number_of_nodes=int(number_of_nodes.get())
    global COUNT
    lbl = Label(window, text="Enter Name of Nodes ", font=('Helvetica', 10, 'bold'))
    lbl.grid(column=3, row=1)
    for i in range(int_number_of_nodes):
        node_box.append(i)
        node_box[i] = Entry(window, bd=5)
        node_box[i].grid(column=3, row=i+2)
        COUNT += 1
    global button
    button = Button(window, text='Accept Nodes', command=getEdgesAndWeights, height=1, width=17, font=('Helvetica', 10, 'bold'))
    button.grid(column=3, row=i+3, columnspan=1)
    button.configure(background='Steelblue1')
    lbl = Label(window, text="Enter Start Node ", font=('Helvetica', 10, 'bold'))
    lbl.grid(column=4, row=1)
    lbl = Label(window, text="Enter End Node ", font=('Helvetica', 10, 'bold'))
    lbl.grid(column=4, row=3)
    global StartNode
    global EndNode
    StartNode = Entry(window, bd=5)
    StartNode.grid(column=4, row=2)
    EndNode = Entry(window, bd=5)
    EndNode.grid(column=4, row=4)

def getEdgesAndWeights():
    lbl = Label(window, text="Enter Source Node", font=('Helvetica', 10, 'bold'))
    lbl.grid(column=5, row=1)
    lbl = Label(window, text="Enter Dest Node ", font=('Helvetica', 10, 'bold'))
    lbl.grid(column=6, row=1)
    lbl = Label(window, text="Enter Edge Weight", font=('Helvetica', 10, 'bold'))
    lbl.grid(column=7, row=1)
    global COUNTEdge
    COUNTEdge = int(number_of_edges.get())
    for j in range(COUNTEdge):
        source_box.append(j)
        source_box[j] = Entry(window, bd=5)
        source_box[j].grid(column=5, row=j+2)
        destination_box.append(j)
        destination_box[j] = Entry(window, bd=5)
        destination_box[j].grid(column=6, row=j+2)
        weight_box.append(j)
        weight_box[j] = Entry(window, bd=5)
        weight_box[j].grid(column=7, row=j+2)
    global button
    button = Button(window, text='Accept Data', command=graphs, height=1, width=40, font=('Helvetica', 10, 'bold'))
    button.grid(column=5, row=j+3, columnspan=3)
    button.configure(background='Steelblue1')

def plot(start, weighted_path, g, routes):
    if weighted_path['path'][-1] == g.end:
        routes.append(weighted_path)

    for edge in g.edges[start]:
        if edge not in weighted_path['path']:
            newpath = weighted_path['path'] + [edge]
            newweight = weighted_path['weight'] + g.distances[(start, edge)]

            plot(edge, {'path': newpath, 'weight': newweight}, g, routes)

    return routes

def travel(g):
    weighted_path = {'path': [g.start], 'weight': 0}
    return plot(g.start, weighted_path, g, [])


def graphs():
    G = nx.DiGraph()
    for j in range(COUNTEdge):
        SourceNode= (source_box[j].get())
        DestinationNode=(destination_box[j].get())
        WeightEdge=(weight_box[j].get())
        G.add_edges_from([(SourceNode,DestinationNode)], weight=WeightEdge)

    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    pos = nx.spring_layout(G)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_size=1500, edge_cmap=plt.cm.Reds)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    pylab.show()

    StartNodeF = (StartNode.get())
    EndNodeF = (EndNode.get())
    large_graph = Graph(StartNodeF,EndNodeF)
    for k in range(COUNT):
        AllNode=(node_box[k].get())
        large_graph.add_node(AllNode)


    for l in range(COUNTEdge):
        SourceNodeDik =(source_box[l].get())
        DestinationNodeDik =(destination_box[l].get())
        WeightEdgeDik =int(weight_box[l].get())
        large_graph.add_edge(SourceNodeDik, DestinationNodeDik, WeightEdgeDik)

    large_graph.distances
    print(travel(large_graph))


global window
window = Tk()
window.title("Transmission Simulation")
window.geometry('1200x600')
filename = PhotoImage(file="GuiMaths.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# To display Number of Node label,spin box
lbl = Label(window, text="Enter number of Nodes: ", font=('Helvetica', 10, 'bold'))
lbl.grid(column=0, row=1)
global number_of_nodes
number_of_nodes = Spinbox(window, from_=0, to=1000, width=20)
number_of_nodes.grid(column=1, row=1)

lbl = Label(window, text="Enter number of Edges: ", font=('Helvetica', 10, 'bold'))
lbl.grid(column=0, row=2)
global number_of_edges
number_of_edges = Spinbox(window, from_=0, to=1000, width=20)
number_of_edges.grid(column=1, row=2)


# # To display a button
global button
button = Button(window, text='Accept', command=printThis, height=1, width=17, font=('Helvetica', 10, 'bold'))
button.grid(column=2, row=1, columnspan=1)
button.configure(background='Steelblue1')



window.mainloop()



