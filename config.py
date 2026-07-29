import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة من ملف .env
load_dotenv()

# قراءة مفتاح OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# إعدادات النموذج
MODEL_NAME = "gpt-4.1-mini"

# درجة الإبداع
TEMPERATURE = 0.3       