from CheckingAccount import *
import unittest


class Test(unittest.TestCase):
    def test_CheckingAccount(self):
        result = CheckingAccount.rewardsPoints(self,200)
        expected = 2
        self.assertEqual(expected, result)
        
        
        
        
        
if __name__== '__main__':
    unittest.main()
