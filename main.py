import os
from subprocess import call
import sys
import pickle

'''
HR Recruitment Model: Interview portal
After registration, shortlisted by the committee, and presenting the seminar, 
the applicant gives the interview to the selection committee.

This is a python based setup, where create_applicant.py create the list of applicants and store it in applicant.dat. 
The main program is main.py, which accesses the applicant's info and updates the info into result.dat. 
You can see the result after running result.py.
'''
       
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
    elif not type(evalu) is int:
        raise TypeError("Only int are allowed")
    elif not type(mob) is int :
        raise TypeError("Only int are allowed")
    elif evalu<0 or evalu>100:
        raise ValueError("Invalid evaluation report")
    else:
        name=name.upper()
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
                    # print("match found")
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

#This calls applicant program, and stores evaluated report given by committee
def checkinn():
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
    evalu=input()
    for i in evalu:
        if i.isalpha():
            print("Invalid Input!\n")
            return
    ev=int(evalu)
    if ev<0 or ev>100:
        print("Invalid evaluation report!\n")
        return
    a=check(name,mob,ev)
    if a==1:
        print("Found and Updated!")
    else :
        print("\nINVALID INPUT!  MATCH NOT FOUND!!\n")


#This call list.py and shows the list of current applicant
#You can add applicant by running create_applicant.py
def click_list():
    call(["python", "list.py"])

#This shows evaluated report
def  result():
    call(["python", "result.py"])

#This is the main body of the program
class INTERVIEW:
    def __init__(self):
        a=1
        while a!='4':
            print("\n\n================= WELCOME TO IITJ INTERVIEW PORTAL ====================\n")
            print("1. Applicant Report")
            print("2. Lists of Applicant")
            print("3. Result list")
            print("4. Exit portal\n")
            print("Choose : ")
            a=input()
            if a<'1' or a>'4':
                print("Invalid Input!\n\n")
            if a=='2':
                click_list() 
            if a=='1':
                checkinn()
            if a=='3':
                result()

    
if __name__ == '__main__':
    GUUEST=INTERVIEW()


