
def ChkPrime(No):
    for i in range(2,int(No/2) + 2):
        if(No % i == 0):
            return False
    return True

def main():
    No = int(input("Enter a number : "))
    Result = ChkPrime(No)

    if(Result == True):
        print("Number is prime")
    else:
        print("Number is not prime")

if __name__ == "__main__":
    main()