
if __name__ == "__main__":
    print("Enter the name of first file : ")
    filename1 = input()
    print("Enter the name of second file : ")
    filename2 = input()

    try:
        fobj1 = open(filename1,"r")
        fobj2 = open(filename2,"r")
        if(fobj1 and fobj2):
            data1 = fobj1.read()
            data2 = fobj2.read()
            if(data1 == data2):
                print("Success")
            else:
                print("Failure")
        else:
            print("File does not exist")

    except Exception as eobj:
        print("Error : ",eobj)
