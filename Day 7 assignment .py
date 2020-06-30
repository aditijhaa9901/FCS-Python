ASSIGNMENT 1

#Creating a sample file as to complete the given task
F=open("LetsUpgradeAssignment.txt","w")
F.write("Hello everyone this is the sample file created")
F.close()


#The assignment asked to be done
F=open("LetsUpgradeAssignment.txt", "r")
try:
    F.write("This is the text I am trying to add to the sample file which was already created")
except Exception as e:
    print("There was an error in your statement.\nthe error is ->", e)
finally:
    F.close()


 ASSIGNMENT 2

! pip install Pylint
import unittest
%%writefile prime_number.py
#The function to find whether the number is prime or not

def prime_num(num):
    A=0
    if (num==2):
        return True
    else:
        for i in range(2,num):
            if (num%i==0):
                A=1
                return False
                break
        if(A==0):
            return True

OVERWRITING 


%%writefile prime_number_test.py

#This is the code where we test if the function works
import unittest
import prime_number

class PrimeTesting(unittest.TestCase):
    def test1(self):
        temp_num= 2
        result= prime_number.prime_num(temp_num)
        self.assertAlmostEqual(result,True)

    def test2(self):
        temp_num= 5
        result= prime_number.prime_num(temp_num)
        self.assertAlmostEqual(result,True)
    
    def test3(self):
        temp_num= 97
        result= prime_number.prime_num(temp_num)
        self.assertAlmostEqual(result,True)
    
    def test4(self):
        temp_num= 56
        result= prime_number.prime_num(temp_num)
        self.assertAlmostEqual(result,False)

    def test5(self):
        temp_num= 45
        result= prime_number.prime_num(temp_num)
        self.assertAlmostEqual(result,False)
    
    def test6(self):
        temp_num=100
        result= prime_number.prime_num(temp_num)
        self.assertAlmostEqual(result,False)
    
if __name__ == "__main__":
    unittest.main()

! python prime_number_test.py
