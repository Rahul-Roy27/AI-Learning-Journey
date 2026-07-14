import streamlit as st
import os
from rag_backend import create_collection,index_pdf

# Initialize session state :-> If this is the first time the app is running, create a variable called indexed and set it to False.
if "indexed" not in st.session_state:
    st.session_state.indexed = False

# Page Title
st.title("📄 AI PDF Assistant")

# Short Description
st.markdown(
    """
    Upload a PDF and ask questions about its contents using Retrieval-Augmented Generation (RAG) powered by Gemini.
    """
)

# Upload Section
st.header("📂 Upload Your PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type="pdf"
)

#to check if file is uploaded or not
if uploaded_file is not None:
        # SAVE PDF
    st.write(f"**Uploaded File:** {uploaded_file.name}")   
    # Create the file path
    pdf_path = os.path.join("documents", uploaded_file.name)
    # Save the uploaded PDF
    with open(pdf_path, "wb") as file:
        file.write(uploaded_file.getbuffer())
    st.success("PDF saved successfully!")  
        #INDEXING THE PDF
    if st.button("Index PDF"):

        st.write("Button clicked!")
        print("Button clicked!")

        collection = create_collection(pdf_path)

        print("Collection created!")

        index_pdf(collection, pdf_path)

        print("Indexing completed!")

        st.session_state.indexed = True
        st.success("PDF indexed successfully!")

# Question Input
if st.session_state.indexed:

    st.header("💬 Chat with your PDF")

    user_question = st.chat_input(
        "Ask anything about the uploaded PDF..."
    )

    if user_question:
        st.chat_message("user").write(user_question)
    
    