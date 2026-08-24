import json
import os
from models import Kullanici,PremiumKullanici

def kullanicilari_yukle():
    if os.path.exists("kullanicilar.json"):
        with open("kullanicilar.json","r",encoding="utf-8") as f:
            veri=json.load(f)
            return veri
    else:
        return []

def kullanicilari_kaydet(kullanici_listesi):
    with open("kullanicilar.json","w", encoding="utf-8") as f:
        f.write(json.dumps(kullanici_listesi,indent=4))

def kullanici_to_dict(kullanici):
    return {
        "kullanici_adi" : kullanici.kullanici_adi,
        "sifre" : kullanici.sifre,
        "bakiye" : kullanici.bakiye,
        "rol" : kullanici.rol,
        "ad_soyad" : kullanici.ad_soyad
    }

def dict_to_kullanici(veri_dict):

    if veri_dict.get("rol") == "Premium":
        return PremiumKullanici(
            kullanici_adi = veri_dict.get("kullanici_adi"),
            sifre = veri_dict.get("sifre"),
            bakiye = veri_dict.get("bakiye",0.0),
            ad_soyad = veri_dict.get("ad_soyad","")
        )
    else:
        return Kullanici(
            kullanici_adi=veri_dict.get("kullanici_adi"),
            sifre=veri_dict.get("sifre"),
            bakiye=veri_dict.get("bakiye"),
            ad_soyad=veri_dict.get("ad_soyad")
        )
def kullanici_guncelle(guncel_kullanici):
    mevcut_kullanicilar = kullanicilari_yukle()
    for k in mevcut_kullanicilar:
        if k ["kullanici_adi"] == guncel_kullanici.kullanici_adi:
            k["bakiye"] = guncel_kullanici.bakiye
            k["rol"] = guncel_kullanici.rol
            k["ad_soyad"] = guncel_kullanici.ad_soyad
            break
    kullanicilari_kaydet(mevcut_kullanicilar)


TARIFLER=[
    {
        "ad" : "Klasik Menemen",
        "tip" :"Standart",
        "malzemeler":["2 adet domates ","2 adet biber" ,"2 adet yumurta","Zeytinyagi"],
        "hazirlanis":"Biberleri doğrayıp tavada kavurun.Domatesleri ekleyip suyunu çekene kadar pişirin.Yumurtaları eklerek servis edin. "
    },{
        "ad" : "Ozel Firin Somon",
        "tip" : "Premium",
        "malzemeler": ["Somon fileto", "Kuşkonmaz", "Limon", "Zeytinyağı", "Taze kekik"],
        "hazirlanis" :"Somonları marine edin. Kuşkonmazlarla birlikte 180°C fırında 20 dakika pişirin."
    }
]
def tarifleri_yukle():
    return TARIFLER

def yorum_yukle():
    if os.path.exists("yorumlar.json"):
        try:
            with open("yorumlar.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Dosya boşsa veya içi bozulmuşsa çökme, boş liste dön
            return []
    return []
def yorum_ekle(yeni_yorum):
    yorumlar = yorum_yukle()
    yorumlar.append(yeni_yorum)
    with open("yorumlar.json","w", encoding="utf-8") as f:
        json.dump(yorumlar,f,indent=4,ensure_ascii=False)

def yorum_sil(silinecek_yorum):
    tum_yorumlar = yorum_yukle()

    kalan_yorumlar =[ y for y in tum_yorumlar if y != silinecek_yorum]
    with open ("yorumlar.json","w", encoding="utf-8") as f:
        json.dump(kalan_yorumlar,f,indent=4,ensure_ascii=False)


