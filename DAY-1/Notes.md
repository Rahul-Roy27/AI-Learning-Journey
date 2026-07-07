# Artificial Intelligence (AI)

## Definition
Artificial Intelligence is the field of creating systems that perform tasks that normally require human intelligence.

## Examples
- ChatGPT
- Face Unlock
- Google Maps
- Recommendation Systems

## AI vs Traditional Programming

Traditional:
Rules + Data → Output

AI:
Data + Expected Answers → Learning → Model → Prediction

## Key Point
AI is the broad field. Machine Learning and Deep Learning are subsets of AI.


# Machine Learning

## Definition
Machine Learning is a branch of AI where computers learn patterns from data instead of being explicitly programmed.

## Traditional Programming
Rules + Data → Output

## Machine Learning
Data + Labels → Learning → Model → Prediction

## Types of Machine Learning

1. Supervised Learning
- Uses labeled data.
- Example: Spam detection.

2. Unsupervised Learning
- Uses unlabeled data.
- Example: Customer clustering.

3. Reinforcement Learning
- Learns through rewards and penalties.
- Example: Game-playing AI.


### Relationship

Artificial Intelligence
│
└── Machine Learning
     │
     └── Deep Learning
          │
          └── Large Language Models (LLMs)

Example:
ChatGPT is an AI system built using Deep Learning, which is a subset of Machine Learning.


# Deep Learning

## Definition
Deep Learning is a subset of Machine Learning that uses Artificial Neural Networks with many layers to learn complex patterns.

## Neural Network
A computational model inspired by how neurons connect, capable of learning features from data.

## Why Deep Learning?
- Handles huge datasets
- Works well with text, images, speech, and video
- Powers modern AI applications

## Examples
- ChatGPT
- Gemini
- Face Unlock
- Google Translate

## Relationship

AI
└── Machine Learning
     └── Deep Learning
          └── Large Language Models (LLMs)


## What is a Model?

A model is a trained AI system that has learned patterns from data and can make predictions or generate outputs.

Examples:
- ChatGPT
- Gemini
- Sentence Transformer


# Large Language Models (LLMs)

## Definition
A Large Language Model (LLM) is a Deep Learning model trained on a massive amount of text to understand and generate human language.

## LLM Breakdown
- Large → Trained on huge amounts of text.
- Language → Understands and generates human language.
- Model → A trained AI system that has learned patterns from data.

## What Can an LLM Do?
- Answer questions
- Summarize text
- Translate languages
- Generate code
- Write articles
- Hold conversations

## Important Points
- An LLM is NOT a database.
- It generates answers based on learned language patterns.
- It does not automatically know private documents or files.
- It can sometimes produce incorrect or made-up answers (hallucinations).

## Examples
- ChatGPT
- Gemini
- Claude
- Llama


# Hallucination

## Definition
A hallucination occurs when an LLM generates incorrect or fabricated information while sounding confident.

## Why does it happen?
- The required information was not part of the model's training.
- The model has no access to private or external data unless provided.

## Example
Question:
How many casual leave days are allowed in my company?

Without access to the company PDF, the LLM may guess an incorrect answer instead of using factual information.



# Retrieval-Augmented Generation (RAG)

## Definition
RAG (Retrieval-Augmented Generation) is an AI technique that retrieves relevant information from external documents and provides it to an LLM before generating an answer.

## Why not send the entire PDF?

- Too many tokens
- Slower responses
- Higher API cost
- Irrelevant information

Instead, RAG retrieves only the most relevant chunks.

## Why RAG?
- LLMs do not know private documents.
- LLMs can hallucinate.
- RAG provides factual context before generation.

## RAG Workflow

User Question
↓
Retrieve Relevant Documents
↓
Provide Context to LLM
↓
Generate Accurate Answer

## Advantages
- Uses up-to-date information.
- Works with private documents.
- Reduces hallucinations.
- More accurate than using an LLM alone.

## Example Use Cases
- HR Policy Chatbot
- Customer Support
- Research Assistant
- Legal Document Search
- Medical Knowledge Base


## RAG Architecture

PDFs
↓
Extract Text
↓
Split into Chunks
↓
Convert Chunks into Embeddings
↓
Store in Vector Database
↓
User asks a Question
↓
Retrieve Relevant Chunks
↓
Send Context + Question to LLM
↓
Generate Accurate Answer



# Embeddings

## Definition
An embedding is a numerical vector that represents the meaning of text.

## Why are embeddings needed?
Computers cannot understand language directly. Embeddings convert text into numbers so computers can compare meanings mathematically.

## Semantic Search
Semantic search finds information based on meaning rather than exact keywords.

Example:
PDF: "Employees receive casual leave."
Question: "How many vacation days are allowed?"

A keyword search may fail, but embeddings recognize the similar meaning.

## Important Note

Embeddings do not search for exact words.
They represent the meaning of text as vectors.

