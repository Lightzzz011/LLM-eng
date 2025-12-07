from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("Explain {topic}.")
llm = ChatOpenAI(model="gpt-4o-mini")

chain = RunnableSequence([prompt, llm])

print(chain.invoke({"topic": "RAG"}))
