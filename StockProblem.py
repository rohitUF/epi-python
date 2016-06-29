import unittest

def findMaxProfit(start):
    if not start:
        return 0
        
    maxProfit = 0
    minPrice = start[0]
    
    for price in start:
        if price < minPrice:
            minPrice = price
        
        profit = price - minPrice
        if profit > maxProfit:
            maxProfit = profit
            
    return maxProfit
    
class TestMaxProfit(unittest.TestCase):
    
    def testMaxProfit(self):
        start = [3, 11, 2, 24, 1, 17, 12, 9, 3, 11]
        self.assertEqual(findMaxProfit(start), 22)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxProfit)
    unittest.TextTestRunner(verbosity=2, buffer=False).run(suite)