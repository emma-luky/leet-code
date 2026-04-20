"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def bfs(node, height):
            if node:
                height += 1
                if not node.children:
                    return height
                return max(bfs(child, height) for child in node.children)
            else:
                return height
        return bfs(root, 0)
