class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        combo = []
        def backtrack(opened, closed):
            # only add open paranthesis if open < n
            # only add closed paranthesis if closed < open
            if closed == n and opened == n:
                ans.append("".join(combo))
                return
            
            if opened < n:
                combo.append("(")
                backtrack(opened + 1, closed)
                combo.pop()
            
            if closed < opened:
                combo.append(")")
                backtrack(opened, closed + 1)
                combo.pop()

        backtrack(0, 0)
        return ans
