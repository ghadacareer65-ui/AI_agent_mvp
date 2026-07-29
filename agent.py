from langchain_google_genai import ChatGoogleGenerativeAI

from config import MODEL_NAME, TEMPERATURE, GOOGLE_API_KEY
from prompt import CHAT_PROMPT


llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    google_api_key=GOOGLE_API_KEY
)

chain = CHAT_PROMPT | llm


def generate_draft(user_input, admin_feedback=""):
    response = chain.invoke(
        {
            "user_input": user_input,
            "admin_feedback": admin_feedback
        }
    )

    return response.content
