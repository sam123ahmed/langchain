from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('./20.Document_Loader/2_Py_PDF_Loader/dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)