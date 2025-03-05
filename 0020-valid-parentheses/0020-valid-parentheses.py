class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      checks = {")":"(","]":"[","}":"{"}
      for c in s:
        if c in checks:
            if stack and stack[-1] == checks[c]:
                stack.pop()
            else:
                return False

        else:
            stack.append(c)
      return True if not stack else False