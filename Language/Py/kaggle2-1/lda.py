import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import LatentDirichletAllocation

# Load data
data = pd.read_csv('abcnews-date-text.csv')[0:50000]
sentences = data['headline_text'].values.tolist()

# Preprocess text to remove numerical values
import re
sentences = [re.sub(r'\d+', '', s) for s in sentences]

# Generate sentence embeddings
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2') 
embeddings = model.encode(sentences)

# Normalize embeddings
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
embeddings = scaler.fit_transform(embeddings)

# Create LDA model
lda = LatentDirichletAllocation(n_components=10, random_state=0)

# Fit LDA model to embeddings
lda_topic_matrix = lda.fit_transform(embeddings)

# Extract topics from LDA model
def get_topics(components, feature_names, n=3):
    topics = []
    # Get the number of terms in the vocabulary
    num_terms = len(feature_names)
    for idx, topic in enumerate(components):
        # Only include topics with valid term indices
        if len(topic) <= num_terms:
            topics.append(' '.join([feature_names[i] for i in topic.argsort()[:-n - 1:-1]]))
    return topics

from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer(stop_words='english')
count.fit(sentences)
topics = get_topics(lda.components_, count.get_feature_names_out())

# Output topics
for idx, topic in enumerate(topics):
    print("Topic " + str(idx) + ": " + topic)

# Assign topics to each headline
topic_labels = lda_topic_matrix.argmax(axis=1)

# Count the number of headlines in each topic
import numpy as np
topic_counts = np.bincount(topic_labels)

# Create a dictionary mapping each topic label to its count
topic_dict = {idx: count for idx, count in enumerate(topic_counts)}

# Create a dictionary mapping each topic label to its top words
word_dict = {idx: words for idx, words in enumerate(topics)}

# Create a bar chart of the topic counts and top words
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for idx in range(len(topic_dict)):
    ax.barh(word_dict[idx], topic_dict[idx], label='Topic ' + str(idx))

ax.invert_yaxis()
ax.set_xlabel('Number of headlines')
ax.set_ylabel('Top words')
ax.set_title('LDA Topic Modeling Results')
ax.legend(loc="upper right")
plt.show()