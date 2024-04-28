

def MinList(List):
    Min = List[0]
    for i in range(len(List)):
        if(List[i] < Min):
            Min = List[i]
    return Min


if __name__ == "__main__":
    print("Enter number of elements you want to enter : ")
    Size = int(input())
    List = []
    for i in range(Size):
        No = int(input())
        List.append(No)
    
    Result = MinList(List)
    print("Minimum number from the list is : ",Result)