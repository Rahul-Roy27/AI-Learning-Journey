import pymupdf

# open pdf files
doc = pymupdf.open("../Syllabus/Artificial Intelligence with Machine Learning.pdf")

print(f'Total Pages : {len(doc)}')
print("-" * 50)

#read every page
all_text = ""
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()
    
    #But in RAG, we usually want one big string containing the entire document.
    all_text += text + "\n" # ---> add this page's text to all_text
    print(f"\n------Page {page_num+1}-----\n")
    # print(text)
    
doc.close()

print("\n" + "=" * 60)
print("COMPLETE DOCUMENT")
print("=" * 60)

print(all_text)


