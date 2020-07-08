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
	create_list("Nishant",98132,"Graduated from IITJ")
	create_list("Rushil",12456,"Graduated from IITB")
	create_list("Ritu",56789,"Graduated from IITK")
	create_list("xyz",12345,"Graduated from IITR")
	create_list("sahil",45678,"Graduated from IITD")