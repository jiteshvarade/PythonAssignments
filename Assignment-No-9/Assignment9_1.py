
if __name__ == "__main__":
    print("Enter the filename you want to open : ")
    filename = input()
    try:
        fobj = open(filename)
        if(fobj):
            print("File exists in the current directory")
        else:
            print("File does not exist")
    except Exception as eobj:
        print("Error opening file")
