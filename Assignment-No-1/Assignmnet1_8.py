
def Display(No):
    for i in range(No):
        print("*", end=" ")

def main():
    No = int(input("Enter a number : "))
    Display(No)

if __name__ == "__main__":
    main()