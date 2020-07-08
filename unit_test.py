#Author : Nishant Sarraff
#Roll No. : B18CSE064
import pytest
import main
import unittest

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


class TestMain(unittest.TestCase):
    def test_check(self):
        a=main.check("Nishant",98132,98)
        b=main.check("Rushil",12456,45)
        c=main.check("Ritu",56789,65)
        d=main.check("xyz",12345,94)
        self.assertEqual(a,1)
        self.assertEqual(b,1)
        self.assertEqual(c,1)
        self.assertEqual(d,1)


    def test_check2(self):
        a=main.check("Nisha",98132,45)
        b=main.check("Rushil",12476,41)
        c=main.check("Ritu",56349,64)
        d=main.check("xyza",1234,65)
        self.assertEqual(a,0)
        self.assertEqual(b,0)
        self.assertEqual(c,0)
        self.assertEqual(d,0)


    def test_check3(self):
        with self.assertRaises(TypeError):
            a=main.check(98132,"Nishant",53)
        with self.assertRaises(TypeError):
            a=main.check("xyz","xyz","34")
        with self.assertRaises(TypeError):
            a=main.check("xyz",12345,"12345")  

    def test_check4(self):
        with self.assertRaises(ValueError):
            d=main.check("xyz",12345,-94)
        with self.assertRaises(ValueError):
            d=main.check("xyz",12345,294)
        with self.assertRaises(ValueError):
            d=main.check("xyz",12345,101) 
        

if __name__ == '__main__':
    unittest.main()


