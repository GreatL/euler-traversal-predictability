# Eulerian Traversal–Induced Predictability in Complex Networks

This repository provides the source code accompanying the paper

**“Traversal-induced structural constraints on link predictability in complex networks”**

which investigates intrinsic limits of link predictability from a structural and symbolic-dynamical perspective.

The code implements the generation of Eulerian traversal sequences on undirected networks, the computation of traversal-induced structural constraints, and the empirical analyses reported in the paper.

---

## Overview

Rather than proposing new link prediction algorithms, the associated study focuses on how **network topology itself constrains predictability**.  
By transforming static networks into **Eulerian traversal–induced symbolic dynamics**, the framework identifies structural constraints that govern intrinsic predictability, including:

- **Traversal-induced global recurrence**
- **Local branching uncertainty**
- **Network connectivity as a prerequisite constraint**

Link prediction algorithms are treated as **probes** of these intrinsic structural constraints rather than as definitions of predictability.

This repository contains all code developed by the authors to reproduce the traversal construction and structural measurements used in the paper.

---

## Methods Implemented

The repository implements the following key steps described in the paper:

1. **Eulerian Traversal Construction**
   - Handles disconnected and non-Eulerian networks
   - Uses edge duplication for Eulerization
   - Introduces jump transitions for traversal continuity (excluded from measurements)

2. **Traversal-Induced Structural Constraints**
   - Global recurrence based on node revisit statistics
   - Local branching uncertainty based on conditional entropy of edge transitions
   - Network fragmentation quantified by the number of connected components

3. **Intrinsic Predictability Ordering**
   - Combines traversal-induced constraints and connectivity penalty
   - Designed as a structure-imposed ordering, not a fitted predictive score

---

## Data

The real-world network datasets analyzed in the study are publicly available from the **Noesis repository**:

https://noesis.ikor.org/datasets/link-prediction

Model networks (Erdős–Rényi and Watts–Strogatz graphs) are generated programmatically using standard random graph models.

---

## Link Prediction Algorithms

This repository **does not reimplement link prediction algorithms**.

Experiments involving learning-based link prediction use the official SEAL implementation:

https://github.com/facebookresearch/SEAL

Heuristic predictors (e.g., Resource Allocation) are implemented directly as structural baselines where needed.

---

## Reproducibility Notes

- All traversal-induced quantities are averaged over multiple Eulerian traversals with randomized starting points.
- Jump transitions introduced for disconnected components are explicitly excluded from all measurements.
- The code is designed to reproduce qualitative trends and orderings reported in the paper rather than to optimize algorithmic performance.

---

## Requirements

The code is written in Python and requires:

- Python ≥ 3.8
- NumPy
- NetworkX
- SciPy
- Matplotlib

Dependencies can be installed via:

```bash
pip install -r requirements.txt

---

## License
This code is released for academic and research use.
Please contact the author for other usage.



