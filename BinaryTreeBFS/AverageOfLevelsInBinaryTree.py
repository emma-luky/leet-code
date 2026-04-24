# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # sums = []
        # counts = []
        # curr = root
        # def dfs(node, lvl):
        #     if node:
        #         if lvl == len(sums):
        #             sums.append(node.val)
        #             counts.append(1)
        #         else:
        #             sums[lvl] += node.val
        #             counts[lvl] += 1
        #         bfs(node.left, lvl + 1)
        #         bfs(node.right, lvl + 1)
        # bfs(root, 0)
        # avgs = []
        # for i in range(len(sums)):
        #     avgs.append(sums[i]/counts[i])
        # return avgs
        queue = deque([root])
        avgs = []
        while queue:
            size = len(queue)
            sum = 0
            for i in range(size):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avgs.append(sum/size)
        return avgs
