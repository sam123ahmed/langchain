from abc import ABC, abstractmethod

class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass

import random

class NakliLLM(Runnable):

    def __init__(self):
        print("LLM Created")

    def invoke(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for the artificial intelligence"
        ]

        return {"response": random.choice(response_list)}

    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for the artificial intelligence"
        ]

        return {"response": random.choice(response_list)}


llm = NakliLLM()

class NakliPromptTemplate(Runnable):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)


class NakliStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data["response"]

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data



template = NakliPromptTemplate(
    template="write a {length} poem about {topic}",
    input_variables=["length", "topic"]
)


llm = NakliLLM()


parser = NakliStrOutputParser()


chain = RunnableConnector([template, llm, parser])


chain.invoke({"length": "long", "topic": "India"})




template1 = NakliPromptTemplate(
    template = "write a joke about {topic}",
    input_variables=["topic"]
)



template2 = NakliPromptTemplate(
    template="Explain the following joke {response}",
    input_variables=["response"]
)


llm = NakliLLM()


parser = NakliStrOutputParser()


chain1 = RunnableConnector([template1, llm])

chain2 = RunnableConnector([template2, llm, parser])

final_chain = RunnableConnector([chain1, chain2])

final_chain.invoke({"topic": "cricket"})