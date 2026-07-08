import chromadb

# create client
client = chromadb.Client()

# create collection
collection = client.create_collection(name = "rag_documents1")

# add a sample data
collection.add(
    ids=["chunk_1", "chunk_2", "chunk_3"],
    documents=[
        "Python supports object-oriented programming.",
        "Machine Learning is a subset of Artificial Intelligence.",
        "Deep Learning uses neural networks."
    ],
    embeddings=[
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
        [0.7, 0.8, 0.9]
    ],
    metadatas=[
        {"source": "Python.pdf", "page": 2},
        {"source": "AI.pdf", "page": 5},
        {"source": "DL.pdf", "page": 8}
    ]
)

# collection the query
results = collection.query(
    query_embeddings=[
        [0.4, 0.5, 0.6] # --> same embedding as chunk 2
    ],
    n_results = 2
)

print(results)