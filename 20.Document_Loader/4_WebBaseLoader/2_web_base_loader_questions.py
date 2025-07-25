from langchain_community.document_loaders import WebBaseLoader, TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text - \n {text}",
    input_variables=["question", "text"]
)

parser = StrOutputParser()



url="https://www.flipkart.com/apple-macbook-air-m2-8-gb-256-gb-ssd-mac-os-monterey-mly33hn-a/p/itmdc5308fa78421?pid=COMGFB2GMCRXZG85&lid=LSTCOMGFB2GMCRXZG855GPGWQ&marketplace=FLIPKART&cmpid=content_computer_22491449648_x_8965229628_gmc_pla&tgi=sem,1,G,11214002,x,,,,,,,c,,,,,,,&entryMethod=22491449648&&cmpid=content_22491449648_gmc_pla&gad_source=1&gad_campaignid=22491456398&gbraid=0AAAAADxRY58z2HjGuFSX1xTmjVZ68DyQ6&gclid=CjwKCAjw7fzDBhA7EiwAOqJkh9-J4gKoyuYrvZIqhwmxvJ6K9I8ttwWanf3iM2eL-MRKtw7pbkBnnxoCoToQAvD_BwE"
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | print

result = chain.invoke({"question": "what is the product that we are talking about ?", "text": docs[0].page_content})

print(result)