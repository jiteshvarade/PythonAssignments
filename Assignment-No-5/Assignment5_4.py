Sum = 0

def SumOfDigits(No):
    global Sum
    if(No != 0):
        Sum = Sum + (No % 10)
        No = int(No / 10)
        SumOfDigits(No)
    return Sum
    


if __name__ == "__main__":
    Result = SumOfDigits(int(input("Enter a number : ")))
    print("Sum of digits of number is : ",Result)