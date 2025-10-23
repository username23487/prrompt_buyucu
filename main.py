# main.py

import google.generativeai as genai
import os

# ==============================================================================
# ### YENİ EKLENEN BÖLÜM: API ANAHTARI YAPILANDIRMASI ###
# Projeyi ilk kez kuruyorsanız, en kolay yol API anahtarınızı aşağıdaki
# tırnak işaretlerinin arasına yapıştırmaktır.
#
# Örnek: API_KEY_IN_CODE = "AbCdEfGhIjKlMnOpQrStUvWxYz1234567890"
#
# ⚠️ GÜVENLİK UYARISI: API anahtarınızı bu dosyaya yazdıysanız,
# bu dosyayı ASLA GitHub gibi herkese açık bir platforma yüklemeyin!
# .gitignore dosyanızın bu dosyayı korumadığını unutmayın.
# ==============================================================================
API_KEY_IN_CODE = "YOUR_GEMINI_API_KEY_HERE"


def configure_api_key():
    """
    Gemini API anahtarını yapılandırır.
    Öncelik sırası:
    1. Ortam değişkenini (environment variable) kontrol eder (En Güvenli Yöntem).
    2. Kod içine yazılmış API_KEY_IN_CODE değişkenini kontrol eder (Kolay Yöntem).
    3. Hiçbiri bulunamazsa kullanıcıdan giriş yapmasını ister (Son Çare).
    """
    # 1. Ortam değişkenini kontrol et
    api_key = os.environ.get('GOOGLE_API_KEY')
    if api_key:
        genai.configure(api_key=api_key)
        print("✅ API anahtarı ortam değişkeninden başarıyla yüklendi.")
        return True

    # 2. Kod içine yazılmış anahtarı kontrol et
    if API_KEY_IN_CODE != "YOUR_GEMINI_API_KEY_HERE":
        genai.configure(api_key=API_KEY_IN_CODE)
        print("✅ API anahtarı kod içerisinden başarıyla yüklendi.")
        print("   ⚠️ UYARI: API anahtarınızı kod içine yazdınız. Bu dosyayı herkese açık yerlerde paylaşmamaya dikkat edin!")
        return True

    # 3. Kullanıcıdan anahtar iste
    print("❌ HATA: API anahtarı bulunamadı.")
    print("   Lütfen API anahtarınızı https://aistudio.google.com/app/apikey adresinden alın ve:")
    print("   a) Kod içinde 'API_KEY_IN_CODE' değişkenine atayın, YA DA")
    print("   b) Bir ortam değişkeni olarak ayarlayın.")
    
    api_key_input = input("\nGeçici olarak kullanmak için API anahtarınızı şimdi girin: ")
    if api_key_input:
        genai.configure(api_key=api_key_input)
        print("✅ API anahtarı geçici olarak ayarlandı.")
        return True
    else:
        print("API anahtarı girilmedi. Program sonlandırılıyor.")
        return False

def main():
    """
    Chatbot'un ana çalışma fonksiyonu.
    Modeli başlatır ve kullanıcıyla sohbet döngüsünü yönetir.
    """
    if not configure_api_key():
        return

    # Chatbot'umuz için ana (master) prompt.
    MASTER_PROMPT = """
    ROL/PERSONA:
    Sen, Netflix, HBO, Disney+ gibi tüm platformlardaki içeriklere hakim, sinema ve dizi kültürünü yakından takip eden, adı 'Sinefil Dostum' olan, arkadaş canlısı ve bilgili bir sohbet arkadaşısın.

    AMAÇ:
    Kullanıcının ruh haline, sevdiği türlere ve belirttiği diğer kriterlere göre kişiselleştirilmiş film/dizi önerileri sunmak.

    KURALLAR:
    - Sadece film ve dizi öner. Asla kitap veya oyun önerme.
    - Kesinlikle spoiler (sürprizbozan) verme.
    - Cevapların samimi ama saygılı olsun. Argo veya küfür kullanma.
    - Eğer kullanıcının isteğine uygun bir film/dizi bulamazsan, "Maalesef bu kriterlere uygun bir öneri bulamadım ama istersen benzer bir türde şunu önerebilirim:" diye cevap ver.
    - Her seferinde sadece bir tane öneri sun, eğer kullanıcı daha fazla istemezse.

    ÇIKTI FORMATI:
    Kullanıcı bir öneri istediğinde, cevabını aşağıdaki Markdown formatında ver:

    **Film/Dizi Adı (Yıl)**
    *   **Tür:** [Türleri buraya yaz]
    *   **Konu:** [2-3 cümlelik kısa özet buraya yaz]
    *   **Neden İzlemelisin:** [Neden önerdiğine dair kişisel ve ikna edici bir yorumunu buraya yaz]
    *   **İzleyebileceğin Platform:** [Platform adını buraya yaz]
    """

    # Gemini modelini yapılandır
    generation_config = {
      "temperature": 0.7,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 2048,
    }

    safety_settings = [
      {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
      {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
      {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
      {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    # Sohbet geçmişini tutarak chatbot'un önceki konuşmaları hatırlamasını sağlıyoruz.
    convo = model.start_chat(history=[
        {'role': 'user', 'parts': [MASTER_PROMPT]},
        {'role': 'model', 'parts': ["Anlaşıldı! Ben Sinefil Dostum. Sana yardımcı olmak için buradayım. Nasıl bir film veya dizi arıyorsun?"]}
    ])

    print("\n--- Sinefil Dostum Chatbot ---")
    print("Merhaba! Ben Sinefil Dostum. Sana harika film/dizi önerileri yapmak için buradayım.")
    print("Sohbetten çıkmak için 'çıkış' yazman yeterli.")
    print("-" * 30)

    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ['çıkış', 'exit', 'quit']:
            print("\nSinefil Dostum: Görüşmek üzere! İyi seyirler dilerim.")
            break

        # Kullanıcının mesajını modele gönder
        convo.send_message(user_input)
        
        # Modelin cevabını al ve ekrana yazdır
        print(f"\nSinefil Dostum: {convo.last.text}\n")


if __name__ == "__main__":
    main()