Sentences with similar meanings have embeddings that are close together in vector space.

## Advantages
- Understands meaning
- Finds similar sentences
- Powers semantic search
- Core component of RAG


### Keyword Search vs Semantic Search

Keyword Search:
- Matches exact words.
- Fails when synonyms are used.

Semantic Search:
- Matches meaning instead of exact words.
- Uses embeddings.
- Can understand similar words like:
  - buy ↔ purchase
  - cafeteria ↔ dining hall
  - leave ↔ vacation



  # Activating a Virtual Environment

## Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

## How to know it's activated?

The terminal prompt changes to:

```text
(.venv)
```

This means the terminal is now using the Python interpreter inside the virtual environment instead of the global Python installation.


## Verify Active Python

PowerShell:

```powershell
Get-Command python
```

If the path points to:

```
...\.venv\Scripts\python.exe
```

then the virtual environment is active.



## pip

`pip` is Python's package manager.

### What does it do?

- Downloads Python packages from **PyPI (Python Package Index)**.
- Installs them into the currently active Python environment.

### Important

If `.venv` is activated:

```bash
pip install package_name
```

The package is installed inside `.venv`.

If `.venv` is NOT activated:

The package is installed into the global Python installation.



| Library                   | Job                                   |
| ------------------------- | ------------------------------------- |
| **PyMuPDF**               | 📄 Read PDFs                          |
| **sentence-transformers** | 🧠 Create embeddings                  |
| **ChromaDB**              | 🗂️ Store embeddings                  |
| **LangChain**             | 🔗 Connect everything together        |
| **Gemini API**            | 🤖 Generate answers                   |
| **Streamlit**             | 🌐 Build the user interface (website) |



# Dependencies

## Definition

A dependency is another package that a library needs in order to work.

Example:

When installing Streamlit, pip automatically installs packages like:
- NumPy
- Pandas
- Requests

because Streamlit depends on them.


## Useful pip Commands

### Install a package

```bash
pip install package_name
```

### View installed packages

```bash
pip list
```

### View package details

```bash
pip show package_name
```

Important fields:
- Location → Where the package is installed.
- Requires → Dependencies needed by the package.


# PyMuPDF

## Why do we need it?

Python's built-in `open()` cannot extract readable text from PDF files because PDFs are complex document formats.

PyMuPDF reads PDF files and extracts their text so it can be processed by the RAG pipeline.

## RAG Flow

PDF
↓
PyMuPDF
↓
Extract Text
↓
Chunking
↓
Embeddings
↓
Vector Database
↓
LLM

# Sentence Transformers

## What is it?

A Sentence Transformer converts text into embeddings (vectors).

Example:

"I love AI."

↓

[-0.001, 0.074, -0.015, ...]

## What is an Embedding?

An embedding is a list of numbers that represents the meaning of a piece of text.

The model places sentences with similar meanings close together in a high-dimensional vector space.

## Why are embeddings important?

They allow semantic search.

Instead of matching exact words, we compare embeddings to find similar meanings.

## Why 384?

The model `all-MiniLM-L6-v2` represents each sentence using a vector of **384 numbers**.


# Chunking

## Definition

Chunking is the process of splitting a large document into smaller pieces (chunks) before creating embeddings.

## Why is chunking needed?

- Sending an entire PDF to the LLM increases token usage and API cost.
- A single embedding for the whole document cannot retrieve specific information.
- Chunking allows each section of the document to be searched independently.

## Chunk Flow

PDF
↓
Extract Text
↓
Split into Chunks
↓
Create an Embedding for each Chunk
↓
Store Embeddings in a Vector Database

## Chunk Size

Chunk size defines how much text is stored in one chunk.

Examples:
- 300 words
- 500 characters
- 500 tokens

## Chunk Overlap

Chunk overlap repeats a portion of one chunk at the beginning of the next chunk to preserve context.

Example:

Chunk Size = 100 words
Overlap = 20 words

Chunk 1:
Words 1–100

Chunk 2:
Words 81–180

## Why not create one chunk for the entire PDF?

- Retrieval becomes less precise.
- The entire PDF is returned for every question.
- Higher token usage and API cost.
- Slower responses due to unnecessary context.


# RecursiveCharacterTextSplitter

## What is it?

A LangChain text splitter that recursively splits text while trying to preserve meaningful boundaries such as paragraphs, new lines, and sentences.

## Why use it?

Instead of splitting text randomly, it attempts to keep related information together.

## Parameters

### chunk_size

Maximum size of each chunk.

Example:

chunk_size = 300

### chunk_overlap

Repeats a portion of one chunk at the beginning of the next chunk.

Example:

chunk_size = 300
chunk_overlap = 50

This preserves context between adjacent chunks.

## Workflow

Large Text
↓

RecursiveCharacterTextSplitter

↓

Chunk 1

Chunk 2

Chunk 3

