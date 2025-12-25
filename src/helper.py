from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.embeddings import Embeddings
import os
import requests
import time


class RobustHFEmbeddings(Embeddings):
    def __init__(self, api_key, model_name):
        self.api_url = f"https://router.huggingface.co/models/{model_name}"
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def embed_documents(self, texts):
        try:
            response = requests.post(
                self.api_url, 
                headers=self.headers, 
                json={"inputs": texts, "options": {"wait_for_model": True}}
            )
            result = response.json()
        except Exception as e:
            raise ValueError(f"Connection Error: {e}")


        if isinstance(result, dict) and 'error' in result:
            print(f"❌ HF API Error: {result}")
            raise ValueError(f"Hugging Face API Error: {result['error']}")
            
        return result

    def embed_query(self, text):
        result = self.embed_documents([text])
        return result[0]


def load_pdf_file(data):
    loader = DirectoryLoader(data,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

def download_hugging_face_embeddings():
    embeddings = RobustHFEmbeddings(
        api_key=os.environ.get("HUGGINGFACEHUB_API_TOKEN"),
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings
