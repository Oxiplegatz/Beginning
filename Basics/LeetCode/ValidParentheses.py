from collections import deque
# Given a string s containing just the characters '(', ')',
# '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


class Solution:
    def is_valid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        else:
            brackets = {
                '(': ')',
                '[': ']',
                '{': '}'
            }
            stack = deque()
            for char in s:
                if char in brackets.keys():
                    stack.append(char)
                else:
                    if not stack or brackets[stack[-1]] != char:
                        return False
                    else:
                        stack.pop()
            if len(stack) > 0:
                return False
            return True


check1 = Solution().is_valid('((')

print(check1)
