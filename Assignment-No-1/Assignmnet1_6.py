
def ChkNumber(No):
    if(No > 0):
        return True,False
    elif(No < 0):
        return False,True
    else:
        return False,False

def main():
    No = int(input("Enter number : "))
    Result1, Result2 = ChkNumber(No)

    if(Result1 == True):
        print("Number is positive")
    elif(Result2 == True):
        print("Number is negative")
    else:
        print("Nummber is zero")

if __name__ == "__main__":
    main()