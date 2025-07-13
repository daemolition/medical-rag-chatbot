import os
from dotenv import load_dotenv

load_dotenv()

# Configuration variables for the application.

HF_TOKEN = os.getenv(
    "HF_TOKEN"
)  #: Your Hugging Face API token. Required for interacting with Hugging Face models and datasets.

<<<<<<< HEAD
HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"  #: The ID of the Mistral-7B-Instruct-v0.3 model repository on Hugging Face.
DB_FAISS_PATH = "vectoresore/db_faiss"  #:  The path to the FAISS index used for storing and retrieving embeddings.
=======

DB_FAISS_PATH = "vectorestore/db_faiss"  #:  The path to the FAISS index used for storing and retrieving embeddings.
>>>>>>> a845227 (new config)
DATA_PATH = (
    "data/"  #: The directory path where your training/processing data is located.
)
CHUNK_SIZE = 500  #: The number of data points to process in each batch.
CHUNK_OVERLAP = 50  #: The number of data points to overlap between consecutive batches.
<<<<<<< HEAD
=======
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3.1-8b-instruct"
>>>>>>> a845227 (new config)
