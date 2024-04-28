i = 1

def Display(No):
    global i
    if(i > No):
        return
    print(i, end =" ")
    i = i + 1
    Display(No)

if __name__ == "__main__":
    Display(int(input("Enter a number : ")))