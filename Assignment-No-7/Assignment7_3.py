
class Arithmetic:
    PI = 3.14

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self,i,j):
        self.Value1 = i
        self.Value2 = j

    def Addition(self):
        return self.Value1+self.Value2

    def Substraction(self):
        return self.Value1-self.Value2

    def Multiplication(self):
        return self.Value1*self.Value2

    def Division(self):
        return self.Value1/self.Value2

if __name__ == "__main__":
    Obj1 = Arithmetic()
    Obj1.Accept(11,21)

    Ret = Obj1.Addition()
    print("Addition of two numbers is : ",Ret)
    Ret = Obj1.Substraction()
    print("Substraction of two numbers is : ",Ret)
    Ret = Obj1.Multiplication()
    print("Multiplication of two numbers is : ",Ret)
    Ret = Obj1.Division()
    print("Division of two numbers is : ",Ret)
