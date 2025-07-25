from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

## same output
# chat_template = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful {domain} expert"),
#     ("human", "Explain in simple terms, what is {topic}")
# ])

prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})

print(prompt)

