import unittest

from .run import run

class TestSort(unittest.TestCase):
    
    def check_output(self, input_arr, sample_output):
        actual_output = list(run(input_arr))
        
        self.assertSequenceEqual(sample_output,
                                 actual_output)
        

    def test_sorted(self):
#        N = 5
        input_arr = [ 2, 4, 6, 8, 3 ]
        sample_output = [ [ 2, 4, 6, 8, 8 ], 
                          [ 2, 4, 6, 6, 8 ], 
                          [ 2, 4, 4, 6, 8 ], 
                          [ 2, 3, 4, 6, 8 ] ]
        self.check_output(input_arr, sample_output)


    def test_simple(self):
#        N = 3
        input_arr = [ 1, 3, 2 ]
        sample_output = [ [ 1, 3, 3 ], 
                          [ 1, 2, 3 ] ]
        self.check_output(input_arr, sample_output)
        

    def test_presorted(self):
        input_arr = [ 1, 2, 3 ]
        sample_output = [ [ 1, 2, 3 ] ]
        self.check_output(input_arr, sample_output)


    def test_length_one(self):
        input_arr = [ 1 ]
        sample_output = [ [ 1 ] ]
        self.check_output(input_arr, sample_output)


    def test_to_front(self):
        input_arr = [ 2, 1 ]
        sample_output = [ [ 2, 2 ],
                          [ 1, 2 ] ]
        self.check_output(input_arr, sample_output)

if __name__ == "__main__":
    unittest.main()
