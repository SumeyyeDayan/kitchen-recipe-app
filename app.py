import streamlit as st
from components.auth import auth_ekrani
from components.sidebar import sidebar_goster
from views.tarif import tarifler_sayfasi
from views.profil import profil_sayfasi
from views.cuzdan import cuzdan_sayfasi
from views.asistan import asistan_sayfasi

st.set_page_config(page_title="🍳 Mutfak Tarifleri & Üyelik", layout="wide", initial_sidebar_state="expanded")
st.title("🍳 Mutfak Tarifleri & Üyelik Sistemi")

if "aktif_sayfa" not in st.session_state:
    st.session_state["aktif_sayfa"] = "ana_sayfa"
if "aktif_kullanici" not in st.session_state:
    st.session_state["aktif_kullanici"] = None

if st.session_state["aktif_kullanici"] is None:
    auth_ekrani()
else:
    aktif_kullanici = st.session_state["aktif_kullanici"]
    sidebar_goster(aktif_kullanici)

    sayfa = st.session_state["aktif_sayfa"]
    if sayfa == "ana_sayfa":
        tarifler_sayfasi(aktif_kullanici)
    elif sayfa == "profil":
        profil_sayfasi(aktif_kullanici)
    elif sayfa == "cuzdan":
        cuzdan_sayfasi(aktif_kullanici)
    elif sayfa == "asistan":
        asistan_sayfasi(aktif_kullanici)