# test/test_problem1071.py

import sys
import os

# Add the main directory (project_root) to the Python path
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(main_dir)

from problem1071 import Solution

def test_case_1():
    solution = Solution()
    str1 = "ABCABC"
    str2 = "ABC"
    result = solution.gcdOfStrings(str1, str2)
    assert result == "ABC"


def test_case_2():
    solution = Solution()
    str1 = "ABABAB"
    str2 = "ABAB"
    result = solution.gcdOfStrings(str1, str2)
    assert result == "AB"


def test_case_3():
    solution = Solution()
    str1 = "LEET"
    str2 = "CODE"
    result = solution.gcdOfStrings(str1, str2)
    assert result == ""
