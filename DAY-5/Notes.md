# 📅 Day 5 – Persistent ChromaDB & RAG Backend Refactoring

## 🎯 Objective

Improve the RAG application by making it efficient, reusable, and scalable.

Instead of recreating embeddings every time the program runs, we store them permanently and reuse them in future runs.

---

# 📚 Theory

## 1. In-Memory Database vs Persistent Database

### In-Memory Database

Data exists only while the program is running.

```
Run Program
      ↓
Create Collection
      ↓
Store Embeddings
      ↓
Close Program
      ↓
Everything is Lost ❌
```

Example:

```python
client = chromadb.Client()
```

Every time the program starts, all embeddings must be generated again.

---

### Persistent Database

Data is stored on disk.

```
Run Program
      ↓
Create Embeddings
      ↓
Store on Disk
      ↓
Close Program
      ↓
Run Again
      ↓
Load Existing Database ✅
```

Example:

```python
client = chromadb.PersistentClient(
    path="./chroma_db"
)
```

The `chroma_db` folder stores all vectors permanently.

---

## 2. Why Persistence is Important

Without persistence:

```
Read PDF
↓

Split into Chunks
↓

Generate Embeddings
↓

Store
```

This process repeats every time the application starts.

With persistence:

```
Load Existing Collection
↓

Ask Question Immediately
```

This makes the application much faster and more efficient.

---

## 3. Why Use `get_or_create_collection()`

Using:

```python
collection = chroma_client.create_collection(
    name="rag_documents"
)
```

works only once.

Running the program again causes an error because the collection already exists.

Instead, use:

```python
collection = chroma_client.get_or_create_collection(
    name="rag_documents"
)
```

This means:

* If the collection exists → load it.
* If it doesn't exist → create it.

---

## 4. Collection Count

Every collection knows how many chunks it contains.

```python
collection.count()
```

Example:

```
Collection contains 5 chunks.
```

This tells us whether the PDF has already been indexed.

---

## 5. Indexing

Indexing means preparing a document for searching.

The indexing process consists of:

```
PDF
↓

Extract Text
↓

Split into Chunks
↓

Generate Embeddings
↓

Store in ChromaDB
```

After indexing, the document is ready for semantic search.

---

## 6. Skip Re-Indexing

Instead of indexing every time:

```
Start Program
↓

Read PDF
↓

Chunk
↓

Embed
↓

Store
```

we now check:

```python
if collection.count() == 0:
```

If the collection is empty:

```
Index PDF
```

Otherwise:

```
Skip Indexing
```

This avoids unnecessary work.

---

## 7. Dynamic Collection Names

Previously:

```python
name="rag_documents"
```

Every PDF used the same collection.

Now the collection name is created automatically from the PDF filename.

Example:

```
Artificial Intelligence with Machine Learning.pdf
```

↓

```
artificial_intelligence_with_machine_learning
```

This allows different PDFs to have different collections.

---

## 8. Creating Dynamic Collection Names

### Get only the filename

```python
filename = os.path.basename(pdf_path)
```

Output:

```
Artificial Intelligence with Machine Learning.pdf
```

---

### Remove ".pdf"

```python
filename = os.path.splitext(filename)[0]
```

Output:

```
Artificial Intelligence with Machine Learning
```

---

### Convert into a collection name

```python
collection_name = (
    filename
    .lower()
    .replace(" ", "_")
)
```

Output:

```
artificial_intelligence_with_machine_learning
```

---

## 9. Why Pass `pdf_path` into `create_collection()`

Old:

```python
create_collection()
```

The function had no idea which PDF was being used.

New:

```python
create_collection(pdf_path)
```

Now the function can automatically create the correct collection name.

---

## 10. Refactoring

Refactoring means improving the structure of the code **without changing what it does**.

Example:

Old:

```text
Main Program

↓

Read PDF

↓

Chunk

↓

Embed

↓

Store
```

New:

```text
Main Program

↓

create_collection()

↓

index_pdf()

↓

Chat
```

The functionality remains the same, but the code becomes cleaner and easier to maintain.

---

## 11. The `index_pdf()` Function

Instead of keeping indexing logic inside the main program, we moved it into its own function.

Responsibilities:

* Check if the collection is empty.
* Extract text.
* Split text.
* Generate embeddings.
* Store embeddings.
* Skip indexing if embeddings already exist.

This follows the principle:

> One function should have one responsibility.

---

## 12. Current RAG Architecture

```
User Selects PDF
        │
        ▼
Create / Load Collection
        │
        ▼
Is Collection Empty?
        │
   ┌────┴────┐
   │         │
  YES        NO
   │         │
   ▼         ▼
Index PDF    Skip Indexing
      │
      ▼
User Asks Question
      │
      ▼
Generate Question Embedding
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build Prompt
      │
      ▼
Gemini Generates Answer
      │
      ▼
Display Answer
```

---

# 💻 Practical Work Completed

✅ Replaced:

```python
chromadb.Client()
```

with

```python
chromadb.PersistentClient()
```

---

✅ Stored ChromaDB on disk using:

```python
path="./chroma_db"
```

---

✅ Replaced:

```python
create_collection()
```

with

```python
get_or_create_collection()
```

---

✅ Added dynamic collection names.

---

✅ Used:

```python
collection.count()
```

to determine whether indexing is required.

---

✅ Created a dedicated:

```python
index_pdf()
```

function.

---

✅ Refactored the main program.

Old:

```
Extract
↓

Chunk

↓

Embeddings

↓

Store
```

New:

```
Create Collection
↓

Index PDF
↓

Chat
```

---

# 🧠 Key Python Concepts Learned

* `os.path.basename()`
* `os.path.splitext()`
* String methods:

  * `.lower()`
  * `.replace()`
* Function parameters
* Refactoring
* Program flow
* Separation of responsibilities

---

# 🎯 Key Takeaways

* Persistence saves embeddings permanently.
* Collections allow documents to be organized.
* Dynamic collection names make the application reusable.
* Indexing prepares documents for semantic search.
* Refactoring makes code easier to understand and maintain.
* Clean functions are easier to reuse when building larger applications.

---

# 📈 Progress So Far

## ✅ Day 1

* AI Fundamentals
* PDF Extraction
* Chunking
* Embeddings

---

## ✅ Day 2

* ChromaDB
* Semantic Search
* Vector Database

---

## ✅ Day 3

* Retrieval Pipeline
* Real Embeddings
* Complete Retrieval Engine

---

## ✅ Day 4

* Gemini API
* Prompt Engineering
* First RAG Chatbot

---

## ✅ Day 5

* Persistent ChromaDB
* Dynamic Collection Names
* Automatic Collection Loading
* Skip Re-Indexing
* PDF Indexing Function
* Backend Refactoring

---

# 🚀 Ready for Day 6

The backend is now modular and reusable.

Next step:

Build a Streamlit web application where users can:

* Upload PDFs
* Automatically create/load collections
* Ask questions
* Receive grounded answers from Gemini through the RAG pipeline
