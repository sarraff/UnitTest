import os
from subprocess import call
import sys
import pickle

#This program shows list of current applicants 

class save:
    def __init__(self,name,mob,rep):
        self.name=name
        self.mob=mob
        self.rep=rep

    
if __name__ == '__main__':
    print("\n========================= LIST OF APPLICANT ==========================\n")
    print("=NAME=                =MOBILE NUMBER=       =REPORT=\n")

    f2 = open("applicant.dat", "rb")
    try:
        while True:
            s = pickle.load(f2)
            name = s.name.upper()
            mob = int(s.mob)
            rep = s.rep
            print(name.ljust(25,' '),str(mob).ljust(16,' '),rep)
            continue
            
    except EOFError:
        pass
    f2.close()
    


