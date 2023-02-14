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

        response = requests.post(url, json=data)

        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)


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


class PatternTwo:

    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        n, m = self.get_shape(solution)
        expected_arr = self.fill_ones(n, m)
        expected_arr[n//2:,m//2:] = 2
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
                {'isSolved': bool(isSolved), 'name': 'pattern_2'}]
            }
        response = requests.post(url, json=data)
        
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)


class PatternThree:

    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        n, m = self.get_shape(solution)
        expected_arr = self.fill_ones(n, m)
        expected_arr[1:-1,1:-1] = 2
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
                {'isSolved': bool(isSolved), 'name': 'pattern_3'}]
            }
        response = requests.post(url, json=data)
        
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)


class PatternFour:

    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        n, m = self.get_shape(solution)
        expected_arr = self.fill_ones(n, m)
        expected_arr[:n//2,:m//2] = 2
        expected_arr[n//2:,:m//2] = 3
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
                {'isSolved': bool(isSolved), 'name': 'pattern_4'}]
            }
        response = requests.post(url, json=data)
        
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)

# ones_array[:n//2,m//2:] = 2
# ones_array[n//2:,m//2:] = 3
class PatternFive:

    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        n, m = self.get_shape(solution)
        expected_arr = self.fill_ones(n, m)
        expected_arr[:n//2,m//2:] = 2
        expected_arr[n//2:,m//2:] = 3
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
                {'isSolved': bool(isSolved), 'name': 'pattern_5'}]
            }
        response = requests.post(url, json=data)
        
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)


# ones_array[:n//2,m//2:] = 2
# ones_array[n//2:,m//2:] = 4
# ones_array[n//2:,:m//2] = 3
class PatternSix:
    
    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        n, m = self.get_shape(solution)
        expected_arr = self.fill_ones(n, m)
        expected_arr[:n//2,m//2:] = 2
        expected_arr[n//2:,m//2:] = 4
        expected_arr[n//2:,:m//2] = 3
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
                {'isSolved': bool(isSolved), 'name': 'pattern_6'}]
            }
        response = requests.post(url, json=data)
        
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)


# ones_array[1:-1,1:-1] = 2
# ones_array[2:-2,2:-2] = 4
class PatternSeven:
    
    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        n, m = self.get_shape(solution)
        expected_arr = self.fill_ones(n, m)
        expected_arr[1:-1,1:-1] = 2
        expected_arr[2:-2,2:-2] = 4
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
                {'isSolved': bool(isSolved), 'name': 'pattern_7'}]
            }
        response = requests.post(url, json=data)
        
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)

# test chess
# ones_array[::2,::2] = 2
# ones_array[1::2,1::2] = 2
class Chess:
        
    def get_shape(self, solution):
        return solution.shape

    def fill_ones(self, n, m):
        arr = np.ones(shape=(n, m),dtype=np.uint8)
        return arr

    def test_case_1(self, solution):
        n, m = self.get_shape(solution)
        expected_arr = self.fill_ones(n, m)
        expected_arr[::2,::2] = 2
        expected_arr[1::2,1::2] = 2
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
                {'isSolved': bool(isSolved), 'name': 'chess'}]
            }
        response = requests.post(url, json=data)
        
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)
q0 = FillOnes()
q1 = PatternOne()
q2 = PatternTwo()
q3 = PatternThree()
q4 = PatternFour()
q5 = PatternFive()
q6 = PatternSix()
q7 = PatternSeven()
q8 = Chess()