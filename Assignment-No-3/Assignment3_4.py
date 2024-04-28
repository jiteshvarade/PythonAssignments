
def Frequency(List, No):
    Freq = 0
    for i in range(len(List)):
        if(List[i] ==  No):
            Freq = Freq + 1
    return Freq


if __name__ == "__main__":
    print("Enter number of elements you want to enter : ")
    Size = int(input())
    List = []
    for i in range(Size):
        No = int(input())
        List.append(No)

    print("Enter the number you want to find frequency of : ")
    No = int(input())
    
    Result = Frequency(List, No)
    print("Frequency of  number from the list is : ",Result)