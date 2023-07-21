# test/test_problem345.py

import sys
import os

# Add the main directory (project_root) to the Python path
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(main_dir)

from problem605 import Solution

def test_case_1():
    solution = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    assert result == True


def test_case_2():
    solution = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    result = solution.canPlaceFlowers(flowerbed, n)
    assert result == False
