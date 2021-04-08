import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def generate_erdos(n,p=0.5):
    G = nx.erdos_renyi_graph(n,p)
    while not nx.is_connected(G):
        G = nx.erdos_renyi_graph(n,p)

    R = np.random.uniform(1.0,100.0)
    id = 0
    for edge_nodes in G.edges:
        edge = G.edges[edge_nodes[0],edge_nodes[1]]
        edge['current'] = None
        edge['resistance'] = R
        edge['voltage'] = 0
        edge['id'] = id
        edge['direction'] = -1
        id +=1

    a = random.choice(list(G.nodes))
    b = random.choice(list(G.nodes))
    while a == b or G.has_edge(a, b):
        a = random.choice(list(G.nodes))
        b = random.choice(list(G.nodes))

    voltage = np.random.uniform(1.0,100.0)
    G.add_edge(a,b)
    SEM_edge = G.edges[a,b]
    SEM_edge['current'] = None
    SEM_edge['resistance'] = float("inf")
    SEM_edge['voltage'] = voltage
    SEM_edge['direction'] = -1
    return G

def generate_cubic(n):
    G = nx.random_regular_graph(3,n)

    R = np.random.uniform(1.0,100.0)
    id = 0
    for edge_nodes in G.edges:
        edge = G.edges[edge_nodes[0],edge_nodes[1]]
        edge['current'] = None
        edge['resistance'] = R
        edge['voltage'] = 0
        edge['id'] = id
        edge['direction'] = -1
        id +=1

    a = random.choice(list(G.nodes))
    b = random.choice(list(G.nodes))
    while a == b or G.has_edge(a, b):
        a = random.choice(list(G.nodes))
        b = random.choice(list(G.nodes))

    voltage = np.random.uniform(1.0,100.0)
    G.add_edge(a,b)
    SEM_edge = G.edges[a,b]
    SEM_edge['current'] = None
    SEM_edge['resistance'] = float("inf")
    SEM_edge['voltage'] = voltage
    SEM_edge['direction'] = -1
    

    return G

def generate_mesh(m,n=2):
    G = nx.grid_2d_graph(m,n)
    R = np.random.uniform(1.0,100.0)
    id = 0
    for edge_nodes in G.edges:
        edge = G.edges[edge_nodes[0],edge_nodes[1]]
        edge['current'] = None
        edge['resistance'] = R
        edge['voltage'] = 0
        edge['id'] = id
        edge['direction'] = -1
        id +=1

    a = random.choice(list(G.nodes))
    b = random.choice(list(G.nodes))
    while a == b or G.has_edge(a, b):
        a = random.choice(list(G.nodes))
        b = random.choice(list(G.nodes))

    voltage = np.random.uniform(1.0,100.0)
    G.add_edge(a,b)
    SEM_edge = G.edges[a,b]
    SEM_edge['current'] = None
    SEM_edge['resistance'] = float("inf")
    SEM_edge['voltage'] = voltage
    SEM_edge['direction'] = -1
    

    return G

def generate_small_world(n,k=2,p=0.5):

    G = nx.connected_watts_strogatz_graph(n,k,p)
    R = np.random.uniform(1.0,100.0)
    id = 0
    for edge_nodes in G.edges:
        edge = G.edges[edge_nodes[0],edge_nodes[1]]
        edge['current'] = None
        edge['resistance'] = R
        edge['voltage'] = 0
        edge['id'] = id
        edge['direction'] = -1
        id +=1

    a = random.choice(list(G.nodes))
    b = random.choice(list(G.nodes))
    while a == b or G.has_edge(a, b):
        a = random.choice(list(G.nodes))
        b = random.choice(list(G.nodes))

    voltage = np.random.uniform(1.0,100.0)
    G.add_edge(a,b)
    SEM_edge = G.edges[a,b]
    SEM_edge['current'] = None
    SEM_edge['resistance'] = float("inf")
    SEM_edge['voltage'] = voltage
    SEM_edge['direction'] = -1
    

    return G







