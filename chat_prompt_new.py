import os
import streamlit as st
import vertexai
from langchain_google_vertexai import ChatVertexAI,VertexAIEmbeddings #pip install -U langchain-google-vertexai
from langchain.prompts import PromptTemplate
from scripts.utils import read_contents,split
from langchain_community.document_loaders import TextLoader #pip install langchain_community
from langchain_community.vectorstores import FAISS 
#from langchain_openai import OpenAIEmbeddings #pip install langchain_openai
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains import RetrievalQA

from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

#vertexai.init(project="fiery-palace-418612", location="us-central1")
#user_message='talking points'
#response_file_path='C:\\Users\\ajain2\\Downloads\\minutes_generator\\minutes_generator\\customer_conversation_input.txt'

def create_llm(user_message,response_file_path):
    print(user_message,response_file_path)
    loader = TextLoader(f'{response_file_path}')
    splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=20,
    )
    llm = ChatVertexAI(model_name="chat-bison-32k@002", streaming=True)
    embeddings = VertexAIEmbeddings(model_name='textembedding-gecko@003')
    documents = loader.load()
    #print(f'len of doc {len(documents)}')
    docs = splitter.split_documents(documents)
    #print(f'no of chunks {len(docs)}')
    db = FAISS.from_documents(docs, embeddings)
    #print(db.size())
    retriever = db.as_retriever()

    # Define the template to be passed to the LLM
    template = "Answer:"

    # Define the Question-Answer system with template
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    # Define the question
    
    #question = user_message
    #print(question)
    # Perform question answering using the QA system
    #result = retriever.invoke(question)
    result=db.similarity_search(user_message)
    #result = retriever.invoke({"query": question})  # Use invoke method instead of __call__
    return result[0].page_content

    #answer=result.get("result","Irrelevant message:No relevant data found")
    
    #return answer

    #except Exception as e:
    #    print("An error occurred:", e)
    #    return "Try again"
#create_llm(user_message,response_file_path)