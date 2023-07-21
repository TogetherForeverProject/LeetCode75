from memory_profiler import memory_usage
from timeit import timeit


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and s_list[i] not in vowels:
                i += 1
            while i < j and s_list[j] not in vowels:
                j -= 1

            if i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1

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
