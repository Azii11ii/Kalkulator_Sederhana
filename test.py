import streamlit as st

st.header('Aplikasi Penjumlahan Numerik', divider='rainbow')

angka_pertama = st.number_input('Masukkan angka pertama')
st.write('The current number is', angka_pertama)

angka_kedua = st.number_input('Masukkan angka kedua')
st.write('The number is', angka_kedua)

operasi_matematika_perkalian = angka_pertama * angka_kedua
operasi_matematika_pengurangan = angka_pertama - angka_kedua
operasi_matematika_penjumlahan = angka_pertama + angka_kedua
operasi_matematika_pembagian = angka_pertama / angka_kedua
operasi_matematika_pemangkatan = angka_pertama ** angka_kedua

st.write(f"Angka pertama {angka_pertama} x Angka kedua {angka_kedua} = {operasi_matematika_perkalian}")
st.write(f"Angka pertama {angka_pertama} + Angka kedua {angka_kedua} = {operasi_matematika_penjumlahan}")
st.write(f"Angka pertama {angka_pertama} - Angka kedua {angka_kedua} = {operasi_matematika_pengurangan}")
st.write(f"Angka pertama {angka_pertama} / Angka kedua {angka_kedua} = {operasi_matematika_pembagian}")
st.write(f"Angka pertama {angka_pertama} ** Angka kedua {angka_kedua} = {operasi_matematika_pemangkatan}")