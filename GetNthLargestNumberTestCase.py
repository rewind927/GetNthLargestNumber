import unittest
from GetNthLargestNumber import *

class NthLargestNumberTestCase(unittest.TestCase):
    def test_get_nth_largest_number1(self):
        self.assertEquals(getNthLargestNumber(3,["10","20","30","1","2","3","4"]),[30,20,10])

    def test_get_nth_largest_number2(self):
        self.assertEquals(getNthLargestNumber(2,["10","20","30","1","2","3","4"]),[30,20])

    def test_get_nth_largest_number3(self):
        self.assertEquals(getNthLargestNumber(4,["10","20","30","1","2","3","4"]),[30,20,10,4])

    def test_get_nth_largest_number4(self):
        self.assertEquals(getNthLargestNumber(3,["10000","10","20","30","1","9999","2","3","4","9998"]),[10000,9999,9998])

    def test_get_nth_largest_number5(self):
        self.assertEquals(getNthLargestNumber(4,["10000","10","20","30","1","9999","2","3","4","9998"]),[10000,9999,9998,30])
    
    def test_get_nth_largest_number6(self):
        self.assertEquals(getNthLargestNumber(3,["23","10000","10001","10","20","30","1","9999","2","3","4","9998"]),[10001,10000,9999])
if __name__ == '__main__':
    unittest.main()
