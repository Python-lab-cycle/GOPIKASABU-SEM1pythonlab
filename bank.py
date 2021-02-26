Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class bank():
    def __init__(self,acnt,name,typ,amt):
        self.ac=acnt
        self.nam=name
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("acnt name=",self.nam)
        print("acnt num=",self.ac)
        print("acnt type=",self.type)
        print("bal=",self.amount)
    def withl(self,wl):
        return(self.amount-wl)
n=input("Enter name:")
t=input("Enter type:")
a=int(input("Enter numbr:"))
am=int(input("Enter amount:"))
obj=bank(a,n,t,am)
print("Account details")
obj.printamt()
w=int(input("Enter amount to withdraw:"))
print("b1=",obj.withl(w))