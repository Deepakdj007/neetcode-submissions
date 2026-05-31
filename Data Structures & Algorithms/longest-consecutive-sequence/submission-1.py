class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in numsSet:
            length = 1
            if num-1 in numsSet:
                continue

            while num+length in numsSet :
                    length+=1
                    
            longest = max(longest,length)
        return longest
