from langchain_groq import ChatGroq
from pydantic import SecretStr

from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import GROQ_API_KEY

logger = get_logger(__name__)


def load_llm(model_name: str = "llama-3.1-8b-instant", groq_api_key: str = GROQ_API_KEY):
    """Loads a large language model (LLM) from the Groq API.

    Args:
        model_name (str, optional): The name of the LLM model to load. Defaults to "llama-3.1-8b-instant".
        groq_api_key (str, optional): The API key for accessing the Groq API. Defaults to the value specified in `app.config.config.GROQ_API_KEY`.

    Returns:
        ChatGroq: The instantiated ChatGroq object representing the loaded LLM.

    Raises:
        CustomException: If an error occurs during the LLM loading process.

    """
    try:
        logger.info("Loading LLM from Groq")
        llm = ChatGroq(
            api_key=SecretStr(groq_api_key),
            model=model_name,
            temperature=0.3,
            max_tokens=256
        )
        
        logger.info("LLM Model loaded successfully")
        return llm

    except Exception as e:
        error_message = CustomException("Failed to load an LLM from Groq", e)
        logger.error(f"str{error_message}")
        raise