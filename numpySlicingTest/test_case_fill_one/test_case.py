import numpy as np

class TestCaseFillOne:
    def __init__(self, solution):
        self.solution = solution
    
    def get_shape(self):
        return self.solution.shape

    def fill_ones(self):
        n, m = self.get_shape()
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def case_1(self):
        return np.equal(self.fill_ones(), self.solution).all()
    
    def case_2(self):
        return (self.solution).__class__ == np.ndarray