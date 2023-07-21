from typing import List
from timeit import timeit
from memory_profiler import memory_usage


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Initialize a counter to keep track of how many flowers are planted
        count = 0

        # Initialize a pointer, i, to iterate through the flowerbed
        i = 0

        # Get the length of the flowerbed list for easier access
        length = len(flowerbed)

        # Iterate through the flowerbed to check if flowers can be placed
        while i < length:
            # Check if the current position is empty (0)
            if flowerbed[i] == 0:
                # Check if the previous position is also empty or if we are at the first position
                if i == 0 or (i > 0 and flowerbed[i - 1] == 0):
                    # Check if the next position is also empty or if we are at the last position
                    if i == length - 1 or (i < length - 1 and flowerbed[i + 1] == 0):
                        # Plant a flower at the current position
                        flowerbed[i] = 1

                        # Increment the flower counter
                        count += 1

            # Move to the next position in the flowerbed
            i += 1

        # Check if enough flowers have been planted to meet the requirement (n)
        return count >= n


def main():
    solution = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
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
