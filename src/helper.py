from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.embeddings import Embeddings
from huggingface_hub import InferenceClient
import os
import time

# --- Robust Embedding Class using Official Client ---
class RobustHFEmbeddings(Embeddings):
    def __init__(self, api_key, model_name):
        self.client = InferenceClient(api_key=api_key)
        self.model_name = model_name

    def embed_documents(self, texts):
        # We attempt the request with a retry loop for stability
        retries = 3
        for attempt in range(retries):
            try:
                # The client handles the URL and "wait_for_model" logic automatically
                response = self.client.feature_extraction(
                    texts, 
                    model=self.model_name,
                )
                
                # Convert numpy/tensor result to standard list for Pinecone
                if hasattr(response, "tolist"):
                    return response.tolist()
                return response

            except Exception as e:
                print(f"⚠️ Attempt {attempt + 1} failed: {e}")
                if attempt < retries - 1:
                    time.sleep(2)  # Wait 2 seconds before retrying
                else:
                    # If all retries fail, return empty embeddings to prevent crash
                    # (Returns a list of 384 zeros, which matches MiniLM dimension)
                    print("❌ All retries failed. Returning empty embeddings.")
                    return [[0.0] * 384 for _ in texts]

    def embed_query(self, text):
        result = self.embed_documents([text])
        if isinstance(result, list):
            return result[0]
        return result

# --- Original Helper Functions ---

def load_pdf_file(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

def download_hugging_face_embeddings():
    # Using the official client is much safer than manual URL requests
    embeddings = RobustHFEmbeddings(
        api_key=os.environ.get("HUGGINGFACEHUB_API_TOKEN"),
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings
