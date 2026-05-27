class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter = {}
        for num in nums:
            freqCounter[num] = freqCounter.get(num,0)+1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqCounter.items():
            buckets[freq].append(num)
        
        result = []

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result)==k:
                    return result

