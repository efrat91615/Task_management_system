import os
import ssl
import httpx
from google import genai
from dotenv import load_dotenv
import todo_service

load_dotenv()
original_init = httpx.Client.__init__
def patched_init(self, *args, **kwargs):
    kwargs['verify'] = False
    original_init(self, *args, **kwargs)
httpx.Client.__init__ = patched_init
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
print("Available models:")
try:
    for model in client.models.list():
        print(f"  - {model.name}")
except Exception as e:
    print(f"Could not list models: {e}")

def agent(query):
    try:
        chat = client.chats.create(
            model='models/gemini-flash-lite-latest',
            config={
                'tools': [todo_service.get_tasks, todo_service.add_task, todo_service.update_task_status, todo_service.delete_task],
                'system_instruction': """אתה עוזר ניהול משימות. כשמוסיפים משימה, השתמש בערכים אלה:
- task_type: "מטלה יומית" (אם לא צוין)
- start_date: התאריך הנוכחי
- end_date: התאריך הנוכחי
- status: "ממתין" (אם לא צוין)
ענה בעברית."""
            }
        )
        response = chat.send_message(query)
        return response.text if response.text else "הפעולה בוצעה."
    except Exception as e:
        print(f"DEBUG: {str(e)}")
        return f"שגיאה: {str(e)}"
