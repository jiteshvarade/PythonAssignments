import threading

def DisplayEven(No):
    j = 2
    for i in range(No):
        print(j)
        j = j + 1

def DisplayOdd(No):
    j = 1
    for i in range(No):
        print(j)
        j = j + 1

if __name__ == "__main__":
    
    t1 = threading.Thread(DisplayEven(10))
    t2 = threading.Thread(DisplayOdd(10))

    t1.start()
    t2.start()

    t2.join()
    t2.join()
