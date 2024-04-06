import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load the data and extract the sentences
data = pd.read_csv('abcnews-date-text.csv')[0:50000]
sentences = data['headline_text'].values.tolist()

# Create the sentence transformer model and get the sentence embeddings
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2') 
embeddings = model.encode(sentences)


# Reduce the dimensionality of the embeddings using PCA
pca = PCA(n_components=2)
embeddings_2d = pca.fit_transform(embeddings)

# Perform k-means clustering on the embeddings
num_clusters = 5  # Set the number of clusters
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(embeddings_2d)
labels = kmeans.labels_

# Plot the embeddings with different colors for each cluster
plt.figure(figsize=(10, 10))
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for i in range(num_clusters):
    cluster_embeddings = [embeddings_2d[j] for j in range(len(embeddings_2d)) if labels[j] == i]
    plt.scatter([x[0] for x in cluster_embeddings], [x[1] for x in cluster_embeddings], c=colors[i], label=f"Cluster {i+1}")
plt.legend()
plt.show()

# Print the sentences in each cluster
# for i in range(num_clusters):
#     cluster_sentences = [sentences[j] for j in range(len(sentences)) if labels[j] == i]
#     print(f"Cluster {i+1}: {cluster_sentences}")