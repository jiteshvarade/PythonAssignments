

def MaxList(List):
    Max = 0
    for i in range(len(List)):
        if(List[i] > Max):
            Max = List[i]
    return Max


if __name__ == "__main__":
    print("Enter number of elements you want to enter : ")
    Size = int(input())
    List = []
    for i in range(Size):
        No = int(input())
        List.append(No)
    
    Result = MaxList(List)
    print("Maximum number from the list is : ",Result)