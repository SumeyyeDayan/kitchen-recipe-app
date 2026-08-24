import streamlit as st

from database import tarifleri_yukle

def tarifler_sayfasi(aktif_kullanici):
    tarifler_listesi = tarifleri_yukle()
    st.subheader("🍲 Mutfak Tarifleri")
    for tarif in tarifler_listesi:
        with st.expander(f"{tarif['ad']} ({tarif['tip']})"):
            if tarif["tip"] == "Premium" and aktif_kullanici.rol != "Premium":
                st.warning("🔒 Bu tarif sadece Premium üyelere özeldir")
            else:
                st.write("**Malzemeler:**", tarif["malzemeler"])
                st.write("**Hazırlanışı:**", tarif["hazirlanis"])