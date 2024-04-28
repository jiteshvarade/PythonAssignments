
from functools import reduce

GreaterThan70 = lambda a : a >= 70

PlusTen = lambda a : a+10

Product = lambda a,b : a*b

if __name__ == "__main__":
    Size = int(input("Enter the number of elements : "))
    List = []
    print("Enter the elements : ")
    for i in range(Size):
        List.append(int(input()))
    
    print("Input list = ",List)
    FData = list(filter(GreaterThan70, List))
    print("List after filter = ",FData)
    MData = list(map(PlusTen, FData))
    print("List after map = ",MData)
    RData = reduce(Product, MData)
    print("Output after reduce = ", RData)
