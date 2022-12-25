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
        pass


        
def main():
    s = Solution()
    value = s.hasCycle(head = [3,2,0,-4], pos = 1)
    print(value)
        
        
if __name__ == "__main__":
    main()




