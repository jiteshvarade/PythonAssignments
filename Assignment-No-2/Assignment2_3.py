
def Factorial(No):

    if(No == 0):
        return 0

    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
    return Fact

def main():
    No = int(input("Enter a number : "))
    Result = Factorial(No)
    print("Factorial of number is : ",Result)

if __name__ == "__main__":
    main()