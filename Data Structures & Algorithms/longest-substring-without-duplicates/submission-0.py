class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        start=0
        end=0

        while end<len(s) and start<len(s):
            end = start+1
            sub_string = set(s[start])
            while end<len(s) and s[end] not in sub_string:
                sub_string.add(s[end])
                end+=1
            max_length = max(max_length,end-start)
            if end == len(s)-1:
                break
            start+=1
        return max_length
        

        
