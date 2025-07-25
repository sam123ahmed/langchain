from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model1 = ChatOpenAI()

model2 = ChatAnthropic(model_name="claude-3-7-sonnet-20250219")

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=["text"]    
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answers from the following text \n {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template = "Merge the provided notes and quiz into a single document \n notes-> {notes} and quiz-> {quiz}",
    input=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text="""
Long text here
"""
result = chain.invoke({"text": text})

print(result)

chain.get_graph().print_ascii()
