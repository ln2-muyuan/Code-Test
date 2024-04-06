from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

data = "I love you"
encoding = tokenizer.encode_plus(data)
print(encoding)
