# !pip install langchain chromadb faiss-cpu openai tiktoken langchain_openai langchain-community wikipedia

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document


# Step 1: your source documents
documents = [
    Document(page_content="Langchain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models.")    
]


# Step 2: Initialize embedding model
embedding_model = OpenAIEmbeddings()

# Step 3: Create chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)


# Step 4: Convert vectorstore into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})


query = "what is chroma used for?"
results = retriever.invoke(query)



for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)





results = vectorstore.similarity_search(query, k=2)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)