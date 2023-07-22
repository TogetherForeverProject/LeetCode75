from timeit import timeit
from typing import List
from memory_profiler import memory_usage


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the input list 'nums'
        n = len(nums)

        # Create a new list 'answer' initialized with all ones, which will store the final result
        answer = [1] * n

        # Calculate the product of all elements to the left of each element
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            answer[i] *= left_product

        # Calculate the product of all elements to the right of each element
        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            answer[i] *= right_product

        # Return the 'answer' list containing the product of all elements except itself for each element
        return answer


def main():
    solution = Solution()
    nums = [-1, -1, 0, -3, 3]
    result = solution.productExceptSelf(nums)
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
    print(f"Runtime: {runtime_ms:.2f} milliseconds")
    print(f"Average Memory Usage: {average_memory_usage_mb:.2f} MB")
