class atm:
    def __init__(self,name,acc_no,mobile,address,pin,balance):
        self.name=name
        self.acc_no=acc_no
        self.mobile=mobile
        self.address=address
        self.pin=pin
        self.balance=balance
    
    def Account_info(self):
        print("Name:" ,self.name)
        print("Account Number:",self.acc_no)
        print("Mobile Number:",self.mobile)
        print("Address:",self.address)
        #print("Pin:",self.pin)
    
    def Pin_change(self):
        while(True):
            new_pin=input("Enter new PIN ")
            pin_check=input("Enter new PIN ")
            if new_pin==pin_check:
                self.pin=new_pin
                print("PIN change succesful")
                break
            else:
                print("Try Again")
                continue
    
    def Balance_enquiry(self):
        print("Name:" ,self.name)
        print("Account Number:",self.acc_no)
        print("Account Balance:",self.balance)
    
    def Withdrawal(self):
        while(True):
            amt=int(input("Enter amount to withdraw "))
            if amt>self.balance:
                print("Not enough balance\nTry again")
                continue
            elif amt<=self.balance:
                self.balance-=amt
                print("Withdrawal successfull")
                print("Account balance:",self.balance)
                break

    def Deposit(self):
        amt=int(input("Enter amount to deposit "))
        self.balance+=amt
        print("Deposit successfull")
        print("Account balance:",self.balance)
        


user={}
blocked_acc=[]

def User_input():
    name=input("Enter name ")
    acc_no=input("Enter account number ")
    mobile=input("Enter mobile number ")
    address=input("Enter address ")
    pin=input("Enter pin ")
    balance=0
    user[acc_no]=atm(name,acc_no,mobile,address,pin,balance)
    #print(user)

def Data_fill():
    user["1"]=atm("Berlin","1","8123456711","Pune","1111",100040)
    user["2"]=atm("Tokyo","2","7658478221","Pune","2222",10000)
    user["3"]=atm("Denver","3","9970716075","Pune","3333",800)
    user["4"]=atm("Professor","4","9854712344","Pune","4444",28000)
    user["5"]=atm("Lisbon","5","8087564890","Pune","5555",12040)

Data_fill()

while(True):
    ch=int(input("Select one of the following Options\n1.New User\n2.Account Info\n3.PIN Change\n4.Balance Enquiry\n5.Withdraw Money\n6.Deposit Money\n0.Quit\nEnter Choice="))
    if ch==1:
        User_input()
    elif ch==2:
        count=3
        acc_no=input("Enter account number ")
        if acc_no in blocked_acc:
            print("Your account is blocked\nContact bank for details")
            continue
        while(True):
            pin_no=input("Enter pin ")
            #flag=Pin_check(acc_no,pin_no,count)
            if pin_no==user[acc_no].pin:
                user[acc_no].Account_info()
                break
            else:
                count-=1
                if count==0:
                    print("Your account is blocked")
                    blocked_acc.append(acc_no)
                    break
                print("Try again\nYou have",count,"tries")
                continue
    elif ch==3:
        count=3
        acc_no=input("Enter account number ")
        if acc_no in blocked_acc:
            print("Your account is blocked\nContact bank for details")
            continue
        while(True):
            pin_no=input("Enter pin ")
            if pin_no==user[acc_no].pin:
                user[acc_no].Pin_change()
                break
            else:
                count-=1
                if count==0:
                    print("Your account is blocked")
                    blocked_acc.append(acc_no)
                    break
                print("Try again\nYou have",count,"tries")
                continue
    elif ch==4:
        count=3
        acc_no=input("Enter account number ")
        if acc_no in blocked_acc:
            print("Your account is blocked\nContact bank for details")
            continue
        while(True):
            pin_no=input("Enter pin ")
            if pin_no==user[acc_no].pin:
                user[acc_no].Balance_enquiry()
                break
            else:
                count-=1
                if count==0:
                    print("Your account is blocked")
                    blocked_acc.append(acc_no)
                    break
                print("Try again\nYou have",count,"tries")
                continue
    elif ch==5:
        count=3
        acc_no=input("Enter account number ")
        if acc_no in blocked_acc:
            print("Your account is blocked\nContact bank for details")
            continue
        while(True):
            pin_no=input("Enter pin ")
            if pin_no==user[acc_no].pin:
                user[acc_no].Withdrawal()
                break
            else:
                count-=1
                if count==0:
                    print("Your account is blocked")
                    blocked_acc.append(acc_no)
                    break
                print("Try again\nYou have",count,"tries")
                continue
    elif ch==6:
        count=3
        acc_no=input("Enter account number ")
        if acc_no in blocked_acc:
            print("Your account is blocked\nContact bank for details")
            continue
        while(True):
            pin_no=input("Enter pin ")
            if pin_no==user[acc_no].pin:
                user[acc_no].Deposit()
                break
            else:
                count-=1
                if count==0:
                    print("Your account is blocked")
                    blocked_acc.append(acc_no)
                    break
                print("Try again\nYou have",count,"tries")
                continue
    elif ch==0:
        break
