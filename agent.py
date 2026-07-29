from langchain_openai import ChatOpenAI

from config import MODEL_NAME, TEMPERATURE, OPENAI_API_KEY
from prompt import CHAT_PROMPT


llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    api_key=OPENAI_API_KEY
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