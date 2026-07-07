from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentence = "I love Artificial Intelligence."

embedding = model.encode(sentence)

print(f"Embedding Length: {len(embedding)}")
print("\nFirst 10 values:")
print(embedding[:10])