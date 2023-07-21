# test/test_problem238.py

import sys
import os

# Add the main directory (project_root) to the Python path
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(main_dir)

from problem151 import Solution

def test_case_1():
    solution = Solution()
    s = "the sky is blue"
    result = solution.reverseWords(s)
    assert result == "blue is sky the"


def test_case_2():
    solution = Solution()
    s = "  hello world  "
    result = solution.reverseWords(s)
    assert result == "world hello"
    # Your rversed string should not contain leading or trailing spaces

def test_case_3():
    solution = Solution()
    s = "a good   example"
    result = solution.reverseWords(s)
    assert result == "example good a"
    # You need to reduce multiple spaces between two words to a single space in the reversed string
