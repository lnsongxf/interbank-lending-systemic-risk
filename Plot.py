# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:37:15 2015

@author: Marco Tinacci
"""

import networkx as nx
import matplotlib.pyplot as plt
import Contagion

def plotGraph(g,alpha,node_scale=1, seed=None, pos=None):
    # layout
    if pos == None:
       pos = nx.circular_layout(g)
#       pos = nx.random_layout(g)
    # draw nodes
    nx.draw_networkx_nodes(g,pos,
        nodelist = filter(lambda x:not Contagion.checkBankrupt(x,g),g.nodes()),
        node_size = [node_scale*g.node[k]['ASSET'] for k in g.nodes()],
        node_color = 'b',#[node_scale*g.node[k]['ASSET'] for k in g.nodes()],
        cmap = plt.cm.Blues)
    nx.draw_networkx_nodes(g,pos,
        nodelist = filter(lambda x:Contagion.checkBankrupt(x,g),g.nodes()),
        node_size = [node_scale*g.node[k]['ASSET'] for k in g.nodes()],
        node_color = 'r')


    # draw edges
    edges,weights = zip(*nx.get_edge_attributes(g,'weight').items())
    nx.draw_networkx_edges(g, pos,
        edge_color = weights,
        width=0.5,
        edge_cmap = plt.cm.Blues,
        arrows=False)
    # plot graph
    if not seed == None:
        nx.write_gml(g,'output_graphs/n'+str(len(g))+'a'+str(alpha)+'s'+str(seed)+'.gml')
        plt.savefig('output_graphs/n'+str(len(g))+'a'+str(alpha)+'s'+str(seed)+'.png')
        plt.show()
    return pos

def scatterDegreeSize(g):
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.scatter(map(lambda x:g.degree(x), g.nodes()),
                map(lambda y:y['ASSET'], g.node.values()))