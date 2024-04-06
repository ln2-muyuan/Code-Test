# 跑不动





import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import LatentDirichletAllocation

# Load data
data = pd.read_csv('abcnews-date-text.csv')[0:10000]
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
lda = LatentDirichletAllocation(n_components=10, learning_method = 'online', random_state=0, verbose = 0)

# Fit LDA model to embeddings
lda_topic_matrix = lda.fit_transform(embeddings)

from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer(stop_words='english')

# Define helper functions
def get_keys(topic_matrix):
    keys = topic_matrix.argmax(axis=1).tolist()
    return keys

def keys_to_counts(keys):
    count_pairs = [(key, keys.count(key)) for key in set(keys)]
    categories = [topic for topic, count in count_pairs]
    count_pairs.sort(key=lambda x: x[1], reverse=True)
    return (categories, count_pairs)

# Get topic keys
lda_keys = get_keys(lda_topic_matrix)
lda_categories, lda_counts = keys_to_counts(lda_keys)

def get_top_n_words(n, keys, document_term_matrix, count_vectorizer):
    top_word_indices = []
    for topic in range(n):
        # Get indices of top n words for each topic
        top_n_word_indices = (-document_term_matrix[topic, :]).argsort()[:n]
        top_word_indices.append(top_n_word_indices)
    # Get top n words for each topic
    top_words = []
    for topic in top_word_indices:
        topic_words = []
        for index in topic:
            topic_words.append(count_vectorizer.get_feature_names_out()[index])
        top_words.append(" ".join(topic_words))
    return top_words

top_n_wrods_lda = get_top_n_words(10, lda_keys, lda_topic_matrix, count)

# Output top words
for idx, topic in enumerate(top_n_wrods_lda):
    print("Topic " + str(idx) + ": " + topic)

print("Done!")