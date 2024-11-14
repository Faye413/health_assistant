from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from health_assistant.config import set_openai_key
from langchain.schema import Document
import pickle

api_key = set_openai_key()
embedding_model = OpenAIEmbeddings(api_key=api_key)

def create_faiss_index(texts, embedding_model):
    # Convert texts to Document objects
    documents = [
        Document(page_content=text) for text in texts
    ]
    
    # Create FAISS index from documents
    faiss_index = FAISS.from_documents(documents, embedding_model)
    
    # Save the index
    with open("faiss_index.pkl", "wb") as f:
        pickle.dump(faiss_index, f)
    return faiss_index

def create_rag_system(llm):
    # Load or create the FAISS index
    try:
        with open("faiss_index.pkl", "rb") as f:
            faiss_index = pickle.load(f)
        print("FAISS index loaded successfully.")
    except FileNotFoundError:
        print("FAISS index not found. Creating a new index...")
        texts = [
            "Sleep hygiene practices can improve sleep quality.",
            "Regular exercise helps maintain a healthy heart rate.",
            "Nutritional foods contribute to overall well-being."
        ]
        faiss_index = create_faiss_index(texts, embedding_model)
        print("FAISS index created and saved.")

    # Set up the retriever from the FAISS index
    retriever = faiss_index.as_retriever()

    # Create and return the RetrievalQA chain
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
        )