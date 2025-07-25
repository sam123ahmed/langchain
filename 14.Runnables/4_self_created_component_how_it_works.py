import random

## for llm component
class NakliLLM:

    def __init__(self):
        print("LLM Created")

    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for the artificial intelligence"
        ]

        return {"response": random.choice(response_list)}

llm = NakliLLM()

llm.predict("what is the capital of india")


## for prompt template component
class NakliPromptTemplate:

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)

template = NakliPromptTemplate(
    template="write a {length} poem about {topic}",
    input_variables=["length", "topic"]
)

prompt = template.format({"length": "short", "topic": "india"})

llm = NakliLLM()

llm.predict(prompt)


## llm chain component
class NakliLLMChain:

    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)
        return result["response"]

template = NakliPromptTemplate(
    template="write a {length} poem about {topic}",
    input_variables=["length", "topic"]
)

llm = NakliLLM()

chain = NakliLLMChain(llm, template)

chain.run({"length": "short", "topic": "india"})