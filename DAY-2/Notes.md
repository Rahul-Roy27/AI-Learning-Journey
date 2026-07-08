# DAY - 2

# ChromaDB

## What is ChromaDB?

ChromaDB is an open-source vector database used to store embeddings and perform semantic similarity search.

Unlike traditional databases, ChromaDB searches based on the meaning of text rather than exact keyword matches.

---

# Vector Database

## Definition

A Vector Database stores embeddings (vectors) and efficiently retrieves the most similar vectors using semantic similarity.

Instead of searching for exact words, it searches for text with similar meaning.

---

## Why do we need a Vector Database?

After chunking a PDF, every chunk is converted into an embedding.

Example:

Chunk 1 → Embedding

Chunk 2 → Embedding

Chunk 3 → Embedding

If a document contains thousands of chunks, storing them in a normal Python list becomes inefficient.

A Vector Database is optimized for storing embeddings and performing fast similarity searches.

---

## Why not use a Traditional Database?

Traditional databases (MySQL, PostgreSQL, SQLite) are designed for exact-value searches.

Example:

```sql
SELECT * FROM Students
WHERE Name = 'Rahul';
```

## Examples

- ChromaDB
- FAISS
- Pinecone
- Weaviate
- Milvus
- Qdrant

## Why ChromaDB?

- Open Source
- Runs locally
- Beginner-friendly
- Easy to integrate with LangChain
- Widely used for learning RAG


# Collections

## What is a Collection?

A Collection is a container inside ChromaDB that stores related documents and their embeddings.

It is similar to a folder that groups related data together.

Example:

ChromaDB
│
├── rag_documents
├── medical_documents
└── college_notes

Each RAG project usually has its own collection.

## What does a Collection store?

Every record inside a collection consists of:

### 1. ID

A unique identifier for each chunk.

Example:

chunk_1

chunk_2

chunk_3

### 2. Document

The actual chunk text.

Example:

Machine Learning is a subset of Artificial Intelligence.

### 3. Embedding

The numerical vector representing the meaning of the document.

Embeddings are generated using a Sentence Transformer.

### 4. Metadata

Additional information about the document.

Example:

```python
{
    "source": "AI.pdf",
    "page": 5
}
```

Metadata helps identify the source of retrieved information.


# ChromaDB Client

## What is a Client?

A Client establishes the connection between Python and the ChromaDB database.

Example:

```python
import chromadb

client = chromadb.Client()
```

Without a client, Python cannot create collections or store data.

## Creating a Collection

```python
collection = client.create_collection(
    name="rag_documents"
)
```

This creates an empty collection named `rag_documents`.

---

# Adding Data

Data is stored using:

```python
collection.add(
    ids=[...],
    documents=[...],
    embeddings=[...],
    metadatas=[...]
)
```

## Why are Lists used?

ChromaDB is designed for batch insertion, allowing multiple records to be added in a single function call.

All lists must have the same length because elements are matched by their index.


# Retrieving Data

Data is retrieved from ChromaDB using:

```python
results = collection.query(
    query_embeddings=[...],
    n_results=3
)
```

## query_embeddings

The embedding of the user's question.

Instead of comparing raw text, ChromaDB compares the question embedding with stored embeddings.

## n_results

Specifies the number of most relevant chunks to retrieve.

Example:

```python
n_results = 3
```

returns the Top 3 most similar chunks.

## What does query() return?

`query()` returns a dictionary containing:

- IDs
- Documents
- Metadata

The retrieved documents are later passed to the LLM for answer generation.


# Distances

ChromaDB returns the distance between the query embedding and the stored embeddings.

A smaller distance indicates that the embeddings are more similar.

Example:

Distance = 0.0

→ Perfect match.

Distance = 0.27

→ Similar, but less relevant than a perfect match.

Unlike similarity scores (where higher is better), ChromaDB returns distances by default, where lower values indicate better matches.