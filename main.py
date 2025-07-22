from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.1")

template = """
You are a Pokemon expert. You know everything about Pokemon, including their types, abilities, and evolutions.
You will be given a question about Pokemon, and you should answer it in detail.

Here is some relevant pokemon info: {pokeInfo}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while true:
    print("\n\n-------------------------------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    result = chain.invoke({"pokeInfo": [], "question": question})
    print(result)
