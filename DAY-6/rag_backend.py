# Import required libraries
import fitz
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
# Gemini
from google import genai
# Environment Variables
from dotenv import load_dotenv
import os


# Load the Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
print("Embedding model loaded successfully!")


# Function to extract text from a PDF
def extract_text(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    # Variable to store all extracted text
    text = ""
    # Loop through every page
    for page in doc:
        text += page.get_text()
    # Close the PDF
    doc.close()
    # Return the extracted text
    return text

# Function to split extracted text into smaller chunks
def split_text(text):

    # Create a text splitter object
    text_splitter = RecursiveCharacterTextSplitter(

        # Maximum characters in one chunk
        chunk_size=500,

        # Overlap between consecutive chunks
        chunk_overlap=50
    )

    # Split the text into chunks
    chunks = text_splitter.split_text(text)

    # Return the list of chunks
    return chunks

# Function to generate embeddings for all chunks
def create_embeddings(chunks):

    # Generate embeddings for every chunk
    embeddings = embedding_model.encode(chunks)

    # Return the embeddings
    return embeddings


# Function to create a ChromaDB collection
def create_collection(pdf_path):

    # Create a ChromaDB client
    chroma_client = chromadb.PersistentClient(
        path="./chroma_db"
       
    )
    # Get only the PDF filename
    filename = os.path.basename(pdf_path)
    # Remove the .pdf extension
    filename = os.path.splitext(filename)[0]
    # Convert filename into a valid collection name
    collection_name = filename.lower().replace(" ", "_")

    print(f"Collection Name: {collection_name}")

    # Create a collection
    collection = chroma_client.get_or_create_collection(
        name=collection_name
    )
    
    # Print number of chunks in the collection
    print(f"Collection contains {collection.count()} chunks.")
    
    # Return the collection
    return collection


# Function to store chunks and embeddings in ChromaDB
def store_in_chromadb(collection, chunks, embeddings):
    # Generate unique IDs for each chunk
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Create metadata for every chunk
    metadatas = []

    for i in range(len(chunks)):
        metadatas.append(
            {
                "chunk_number": i
            }
        )

    # Store everything in ChromaDB
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

# Function to index the PDF only if it hasn't been indexed before
def index_pdf(collection, pdf_path):
    # Process the PDF only if the collection is empty
    if collection.count() == 0:

        print("Collection is empty. Processing PDF...")
        print("No embeddings found. Indexing PDF...")

        # Extract text from the PDF
        text = extract_text(pdf_path)

        # Split the text into chunks
        chunks = split_text(text)
        

        # Generate embeddings
        embeddings = create_embeddings(chunks)

        # Store chunks and embeddings
        store_in_chromadb(collection, chunks, embeddings)

        print("PDF processed and stored successfully!")
        print("PDF indexed successfully!")

    else:
        print("Collection already exists. Skipping PDF processing.")


# Function to retrieve the most relevant chunks
def retrieve_chunks(collection, question):

    # Convert the user's question into an embedding
    question_embedding = embedding_model.encode(question)

    # Search the collection
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=3
    )

    # Return the retrieved results
    return results




# Load environment variables
load_dotenv()

# Get the Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini Client
gemini_client = genai.Client(api_key=api_key)

