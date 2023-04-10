class car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.pintu = "terbuka"
        self.mobil = "mati"

    def MembukaPintu(self):
        if self.pintu == "tertutup":
            print("buka pintu")
            self.pintu == "terbuka"
        else:
            print("tutup pintu")
    def Menutuppintu(self):
        if self.pintu != "tertutup":
            print("tutup pintu")
            self.pintu == "tertutup"
        else:
            print("buka Pintu")
    def MesinMenyala(self):
        if self.mobil == "mati":
            print("Nyalakan Mobil")
            self.mobil == "menyala"
        else:
            print("matikan mesin")

car1 =  car("toyota", 2022)
car1.MembukaPintu()
car1.Menutuppintu()
car1.MesinMenyala()

