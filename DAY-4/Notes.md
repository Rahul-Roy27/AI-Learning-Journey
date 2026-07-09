# Day 4 - Gemini Integration & First RAG Chatbot

## Objective

Connect the retrieval engine built in Day 3 with a Large Language Model (LLM) to build a complete Retrieval-Augmented Generation (RAG) chatbot.

---

# 1. What is an LLM?

LLM stands for **Large Language Model**.

- **Large** → Trained on massive amounts of text and contains billions of parameters.
- **Language** → Understands and generates human language.
- **Model** → A trained AI system that learns patterns from data.

Examples:
- Google Gemini
- ChatGPT
- Claude
- Llama

LLMs generate text by predicting the next most probable token.

---

# 2. What is a Token?

A token is the smallest unit of text processed by an LLM.

A token may be:
- A word
- Part of a word
- Punctuation
- Spaces

Example:

Sentence:

```
I love AI
```

Possible Tokens:

- I
- love
- AI

Models have a maximum context window measured in tokens.

---

# 3. Normal Chatbot vs RAG Chatbot

## Normal Chatbot

```
User Question
      │
      ▼
     LLM
      │
      ▼
    Answer
```

The LLM answers using only its training knowledge.

---

## RAG Chatbot

```
User Question
      │
      ▼
Question Embedding
      │
      ▼
 Vector Database
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
 Prompt Engineering
      │
      ▼
      LLM
      │
      ▼
    Answer
```

The LLM answers using retrieved information from external documents, reducing hallucinations.

---

# 4. What is an API?

API stands for **Application Programming Interface**.

An API allows one software application to communicate with another by sending requests and receiving responses.

Example:

```
Python Program
      │
      ▼
 Gemini API
      │
      ▼
Google Servers
      │
      ▼
   Response
```

---

# 5. What is an API Key?

An API Key is a unique identifier used to authenticate requests made to an API.

It helps:

- Identify the developer
- Track API usage
- Apply quotas and rate limits
- Secure access to the service

API keys should never be uploaded to GitHub.

---

# 6. Why Does RAG Send Both Context and the User Question?

The retrieved context provides the source of information.

The user's question tells the LLM what information it should extract or explain.

Both are required to generate an accurate response.

Example:

```
Context:
{context}

Question:
{user_question}
```

---

# 7. What is Google Gemini?

Gemini is Google's family of Large Language Models developed by Google DeepMind.

It can:

- Answer questions
- Generate text
- Explain concepts
- Summarize documents
- Write code

In a RAG application, Gemini generates the final answer using the retrieved context.

---

# 8. Why Use Gemini API?

Instead of running an LLM locally, the application sends requests to Google's servers.

Advantages:

- No powerful hardware required
- Faster inference
- Easy integration
- Access to Google's latest models

Workflow:

```
Python Program
      │
      ▼
 Gemini API
      │
      ▼
Google Servers
      │
      ▼
Generated Response
```

---

# 9. Role of ChromaDB and Gemini

## ChromaDB

Responsibilities:

- Store document embeddings
- Store document chunks
- Store metadata
- Perform similarity search
- Retrieve the most relevant chunks

---

## Gemini

Responsibilities:

- Receive retrieved context
- Receive the user's question
- Understand both
- Generate the final answer

Gemini does **not**:

- Read PDFs
- Generate embeddings
- Search ChromaDB

Those tasks are handled by the retrieval pipeline.

---

# 10. Required Libraries

## Google Gemini

```python
from google import genai
```

Used to communicate with Gemini.

---

## python-dotenv

```python
from dotenv import load_dotenv
```

Loads environment variables stored inside a `.env` file.

---

## os

```python
import os
```

Used to access environment variables.

Example:

```python
os.getenv("GEMINI_API_KEY")
```

---

# 11. Reading the API Key Securely

```python
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
```

## load_dotenv()

Reads the `.env` file and loads all variables into Python.

---

## os.getenv()

Retrieves the value of a specific environment variable.

Example:

```
.env
```

