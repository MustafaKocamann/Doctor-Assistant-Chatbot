"""
Terminal üzerinden FastAPI ile sürekli çalışan(post atarak) bir doktor asistanı API'si oluşturulacak.
api endpoint: /chat
"""

"""
Client tarafı: FastAPI üzerinden GPT tabanlı dijital doktor asistanına bağlanır.
Function call destekli.
"""
# client_test.py
import requests

API_URL = "http://127.0.0.1:8000/chat"

user_name = input("Adınız: ")
age = input("Yaşınız: ")

print("\nSohbet başladı. Çıkmak için 'exit', 'quit' veya 'çıkış' yazın.\n")

def send_message_to_api(user_name: str, age: int, message: str):
    payload = {
        "user_name": user_name,
        "age": int(age),
        "message": message
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=25)
        if response.status_code == 200:
            return response.json().get("response")
        else:
            return f"Hata: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"İstek sırasında bir hata oluştu: {e}"

while True:
    user_message = input(f"{user_name}: ")
    if user_message.lower() in ["exit", "quit", "çıkış"]:
        print("Sohbet sonlandırıldı.")
        break

    reply = send_message_to_api(user_name, age, user_message)
    print(f"Dijital Doktor Asistanı: {reply}")
