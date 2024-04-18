class Box:
    def _init_(self,name,roll):
        self.name = name
        self.roll = roll

class Student:
    def _init_(self,fees):
        self.fees = fees

class Box2(Box,Student):
    def _init_(self,name,rollNo,marks,fees):
        self.marks = marks
        Student._init_(self,fees)
        Box._init_(self,name,rollNo)

class Box3(Box2):
    def _init_(self,sem):
        self.sem = sem
        Box2._init_(self,"shiv-raj",12,23,20000)

obj = Box3("2-1")
print(obj.sem)
print(obj.name)


obj2 = Box2("shiv",12,13,20000)
print(obj2.fees)
print(obj2.marks)
print(obj2.name)
print(obj2.roll)

obj3 = Box2("Raj kumar",45,234,10000)
print(obj3.name)
print(obj3.roll)
print(obj3.marks)
print(obj3.fees)
