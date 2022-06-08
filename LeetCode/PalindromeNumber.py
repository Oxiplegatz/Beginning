class Solution:
    def is_palindrome(self, x: int) -> bool:

        if x < 0:
            return False

        elif x == 0:
            return True

        numbers = []

        while x:
            digit = x % 10
            numbers.append(digit)
            x //= 10
        while numbers[0] == numbers[-1]:
            numbers = numbers[1:-1]
            if len(numbers) <= 1:
                return True
        return False


print(Solution().is_palindrome(0))
