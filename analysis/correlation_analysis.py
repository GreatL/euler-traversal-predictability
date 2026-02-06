import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("metrics.csv")

corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
plt.imshow(corr, cmap="coolwarm")
plt.xticks(range(len(corr)), corr.columns, rotation=90)
plt.yticks(range(len(corr)), corr.columns)
plt.colorbar()
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=300)
plt.close()
