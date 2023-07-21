# test/test_problem1431.py

import sys
import os

# Add the main directory (project_root) to the Python path
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(main_dir)

from problem1431 import Solution

def test_case_1():
    solution = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    result = solution.kidsWithCandies(candies, extraCandies)
    assert result == [True, True, True, False, True]


def test_case_2():
    solution = Solution()
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    result = solution.kidsWithCandies(candies, extraCandies)
    assert result == [True, False, False, False, False]
