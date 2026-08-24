import string
import random
import streamlit as st
from captcha.image import ImageCaptcha
from database import kullanicilari_yukle, kullanicilari_kaydet, dict_to_kullanici, kullanici_to_dict
from models import Kullanici

def auth_ekrani():

    if "captcha_kodu" not in st.session_state:
        havuz = string.ascii_uppercase + string.digits
        guvenlik_kodu = "".join(random.choices(havuz, k=4))
        st.session_state["captcha_kodu"] = guvenlik_kodu
        st.session_state["captcha_resmi"] = ImageCaptcha().generate_image(guvenlik_kodu)

    st.subheader("Hoş Geldiniz!")
    tab1, tab2 = st.tabs(["Kaydol", "Giris Yap"])


    with tab1:
        with st.form("giris_formu"):
            st.subheader("Giriş Ekranı")
            giris_kullanici_adi = st.text_input("Kullanıcı Adı")
            giris_sifre = st.text_input("Sifre", type="password")
            giris_butonu = st.form_submit_button("Giriş Yap")

            if giris_butonu:
                mevcut_kullanicilar = kullanicilari_yukle()
                eslesen = next((k for k in mevcut_kullanicilar if k["kullanici_adi"] == giris_kullanici_adi and k["sifre"] == giris_sifre), None)

                if eslesen:
                    st.session_state["aktif_kullanici"] = dict_to_kullanici(eslesen)
                    st.rerun()
                else:
                    st.error("Kullanıcı adı veya şifre yanlış")
    with tab2:
        with st.form("kayit_formu"):
            st.subheader("Kayıt Ekranı")
            st.image(st.session_state["captcha_resmi"])
            girilen_kod = st.text_input("Doğrulama kodunu giriniz:")
            yeni_kullanici_adi = st.text_input("Kullanıcı Adı").strip()
            yeni_ad_soyad = st.text_input("Ad Soyad").strip()
            yeni_sifre = st.text_input("Şifre", type="password").strip()
            tekrar_sifre = st.text_input("Şifrenizi Tekrar Girin", type="password").strip()
            kayit_butonu = st.form_submit_button("Kaydol")

        if kayit_butonu:
            mevcut_kullanicilar = kullanicilari_yukle()
            zaten_var = any(k["kullanici_adi"] == yeni_kullanici_adi for k in mevcut_kullanicilar)

            if not yeni_kullanici_adi or not yeni_sifre:
                st.error("Lütfen tüm alanları doldurun")
            elif len(yeni_sifre) < 6:
                st.error("Şifre 6 karakterden az olamaz!")
            elif yeni_sifre != tekrar_sifre:
                st.error("Şifreleriniz uyuşmuyor!")
            elif not any(c in "@#$%&*!?.,:;-_" for c in yeni_sifre):
                st.error("Şifreniz en az bir özel karakter (@, #, vs.) içermelidir!")
            elif girilen_kod != st.session_state["captcha_kodu"]:
                st.error("Captcha kodu yanlış!")
                del st.session_state["captcha_kodu"]
                st.rerun()
            elif zaten_var:
                st.error("Bu kullanici adi kullaniliyor")
            else:
                yeni_nesne = Kullanici(yeni_kullanici_adi, yeni_sifre)
                yeni_nesne.ad_soyad = yeni_ad_soyad
                mevcut_kullanicilar.append(kullanici_to_dict(yeni_nesne))
                kullanicilari_kaydet(mevcut_kullanicilar)
                del st.session_state["captcha_kodu"]
                st.success("Kayıt başarılı! Giris yap sekmesinden giriş yapabilirsiniz!")