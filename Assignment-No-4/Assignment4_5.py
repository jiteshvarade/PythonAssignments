
from functools import reduce

def ChkPrime(No):
    for i in range(2,int(No/2)+1):
        if(No % i == 0):
            return False
    return True

def FindMax(a,b):
    if(a >= b):
        return a
    else:
        return b
        

Prime = lambda a : ChkPrime(a)

Multiply = lambda a : a*2

Max = lambda a,b : FindMax(a,b)

if __name__ == "__main__":
    Size = int(input("Enter the number of elements : "))
    List = []
    print("Enter the elements : ")
    for i in range(Size):
        List.append(int(input()))
    
    print("Input list = ",List)
    FData = list(filter(Prime, List))
    print("List after filter = ",FData)
    MData = list(map(Multiply, FData))
    print("List after map = ",MData)
    RData = reduce(Max, MData)
    print("Output after reduce = ", RData)
