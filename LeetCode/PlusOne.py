class Solution:
    def plus_one(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        if digits == [9]:
            return [1, 0]
        return self.plus_one(digits[:-1]) + [0]


check1 = Solution().plus_one([9, 9, 9, 9, 9, 9])

print(check1)
