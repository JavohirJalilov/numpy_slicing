import requests
import numpy as np
import json

url = "https://codeschoolhomeworkapi.pythonanywhere.com/homework/attempt/"

class FillOnes:
    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        n, m = self.get_shape(solution)
        return np.equal(self.fill_ones(n, m), solution).all()
    
    def test_case_2(self, solution):
        return solution.__class__ == np.ndarray

    def check(self, solution, github_username):
        """
        Chack if the solution is correct

        Args:
            solution (np.ndarray): solution to check
            github_username (str): github username

        Returns:
            bool: True if the solution is correct
        """
        
        case1 = self.test_case_1(solution)
        case2 = self.test_case_2(solution)
        isSolved = case1 and case2

        data = {
            'github': github_username,
            'repo': 'AIGroup/numpy_slicing',
            'tasks': [
                {'isSolved': bool(isSolved), 'name': 'fill_ones'}]
            }
        print(data)
        response = requests.post(url, json=data)

        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)

    def hint(self):
        """
        Return a hint to the user

        Returns:
            str: hint
        """
        print("Create an array of NxN ones.")




class PatternOne:

    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        n, m = self.get_shape(solution)
        expected_arr = self.fill_ones(n, m)
        expected_arr[:,m//2:] = 2
        return np.equal(expected_arr, solution).all()

    def test_case_2(self, solution):
        return solution.__class__ == np.ndarray

    def check(self, solution, github_username):
        """
        Chack if the solution is correct

        Args:
            solution (np.ndarray): solution to check
            github_username (str): github username

        Returns:
            bool: True if the solution is correct
        """
        case1 = self.test_case_1(solution)
        case2 = self.test_case_2(solution)

        isSolved = case1 and case2

        data = {
            'github': github_username,
            'repo': 'AIGroup/numpy_slicing',
            'tasks': [
                {'isSolved': bool(isSolved), 'name': 'pattern_1'}]
            }
        response = requests.post(url, json=data)
        
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)

    def hint(self):
        """
        Return a hint to the user

        Returns:
            str: hint
        """
        print("Make a pattern")

q0 = FillOnes()
q1 = PatternOne()

arr = np.ones((10,10))
q1.check(arr, "JavohirJalilov")