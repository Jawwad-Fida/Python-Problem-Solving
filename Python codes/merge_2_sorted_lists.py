"""
Topic: Linked Lists
Leetcode: 21. Merge Two Sorted Lists.
https://leetcode.com/problems/merge-two-sorted-lists/
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # NOTE: utlize the fact that the lists are sorted
        
        # 1) Create head node of new list
        head = ListNode(0) # an initial value of head node (dummy node)
        itr = head
        
        # change the name of the head pointers in both lists (my own convenience) 
        l1 = list1
        l2 = list2
        
        # 2) Loop over the 2 linked lists in parallel (exit when one list reaches None)
        while(l1 and l2):
            # 3) Compare between the values of 2 nodes in the 2 lists
            # 4) Append the smaller node to the new list
            if l1.val < l2.val:
                itr.next = l1 # append the node to the new list 
                l1 = l1.next # 5) move the pointer to the next node in the list (iteration)
            else:
                itr.next = l2
                l2 = l2.next
                
            # 5) move the pointer itr to the next node in the new list (iteration)
            itr = itr.next
            
        # 6) Loop over the remaining list and append it to the new list - Add the remaining of the valid list (list that still contains elements and not reached None yet) 
        while(l1):
            itr.next = l1
            l1 = l1.next
            itr = itr.next
            
        while(l2):
            itr.next = l2
            l2 = l2.next
            itr = itr.next
        
        # the actual start of our list is not the head node (0), but the next node after the head node (head.next)
        return head.next
            
        
def main():
    list1 = [1,2,4] 
    list2 = [1,3,4]
    s = Solution()
    merged_list = s.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4])
    
    print(merged_list) # just verify
    
    # print the entire connected list
    while(merged_list):
        print(merged_list.val) # print value of current node
        merged_list = merged_list.next # move to the next node
        
    # T(n) = O(n) # loop over the linked list
    # S(n) = O(1) # no addition ds created    
        
        
        
if __name__ == "__main__":
    main()




