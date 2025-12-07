from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke("Explain RAG simply.")
print(response)
