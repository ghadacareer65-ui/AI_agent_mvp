import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

# قراءة مفتاح Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# إعدادات النموذج
MODEL_NAME = "gemini-2.5-flash"

# درجة الإبداع
TEMPERATURE = 0.3
