
def AdditionOfDigits(No):
    Ans = 0
    while(No != 0):
        Ans = Ans + (No % 10)
        No = int(No / 10)
    return Ans

def main():
    No = int(input("Enter a number : "))
    Result = AdditionOfDigits(No)
    print("Addition of Digits in the given number is : ", Result)

if __name__ == "__main__":
    main()