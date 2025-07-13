from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Bu ürün gerçekten çok kötüydü."

# Preprocess
inputs = tokenizer(text, return_tensors="pt")

# Model prediction
with torch.no_grad():
    logits = model(**inputs).logits

# Convert to prediction
predicted_class_id = logits.argmax().item()
print("Predicted class:", predicted_class_id)
