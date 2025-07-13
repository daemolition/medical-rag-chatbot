import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import DATA_PATH, CHUNK_OVERLAP, CHUNK_SIZE

logger = get_logger(__name__)


def load_pdf_files():
    """
    Loads PDF files from a specified directory.

    Returns:
        List[langchain.document.Document]: A list of document objects representing the loaded PDFs.
    
    Raises:
        CustomException: If the data path doesn't exist or if there are errors loading the documents.
    """
    
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Data path does not exists")
        
        logger.info(f"Loading files form {DATA_PATH}")
        
        loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        
        if not documents:
            logger.warning("No PDFs found")
        else:
            logger.info(f"Successfully fetched {len(documents)} documents")
        
        return documents
    
    except Exception as e:
        error_message = CustomException("Failed to load PDF", e)
        logger.error(str(error_message))
        raise error_message      



def create_text_chunks(documents): 
    """
    Splits documents into text chunks using a recursive character splitter.

    Args:
        documents (List[langchain.document.Document]): A list of document objects to split.

    Returns:
        List[str]: A list of text chunks.
    
    Raises:
        CustomException: If no documents are provided or if there are errors splitting the documents.
    """
    
    try:
        if not documents:
            raise CustomException("No documents found")
        
        logger.info(f"Splitting {len(documents)} documents into chunks")
        
        text_spitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        
        text_chunks = text_spitter.split_documents(documents=documents)
        
        logger.info(f"Generated {len(text_chunks)} text chunks")
        return text_chunks
    
    except Exception as e:
        error_message = CustomException("Failed to generate chunks", e)
        logger.error(str(error_message))
        raise error_message   


