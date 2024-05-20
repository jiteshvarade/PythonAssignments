
if __name__ == "__main__":
    print("Enter the filename you want to open : ")
    filename = input()

    try:
        fobj1 = open(filename,"r")

        if(fobj1):
            print("File exists in the current directory")
        else:
            print("File does not exist")

        data = fobj1.read()

        fobj2 = open("Demo.txt","x")
        fobj2.write(data)
        print("Data copied into Demo.txt successfully")
        
    except Exception as eobj:
        print("Error : ",eobj)
