
class BankAccount:
    ROI = 10.5

    def __init__(self,i,j):
        self.Name = i
        self.Amount = j

    def Display(self):
        print("Name of account holder : ",self.Name)
        print("Amount : ",self.Amount)

    def Deposit(self, i):
        self.Amount = self.Amount + i

    def Withdraw(self, i):
        self.Amount = self.Amount - i

    def CalculateIntrest(self):
        return float(self.Amount) * (BankAccount.ROI/100.00)

if __name__ == "__main__":
    Obj1 = BankAccount("Jagdish Banner",5000)
    Obj1.Deposit(2000)
    Obj1.Withdraw(200)
    Obj1.Display()
    print("Intrest earned after 1 year : ",Obj1.CalculateIntrest())

    Obj2 = BankAccount("Chatur Ramalingam",100)
    Obj2.Deposit(4000)
    Obj2.Withdraw(300)
    Obj2.Display()
    print("Intrest earned after 1 year : ",Obj2.CalculateIntrest())
