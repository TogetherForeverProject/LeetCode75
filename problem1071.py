from timeit import timeit
from memory_profiler import memory_usage


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 concatenated with str2 is equal to str2 concatenated with str1
        if str1 + str2 != str2 + str1:
            return ""

        # Define a helper function to find the greatest common divisor using Euclidean algorithm
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        # Calculate the GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))

        # Return the substring of str1 up to the GCD length as the result
        return str1[:gcd_length]


def main():
    solution = Solution()
    str1 = "ABCABC"
    str2 = "ABC"
    result = solution.gcdOfStrings(str1, str2)
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
