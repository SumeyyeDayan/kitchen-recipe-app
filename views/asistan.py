import streamlit as st
from database import tarifleri_yukle, yorum_yukle, yorum_ekle, yorum_sil

def asistan_sayfasi(aktif_kullanici):
    tarifler_listesi = tarifleri_yukle()
    st.title("👩‍🍳 Akıllı Mutfak Asistanı")
    yemek_adlari = [t["ad"] for t in tarifler_listesi]
    secilen_ad = st.selectbox("Pişirmek istediğiniz yemeği seçin:", yemek_adlari)
    secilen_tarif = next(t for t in tarifler_listesi if t["ad"] == secilen_ad)

    if secilen_tarif["tip"] == "Premium" and aktif_kullanici.rol != "Premium":
        st.warning("🔒 Bu yemek Premium üyelere özeldir.")
    else:
        st.write("📋 **Elinizde olan malzemeleri işaretleyin:**")
        secilen_malzemeler = []
        for m in secilen_tarif["malzemeler"]:
            if st.checkbox(m, key=f"{secilen_ad}_{m}"):
                secilen_malzemeler.append(m)

        eksikler = [m for m in secilen_tarif["malzemeler"] if m not in secilen_malzemeler]

        if not eksikler:
            st.success("🎉 Harika! Tüm malzemeleriniz tamam.")
            st.info(f"**Hazırlanışı:** {secilen_tarif['hazirlanis']}")
        else:
            st.warning(f"⚠️ **Eksik Malzemeleriniz:** {', '.join(eksikler)}")
            if st.button("📖 Yine de Yapılışını Gör"):
                st.info(f"**Hazırlanışı:** {secilen_tarif['hazirlanis']}")

    st.divider()
    st.write("💬 Tarif Yorumları")
    tum_yorumlar = yorum_yukle()
    ilgili_yorumlar = [y for y in tum_yorumlar if y.get("yemek_adi") == secilen_ad]


    if aktif_kullanici.rol != "Premium" and secilen_tarif["tip"]== "Premium":
        st.error("Yorum görüntülemek için Premium Üye olmalısınız")
    else:
        if ilgili_yorumlar:
            for i, y in enumerate(ilgili_yorumlar):
                with st.container(border=True):
                    col1, col2 = st.columns([5, 1])
                    with col1:
                        st.write(f"⭐ **{y['puan']}/5** - **{y['yazan']}:** {y['yorum']}")
                    with col2:
                        if y.get("yazan") == aktif_kullanici.kullanici_adi:
                            if st.button("🗑️ Sil", key=f"sil_{i}_{y['yazan']}"):
                                yorum_sil(y)
                                st.rerun()
        else:
            st.write("Bu yemek için hiç yorum yapılmamış.")

    if aktif_kullanici.rol != "Premium" and secilen_tarif["tip"] == "Premium":
        st.error("Yorum bırakmak için Premium Üye olmalısınız")
    else:
        with st.form("yorum_form", clear_on_submit=True):
            puan = st.slider("Puan", 1, 5, 5)
            yorum_metni = st.text_area("Yorumunuzu yazın:")

            if st.form_submit_button("Gönder"):
                if yorum_metni.strip():
                    yorum_ekle({
                        "yemek_adi": secilen_ad,
                        "yazan": aktif_kullanici.kullanici_adi,
                        "yorum": yorum_metni.strip(),
                        "puan": puan
                    })
                    st.success("Yorum eklendi!")
                    st.rerun()