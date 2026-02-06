import networkx as nx
import random
from collections import Counter

def shorten_path(path):
    edges = [(min(u,v), max(u,v)) for u,v in path]
    unique_edges = set(edges)
    for i in range(1, len(edges)+1):
        if set(edges[:i]) == unique_edges:
            return path[:i]
    return path

def graph_to_euler_path(G: nx.Graph):
    if not nx.is_connected(G):
        components = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    else:
        components = [G]

    random.shuffle(components)

    path = []
    last_node = None
    jump_edges = 0
    duplicate_edges = 0

    for comp in components:
        original_edges = comp.number_of_edges()

        if len(comp) > 1 and not nx.is_eulerian(comp):
            comp = nx.eulerize(comp)

        duplicate_edges += comp.number_of_edges() - original_edges

        if len(comp) == 1:
            node = list(comp.nodes())[0]
            if last_node is not None:
                path.append((last_node, node))
                jump_edges += 1
            last_node = node
        else:
            start = random.choice(list(comp.nodes()))
            raw_path = list(nx.eulerian_path(comp, source=start))
            spath = shorten_path(raw_path)

            if path:
                path.append((last_node, spath[0][0]))
                jump_edges += 1

            path.extend(spath)
            last_node = spath[-1][1]

    return path, jump_edges, duplicate_edges

def path_to_node_sequence(path):
    if not path:
        return []
    seq = [u for u,v in path]
    seq.append(path[-1][1])
    return seq
