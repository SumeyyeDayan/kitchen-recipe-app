class Kullanici():
    def __init__(self,kullanici_adi,sifre,bakiye= 0.0,rol="Standart",ad_soyad=""):
        self.kullanici_adi=kullanici_adi
        self.sifre=sifre
        self.bakiye=bakiye
        self.rol=rol
        self.ad_soyad=ad_soyad
    def bakiye_ekle(self,miktar):

        if miktar <= 0:
            print("Hata: Gecersiz Giris!")
            return False
        else:
            self.bakiye += miktar
            print("Basarili islem")
            return True

    def bakiye_harca(self,miktar):
        if miktar <= 0:
            print("Hata: Gecersiz Giris!")
            return False
        elif self.bakiye < miktar:
            print("Hata: Yetersiz Bakiye!")
            return False
        else :
            self.bakiye -= miktar
            print("Basarili islem")
            return True

class PremiumKullanici(Kullanici):

    def __init__(self,kullanici_adi,sifre,bakiye=0.0,ad_soyad=""):
        super().__init__(kullanici_adi=kullanici_adi, sifre= sifre , bakiye = bakiye ,rol="Premium",ad_soyad=ad_soyad)
        self.indirim_orani = 0.20