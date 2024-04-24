def ChkNumber(No):
    if No % 2 == 0 : 
        return True
    else :
        return False

def main():
    No = int(input("Enter the number : "))
    Ret = ChkNumber(No)

    if Ret == True:
        print("Number is even")
    else:
        print("Number is odd")

if __name__ == "__main__" : 
    main()