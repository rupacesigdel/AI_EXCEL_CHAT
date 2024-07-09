import mindsdb_sdk
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

try:
    connection = mindsdb_sdk.connect(settings.MINDSDB_SERVER)
    logger.info("Successfully connected to MindsDB.")
except Exception as e:
    logger.error("Error connecting to MindsDB: %s", str(e))

def predict_with_mindsdb(user_message, model_name='excel_knowledge_model'):
    try:
        query = f"""
        SELECT answer
        FROM {model_name}
        WHERE question ILIKE '%{user_message}%'
        """
        result = connection.query(query)
        return result.to_dict()  # Convert result to dictionary
    except Exception as e:
        logger.error("Error in predict_with_mindsdb: %s", str(e))
        return {"error": str(e)}
    