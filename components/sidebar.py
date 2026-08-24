import streamlit as st

def sidebar_goster(aktif_kullanici):
    with st.sidebar:
        gosterim_adi = aktif_kullanici.ad_soyad if aktif_kullanici.ad_soyad else aktif_kullanici.kullanici_adi
        st.markdown(f"### 👤 {gosterim_adi}")
        st.divider()

        if st.button("🍳 Tarifler", use_container_width=True):
            st.session_state["aktif_sayfa"] = "ana_sayfa"
            st.rerun()
        if st.button("👤 Profil", use_container_width=True):
            st.session_state["aktif_sayfa"] = "profil"
            st.rerun()
        if st.button("💳 Cüzdan Yönetimi", use_container_width=True):
            st.session_state["aktif_sayfa"] = "cuzdan"
            st.rerun()
        if st.button("👩‍🍳 Mutfak Asistanı", use_container_width=True):
            st.session_state["aktif_sayfa"] = "asistan"
            st.rerun()

        st.divider()
        if st.button("🚪 Çıkış Yap", use_container_width=True):
            st.session_state["aktif_kullanici"] = None
            st.session_state["aktif_sayfa"] = "ana_sayfa"
            st.rerun()