from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableBranch, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="write a detail report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    temlate="Summarize the following text \n {text}",
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

# report_gen_chain = RunnableSequence(prompt1, model, parser)
report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({"topic": "Russia vs Ukrain"})

print(result)