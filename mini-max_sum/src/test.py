
import unittest

from .solution import mini_max_sum

class testMiniMaxSum(unittest.TestCase):

    def test_basic(self):
        
        nums = [ 1, 2, 3, 4, 5 ]

        mini, maxi = mini_max_sum(nums)

        self.assertEqual( mini, 10 )
        self.assertEqual( maxi, 14 )


    def test_same(self):

        nums = [ 1, 1, 1, 1, 1 ]

        mini, maxi = mini_max_sum(nums)

        self.assertEqual( mini, 4 )
        self.assertEqual( maxi, 4 )


    def test_highest(self):

        nums = [ 10**9, 10**9, 10**9, 10**9, 10**9 ]

        mini, maxi = mini_max_sum(nums)

        self.assertEqual( mini, 4*10**9 )
        self.assertEqual( maxi, 4*10**9 )


    def test_rounding(self):

        nums = [ 10**9, 1, 10**9, 10**9, 10**9 ]

        mini, maxi = mini_max_sum(nums)

        self.assertEqual( mini, 3*10**9 + 1 )
        self.assertEqual( maxi, 4*10**9 )

