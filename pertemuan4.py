class Orang():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname
    
class Alamat():
    def __init__(self, jalan, kota):
        self.jalan = jalan
        self.kota = kota

    def getfirstname(self):
        return self.jalan
    def getlastname(self):
        return self.kota

class Mahasiswa(Orang, Alamat):
    def __init__(self, firstname, lastname, nim, jalan, kota):
        self.nim = nim

        Orang.__init__(self, firstname, lastname)
        Alamat.__init__(self, jalan, kota)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.nim}, {self.jalan}, {self.kota}"
    
    def printData(self):
        print(f"Nama  : {self.getfirstname()} {self.lastname}")
        print(f"NIM   : {self.nim}")
        print(f"Alamat: {self.jalan}, {self.kota}")

mhs = Mahasiswa("Sendi", "Rijali", "2207006", "Salamnunggal", "Garut")
#print(mhs.getfirstname(), mhs.getlastname())
#print(mhs)
mhs.printData()