
class Numbers:

    def __init__(self,i):
        self.Value = i

    def ChkPrime(self):
        for i in range(2,int(self.Value/2) + 1):
            if(self.Value % i == 0):
                return False
        return True

    def ChkPerfect(self):
        sum = self.SumFactors()
        if(sum == self.Value):
            return True
        else:
            False

    def SumFactors(self):
        sum = 0
        for i in range(1,int(self.Value/2) + 1):
            if(self.Value % i == 0):
                sum = sum + i
        return sum

    def Factors(self):
        for i in range(1,int(self.Value/2) + 1):
            if(self.Value % i == 0):
                print(i,end=" ")

if __name__ == "__main__":
    Obj1 = Numbers(6)
    if(Obj1.ChkPrime()):
        print("Number is prime")
    else:
        print("Number is not prime")

    if(Obj1.ChkPerfect()):
        print("Number is perfect")
    else:
        print("Number is not perfect")

    print("Factors of number are : ")
    Obj1.Factors()

    Obj2 = Numbers(24)
    if(Obj2.ChkPrime()):
        print("Number is prime")
    else:
        print("Number is not prime")

    if(Obj1.ChkPerfect()):
        print("Number is perfect")
    else:
        print("Number is not perfect")

    print("Factors of number are : ")
    Obj2.Factors()
