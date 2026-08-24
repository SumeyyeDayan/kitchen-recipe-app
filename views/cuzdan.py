import streamlit as st
from database import kullanici_guncelle

def cuzdan_sayfasi(aktif_kullanici):
    st.title("💳 Cüzdan & Bakiye")
    st.write(f"**Anlık Bakiyeniz:** {aktif_kullanici.bakiye:.2f} TL")

    yuklenecek = st.number_input("Yüklenecek Tutar (TL)",min_value=10,step=10)
    if st.button("Bakiye Yükleyin"):
        aktif_kullanici.bakiye_ekle(yuklenecek)
        kullanici_guncelle(aktif_kullanici)
        st.success("Bakiyeniz Güncellendi")
        st.rerun()

