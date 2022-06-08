class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:

        for number_one in nums:
            for number_two in nums[nums.index(number_one) + 1:]:
                if number_one + number_two == target:
                    return [nums.index(number_one), nums.index(number_two, nums.index(number_one) + 1)]
            nums.append(number_one)


check1 = Solution().two_sum([7, 0, 2, 8, 5, 7, 6, 84, 11, 26, 87], 10)
check2 = Solution().two_sum([2, 3, 0, 5], 5)
check3 = Solution().two_sum([3, 3], 6)

print(check1)
print(check2)
print(check3)
