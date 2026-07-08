# Import required libraries
import fitz
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# Load the Embedding Model
model = SentenceTransformer("all-MiniLM-L6-v2")
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
    embeddings = model.encode(chunks)

    # Return the embeddings
    return embeddings


# Function to create a ChromaDB collection
def create_collection():

    # Create a ChromaDB client
    client = chromadb.Client()

    # Create a collection
    collection = client.create_collection(
        name="rag_documents"
    )

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
    
# Function to retrieve the most relevant chunks
def retrieve_chunks(collection, question):

    # Convert the user's question into an embedding
    question_embedding = model.encode(question)

    # Search the collection
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=3
    )

    # Return the retrieved results
    return results


# Main function
if __name__ == "__main__":

    # Path to the PDF
    pdf_path = "../Syllabus/Artificial Intelligence with Machine Learning.pdf"

    # Step 1: Extract text from the PDF
    pdf_text = extract_text(pdf_path)

    # Step 2: Split the text into chunks
    chunks = split_text(pdf_text)

    # Step 3: Generate embeddings
    embeddings = create_embeddings(chunks)
    
    # Create a ChromaDB collection
    collection = create_collection()

    # Store chunks and embeddings
    store_in_chromadb(collection, chunks, embeddings)

    print("Chunks stored successfully!")

    # Print information
    print(f"Total Chunks: {len(chunks)}")
    print(f"Total Embeddings: {len(embeddings)}")
    print(f"Embedding Dimension: {len(embeddings[0])}")
    
    # Ask a question
    question = "What is Artificial Intelligence?"

    # Retrieve the most relevant chunks
    results = retrieve_chunks(collection, question)

    print("\nRetrieved Chunks:\n")

    # Print every retrieved chunk
    for i, document in enumerate(results["documents"][0], start=1):

        print(f"Chunk {i}:")
        print(document)

        print("-" * 50)
