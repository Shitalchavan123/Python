class bank_account:

    def __init__(self):
        self.name=""
        self.Amount=0
        self.Address=""
        self.Accountno=0

    def createaccount(self):
        print("Enter your name")
        self.Name=input()

        print("Enter initial amount")
        self.Amount= int(input())

        print("Enter your address")
        self.Address = input()

        print("Enter your account number")
        self.Accountno = int(input())

    def displayaccountinfo(self):
        print("_____Your account details are as below:_____")
        print("Name of account holder:",self.name)
        print("Account Number:",self.Accountno)
        print("Address of account holder:",self.Address)
        print("Current amount in account:",self.Amount)




def main():
    user1=bank_account()
    user2=bank_account()

    user1.createaccount()
    user1.displayaccountinfo()


if __name__ == "__main__":
    main()