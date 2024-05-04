import threading

def EvenFactor(No):
    sum = 0
    for i in range(2,int(No/2)+1):
        if No % i == 0:
            if i % 2 == 0:
                sum = sum + i
    print("Sum of even factors : ",sum)

def OddFactor(No):
    sum = 0
    for i in range(2,int(No/2)+1):
        if No % i == 0:
            if i % 2 != 0:
                sum = sum + i
    print("Sum of even factors : ",sum)

if __name__ == "__main__":
    No = int(input("Enter a number : "))

    t1 = threading.Thread(target = EvenFactor, args = (No, ))
    t2 = threading.Thread(target = OddFactor, args = (No, ))

    t1.start()
    t2.start()

    t2.join()
    t2.join()

    print("Exit from main")
