import os
from subprocess import call
import sys
import pickle

#This program update or say add the result given by selection committee

class save:
    def __init__(self,name,mob,rep):
        self.name=name
        self.mob=mob
        self.rep=rep

class new_save:
    def __init__(self,name,mob,rep,evalu):
        self.name=name
        self.mob=mob
        self.rep=rep
        self.evalu=evalu

def check(name,mob,evalu):
    if not type(name) is str :
        raise TypeError("Only strings are allowed")
    elif not type(evalu) is str :
        raise TypeError("Only strings are allowed")
    elif not type(mob) is int :
        raise TypeError("Only int are allowed")
    else:
        try:
            n=0
            f2 = open("applicant.dat", "rb")
            while True:
                s = pickle.load(f2)
                a = str(s.name).upper()
                b = int(s.mob)
    
                if a==name and mob==b:
                    n=1
                    create(s.name,s.mob,s.rep,evalu)
                if n==1:
                    f2.close()
                    return 1
                else:
                    continue
        except EOFError:
            f2.close()
    return 0


def create(name,mob,rep,evalu):
    f = open("result.dat", "ab")
    b = new_save(name,mob,rep,evalu)
    pickle.dump(b,f,protocol=2)
    f.close()
    return 


def entry():
    print("\n============== ENTER DETAILS OF THE APPLICANT ==============")
    print("Enter Name :",sep=' ')
    name=input().upper()
    print("\nEnter mobile Number :",sep=' ')
    mo=input()
    for i in mo:
        if i.isalpha():
            print("Invalid Input!\n")
            return 
    mob=int(mo)
    print("\nEnter evaluation report : ")
    evalu=input().strip()
    a=check(name,mob,evalu)
    if a==1:
        print("Found and Updated!")
    elif a==0:
        print("\nINVALID INPUT!  MATCH NOT FOUND\n")

    

    
if __name__ == '__main__':
    guest=entry()



