import threading

def EvenAdd(List):
    sum = 0
    for i in range(len(List)):
        if(List[i] % 2 == 0):
            sum = sum + List[i]
    print("Sum of all even elements is : ",sum)

def OddAdd(List):
    sum = 0
    for i in range(len(List)):
        if(List[i] % 2 != 0):
            sum = sum + List[i]
    print("Sum of all odd elements is : ",sum)

if __name__ == "__main__":
    No = int(input("Enter number of elements : "))
    List = []

    print("Enter the elements : ")
    for i in range(No):
        a = int(input())
        List.append(a)

    t1 = threading.Thread(target = EvenAdd, args = (List, ))
    t2 = threading.Thread(target = OddAdd, args = (List, ))

    t1.start()
    t2.start()

    t2.join()
    t2.join()

    print("Exit from main")
