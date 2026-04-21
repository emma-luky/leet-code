class Solution:
    def canWinNim(self, n: int) -> bool:
            # def turn(myTurn, stones):
            #     results = []
            #     for take in range(1, 4):
            #         if take > stones:
            #             continue
            #         currStones = stones - take
            #         if currStones == 0:
            #             results.append(myTurn)
            #         else:
            #             results.append(turn(not myTurn, currStones))
            #     return any(results) if myTurn else all(results)
            # return turn(True, n)
            if n % 4 == 0:
                return False
            else:
                return True
