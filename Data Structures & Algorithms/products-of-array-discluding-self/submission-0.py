class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        ans = [1]*len(nums)

        for i, num in enumerate(nums):
            ans[i] = prefix
            prefix*=num

        sufix = 1

        for i in range(len(nums)-1,-1, -1):
            ans[i]*=sufix
            sufix*=nums[i]
        return ans

            