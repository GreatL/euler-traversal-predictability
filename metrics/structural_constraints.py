import numpy as np
from collections import Counter
from scipy.stats import entropy

def node_revisit_ratio(sequence):
    return 1 - len(set(sequence)) / len(sequence)

def edge_pairs(sequence):
    return [(sequence[i], sequence[i+1]) for i in range(len(sequence)-1)]

def conditional_edge_entropy(sequence):
    edges = edge_pairs(sequence)
    if len(edges) < 2:
        return 0.0
    pairs = [(edges[i], edges[i+1]) for i in range(len(edges)-1)]
    counts = Counter(pairs)
    probs = np.array(list(counts.values())) / sum(counts.values())
    return entropy(probs) / np.log(len(counts) + 1e-9)
