class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        count = 0
        for num in numsSet:
            counter = 1
            if num-1 in numsSet:
                continue
            checker = num
            while(True):
                if checker+1 in numsSet:
                    counter+=1
                    checker+=1
                else:
                    break
            count = max(count,counter)
        return count
