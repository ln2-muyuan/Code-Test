import pandas as pd
import numpy as np
from transformers import AutoTokenizer
from transformers import pipeline
from transformers import AutoModelForSequenceClassification

title = pd.read_csv('./abcnews-date-text.csv', usecols=['headline_text'])[0:10]

tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
encoded_input = tokenizer(list(title['headline_text']), padding=True, truncation=True, return_tensors='pt')
print(encoded_input)


