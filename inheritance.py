class Orang():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname
    
class Alamat():
    def __init__(self):
        self.jalan = "Salamnunggal"
        self.kota = "Garut"

class Mahasiswa(Orang, Alamat):
    def __init__(self, firstname, lastname, nim):
        self.nim = nim

        Orang.__init__(self, firstname, lastname)
        Alamat.__init__(self)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.nim}"
    
    def printData(self):
        print(f"Nama  : {self.getfirstname()} {self.lastname}")
        print(f"NIM   : {self.nim}")
        print(f"Alamat: {self.jalan}, {self.kota}")

mhs = Mahasiswa("Sendi", "Rijali", "2207006")
#print(mhs.getfirstname(), mhs.getlastname())
#print(mhs)
mhs.printData()