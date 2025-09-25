"""
1-)Problem Tanımı: Kullanıcının sağlık sorularını anlayan ve yanıtlayan GPT tabanlı dijital doktor asistanı.
    - Kullanıcının adı ve yaşı doğrultusunda yanıtlar üreten bir model.
    - Mesaj geçmişini dikkate alarak diyaloğu sürdüren bir yapı olmalı.
    - OpenAI API kullanılarak geliştirilmiştir.
    - İlk olarak terminalde çalışan bir versiyon, sonra da FastAPI ile web tabanlı bir versiyon geliştirilecektir.
    - Client tarafını yazıp test edilecektir.


2-) Dataset: Veri seti kullanılmayacak, OpenAI'nin GPT-3.5 kullanılarak prompt engineering ile çözülecek.


3-) Model Tanıtımı: OpenAI'nin GPT-3.5 modeli kullanılacak.
    - API üzerinden iletişim kurarak kullanıcılara gerçek zamanlı sağlık önerileri sunan bir sistem olsun.


5-)API Definition: OpenAI API'si ile entegrasyon sağlanacak.

6-)Install Libraries:
    - fastapi: Web api geliştirmek için modern ve hızlı bir framework.Asenkron bir yapıya sahip.
    - uvicorn: FastAPI uygulamasını çalıştırmak için ASGI sunucusudur.
    - openai: OpenAI'nin API'sine erişim sağlamak için kullanılan resmi kütüphane.
    - python-dotenv: Ortam değişkenlerini yönetmek için kullanılır. API anahtarlarını güvenli bir şekilde saklamak için idealdir. .env dosyasından api anahtarlarını yüklemek için kullanılır. 
    

7-) Import Libraries
"""

"""
Terminal tabanlı GPT-3.5 tabanlı dijital doktor asistanı.
Function calling ile yaşa uygun sağlık ipuçları verebilir.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# API key yükle
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Hafıza: kullanıcı mesajlarını ve cevapları tutacak
memory = []

# Kullanıcı bilgisi
user_name = input("Adınız: ")
age = input("Yaşınız: ")

# Intro mesajı
intro = (
    f"Sen bir dijital doktor asistanısın. Hasta {user_name}, {age} yaşında. "
    "Sağlık sorunları hakkında konuşmak istiyorsun. Amacın, hastaya sağlıkla ilgili sorularında yardımcı olmak ve güven verici, anlaşılır yanıtlar üretmektir. "
    "Aşağıdaki kurallara göre hareket et: \n"
    "1. Hastanın yaşına uygun, dikkatli ve nazik cevaplar ver; hastaya ismiyle hitap et.\n"
    "2. Cevapların moral bozucu olmamalı. Ciddi sağlık sorunları varsa, korkutmadan yönlendir.\n"
    "3. Hastayı gerektiğinde bir uzmana başvurması için yönlendir.\n"
    "4. Cinsiyet, dil, din veya ırk ayrımı yapma; tarafsız ol.\n"
    "5. Açık, anlaşılır ve destekleyici bir dil kullan. Gerektiğinde basit öneriler veya ek açıklamalar ver.\n"
    "6. Kesin tanı koyamazsın; yalnızca rehberlik ve bilgilendirme yapabilirsin.\n"
    "7. Tıbbi jargon kullanacaksan, mutlaka açıklamasını yap.\n"
)
memory.append({"role": "user", "content": intro})

print(f"\nMerhaba {user_name}, ben dijital doktor asistanınız 😊 Sorularınızı sorabilirsiniz.\n")

# Sürekli kullanıcı girdisi alma ve yanıt üretme döngüsü
while True:
    user_message = input(f"{user_name}: ")
    if user_message.lower() in ["exit", "quit", "çıkış"]:
        print("Sana yardımcı olabildiysem ne mutlu! Görüşmek üzere!")
        break

    # Kullanıcı mesajını hafızaya ekle
    memory.append({"role": "user", "content": user_message})

    # OpenAI çağrısı
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=memory
    )

    reply_text = response.choices[0].message.content
    print(f"Dijital Doktor Asistanı: {reply_text}")

    # AI cevabını hafızaya ekle
    memory.append({"role": "assistant", "content": reply_text})
