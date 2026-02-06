import networkx as nx
import pandas as pd
import numpy as np
from traversal.euler_traversal import graph_to_euler_path, path_to_node_sequence
from metrics.structural_constraints import node_revisit_ratio, conditional_edge_entropy

def load_edge_list(path):
    edges = []
    with open(path) as f:
        for line in f:
            u,v = map(int, line.split())
            edges.append((u,v))
    return edges

def process_network(edge_file, K=5):
    edges = load_edge_list(edge_file)
    G = nx.Graph()
    G.add_edges_from(edges)

    recurrences = []
    entropies = []
    jumps = []
    dups = []

    for _ in range(K):
        path, j, d = graph_to_euler_path(G)
        seq = path_to_node_sequence(path)

        recurrences.append(node_revisit_ratio(seq))
        entropies.append(conditional_edge_entropy(seq))
        jumps.append(j)
        dups.append(d)

    return {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "components": nx.number_connected_components(G),
        "R_NR": np.mean(recurrences),
        "H_cond": np.mean(entropies),
        "jump_edges": np.mean(jumps),
        "duplicate_edges": np.mean(dups),
    }

if __name__ == "__main__":
    networks = ["data/networks/Power.txt"]
    rows = []

    for net in networks:
        row = process_network(net)
        row["network"] = net
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv("metrics.csv", index=False)
