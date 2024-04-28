

def AddList(List):
    Sum = 0
    for i in range(len(List)):
        Sum = Sum + List[i]
    return Sum

if __name__ == "__main__":
    print("Enter number of elements you want to enter : ")
    Size = int(input())
    List = []
    for i in range(Size):
        No = int(input())
        List.append(No)
    
    Result = AddList(List)
    print("Addition of all elements of list is : ",Result)