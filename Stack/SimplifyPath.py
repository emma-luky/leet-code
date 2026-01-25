class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        stack = []
        for part in split_path:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        print(stack)
        return "/" + "/".join(stack)
