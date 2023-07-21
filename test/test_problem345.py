# test/test_problem345.py

import sys
import os

# Add the main directory (project_root) to the Python path
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(main_dir)

from problem345 import Solution

def test_case_1():
    solution = Solution()
    s = "hello"
    result = solution.reverseVowels(s)
    assert result == "holle"


def test_case_2():
    solution = Solution()
    s = "leetcode"
    result = solution.reverseVowels(s)
    assert result == "leotcede"
