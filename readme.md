# 🩺 GPT Tabanlı Dijital Doktor Asistanı
Bu proje, OpenAI GPT-3.5 API kullanılarak geliştirilmiş bir dijital doktor asistanı uygulamasıdır.
Kullanıcının adı, yaşı ve mesaj geçmişine göre uygun yanıtlar üretir. İlk etapta terminal üzerinden çalışır, ardından FastAPI ile web tabanlı bir sürüm geliştirilmiştir.

## 🚀 Özellikler
* Kullanıcıdan ad ve yaş bilgisi alarak kişiselleştirilmiş sağlık önerileri sunar.
* Mesaj geçmişini dikkate alarak diyaloğu sürdürebilir.
* Function Calling desteğiyle yaşı dikkate alarak özel sağlık ipuçları verir.
* Terminal tabanlı versiyon ve FastAPI tabanlı web API versiyonu mevcuttur.
* OpenAI API ile gerçek zamanlı yanıt üretimi.

## 📌 Problem Tanımı
* Kullanıcıların sağlık sorularını anlamak ve GPT tabanlı öneriler sunmak.
* Kullanıcı yaşına göre farklı yanıtlar üretmek.
* Terminal üzerinden başlatılan basit sürümden, web API entegrasyonuna geçiş.

## 📊 Dataset
* Harici bir veri seti kullanılmamaktadır.
* Tamamen OpenAI GPT-3.5 API ve prompt engineering ile çalışmaktadır.

## 🧠 Model
* GPT-3.5 (OpenAI API) kullanılmaktadır.
* Sağlık önerilerini prompt üzerinden üretir.
* Kullanıcı geçmişine göre bağlamsal yanıt verir

## 🌐 API Yapısı
* FastAPI ile web API geliştirilmiştir.
* /chat endpoint’i ile kullanıcı mesajı alınıp modele gönderilir.
* Function calling sayesinde yaşa uygun öneriler API yanıtına dahil edilir.

## 📦 Kurulum
### 1️⃣ Sanal Ortam Oluşturma
* python -m venv venv

### 2️⃣ Sanal Ortamı Aktifleştirme
.\venv\Scripts\Activate

### 3️⃣ Gerekli Kütüphaneleri Yükleme
* pip install requirements.txt

### 4️⃣ Ortam Değişkeni (.env) Dosyası
* Kök dizinde .env dosyası oluşturup içine kendi OpenAI API anahtarını yaz:
* OPENAI_API_KEY=your_api_key_here

### ▶️ Çalıştırma
* Terminal tabanlı sürüm: python doctor_terminal.py
* FastAPI sürümü: uvicorn main:app --reload
* API çalıştıktan sonra test için: http://127.0.0.1:8000/docs  adresini ziyaret edebilirsin.

## 📚 Kullanılan Teknolojiler
* FastAPI → Modern web framework (asenkron destekli).
* Uvicorn → FastAPI için ASGI server.
* OpenAI → GPT-3.5 API entegrasyonu.
* python-dotenv → Ortam değişkenleri yönetimi.



