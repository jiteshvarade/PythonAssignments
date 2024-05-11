
class Demo:
    Value = 0

    def __init__(self,i,j):
        self.no1 = i
        self.no2 = j

    def Fun(self):
        print("Value of instance variable no1 = ",self.no1)
        print("Value of instance variable no2 = ",self.no2)

    def Gun(self):
        print("Value of instance variable no1 = ",self.no1)
        print("Value of instance variable no2 = ",self.no2)

if __name__ == "__main__":
    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()