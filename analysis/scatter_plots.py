import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("metrics.csv")

for y in ["RA-AUC", "SEAL-AUC"]:
    plt.figure()
    plt.scatter(df["R_NR"], df[y], label=y)
    plt.xlabel("Traversal-induced global recurrence")
    plt.ylabel(y)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"scatter_RNR_{y}.png", dpi=300)
    plt.close()
