from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} to a 10-year-old."
)

print(prompt.format(topic="embeddings"))
