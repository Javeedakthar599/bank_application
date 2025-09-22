class Bank():
    Branch='marathahalli'
    IFSC ='BANK000022'
    ROI = 0.07
    def __init__(self,name,mobno,aadhar,gender,bal,pin):
        self.name=name
        self.mobno=mobno
        self.aadhar=aadhar
        self.gender=gender
        self.bal=bal
        self.pin=pin
    def details(self):
        print(f'name:{self.name}')
        print(f'mobno:{self.mobno}')
        print(f'aadhar:{self.aadhar}')
        print(f'gender:{self.gender}')
        print(f'bal:{self.bal}')
        print(f'pin:{self.pin}')

    @classmethod
    def updatebranch(cls):
        cls.branch='whitefield'
    def withdraw(self):
        count=3
        while count!=0:
            print(f'no.of attempts is {count}')
            if self.password()==self.pin:
                amount=int(input('enter the amount to withdraw'))
                if self.bal>=amount:
                    if 100<=amount<=10000:
                        if amount%100==0:
                            self.bal-=amount
                            print('debited successfully')
                            print(f'available balaance is {self.bal}')
                        else:
                            print('incorrect denomination')
                    else:
                        print('invalid amount')
                else:
                    print('insufficient balance')
            else:
                print('invalid pin')
                count-=1
        else:
            print('try after 24-hours')
        
    def deposite(self):
        cash=int(input('enter the amount to deposite'))
        if 100 <=cash <=10000:
            if cash%100==0:
                self.bal+=cash
                print('amount credited successfully')
                print(f'updated balance is {self.bal}')
            else:
                print('incorrect denomination')
        else:
            print('enter valid amount')

    def checkbal(self):
        count=3
        while count!=0:
            print(f'no of attempts is {count}')
            if self.password()==self.pin:
                print(f' available balance is {self.bal}')
                break
            else:
                print('invalid pin')
                count-=1
        else:
            print('try after 24 hours')

    @staticmethod
    def password():
        a=int(input('enter 4-digit pin'))
        return a
    def changepin(self):
        if self.password==self.pin:
            self.pin=int(input('enter the 4-digit pin'))
            
                
user1=Bank('javeed',7624848538,123456789012,'male',20000,1234)
user2=Bank('akthar',7624848583,123456789021,'female',15000,1211)
user1.deposite()

        
