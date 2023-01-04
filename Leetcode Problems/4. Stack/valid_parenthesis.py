"""
Topic: Stack
Leetcode: 20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""

    
class Solution:
    
    def is_empty(self, st):
        return len(st) == 0

    def isValid(self, s: str) -> bool:
   
        st = []
        bracket_arr = ["(", "{", "["]
        for c in s:
            if c in bracket_arr:
                st.append(c)
        
            elif c == ')' and not(self.is_empty(st)) and st[-1] == '(':
                st.pop()
            elif c == '}' and not(self.is_empty(st)) and st[-1] == '{':
                st.pop()
            elif c == ']' and not(self.is_empty(st)) and st[-1] == '[':
                st.pop()
            else:
                return False
        return self.is_empty(st)