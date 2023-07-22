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
    # Explanation: If you give all extraCandies to:
    # - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
    # - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    # - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
    # - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
    # - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    assert result == [True, True, True, False, True]


def test_case_2():
    solution = Solution()
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    result = solution.kidsWithCandies(candies, extraCandies)
    # Explanation: There is only 1 extra candy.
    # Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
    assert result == [True, False, False, False, False]
