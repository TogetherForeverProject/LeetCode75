from memory_profiler import memory_usage
from timeit import timeit


class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)  # Get the length of the input string
        ans = []  # Initialize a list to store the reversed words
        i = n - 1  # Start from the last character of the input string

        while i >= 0:
            if s[i] == ' ':
                i -= 1  # If the current character is a space, move to the next character
            else:
                temp = [' ']  # Initialize a temporary list with a space character
                j = i
                while j >= 0 and s[j] != ' ':
                    temp.append(s[j])  # Append each character to the temporary list in reverse order
                    j -= 1
                ans.extend(reversed(temp))  # Reverse the characters in the temporary list and append to the final list
                i = j  # Update the index to continue from the next word

        ans.pop()  # Remove the extra space character appended at the end

        return ''.join(ans)  # Return the reversed words as a string


def main():
    solution = Solution()
    s = "the sky is blue"
    result = solution.reverseWords(s)
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
