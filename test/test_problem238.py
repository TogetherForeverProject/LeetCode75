# test/test_problem238.py

import sys
import os

# Add the main directory (project_root) to the Python path
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(main_dir)

from problem238 import Solution

def test_case_1():
    solution = Solution()
    nums = [1, 2, 3, 4]
    result = solution.productExceptSelf(nums)
    assert result == [24, 12, 8, 6]


def test_case_2():
    solution = Solution()
    nums = [-1, 1, 0, -3, 3]
    result = solution.productExceptSelf(nums)
    assert result == [0, 0, 9, 0, 0]
