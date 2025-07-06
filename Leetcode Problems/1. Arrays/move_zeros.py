"""
Topic: Arrays or Lists
Leetcode: 283. Move Zeroes. Easy.
https://leetcode.com/problems/move-zeroes/
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        # Move all non-zero elements to the front
        # and count the number of non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count = count + 1
        
        print(nums)
        print(count)
        # Fill the remaining elements with 0
        for i in range(count, len(nums)):
            nums[i] = 0
            
        print(nums)
        

s = Solution()
s.moveZeroes([0,0,1])
# s.moveZeroes([0,1,0,3,12])