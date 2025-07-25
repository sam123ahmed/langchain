from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="write a summary for the following poem - {poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()

loader = TextLoader("./20.Document_Loader/1_Text_Loader/cricket.txt", encoding="utf-8")

docs = loader.load()



print(docs)
print(type(docs))
print(len(docs))
print(docs[0])
print(docs[0].metadata)
print(docs[0].page_content)
print(type(docs[0]))



chain = prompt | model | parser

result = chain.invoke({"poem": docs[0].page_content})

print(result)