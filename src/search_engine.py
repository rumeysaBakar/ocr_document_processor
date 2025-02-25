from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class SearchEngine:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key="")
        self.vectorstore = Chroma(persist_directory="outputs/vectorstore", embedding_function=self.embeddings)

    def index_document(self, text_path):
        with open(text_path, "r") as f:
            documents = [{"text": f.read()}]
        self.vectorstore.add_documents(documents)
        print(f"{text_path} dosyası dizine eklendi.")

    def query(self, question):
        retriever = self.vectorstore.as_retriever()
        chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=retriever)
        response = chain.run(question)
        return response
