class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for x in s:
            # print(stk)
            if x in '({[':
                stk.append(x)
            elif x == ')':
                if stk and stk[-1]=='(':
                    stk.pop()
                else:
                    return False
            elif x == '}':
                if stk and stk[-1]=='{':
                    stk.pop()
                else:
                    return False
            elif x == ']':
                # print(stk)
                if stk and stk[-1]=='[':
                    stk.pop()
                else:
                    return False
        return not stk