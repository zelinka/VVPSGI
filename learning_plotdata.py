import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

dataset_cckres = pd.read_csv("./datasets/DATASET_cckres.csv").drop('Group', axis=1)
dataset_ccgiga = pd.read_csv("./datasets/DATASET_gigafida.csv").drop('Group', axis=1)

sns.set(font_scale=1.37)

#figsize = 10, 8
f, ax = plt.subplots(figsize=(7, 6))
plt.title("Podatkovna množica VID ccKRES\n")
corr = dataset_cckres.corr()
sns.heatmap(corr, mask=np.zeros_like(corr), cmap="coolwarm", square=True, ax=ax)


f, ax = plt.subplots(figsize=(7, 6))
plt.title("Podatkovna množica VID ccGigafida\n")
corr = dataset_ccgiga.corr()
sns.heatmap(corr, mask=np.zeros_like(corr), cmap="coolwarm", square=True, ax=ax)
plt.show()
