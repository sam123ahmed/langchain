from langchain.schema.runnable import RunnableLambda

def word_counter(text):
    return len(text.split())

runnable_word_counter =  RunnableLambda(word_counter)

result = runnable_word_counter.invoke("Hi there how are you?")

print(result)