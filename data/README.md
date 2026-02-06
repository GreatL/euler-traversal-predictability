# Data Description

The real-world network datasets analyzed in this study are obtained from the **Noesis repository**, which provides benchmark datasets for link prediction research:

https://noesis.ikor.org/datasets/link-prediction

---

## Data Preparation

For reproducibility, users should download the desired network datasets directly from the Noesis repository and extract the **edge list files** corresponding to each network.

Each dataset should be converted into a plain text file (`.txt`) containing one undirected edge per line, formatted as:

u v

where `u` and `v` are integer node identifiers representing an undirected link between two nodes.

Only the edge list files are required for the experiments reported in the paper. No node attributes, edge weights, or temporal information are used.

---

## File Placement

After downloading and extracting the datasets, place the processed edge list files into this directory:


data/networks/


Each file represents a single undirected network and is loaded directly by the experimental scripts.

---

## Notes

- All networks are treated as **undirected, unweighted, and static**.
- Self-loops and duplicate edges should be removed during preprocessing.
- Node indices are assumed to be non-negative integers. If the original dataset uses arbitrary labels, they should be remapped to a consecutive integer range before analysis.

For details on how these datasets are used in the traversal-based experiments, please refer to the accompanying code and the main text of the paper.

