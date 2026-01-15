def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    total = 0
    curr = 0
    startIndex = 0

    for i in range(len(gas)):
        net = gas[i] - cost[i]
        total += net
        curr += net

        if (curr < 0):
            startIndex = i + 1
            curr = 0

    if total >= 0:
        return startIndex
    else:
        return -1
