class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #loop through nums1 - i
        #inner loop with nums2 - j
        #   until reach nums1[i]
        #   after that find the next largest number
        #repeat
        ans = []
        for i in range(len(nums1)):
            found = False
            append = -1
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    found = True
                if nums2[j] > nums1[i] and found:
                    append = nums2[j]
                    break
            ans.append(append)
        return ans

        
        # next_greater = defaultdict(lambda: -1)   # default result is -1
        # waiting_stack = []                       # stack of numbers waiting for next greater
        
        # for current in nums2:
        #     # Resolve next-greater for any smaller numbers on the stack
        #     while waiting_stack and waiting_stack[-1] < current:
        #         smaller_num = waiting_stack.pop()
        #         next_greater[smaller_num] = current
            
        #     # Current element waits for its next greater value
        #     waiting_stack.append(current)
        
        # # Build answer for nums1 in the same order
        # return [next_greater[num] for num in nums1]
