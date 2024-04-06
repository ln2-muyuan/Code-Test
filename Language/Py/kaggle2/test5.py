import pandas as pd
from sentence_transformers import SentenceTransformer

# Load the data and extract the sentences
data = pd.read_csv('abcnews-date-text.csv')[0:10]
sentences = data['headline_text'].values.tolist()

# Create the sentence transformer model and get the sentence embeddings
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2') 
embeddings = model.encode(sentences)

# Print the embeddings
print(embeddings)
