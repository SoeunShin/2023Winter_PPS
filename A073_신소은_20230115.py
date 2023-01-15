# LeetCode
# 412. Fizz Buzz

"""
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [num for num in range(1, n+1)]

        for i in range(len(answer)):
            if answer[i] % 3 == 0 and answer[i] % 5 == 0:
                answer[i] = "FizzBuzz"
            elif answer[i] % 3 == 0:
                answer[i] = "Fizz"
            elif answer[i] % 5 == 0:
                answer[i] = "Buzz"
        answer = list(map(str, answer))

        return answer
