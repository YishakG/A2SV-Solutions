class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for char in path:
            if stack and char == ".." :
                stack.pop()
            elif char != "." and char != "" and char != "..":
                stack.append(char)
        return "/" + "/".join(stack)
        