import unittest

from .solution import competition, compare_scores

class testComplete(unittest.TestCase):


    def test_example(self):

        a_i = ( 5, 6, 7 )
        b_i = ( 3, 6, 10 )

        a_score, b_score = compare_scores( a_i, b_i )

        self.assertEqual(a_score, 1)
        self.assertEqual(b_score, 1)


class testOneComparison(unittest.TestCase):


    def test_alice_wins(self):
        a_score, b_score = competition( 2, 1 )
        self.assertEqual(a_score, 1)
        self.assertEqual(b_score, 0)


    def test_draw(self):
        a_score, b_score = competition( 1, 1 )
        self.assertEqual( a_score, 0 )
        self.assertEqual( b_score, 0 )

    
    def test_bob_wins(self):
        a_score, b_score = competition( 1, 2 )
        self.assertEqual( a_score, 0 )
        self.assertEqual( b_score, 1 )

