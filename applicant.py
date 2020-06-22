import os
from subprocess import call
import sys
import pickle

#This program update or say add the result given by selection committee

class save:
    def __init__(self,name,mob,rep,evalu):
        self.name=name
        self.mobile_no=mob
        self.report=rep
        self.eval=evalu


def create(name,mob,rep,evalu):
    f = open("result.dat", "ab")
    b = save(name,mob,rep,evalu)
    pickle.dump(b,f,protocol=2)
    f.close()
    return 


def check():
    print("\n============== ENTER DETAILS OF THE APPLICANT ==============")
    print("Enter Name :",sep=' ')
    name=input().upper()
    print("\nEnter mobile Number :",sep=' ')
    mob=int(input())

    try:
        n=0
        f2 = open("applicant.dat", "rb")
        while True:
            s = pickle.load(f2)
            a = str(s.name).upper()
            b = int(s.mobile_no)

            if a==name and mob==b:
                n=1
                print("\nNAME : ", s.name)
                print("MOBILE NO.:  ",s.mobile_no)
                print("REPORT : ", s.report)
                print("ENTER EVALUATION :")
                evalu=input().strip()
                create(s.name,s.mobile_no,s.report,evalu)
            if n==1:
                return
            else:
                continue

    except EOFError:
        print("INVALID INPUT!")
        check()
    f2.close()

    
if __name__ == '__main__':
    guest=check()



