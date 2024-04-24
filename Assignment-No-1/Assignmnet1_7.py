
def ChkDivisible(No):
    if (No % 5 == 0):
        return True
    else:
        return False

def main():
    No = int(input("Enter the number : "))
    Result = ChkDivisible(No)
    
    if(Result == True):
        print("Number is divisible by 5")
    else:
        print("Number is not Divisible by 5")

if __name__ == "__main__":
    main()