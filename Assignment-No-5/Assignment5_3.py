
def Display(No):
    if(No < 1):
        return
    print(No, end =" ")
    No = No - 1
    Display(No)

if __name__ == "__main__":
    Display(int(input("Enter a number : ")))