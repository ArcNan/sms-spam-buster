import streamlit as st
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import re
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from contractions import contractions_dict

# --- Fungsi Preprocessing 

def transform_text(text):
    lemmatizer = WordNetLemmatizer()
    text = text.lower()
    text = ' '.join([contractions_dict.get(word, word) for word in text.split()])
    text = word_tokenize(text)
    text = [re.sub(r'[^a-zA-Z0-9]', '', word) for word in text]
    stop_words = set(stopwords.words('english'))
    text = [word for word in text if word not in stop_words and word not in string.punctuation]
    text = [lemmatizer.lemmatize(word) for word in text]
    return " ".join(text)

# --- Muat Model dan Tokenizer 
@st.cache_resource
def load_my_model():
    """Memuat model dan tokenizer dari file."""
    try:
        model = tf.keras.models.load_model('spam_detector_model.h5')
        with open('tokenizer.pkl', 'rb') as handle:
            tokenizer = pickle.load(handle)
        return model, tokenizer
    except Exception as e:
        st.error(f"Error saat memuat model atau tokenizer: {e}")
        return None, None

model, tokenizer = load_my_model()
max_length = 100 # 

# --- Tampilan UI Streamlit ---
st.set_page_config(page_title="Detektor Spam", page_icon="🤖")

st.title("🤖 Detektor SMS Spam")
st.markdown("Aplikasi web ini menggunakan model LSTM untuk mendeteksi apakah sebuah pesan SMS tergolong **Spam** atau **Ham** (bukan spam).")

user_input = st.text_area("Masukkan Pesan SMS di sini:", height=150, placeholder="Contoh: Congratulations! You've won a $1,000 gift card...")

if st.button("Analisis Pesan"):
    if user_input and model and tokenizer:
        
        # 1. Langsung tokenisasi pesan mentah
        message_seq = tokenizer.texts_to_sequences([user_input])
        message_pad = pad_sequences(message_seq, maxlen=max_length, padding='pre')
        
        # 2. Lakukan prediksi
        try:
            prediction_prob = model.predict(message_pad)[0][0]

            # 3. Tampilkan hasil
            st.write("---")
            if prediction_prob > 0.5:
                st.error(f"Pesan Ini Terdeteksi Sebagai SPAM (Skor: {prediction_prob:.2f})")
            else:
                st.success(f"Pesan Ini Terdeteksi Sebagai HAM (Bukan Spam) (Skor: {prediction_prob:.2f})")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat prediksi: {e}")
            
    elif not model or not tokenizer:
        st.error("Model atau tokenizer tidak berhasil dimuat. Periksa kembali file Anda.")
    else:
        st.warning("Mohon masukkan pesan terlebih dahulu untuk dianalisis.")

st.markdown("---")
st.markdown("Dibuat dengan **Streamlit** dan **TensorFlow/Keras**.")
st.markdown("Made by **Tio Rangga Yudhistira**.")