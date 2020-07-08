import os
from subprocess import call
import sys
import pickle

#This program shows evaluated result    

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

    
if __name__ == '__main__':
    print("\n========================= RESULT OF APPLICANT ==========================\n")
    print("=NAME=              =MOBILE NUMBER=         =REPORT=                   =EVALUATION=\n")

    f2 = open("result.dat", "rb")
    try:
        while True:
            s = pickle.load(f2)
            name = s.name.upper()
            mob = int(s.mob)
            rep = s.rep
            evalu=s.evalu
            print(name.ljust(25,' '),str(mob).ljust(15,' '),rep.ljust(30,' '),evalu)
            continue
            
    except EOFError:
        pass
    f2.close()
    


