Fact = 1
i = 1

def FactorialR(No):
    global Fact
    global i
    if(i > No):
        return
    Fact = Fact * i
    i = i + 1
    FactorialR(No)
    return Fact

if __name__ == "__main__":
    No = int(input("Enter number : "))
    Result = FactorialR(No)
    print("Factorial of number is ",Result)