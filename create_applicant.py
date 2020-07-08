import os
from subprocess import call
import sys
import pickle


#This program create new applicant files
class save:
    def __init__(self,name,mob,rep):
        self.name=name
        self.mob=mob
        self.rep=rep;

class create_list:
    def __init__(self,name,mob,rep):
        b=save(name,mob,rep)
        f = open("applicant.dat", "ab")
        pickle.dump(b,f,protocol=2)
        f.close()

    
if __name__ == '__main__':
    a=1
    while a==1:
        print("\n========= ENTER DETAILS OF NEW APPLICANT ==========")
        print("Enter Name :",sep=' ')
        name=input().strip()
        print("\nEnter mobile Number :",sep=' ')
        mob=int(input())
        print("\nEnter Background work :",sep=" ")
        rep=input()
        create_list(name,mob,rep)
        print("\nIf you want to continue Press 1 else Press 0: ",sep=" ")
        a=int(input())
    


