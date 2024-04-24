
def Display(No):
    for i in range(No):
        for j in range(No):
            print(j+1, end=" ")
        print()

def main():
    No = int(input("Enter a number : "))
    Display(No)

if __name__ == "__main__":
    main()