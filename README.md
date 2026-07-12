# AI Learning Journey

This repository documents my journey of learning Artificial Intelligence and building a Retrieval-Augmented Generation (RAG) application from scratch using Python, LangChain, ChromaDB, Sentence Transformers, and Google Gemini.

---

## 📅 Day 1 – AI Fundamentals & Document Processing

### Theory

* Artificial Intelligence (AI)
* Machine Learning (ML)
* Deep Learning (DL)
* Large Language Models (LLMs)
* Hallucinations
* Retrieval-Augmented Generation (RAG)
* Embeddings

### Practical

* PDF Extraction using PyMuPDF
* Text Chunking using LangChain
* Embedding Generation using Sentence Transformers

---

## 📅 Day 2 – Vector Database & Semantic Retrieval

### Theory

* Vector Databases
* ChromaDB
* Collections
* IDs & Metadata
* Similarity Search
* Top-K Retrieval
* Semantic Search

### Practical

* Store Embeddings in ChromaDB
* Perform Semantic Search
* Retrieve Top-K Relevant Chunks

---

## 📅 Day 3 – Real Embeddings & Retrieval Pipeline

### Theory

* Sentence Transformers
* Real 384-Dimensional Embeddings
* Question Embeddings
* Retrieval Pipeline Design

### Practical

* PDF → Chunk → Embedding Pipeline
* Store Real Embeddings in ChromaDB
* Retrieve Relevant Chunks from Real Documents
* Build a Complete Retrieval Engine

---

## 📅 Day 4 – Gemini Integration & First RAG Chatbot

### Theory

* Google Gemini API
* API Keys & Environment Variables
* Prompt Engineering
* Context Injection
* Grounding
* Hallucination Prevention

### Practical

* Integrated Gemini API
* Built a Complete RAG Chatbot
* Connected ChromaDB with Gemini
* Retrieved Top-3 Relevant Chunks
* Generated Grounded Responses
* Implemented Continuous Question Answering Loop

---

## 📅 Day 5 – Persistent ChromaDB & Backend Refactoring

### Theory

* Persistent vs In-Memory Vector Databases
* ChromaDB PersistentClient
* Collection Management
* Dynamic Collection Names
* Document Indexing
* Code Refactoring
* Modular Backend Design

### Practical

* Switched from In-Memory to Persistent ChromaDB
* Stored Vector Database on Disk
* Automatically Created Collections Based on PDF Names
* Implemented Automatic Collection Loading
* Skipped Re-Indexing for Previously Indexed PDFs
* Refactored Indexing Logic into a Dedicated `index_pdf()` Function
* Improved Overall RAG Backend Structure

---

## 🚀 Upcoming

* Day 6 – Streamlit UI
* Day 7 – Deploy the RAG Chatbot
* Final Project – Production-Inspired RAG Application

---

## 🛠️ Technologies Used

* Python
* PyMuPDF
* LangChain
* ChromaDB
* Sentence Transformers
* Google Gemini API
* python-dotenv

---

## 🎯 Final Goal

Build a production-inspired Retrieval-Augmented Generation (RAG) chatbot capable of answering questions accurately from custom PDF documents using semantic search, persistent vector storage, and Google's Gemini LLM.
