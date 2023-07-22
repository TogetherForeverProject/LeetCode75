from typing import List
from timeit import timeit
from memory_profiler import memory_usage


# Question (Kids With the Greatest Number of Candies)
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid
# has, and an integer extraCandies, denoting the number of extra candies that you have.
#

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies among all kids
        max_candies = max(candies)

        # Initialize an empty list to store the result of comparison
        result = []

        # Iterate through each kid's candies
        for candy in candies:
            # Check if the current kid can have the most candies by adding extraCandies
            # If the result is greater than or equal to the max_candies, the kid can have the most candies.
            # Append the result to the result list.
            result.append(candy + extraCandies >= max_candies)

        # Return the list containing True/False for each kid based on whether they can have the most candies.
        return result


def main():
    solution = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    result = solution.kidsWithCandies(candies, extraCandies)
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
