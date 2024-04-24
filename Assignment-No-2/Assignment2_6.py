
def Display(No):
    k = No
    for i in range(No):
        for j in range(k):
            print("*", end=" ")
        k = k - 1
        print()

def main():
    No = int(input("Enter a number : "))
    Display(No)

if __name__ == "__main__":
    main()