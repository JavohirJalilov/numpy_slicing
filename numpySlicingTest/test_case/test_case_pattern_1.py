import numpy as np

class TestCasePatternOne:
    def __init__(self, solution):
        self.solution = solution
    
    def get_shape(self):
        return self.solution.shape

    def fill_ones(self):
        n, m = self.get_shape()
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def case_1(self):
        n, m = self.get_shape()
        expected_arr = self.fill_ones()
        expected_arr[:,m//2:] = 2
        return np.equal(expected_arr, self.solution).all()

    def case_2(self):
        return (self.solution).__class__ == np.ndarray