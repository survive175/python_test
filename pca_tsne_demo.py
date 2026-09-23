import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# 加载数据
digits = load_digits()
X, y = digits.data, digits.target

# PCA 降维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# t-SNE 降维
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X)

# 画图
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', s=5)
axes[0].set_title('PCA')
axes[1].scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10', s=5)
axes[1].set_title('t-SNE')
plt.savefig('pca_vs_tsne.png', dpi=300, bbox_inches='tight')
plt.show()
