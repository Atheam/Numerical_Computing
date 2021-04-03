import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def load_graph(filename):
    G = nx.Graph()
    
    with open(filename,"r") as f:
        lines = f.readlines()
        SEM_info = lines[0].split()
        s = SEM_info[0]
        t = SEM_info[1]
        E = SEM_info[2]

        id = 0
        for edge in lines[1:]:
            elements = edge.split()
            G.add_node(elements[0])
            G.add_node(elements[1])
            if (elements[0] == s and elements[1] == t ) or (elements[1] == s and elements[0] == t):
                G.add_edge(elements[0],elements[1],current = None,resistance = float("inf"),voltage = E,direction = -1)
            else:
                G.add_edge(elements[0],elements[1],current = None,resistance = elements[2], voltage = 0,id = id,direction = -1)
                id+=1
    return G


def solve_ciruit(G):
    cycles = nx.cycle_basis(G)
    
    n = len(G.edges) - 1
    A = np.zeros((n,n))
    B = np.zeros(n) 

    row = 0
    #using 1st Kirchhoff's law
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
            if edge['voltage'] != 0:
                B[row] = edge['voltage']
        row +=1


    #using 2nd Kirchhoff's law
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



def draw_circuit(G,I):
    i = 0
    for edge_nodes in G.edges:
        edge = G.edges[edge_nodes[0],edge_nodes[1]]
        if edge['voltage'] == 0:
            edge['current'] = I[i] 
        else:
            i-=1
        i+=1
    
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    labels = nx.get_edge_attributes(G,'current')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()


G = load_graph("graph.txt")    
I = solve_ciruit(G)


draw_circuit(G,I)








