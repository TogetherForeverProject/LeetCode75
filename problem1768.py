from timeit import timeit
from memory_profiler import memory_usage


# Question (Merge Strings Alternately)
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize an empty string to store the merged result
        merged = ""

        # Initialize two pointers, i and j, to iterate through word1 and word2, respectively
        i, j = 0, 0

        # Merge the strings alternately, taking one character from each string in sequence
        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]
            i += 1
            j += 1

        # If there are remaining characters in word1, append them to the merged result
        if i < len(word1):
            merged += word1[i:]

        # If there are remaining characters in word2, append them to the merged result
        if j < len(word2):
            merged += word2[j:]

        # Return the final merged string
        return merged


def main():
    solution = Solution()
    word1 = "hello"
    word2 = "world"
    result = solution.mergeAlternately(word1, word2)
    return result


def memory_usage_wrapper() -> None:
    main()

if __name__ == "__main__":
    # Measure the runtime and get memory Usage
    result = main()
    runtime_ms = timeit(lambda: main(), number=16000) * 1000  # Repeat 1000 times for better accuracy
    memory_usages_mb = memory_usage((memory_usage_wrapper,), interval=0.1)
    average_memory_usage_mb = sum(memory_usages_mb) / len(memory_usages_mb)

    print("Output:", result)
    print(f"Runtime: {runtime_ms:.5f} milliseconds")
    print(f"Average Memory Usage: {average_memory_usage_mb:.2f} MB")
