def productExceptSelf(self, nums: List[int]) -> List[int]:
    products = [1] * len(nums)
    previous = 1
    for i in range(len(nums)):
        products[i] *= previous
        previous *= nums[i]
    previous = 1
    for i in range(len(nums)-1, -1, -1):
        products[i] *= previous
        previous *=nums[i]
    return products
