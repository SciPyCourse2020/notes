import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
import pandas as pd

def cf():
    plt.close('all')

data, _ = make_classification(n_samples=10000, n_features=7, n_informative=2,
                              n_redundant=1, n_repeated=0, n_classes=1,
                              n_clusters_per_class=4, hypercube=True, random_state=8)

f, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
ax[0].set_xlabel('Dimension 0')
ax[0].set_ylabel('Dimension 1')
ax[0].scatter(data[:, 0], data[:, 1], s=1) # plot x vs. y for first two dimensions
ax[1].set_xlabel('Dimension 2')
ax[1].set_ylabel('Dimension 3')
ax[1].scatter(data[:, 2], data[:, 3], s=1) # plot x vs. y for second two dimensions
ax[2].set_xlabel('Dimension 4')
ax[2].set_ylabel('Dimension 5')
ax[2].scatter(data[:, 4], data[:, 5], s=1) # plot x vs. y for third two dimensions

f, ax = plt.subplots(figsize=(5, 5))

pca = PCA(n_components=2) # create a PCA object, ask for only the top 2 components
d2 = pca.fit_transform(data) # calculate top 2 principal components, project data onto them
ax.scatter(d2[:, 0], d2[:, 1], s=1) # plot x vs. y for all samples in d2
ax.set_title('PCA reduced')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')

df = pd.DataFrame(data, columns=np.arange(7))
df.to_excel('measurements.xlsx', index=False)
