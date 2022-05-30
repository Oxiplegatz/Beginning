class Solution:
    def remove_element(self, nums, val):

        while val in nums:
            nums.remove(val)
        return nums

        # if val not in nums:
        #     return len(nums)
        # counter = nums.count(val)
        # while val in nums:
        #     for i in range(len(nums)):
        #         print(nums)
        #         if nums[i] == val:
        #             nums.pop(nums.index(nums[i]))
        #             nums.append(None)
        #         if nums[i] is None:
        #             break
        # nums = nums[:-counter]
        # return len(nums)


trying = Solution().remove_element([2, 5, 6, 6, 7, 5, 5, 5, 5, 5, 0, 2, 1, 2, 3], 5)

print(trying)
