from langchain_huggingface import HuggingFaceEmbeddings

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def get_embedding_model():
    """
    Initializes and returns a HuggingFace embedding model.

    Returns:
        HuggingFaceEmbeddings: An instance of the HuggingFaceEmbeddings model.

    Raises:
        CustomException: If there are errors while initializing and loading the embedding model.
    """
    
    try:
        logger.info("Initializing the huggingface embedding model")
        
        model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-l6-v2")
        
        logger.info("Huggingface embedding model loaded successfully")
        return model
    
    except Exception as e:
        error_message = CustomException("Error occured while loading embedding mode", e)
        logger.error(str(error_message))
        raise error_message