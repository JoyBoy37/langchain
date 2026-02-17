from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://google.com")
docs = loader.load()
print("Number of pages loaded: "+str(len(docs)))
pageOne = docs[0]
print(pageOne.page_content)