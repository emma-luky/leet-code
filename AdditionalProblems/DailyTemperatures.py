class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # answer = []
        # n = len(temperatures)
        # for i in range(n - 1):
        #     days = 1
        #     index = i + 1
        #     while(index < n):
        #         if temperatures[index] > temperatures[i]:
        #             answer.append(days)
        #             break
        #         elif index == n - 1:
        #             answer.append(0)
        #             break
        #         else:
        #             days += 1
        #             index += 1
        # answer.append(0)
        # return answer
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer
