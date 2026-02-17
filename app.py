from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("data/MachineLearning-Lecture01.pdf")
pages = loader.load()
print("Number of pages loaded: "+str(len(pages)))
second_page = pages[1]
print(second_page.page_content[0:100])
print(second_page.metadata)