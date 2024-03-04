# app.py
import numpy as np
import streamlit as st
import joblib

# Eğitilmiş modelinizi yükleyin
model = joblib.load('C:/Users/moonm/ÖzlemElmalı_222802002/Algoritmalar/best_model.sav')

# Streamlit uygulamasını başlatın
st.title('Model Tahmini Uygulaması')

Amac = st.checkbox('Oyun Bilgisayarı mı')
EkranBoyutu = st.number_input('Ekran Boyutu')
Cozunurluk = st.number_input('Ekran Çözünürlüğü(Çarpımını yazınız: 1090x1080 ise 1,177,200)')
EkranHizi = st.number_input('Ekran Hızı')
RAM = st.number_input('RAM')
SSDgb = st.number_input('SSD Kapasitesi')
USB3Adet = st.number_input('USB 3.0 Adet')
USBcAdet = st.number_input('USB-C Adet')
PilGucu = st.number_input('Pil Gücü')
PilHucre = st.number_input('Pil Hücre Sayısı')

# İşletim Sistemi
isletimSistemi1=0
isletimSistemi2=0
isletimSistemi3=0
SecilenSistem = st.selectbox('İşletim Sistemi Seçin:', ['FreeDOS', 'Windows', 'macOS','Diğer'])
if SecilenSistem == 'FreeDOS':
    isletimSistemi1 = 1
elif SecilenSistem == 'Windows':
    isletimSistemi2 = 1
elif SecilenSistem == 'macOS':
    isletimSistemi3 = 1
elif SecilenSistem == 'Diğer':
    isletimSistemi1=0
    isletimSistemi2=0
    isletimSistemi3=0
# İşlemci Markası
islemciMarka1=0
islemciMarka2=0
islemciMarka3=0
SecilenMarka = st.selectbox('İşlemci Markası Seçin:', ['AMD', 'Apple', 'Intel','Diğer'])
if SecilenMarka == 'AMD':
    islemciMarka1 = 1
elif SecilenMarka == 'Apple':
    islemciMarka2 = 1
elif SecilenMarka == 'Intel':
    islemciMarka3 = 1
elif SecilenMarka == 'Diğer':
    islemciMarka1=0
    islemciMarka2=0
    islemciMarka3=0
# İşlemci
islemci1=0 
islemci2=0 
islemci3=0 
islemci4=0
SecilenIslemci = st.selectbox('İşlemciyi Seçin:', ['AMD Ryzen 7', 'Apple M2 Max', 'Intel Core i5','Intel Core i9','Diğer'])
if SecilenIslemci == 'AMD Ryzen 7':
    islemci1 = 1
elif SecilenIslemci == 'Apple M2 Max':
    islemci2 = 1
elif SecilenIslemci == 'Intel Core i5':
    islemci3 = 1
elif SecilenIslemci == 'Intel Core i9':
    islemci4 = 1
elif SecilenIslemci == 'Diğer':
    islemci1=0
    islemci2=0
    islemci3=0
    islemci4=0
# Tahmin
if st.button('Tahmin Yap'):
    user_input = np.array([Amac, EkranBoyutu, Cozunurluk,EkranHizi, RAM,SSDgb,USB3Adet,USBcAdet, PilGucu, PilHucre,isletimSistemi1, isletimSistemi2, isletimSistemi3, islemciMarka1, islemciMarka2, islemciMarka3,islemci1, islemci2, islemci3, islemci4]).reshape(1, -1)
    prediction = model.predict(user_input)
    st.write('Tahmin Sonucu:', prediction[0])