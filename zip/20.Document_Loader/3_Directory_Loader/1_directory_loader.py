from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="./20.Document_Loader/3_Directory_Loader/books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# docs = loader.load()  ## prepare at once and load at once
docs = loader.lazy_load()  ## load documents one by one in memory and load and blank memory

# print(len(docs))
# print(docs)
# print(docs[0].page_content)
# print(docs[0].metadata)

for document in docs:
    print(document.metadata)