```
GEMINI_API_KEY=AIzaSyxxxxxxxx
```

Then:

```python
api_key
```

contains:

```
AIzaSyxxxxxxxx
```

---

# 12. Creating the Gemini Client

```python
gemini_client = genai.Client(api_key=api_key)
```

## Client

`Client` is a **class** provided by the Gemini SDK.

It communicates with Google's servers.

---

## gemini_client

`gemini_client` is an **object** created from the Client class.

Workflow:

```
API Key
   │
   ▼
Gemini Client
   │
   ▼
Gemini API
   │
   ▼
Google Server
   │
   ▼
Response
```

---

# 13. Sending a Prompt

```python
response = gemini_client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
```

## generate_content()

A method used to send prompts to Gemini and generate responses.

---

## model

Specifies which Gemini model should answer.

Example:

```python
model="gemini-2.5-flash"
```

---

## contents

Contains the prompt sent to Gemini.

---

# 14. Response Object

```python
response = gemini_client.models.generate_content(...)
```

Gemini returns a **Response Object**.

It contains:

- Generated text
- Metadata
- Model information
- Other response details

To extract only the answer:

```python
print(response.text)
```

---

# 15. Building the Context

ChromaDB returns retrieved chunks as a Python list.

Example:

```python
retrieved_chunks = [
    "Chunk 1",
    "Chunk 2",
    "Chunk 3"
]
```

Gemini expects one string.

Convert using:

```python
context = "\n\n".join(retrieved_chunks)
```

`join()` combines all chunks into a single string.

`\n\n` inserts blank lines between chunks.

---

# 16. Prompt Engineering

Prompt Engineering is the process of designing prompts that guide an LLM.

A RAG prompt contains:

1. Instructions
2. Context
3. User Question

Example:

```python
prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context provided below.

Context:
{context}

Question:
{user_question}

If the answer is not present in the context, reply:
"I couldn't find that information in the document."
"""
```

---

# 17. Grounding

Grounding means forcing the LLM to answer using the retrieved document instead of relying only on its training knowledge.

Grounding reduces hallucinations and produces more reliable responses.

---

# 18. Hallucination Prevention

Without retrieved context, an LLM may answer from its own knowledge.

By providing context and adding instructions such as:

```
If the answer is not present in the context,
say:
"I couldn't find that information in the document."
```

the model is less likely to hallucinate.

---

# 19. Continuous Conversation

Instead of answering one question and exiting, the chatbot continuously accepts questions using a `while` loop.

Example:

```python
while True:
```

The conversation ends when the user types:

```
done
```

---

# 20. Complete Gemini Workflow

```
Start Program
      │
      ▼
Import Libraries
      │
      ▼
Read .env
      │
      ▼
Retrieve API Key
      │
      ▼
Create Gemini Client
      │
      ▼
Take User Input
      │
      ▼
Generate Prompt
      │
      ▼
Gemini API
      │
      ▼
Receive Response Object
      │
      ▼
Extract response.text
      │
      ▼
Display Answer
```

---

# 21. Complete RAG Pipeline

```
PDF
 │
 ▼
Extract Text
 │
 ▼
Split into Chunks
 │
 ▼
Generate Embeddings
 │
 ▼
Store in ChromaDB
 │
 ▼
User Question
 │
 ▼
Generate Question Embedding
 │
 ▼
Retrieve Top-3 Relevant Chunks
 │
 ▼
Combine Chunks into Context
 │
 ▼
Build RAG Prompt
 │
 ▼
Gemini API
 │
 ▼
Generate Final Answer
 │
 ▼
Display Response
```

---

# What I Learned in Day 4

By the end of Day 4, I can:

- Integrate Gemini API into a Python application.
- Securely manage API keys using `.env`.
- Create a Gemini client.
- Send prompts to Gemini.
- Handle Response Objects.
- Retrieve relevant document chunks from ChromaDB.
- Build context using retrieved chunks.
- Design RAG prompts.
- Perform context injection.
- Reduce hallucinations using prompt engineering.
- Build a complete command-line RAG chatbot.