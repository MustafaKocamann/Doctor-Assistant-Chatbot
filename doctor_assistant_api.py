"""
FAST API ile GPT tabanlı doktor asistanı 
Her kullanıcı için ayrı bir hafıza (memory) yapısı oluşturulacak.
"""
import os
from typing import Dict, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

# Ortam değişkenlerini yükle
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# FastAPI uygulaması
app = FastAPI(title="Doctor Assistant API")

# Hafıza: kullanıcı adı -> mesaj listesi
user_memories: Dict[str, List[Dict[str, str]]] = {}

# Pydantic modelleri
class ChatRequest(BaseModel):
    user_name: str
    age: int
    message: str

class ChatResponse(BaseModel):
    response: str

# Kullanıcıya intro mesajı ekle
def add_intro_message(user_name: str, age: int):
    intro = (
        f"Sen bir dijital doktor asistanısın. Hasta {user_name}, {age} yaşında. "
        "Sağlık sorunları hakkında konuşmak istiyorsun. Amacın, hastaya sağlıkla ilgili sorularında yardımcı olmak ve güven verici, anlaşılır yanıtlar üretmektir. "
        "Kurallar: \n"
        "1. Hastanın yaşına uygun, dikkatli ve nazik cevaplar ver; hastaya ismiyle hitap et.\n"
        "2. Cevapların moral bozucu olmamalı. Ciddi sağlık sorunları varsa, korkutmadan yönlendir.\n"
        "3. Hastayı gerektiğinde bir uzmana başvurması için yönlendir.\n"
        "4. Cinsiyet, dil, din veya ırk ayrımı yapma; tarafsız ol.\n"
        "5. Açık, anlaşılır ve destekleyici bir dil kullan. Gerektiğinde basit öneriler veya ek açıklamalar ver.\n"
        "6. Kesin tanı koyamazsın; yalnızca rehberlik ve bilgilendirme yapabilirsin.\n"
        "7. Tıbbi jargon kullanacaksan, mutlaka açıklamasını yap.\n"
    )
    user_memories[user_name].append({"role": "user", "content": intro})

# Sohbet endpointi
@app.post("/chat", response_model=ChatResponse)
async def chat_with_doctor(request: ChatRequest):
    try:
        # Kullanıcı için hafıza yoksa oluştur
        if request.user_name not in user_memories:
            user_memories[request.user_name] = []
            add_intro_message(request.user_name, request.age)

        # Kullanıcı mesajını ekle
        user_memories[request.user_name].append({"role": "user", "content": request.message})

        # OpenAI Function Call ile mesajı gönder
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=user_memories[request.user_name]
        )

        reply_text = response.choices[0].message.content
        user_memories[request.user_name].append({"role": "assistant", "content": reply_text})

        # Hafızayı konsola yazdır (opsiyonel)
        print(f"\nMemory for {request.user_name}:")
        for idx, m in enumerate(user_memories[request.user_name], start=1):
            print(f"{idx}. {m['role'].upper()}: {m['content']}")
        print("--------------------------------------------------")

        return ChatResponse(response=reply_text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
