from memory_profiler import memory_usage
from timeit import timeit


class Solution:
    def reverseVowels(self, s: str) -> str:
        # Create a set of vowels for efficient membership test
        vowels = set("aeiouAEIOU")

        # Convert the input string into a list to modify characters
        s_list = list(s)

        # Initialize two pointers, i and j, to traverse the string from both ends
        i, j = 0, len(s) - 1

        # Traverse the string until the two pointers meet
        while i < j:
            # Move the left pointer (i) to the right until it points to a vowel
            while i < j and s_list[i] not in vowels:
                i += 1

            # Move the right pointer (j) to the left until it points to a vowel
            while i < j and s_list[j] not in vowels:
                j -= 1

            # Swap the vowels pointed by the left (i) and right (j) pointers
            if i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1

        # Convert the modified list back to a string and return the result
        return "".join(s_list)


def main():
    solution = Solution()
    s = "leetcode"
    result = solution.reverseVowels(s)
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
