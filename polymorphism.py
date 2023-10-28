# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Drive!")

# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Sail!")

# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Fly!")

# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")

# for x in (car1, boat1, plane1):
#     x.move()

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Move!")

# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")

# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")

# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")

# for x in (car1, boat1, plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()

class BangunDatar():
    def __init__(self, nama, luas, sisi):
        self.nama = nama
        self.luas = luas
        self.sisi = sisi
    
    def firstname(self):
       return self.nama
    def getluas(self)
        return self.luas
    def getpersegi(self):
       return self.sisi
    
class Persegi(BangunDatar):
    def __init__(self, nama, luas, sisi):
        self.nama = nama
        self.sisi = sisi
        self.luas = luas


    BangunDatar.__init__(self.sisi)

    def getpersegi(self):
       return self.sisi
    
    def __str__(self):
        return f"{self.nama}, {self.luas}, {self.sisi}"
    
    def printData(self):
        print(f"
              ")

print("Aku adalah persegi")
print("Luas persegi dengan sisi 4 adalah 16")


