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
    # Explanation: the merged string will be merged as so:
    # word1:  a   b   c
    # word2:    p   q   r
    # merged: a p b q c r
    assert result == "apbqcr"


def test_case_2():
    solution = Solution()
    word1 = "ab"
    word2 = "pqrs"
    result = solution.mergeAlternately(word1, word2)
    # Expalanation: Notice that as word2 is longer, "rs" is appended to the end.
    # word1:  a   b
    # word2:    p   q  r  s
    # merged: a p b q  r  s
    assert result == "apbqrs"


def test_case_3():
    solution = Solution()
    word1 = "abcd"
    word2 = "pq"
    result = solution.mergeAlternately(word1, word2)
    # Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    # word1:  a   b   c  d
    # word2:    p   q
    # merged: a p b q c  d
    assert result == "apbqcd"
