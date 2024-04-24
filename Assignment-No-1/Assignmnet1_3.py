
def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))
    Result = Addition(No1, No2)
    print("Addition is : ",Result)

if __name__ == "__main__":
    main()