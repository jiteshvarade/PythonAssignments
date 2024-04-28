
from functools import reduce

Even = lambda a : a % 2 == 0

Square = lambda a : pow(a,2)

Add = lambda a,b : a+b

if __name__ == "__main__":
    Size = int(input("Enter the number of elements : "))
    List = []
    print("Enter the elements : ")
    for i in range(Size):
        List.append(int(input()))
    
    print("Input list = ",List)
    FData = list(filter(Even, List))
    print("List after filter = ",FData)
    MData = list(map(Square, FData))
    print("List after map = ",MData)
    RData = reduce(Add, MData)
    print("Output after reduce = ", RData)
