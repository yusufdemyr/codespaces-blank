class Bardak:
    def __init__(self, kapasite):
        self.kapasite = kapasite
        self.dolu_miktar = 0
        
    def su_ekle(self, miktar):
        if self.dolu_miktar + miktar > self.kapasite:
            self.dolu_miktar = self.kapasite
            print("Bardak dolu, artık su ekleyemezsiniz.")
        else:
            self.dolu_miktar += miktar
            print(f"{miktar} ml su eklendi, bardakta {self.dolu_miktar} ml su var.")
    
    def su_ic(self, miktar):
        if miktar > self.dolu_miktar:
            self.dolu_miktar = 0
            print("Bardağın içinde yeterli miktarda su yok, bardağı tamamen boşaltıyorum.")
        else:
            self.dolu_miktar -= miktar
            print(f"{miktar} ml su içildi, bardakta {self.dolu_miktar} ml su kaldı.")
    

if __name__ == "__main__":
    bardak = Bardak(500)
    bardak.su_ekle(300)
    bardak.su_ic(200)
    bardak.su_ekle(400)
    
    