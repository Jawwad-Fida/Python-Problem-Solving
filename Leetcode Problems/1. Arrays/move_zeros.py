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
        j = 0 # set a counter to beginning of list
        for num in nums:
            if num!=0: # if the number is not zero, place it at the counter
                nums[j] = num
                j = j + 1
                
        # loop break, now j is at an index
                
        # loop through the rest of the list and set the rest to zero
        for x in range(j,len(nums)):
            nums[x] = 0
        
        print(nums)

s = Solution()
s.moveZeroes([0,1,0,3,12])