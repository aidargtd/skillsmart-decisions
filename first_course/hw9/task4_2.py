# 128. Longest Consecutive Sequence
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums):
        quantity_nums = 1
        max_ans = 0
        nums = sorted(nums)
        if len(nums) == quantity_nums:
            max_ans = quantity_nums
        else:
            for i in range(len(nums) - 1):
                if nums[i] + 1 <= nums[i + 1]:
                    quantity_nums += 1
                    max_ans = max(max_ans, quantity_nums)
                else:
                    max_ans = max(max_ans, quantity_nums)
                    quantity_nums = 1
        return max_ans



