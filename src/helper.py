from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings 
import os

# Extract Data From the PDF File
def load_pdf_file(data):
    loader = DirectoryLoader(data,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

# Split the Data into Text Chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

# Download the Embeddings from HuggingFace
def download_hugging_face_embeddings():
    # Uses the cloud API (Lightweight) instead of local download (Heavy)
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=os.environ.get("HUGGINGFACEHUB_API_TOKEN"),
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings
