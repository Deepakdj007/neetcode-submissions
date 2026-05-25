class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i, num in enumerate(nums):
            difference = target-num
            if difference in differences:
                return [differences[difference], i]
            differences[num] = i