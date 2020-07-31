import dialogflow_v2 as dialogflow
import os
from dialogflow_v2.types import TextInput, QueryInput
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials.json'

def send_text_dialog(project_id, session_id, texts, language_code, private_key):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    text_input = TextInput(text=texts, language_code=language_code)
    query_input = QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    a = {
        'text': response.query_result.fulfillment_text,
        'intent': response.query_result.intent.display_name
    }
    return(a)