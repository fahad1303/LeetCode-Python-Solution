class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        item_list= {')':'(','}':'{',']':'['}
        for x in s:
            if x in item_list:
                if stack and item_list[x]== stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False 