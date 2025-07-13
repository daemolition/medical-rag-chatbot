from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from app.components.llm import load_llm
from app.components.vectorestore import load_vectore_store
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """
    Answer the following medical question in 2-3 lines maximum using only the information 
    provided in the context.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
<<<<<<< HEAD


def set_custom_prompt():
    return PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE, input_variables=["context", "question"]
    )


def create_qa_chain():
    try:
        logger.info("Loading vectorestore for context")
        db = load_vectore_store()

        if db is None:
            raise CustomException("Vectorestore not present or empty")

        llm = load_llm()

        if llm is None:
            raise CustomException("LLM not loaded")

=======
    
def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE, input_variables=["context", "question"])


def create_qa_chain():
    try:        
        logger.info("Loading vectorestore for context")
        db = load_vectore_store()
        
        if db is None:
            raise CustomException("Vectorestore not present or empty")
        
        llm = load_llm()
                
        if llm is None:
            raise CustomException("LLM not loaded")        

        
>>>>>>> 16a58f6 (Final changes)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k": 1}),
            return_source_documents=False,
<<<<<<< HEAD
            chain_type_kwargs={"prompt": set_custom_prompt()},
        )

        logger.info("Successfully created qa chain")

        return qa_chain

    except Exception as e:
        error_message = CustomException("Error while creating chain", e)
        logger.error(str(error_message))
        raise error_message
=======
            chain_type_kwargs={'prompt': set_custom_prompt()}
        )
        
        logger.info("Successfully created qa chain")
        
        return qa_chain
        
    except Exception as e:
        error_message = CustomException("Error while creating chain", e)
        logger.error(str(error_message))
        raise error_message
>>>>>>> 16a58f6 (Final changes)
