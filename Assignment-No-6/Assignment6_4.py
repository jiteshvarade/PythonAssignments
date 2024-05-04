import threading

def small(str):
    num = 0
    for i in str:
        if i >= 'a' and i <= 'z':
            num = num + 1
    print("Number of small characters in string is : ",num)


def capital(str):
    num = 0
    for i in str:
        if i >= 'A' and i <= 'Z':
            num = num + 1
    print("Number of capital characters in string is : ",num)

def digits(str):
    num = 0
    for i in str:
        if i >= '0' and i <= '9':
            num = num + 1
    print("Number of digits in string is : ",num)

if __name__ == "__main__":
    str = input("Enter string : ")

    t1 = threading.Thread(target = small, args = (str, ))
    t2 = threading.Thread(target = capital, args = (str, ))
    t3 = threading.Thread(target = digits, args = (str, ))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")
