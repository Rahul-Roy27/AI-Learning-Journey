import streamlit as st
import os
from rag_backend import (
    create_collection,
    index_pdf,
    generate_answer,
)


if "collection" not in st.session_state:
    st.session_state.collection = None  
if "messages" not in st.session_state:
    st.session_state.messages = [] 
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

    # Save the uploaded PDF locally if it doesn't already exist
    if not os.path.exists(pdf_path):
        with open(pdf_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        st.success("PDF saved successfully!")
    else:
        st.info("PDF already exists.")

        #INDEXING THE PDF
    if st.button("Index PDF"):

        try:
            st.session_state.collection = create_collection(pdf_path)

            index_pdf(
                st.session_state.collection,
                pdf_path,
            )

            st.session_state.indexed = True
            st.success("PDF indexed successfully!")

        except Exception as e:
            st.error(f"Failed to index PDF.\n\n{e}")


# Question Input
if st.session_state.indexed:
    st.header("💬 Chat with your PDF")
    # Display previous chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    user_question = st.chat_input(
        "Ask anything about the uploaded PDF..."
    )
    if user_question:
        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_question
            }
        )
        with st.chat_message("user"):
            st.write(user_question)
            
        # Generate the answer using the backend
        with st.spinner("Generating answer..."):
            try:
                answer, context = generate_answer(
                    st.session_state.collection,
                    user_question
                )
            except Exception as e:
                st.error(f"Failed to generate answer.\n\n{e}")
                st.stop()
                
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
        
        # Display the AI's response
        with st.chat_message("assistant"):
            st.write(answer)
        # Display the retrieved context
        with st.expander("📚 Retrieved Context"):
            st.write(context)
    
    