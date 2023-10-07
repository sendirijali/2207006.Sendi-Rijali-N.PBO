class Mahasiswa:
    nim = "2207006"
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur
    def __str__(self):
        return f"Nama saya adalah {self.nama}, dan Nim saya adalah {self.nim}"
    def tahunlahir(self):
        return 2023 - self.umur
    

saya = Mahasiswa("Sendi", "2207006", 20)
print("Nama saya adalah", saya.nama)
print("NIM saya adalah", saya.nim)
print(saya)
print("Tahun lahir saya adalah", saya.tahunlahir())
print("Tahun angkatan saya adalah", saya.nim[:2])


