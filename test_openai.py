from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful AI."},
        {"role": "user", "content": "Hello!"},
    ],
)

# ✅ message is an object, use .content
print(resp.choices[0].message.content)
