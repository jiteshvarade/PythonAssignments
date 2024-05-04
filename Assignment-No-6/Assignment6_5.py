import threading

def DisplayInOrder(No):
    for i in range(1,No+1):
        print(i)

def DisplayInReverseOrder(No):
    for i in range(No,0,-1):
        print(i)

if __name__ == "__main__":
    No = int(input("Enter number : "))

    t1 = threading.Thread(target = DisplayInOrder, args = (No, ))
    t2 = threading.Thread(target = DisplayInReverseOrder, args = (No, ))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")
