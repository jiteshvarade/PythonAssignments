
def AdditionOfFactors(No):
    sum = 0
    for i in range(1, int(No/2) + 1):
        if((No % i) == 0):
            sum = sum + i
    return sum

def main():
    No = int(input("Enter a number : "))
    Result = AdditionOfFactors(No)
    print("Addition of factors of the number is : ", Result)

if __name__ == "__main__":
    main()