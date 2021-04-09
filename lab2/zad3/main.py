import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from generate import *


def load_graph(filename):
    G = nx.Graph()
    
    with open(filename,"r") as f:
        lines = f.readlines()
        SEM_info = lines[0].split()
        s = SEM_info[0]
        t = SEM_info[1]
        E = float(SEM_info[2])

        id = 0
        for edge in lines[1:]:
            elements = edge.split()
            G.add_node(elements[0])
            G.add_node(elements[1])
            if (elements[0] == s and elements[1] == t ) or (elements[1] == s and elements[0] == t):
                G.add_edge(elements[0],elements[1],current = None,resistance = float("inf"),voltage = E,direction = -1)
            else:
                G.add_edge(elements[0],elements[1],current = None,resistance = float(elements[2]), voltage = 0,id = id,direction = -1)
                id+=1
    return G


def solve_kirch(G):
    cycles = nx.cycle_basis(G)
    
    n = len(G.edges) - 1
    A = np.zeros((n,n))
    B = np.zeros(n) 

    row = 0
    #using 2nd Kirchhoff's law
    for cycle in cycles:
        cycle.append(cycle[0])
        for node in range(len(cycle) - 1):
            node_from = cycle[node]
            node_to = cycle[node+1]
            edge = G.edges[node_from,node_to]
            if edge['voltage'] == 0:
                if edge['direction'] == -1:
                    A[row][edge['id']] = edge['resistance']
                    edge['direction'] = node_to
                else:
                    A[row][edge['id']] = edge['resistance'] if edge['direction'] == node_to else edge['resistance'] * (-1)
            else:
                B[row] = edge['voltage'] 
        row +=1


    #using 1st Kirchhoff's law
    for node in G.nodes:
        SEM_node = False
        for edge_nodes in G.edges(node):
            if G.edges[edge_nodes[0],edge_nodes[1]]['voltage'] != 0:
                SEM_node = True
                break
        if not SEM_node:
            for edge_nodes in G.edges(node):
                edge = G.edges[edge_nodes[0],edge_nodes[1]]
                node_to = edge['direction']
                A[row][edge['id']] = 1.0 if node == node_to else -1.0
              
            row+=1
    I = np.linalg.solve(A,B)
    
    return I

def solve_potential(G):
    nodes_dict = {}
    potential_id = 0
    count = 0
    
    for node in G.nodes:
        SEM_node = False
        for edge_nodes in G.edges(node):
            if G.edges[edge_nodes[0],edge_nodes[1]]['voltage'] != 0:
                potential_node = (edge_nodes[0],G.edges[edge_nodes[0],edge_nodes[1]]['voltage'])
                SEM_node = True
                break
        if not SEM_node:
            nodes_dict[node] = potential_id
            potential_id+=1 
            count+=1
        
    A = np.zeros((count,count))
    B = np.zeros(count)

    for node in G.nodes:
        if node in nodes_dict:
            for edge_nodes in G.edges(node):
                edge = G.edges[edge_nodes[0],edge_nodes[1]]
                node_1 = node
                node_2 = edge_nodes[0] if edge_nodes[0] != node_1 else edge_nodes[1]
                potential_id_1 = nodes_dict[node]

                SEM_node = False
                for edge_nodes in G.edges(node_2):
                    if G.edges[edge_nodes[0],edge_nodes[1]]['voltage'] != 0:
                        SEM_node = True
                        break
                if not SEM_node:
                    potential_id_2 = nodes_dict[node_2]
                    A[potential_id_1][potential_id_2] = 1/edge['resistance']
                else:
                    if node_2 == potential_node[0]:
                        B[potential_id_1] = potential_node[1]/edge['resistance'] * (-1)

                A[potential_id_1][potential_id_1] -= 1/edge['resistance']
    

    V = np.linalg.solve(A,B)
    
    I = np.zeros(len(G.edges)-1)  

    for edge_nodes in G.edges:
        edge = G.edges[edge_nodes[0],edge_nodes[1]] 

        if edge['voltage'] == 0:
            if edge_nodes[0] in nodes_dict and edge_nodes[1] in nodes_dict :
                U = V[nodes_dict[edge_nodes[0]]] - V[nodes_dict[edge_nodes[1]]]

            elif edge_nodes[0] not in nodes_dict:
                if edge_nodes[0] == potential_node[0]:
                    U = potential_node[1] - V[nodes_dict[edge_nodes[1]]]
                else:
                    U = 0 - V[nodes_dict[edge_nodes[1]]]
            else:
                if edge_nodes[1] == potential_node[0]:
                    U =  V[nodes_dict[edge_nodes[0]]] - potential_node[1]
                else:
                    U = V[nodes_dict[edge_nodes[0]]] - 0

            if U > 0:
                edge['direction'] = edge_nodes[1]
            else:
                edge['direction'] = edge_nodes[0]

            I[edge['id']] = abs(U)/edge['resistance']
    return I
    

def draw_circuit(G,I):
    G_di = nx.DiGraph()
    id = 0
    for edge_nodes in G.edges:
        edge = G.edges[edge_nodes[0],edge_nodes[1]] 
        if edge['voltage'] == 0:
            if edge['direction'] != -1:
                node_to = edge['direction']
                node_from = edge_nodes[0] if edge_nodes[0] != node_to else edge_nodes[1]
                if I[id] < 0:
                    node_to,node_from = node_from,node_to
                    I[id] *= -1
                G_di.add_edge(node_from,node_to,current = round(I[id],2))    
                
            else:
                node_from = edge_nodes[0]
                node_to = edge_nodes[1]
                G_di.add_edge(node_from,node_to,current =round(I[id],2))  
            id +=1

        else:
            node_from = edge_nodes[0]
            node_to = edge_nodes[1]
            G_di.add_edge(node_from,node_to,current = None) 

    if nx.check_planarity(G_di)[0]:
        pos = nx.planar_layout(G_di)
    else:
        pos = nx.spring_layout(G_di)
    nx.draw_networkx_nodes(G_di,pos)
    nx.draw_networkx_labels(G_di, pos)
    nx.draw_networkx_edges(G_di, pos)
    labels = nx.get_edge_attributes(G_di,'current')
    nx.draw_networkx_edge_labels(G_di,pos,edge_labels=labels)
    plt.show()









