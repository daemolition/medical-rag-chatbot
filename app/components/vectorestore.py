import os

from langchain_community.vectorstores import FAISS

from app.components.embeddings import get_embedding_model
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import DB_FAISS_PATH


logger = get_logger(__name__)


def load_vectore_store():
    """
    Loads an existing FAISS vector store.

    Loads a pre-existing FAISS vector store from the specified path.

    Returns:
        FAISS: The loaded FAISS vector store.
    Raises:
        CustomException: If an error occurs during the loading process.
    """
    try:
        embedding_model = get_embedding_model()
        
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading existing vectorestore")
            return FAISS.load_local(
                DB_FAISS_PATH,
                embeddings=embedding_model,
                allow_dangerous_deserialization=True
            )
        else:
            logger.warning("No vectorestore found")
    
    except Exception as e:
        error_message = CustomException("Failed to load vectorestore", e)
        logger.error(str(error_message))
        raise error_message
    
    
def save_vectore_store(text_chunks):
    """
    Saves a new vector store.
    Creates a new FAISS vector store and saves it to the specified path.

    Args:

    """
    try:
        
        if not text_chunks:
            raise CustomException("No chunks found")
        
        logger.info("Generating new vectorestore")
        
        embedding_model = get_embedding_model()
        
        db = FAISS.from_documents(text_chunks, embedding=embedding_model)
        
        logger.info("Saving to vectorestore")
        
        db.save_local(DB_FAISS_PATH)
        
        logger.info("Vectorestore saved successfully")
    
    except Exception as e:
        error_message = CustomException("Failed create new vectorestore", e)
        logger.error(str(error_message))
        raise error_message
