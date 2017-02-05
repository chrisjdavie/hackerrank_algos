import unittest

from .run import sort_one_index, run

class TestSortOneIndex(unittest.TestCase):
    
    def check_output(self, input_arr, expected_output, ind_sort):
        actual_output = sort_one_index(input_arr, ind_sort)
        
        self.assertSequenceEqual(expected_output,
                                 actual_output)
        

    def test_sorted(self):
#        N = 5
        input_arr = [ 2, 4, 6, 8, 3 ]
        expected_output = [ 2, 3, 4, 6, 8 ]
        self.check_output(input_arr, expected_output, len(input_arr)-1)


    def test_simple(self):
#        N = 3
        input_arr = [ 1, 3, 2 ]
        expected_output = [ 1, 2, 3 ]
        self.check_output(input_arr, expected_output, len(input_arr)-1)
        

    def test_presorted(self):
        input_arr = [ 1, 2, 3 ]
        expected_output = [ 1, 2, 3 ]
        self.check_output(input_arr, expected_output, len(input_arr)-1)


    def test_length_one(self):
        input_arr = [ 1 ]
        expected_output = [ 1 ]
        self.check_output(input_arr, expected_output, len(input_arr)-1)


    def test_to_front(self):
        input_arr = [ 2, 1 ]
        expected_output = [ 1, 2 ]
        self.check_output(input_arr, expected_output, len(input_arr)-1)


    def test_not_first_index(self):
        input_arr = [ 1, 3, 2, 1 ]
        ind_sort = 2
        expected_output = [ 1, 2, 3, 1 ]
        self.check_output(input_arr, expected_output, ind_sort)


    def test_only_sorts_one_index(self):
        input_arr = [ 1, 3, 2, 1 ]
        ind_sort = 3
        expected_output = [ 1, 1, 3, 2 ]
        self.check_output(input_arr, expected_output, ind_sort)


class TestRun(unittest.TestCase):

    def test_run(self):
        # the functionality should be tested in the above
        # this is more of an integration test than anything
        input_arr = [ 1, 4, 3, 5, 6, 2 ]
        expected_output = [ [ 1, 4, 3, 5, 6, 2 ], 
                            [ 1, 3, 4, 5, 6, 2 ], 
                            [ 1, 3, 4, 5, 6, 2 ], 
                            [ 1, 3, 4, 5, 6, 2 ], 
                            [ 1, 2, 3, 4, 5, 6 ] ]
        for expected, actual in zip(expected_output, run(input_arr)):
            self.assertSequenceEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

