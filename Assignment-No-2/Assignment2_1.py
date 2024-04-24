import Arithmetic

def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    Result = Arithmetic.Addition(No1, No2)
    print("Addition of numbers is : ", Result)

    Result = Arithmetic.Substraction(No1, No2)
    print("Substraction of numbers : ",Result)

    Result = Arithmetic.Multiplication(No1, No2)
    print("Multiplication of numbers : ",Result)

    Result = Arithmetic.Division(No1, No2)
    print("Division of numbers : ",Result)

if __name__ == "__main__":
    main()