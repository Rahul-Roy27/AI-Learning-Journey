import chromadb

# Create a ChromaDB client
client = chromadb.Client()

# Create a collection
collection = client.create_collection(name="rag_documents")

print("Collection created successfully!")
print(collection.name)

# Add one document to the collection
collection.add(
    ids=["chunk_1"],
    documents=["Python supports object-oriented programming."],
    embeddings=[[0.12, 0.34, -0.56]],
    metadatas=[
        {
            "source": "Python.pdf",
            "page": 2
        }
    ]
)

print("Document added successfully!")