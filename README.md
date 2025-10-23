# 🎬 Sinefil Dostum Chatbot

Kişiselleştirilmiş film ve dizi önerileri sunan, Gemini API ile güçlendirilmiş bir komut satırı chatbot'u.

Bu proje, Gemini'ın güçlü dil modelini kullanarak kullanıcının zevklerine ve ruh haline uygun içerikleri bulan "Sinefil Dostum" adında bir sohbet robotu oluşturur.

## ✨ Özellikler

-   **Kişiselleştirilmiş Öneriler:** Sevdiğiniz türlere, oyunculara veya ruh halinize göre öneriler alın.
-   **Detaylı Bilgi:** Her öneri; tür, konu, neden izlemeniz gerektiği ve platform bilgisi ile birlikte gelir.
-   **Akıllı Sohbet:** Sohbet geçmişini hatırlayarak akıcı bir diyalog kurar.
-   **Güvenli ve Kontrollü:** İstenmeyen içerikleri filtreler ve spoiler vermez.

## 🚀 Kurulum

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### 1. Projeyi Klonlayın

```bash
git clone https://github.com/username23487/prrompt_buyucu.git
cd sinefil-dostum-chatbot
```

### 2. Sanal Ortam Oluşturun ve Aktif Edin (Tavsiye Edilir)

-   **macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
-   **Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 3. Gerekli Kütüphaneleri Yükleyin

Projenin ihtiyaç duyduğu tüm kütüphaneler `requirements.txt` dosyasında listelenmiştir. Tek komutla yükleyebilirsiniz:

```bash
pip install -r requirements.txt
```

## ⚙️ Yapılandırma - API Anahtarı

Bu projenin çalışması için bir Google Gemini API anahtarına ihtiyacınız var.

1.  API anahtarınızı [Google AI Studio](https://aistudio.google.com/app/apikey) adresinden ücretsiz olarak alın.

2.  **En Güvenli Yöntem:** API anahtarınızı bir ortam değişkeni (environment variable) olarak ayarlayın.

    -   **macOS / Linux:** Terminal'inize aşağıdaki komutu yazın. `.zshrc` veya `.bash_profile` dosyanıza ekleyerek kalıcı hale getirebilirsiniz.
        ```bash
        export GOOGLE_API_KEY="BURAYA_API_ANAHTARINIZI_YAPIŞTIRIN"
        ```

    -   **Windows (Komut İstemi):**
        ```bash
        set GOOGLE_API_KEY="BURAYA_API_ANAHTARINIZI_YAPIŞTIRIN"
        ```
    -   **Windows (PowerShell):**
        ```powershell
        $env:GOOGLE_API_KEY="BURAYA_API_ANAHTARINIZI_YAPIŞTIRIN"
        ```

    > **⚠️ UYARI:** API anahtarınızı asla doğrudan koda yazmayın veya GitHub gibi herkese açık platformlarda paylaşmayın! `.gitignore` dosyası bu konuda size yardımcı olacaktır.

## ▶️ Çalıştırma

Tüm kurulumlar tamamlandıktan sonra, chatbot'u aşağıdaki komutla başlatabilirsiniz:

```bash
python main.py
```

Çıkmak için sohbet ekranına `çıkış` yazmanız yeterlidir.

## 💬 Örnek Sohbet

```
$ python main.py
API anahtarı ortam değişkeninden başarıyla yüklendi.

--- Sinefil Dostum Chatbot ---
Merhaba! Ben Sinefil Dostum. Sana harika film/dizi önerileri yapmak için buradayım.
Sohbetten çıkmak için 'çıkış' yazman yeterli.
------------------------------
Sen: Bu akşam biraz gizemli ve akıl oyunları içeren bir film izlemek istiyorum.

Sinefil Dostum:
**Prestij (2006)**
*   **Tür:** Gizem, Dram, Bilim Kurgu
*   **Konu:** 19. yüzyıl Londra'sında, birbirleriyle rekabet halinde olan iki sihirbazın takıntı haline gelen üstünlük mücadelesini anlatır. Sırlarını korumak ve birbirlerini alt etmek için her şeyi yapmaya hazırdırlar.
*   **Neden İzlemelisin:** Christopher Nolan'ın yönettiği bu film, başından sonuna kadar merak duygunu en üst seviyede tutacak. Zekice kurgulanmış senaryosu ve şaşırtıcı finali ile aklını başından alacak bir deneyim sunuyor.
*   **İzleyebileceğin Platform:** Prime Video
```
