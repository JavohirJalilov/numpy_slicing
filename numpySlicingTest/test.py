import requests
import numpy as np
import json
from test_case_fill_one.test_case import TestCaseFillOne
from test_case_pattern_1.test_case import TestCasePatternOne

url = "https://codeschoolhomeworkapi.pythonanywhere.com/homework/attempt/"

class FillOnes:
    def check(self, solution, github_username):
        """
        Chack if the solution is correct

        Args:
            solution (np.ndarray): solution to check
            github_username (str): github username

        Returns:
            bool: True if the solution is correct
        """
        
        case1 = TestCaseFillOne(solution).case_1()
        case2 = TestCaseFillOne(solution).case_2()
        isSolved = case1 and case2

        data = {
            'github': github_username,
            'repo': 'AIGroup/numpy_slicing',
            'tasks': [
                {'isSolved': bool(isSolved), 'name': 'fill_ones'}]
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
        print("Create an array of NxN ones.")

class PatternOne:
    def check(self, solution, github_username):
        """
        Chack if the solution is correct

        Args:
            solution (np.ndarray): solution to check
            github_username (str): github username

        Returns:
            bool: True if the solution is correct
        """
        case1 = TestCasePatternOne(solution).case_1()
        case2 = TestCasePatternOne(solution).case_2()

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

# arr = np.ones((10,10))
# q0.check(arr, "JavohirJalilov")