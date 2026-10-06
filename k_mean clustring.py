import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
iris = load_iris()
X = iris.data
# Scaling gives features comparable influence
X_scaled = StandardScaler().fit_transform(X)
model = KMeans(
 n_clusters=3,
 random_state=42,
 n_init=10,
)
labels = model.fit_predict(X_scaled)
print("Cluster labels (first 20):", labels[:20])
print("Inertia:", model.inertia_)
print("Silhouette score:", silhouette_score(X_scaled, labels))
# Elbow method
inertias = []
for k in range(1, 8):
 candidate = KMeans(
 n_clusters=k,
 random_state=42,
 n_init=10,
 )
 candidate.fit(X_scaled)
 inertias.append(candidate.inertia_)
plt.plot(range(1, 8), inertias, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.grid(alpha=0.3)
plt.show()
# Visualize clusters after PCA reduction to 2D
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)
centers_2d = pca.transform(model.cluster_centers_)
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, edgecolor="k")
plt.scatter(
 centers_2d[:, 0], centers_2d[:, 1],
 marker="X", s=220, edgecolor="k",
 label="Centroids",
)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clusters")
plt.legend()
plt.show()