import numpy as np
import requests

class CheckSolution:
    def __init__(self, task_name):
        self.task_name = task_name
        self.url = "https://codeschoolhomeworkapi.pythonanywhere.com/homework/attempt/"
    def checking(self, solution, github_username, isSolved):

        """
        Chack if the solution is correct

        Args:
            solution (np.ndarray): solution to check
            github_username (str): github username

        Returns:
            bool: True if the solution is correct
        """

        data = {
            'github': github_username,
            'repo': 'AIGroup/numpy_slicing',
            'tasks': [
                {'isSolved': bool(isSolved), 'name': self.task_name}]
            }

        response = requests.post(self.url, json=data)

        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)


class FillOnes(CheckSolution):
    def __init__(self, task_name):
        super().__init__(task_name)
    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        try:
            n, m = self.get_shape(solution)
            return bool(np.equal(self.fill_ones(n, m), solution).all())
        except:
            return False
    
    def test_case_2(self, solution):
        return solution.__class__ == np.ndarray

    def check(self, solution, github_username):
        case1 = self.test_case_1(solution)
        case2 = self.test_case_2(solution)
        isSolved = all([case1, case2])
        self.checking(solution, github_username, isSolved)

# expected_arr[:,m//2:] = 2
class PatternOne(CheckSolution):
    def __init__(self, task_name):
        super().__init__(task_name)
    
    def get_shape(self, solution):
        return solution.shape
    
    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr
    
    def test_case_1(self, solution):
        try:
            n, m = self.get_shape(solution)
            return bool(np.equal(self.fill_ones(n, m), solution).all())
        except:
            return False
    
    def test_case_2(self, solution):
        return solution.__class__ == np.ndarray
    
    def test_case_3(self, solution):

        try:
            n, m = self.get_shape(solution)
            expected_arr = self.fill_ones(n, m)
            expected_arr[:,m//2:] = 2
            return bool(np.equal(expected_arr, solution).all())
        except:
            return False
    
    def check(self, solution, github_username):
        case1 = self.test_case_1(solution)
        case2 = self.test_case_2(solution)
        case3 = self.test_case_3(solution)
        isSolved = all([case1, case2, case3])
        self.checking(solution, github_username, isSolved)
    

q0 = FillOnes('fill_ones')
q1 = PatternOne('pattern_1')
arr = np.ones(shape=(3, 4),dtype=np.uint8)
q1.check(arr, 'JavohirJalilov')
# q0.check(arr, 'JavohirJalilov')