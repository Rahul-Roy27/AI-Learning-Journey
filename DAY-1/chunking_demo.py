import pymupdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
# -------------------------------
# Step 1: Read the PDF
# -------------------------------

doc = pymupdf.open("../Syllabus/Artificial Intelligence with Machine Learning.pdf")

all_text = ""
for page in doc:
    all_text += page.get_text()
doc.close()

# -------------------------------
# Step 2: Create the Text Splitter
# -------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 50,
)

# -------------------------------
# Step 3: Split the text
# -------------------------------

chunks = text_splitter.split_text(all_text)

# -------------------------------
# Step 4: Print the results
# -------------------------------

print(f'Total Chunks : {len(chunks)} \n')
for i,chunk in enumerate(chunks):
    print("=" * 60)
    print(f'chunk {i+1}')
    print("=" * 60)
    print(chunk)
    print()