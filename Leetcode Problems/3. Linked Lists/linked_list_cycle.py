"""
Topic: Linked Lists
Leetcode: 141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # list gets converted to 
        
        # Initialize 2 pointers at beginning of list
        hare = head
        turtle = head
        
        # Loop as long as these are valid
        while hare and turtle and hare.next:
            hare = hare.next.next # move 2 steps forward
            turtle = turtle.next # move 1 steps forward
            
            # cycle exists
            if turtle == hare:
                return True
        
        # cycle does not exist - when hare.next becomes null 
        return False


        
def main():
    s = Solution()
    value = s.hasCycle(head = [3,2,0,-4], pos = 1)
    print(value)
        
        
if __name__ == "__main__":
    main()




