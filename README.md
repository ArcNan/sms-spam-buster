# 🤖 Detektor SMS Spam (LSTM)

Aplikasi web interaktif yang dibangun dengan **Streamlit** untuk mengklasifikasikan pesan SMS sebagai **Spam** atau **Ham** (bukan spam). Model ini menggunakan jaringan *Long Short-Term Memory* (LSTM) yang dilatih dengan **TensorFlow/Keras**.

![Demo Aplikasi](https://i.imgur.com/k6Fk5sL.gif)

---

### 🛠️ Teknologi

Python | Streamlit | TensorFlow/Keras | Scikit-learn | Pandas | NLTK

---

### 🚀 Menjalankan Aplikasi

1.  **Clone repositori ini:**
    ```bash
    git clone (https://github.com/ArcNan/sms-spam-buster)
    ```

2.  **Install semua dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan aplikasi Streamlit:**
    ```bash
    streamlit run app.py
    ```

Aplikasi akan terbuka secara otomatis di *browser* Anda.

> **Catatan**: Jika ini pertama kalinya Anda menggunakan NLTK, Anda mungkin perlu mengunduh beberapa paket data. Jalankan Python dan ketik:
> `import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')`

---

Dibuat oleh **Tio Rangga Yudhistira** | [GitHub](https://github.com/ArcNan) | [LinkedIn](https://www.linkedin.com/in/tio-rangga-yudhistira-b09a7515b)
