from langchain.llms  import Ollama
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GPT4AllEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

ollama = Ollama(base_url='http://localhost:11434', model = 'mistral')

loader = WebBaseLoader('https://en.wikipedia.org/wiki/Artificial_intelligence')
data = loader.load()
print(data)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)

all_splits = text_splitter.split_documents(data)

vector_store = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

qachain = RetrievalQA.from_chain_type(ollama, retriever = vector_store.as_retriever())

question  = "What is AI?"
print (qachain({"query":question}))




