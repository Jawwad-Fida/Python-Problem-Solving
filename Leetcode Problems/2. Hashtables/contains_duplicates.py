"""
Topic: Hash Tables
Leetcode: 217. Contains Duplicate. 
https://leetcode.com/problems/contains-duplicate/
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for num in nums:
            if num in m.keys():
                return True
            else:
                m[num] = 1 # Store the number in the dictionary as key. Value does not matter
        return False
                

s = Solution()
val = s.containsDuplicate([1,2,3,1])
print(val)