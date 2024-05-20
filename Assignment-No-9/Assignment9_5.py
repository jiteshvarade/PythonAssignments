
if __name__ == "__main__":
    print("Enter the name of first file : ")
    filename = input()
    print("Enter the string : ")
    str = input()

    try:
        fobj = open(filename,"r")
        if(fobj):
            data = fobj.read()
            count = 0
            index = 0
            while True:
                index = data.find(str,index)
                if(index == -1):
                    break
                count += 1
                index += 1

            print("Frequency of string inside file is : ",count)
        else:
            print("File does not exist")

    except Exception as eobj:
        print("Error : ",eobj)
