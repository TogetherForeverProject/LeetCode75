# test/test_problem1768.py

import sys
import os

# Add the main directory (project_root) to the Python path
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(main_dir)

from problem1768 import Solution

def test_case_1():
    solution = Solution()
    word1 = "abc"
    word2 = "pqr"
    result = solution.mergeAlternately(word1, word2)
    assert result == "apbqcr"


def test_case_2():
    solution = Solution()
    word1 = "ab"
    word2 = "pqrs"
    result = solution.mergeAlternately(word1, word2)
    assert result == "apbqrs"


def test_case_3():
    solution = Solution()
    word1 = "abcd"
    word2 = "pq"
    result = solution.mergeAlternately(word1, word2)
    assert result == "apbqcd"
