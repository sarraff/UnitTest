import os
from subprocess import call
import sys

'''
HR Recruitment Model: Interview portal
After registration, shortlisted by the committee, and presenting the seminar, 
the applicant gives the interview to the selection committee.

This is a python based setup, where create_applicant.py create the list of applicants and store it in applicant.dat. 
The main program is main.py, which accesses the applicant's info and updates the info into result.dat. 
You can see the result after running result.py.
'''

#This calls applicant program, and stores evaluated report given by committee
def checkinn():
    call(["python", "applicant.py"])

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
        while a!=4:
            print("\n\n================= WELCOME TO IITJ INTERVIEW PORTAL ====================\n")
            print("1. Applicant Report")
            print("2. Applicant Lists")
            print("3. Result list")
            print("4. Exit portal\n")
            print("Choose : ")
            a=int(input())
            if a<1 or a>4:
                print("Invalid Input!\n\n")
                INTERVIEW()
            if a==2:
                click_list() 
            if a==1:
                checkinn()
            if a==3:
                result()

class stubi:
    def __init__(self,a):
        self.a=a
        if not (isinstance(a,int)):
            print("INVALID data type\n")          
        elif a<1 or a>4:
            print("Invalid Input!\n\n")
        elif a==2:
            click_list() 
        elif a==3:
            result()
    
if __name__ == '__main__':
    GUUEST=INTERVIEW()


