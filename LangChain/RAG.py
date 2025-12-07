from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Load your data
loader = TextLoader("data.txt")
docs = loader.load()

# Split
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# Embeddings
embeddings = OpenAIEmbeddings()

# Vector DB
db = Chroma.from_documents(chunks, embeddings)

# Retrieval
retriever = db.as_retriever()

# RAG chain
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model="gpt-4o-mini")

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

print(qa.invoke({"query": "What is explained in the document?"}))
