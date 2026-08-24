import streamlit as st
from database import kullanici_guncelle

def profil_sayfasi(aktif_kullanici):
    if st.button("🔙 Ana Sayfaya Dön"):
        st.session_state["aktif_sayfa"] = "ana_sayfa"
        st.rerun()

    st.header("⭕ Profil Kartı")
    st.divider()

    sol_kolon, sag_kolon = st.columns(2)

    with sol_kolon:
        st.subheader("Kişisel Bilgiler")
        st.write(f"**İsim Soyisim:** {aktif_kullanici.ad_soyad}")
        st.write(f"**Kullanıcı Adı:** @{aktif_kullanici.kullanici_adi}")
        st.write("---")

        with st.form("sifre_degistir"):
            st.write("🔒 **Şifre Yenileme**")
            eski_sifre = st.text_input("Eski Şifre", type="password")
            yeni_sifre = st.text_input("Yeni Şifre", type="password")
            if st.form_submit_button("Güncelle"):
                if eski_sifre != aktif_kullanici.sifre:
                    st.error("Eski şifre hatalı!")
                elif len(yeni_sifre) < 4:
                    st.error("Yeni şifre çok kısa!")
                elif not any(c in "@#$%&*!?.,:;-_" for c in yeni_sifre):
                    st.error("Şifreniz en az bir özel karakter (@, #, vs.) içermelidir!")
                else:
                    aktif_kullanici.sifre = yeni_sifre
                    kullanici_guncelle(aktif_kullanici)
                    st.success("Şifreniz güncellendi!")

    with sag_kolon:
        st.subheader("Üyelik Durumu")
        if aktif_kullanici.rol == "Premium":
            st.success("🌟 PREMIUM KULLANICI")
        else:
            st.info("👤 STANDART KULLANICI")
            st.info("⭐ Premium üye olarak gizli tariflere erişin!")
            if st.button("⭐ Premium Ol (50 TL)"):
                if aktif_kullanici.bakiye_harca(50.0):
                    aktif_kullanici.rol = "Premium"
                    kullanici_guncelle(aktif_kullanici)
                    st.success("Tebrikler! Artık Premium Üyesiniz!")
                    st.rerun()
                else:
                    st.error("Yetersiz bakiye! Önce cüzdanınıza para yükleyin.")

        st.write("---")
        st.write(f"**Mevcut Bakiye:** {aktif_kullanici.bakiye:.2f} TL")
        if st.button("💳 Para Yükle (Cüzdana Git)"):
            st.session_state["aktif_sayfa"] = "cuzdan"
            st.rerun()