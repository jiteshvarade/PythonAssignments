
import MarvellousNum

def AddPrimeNumbers(List):
    Sum = 0
    for i in List:
        if(MarvellousNum.ChkPrime(i)):
            Sum = Sum + i
    return Sum

if __name__ == "__main__":
    Size = int(input("Enter the number of elements : "))
    List = []
    for i in range(Size):
        List.append(int(input()))
    
    Result = AddPrimeNumbers(List)
    print("Addition of all prime numbers from the list is  : ",Result)