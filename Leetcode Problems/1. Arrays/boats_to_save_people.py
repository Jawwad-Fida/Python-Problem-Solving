"""
Topic: Arrays or Lists
Leetcode: 881. Boats to Save People. Medium.
https://leetcode.com/problems/boats-to-save-people/
"""

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1. Sort the people's weights in asc order
        people.sort()
        
        # 2. Set 2 pointers for the beginning(lightest) and end of the list(heaviest). Also a counter for the number of boats.
        left = 0
        right = len(people) - 1
        boats_num = 0
        
        # 3. Loop through the list until the left pointer is greater than the right pointer
        while(left <= right):
            
            # 4. If the sum of the 2 people is less than the limit, then we can fit 2 people in 1 boat. Increment the left pointer and decrement the right pointer.
            if people[left] + people[right] <= limit:
                boats_num += 1
                left += 1
                right -= 1
            else:
                 # 5. If the sum of the 2 people is greater than the limit, then we can only fit 1 person in 1 boat (heaviest person). Decrement the right pointer.
                boats_num +=1
                right -=1    
                
            # 6. If there is a single person left, we can fit them in a boat.
            if left == right:
                boats_num += 1
                break
        
        return boats_num
        
        
        
s = Solution()
boats = s.numRescueBoats([3,2,2,1],3)
print(boats)  
