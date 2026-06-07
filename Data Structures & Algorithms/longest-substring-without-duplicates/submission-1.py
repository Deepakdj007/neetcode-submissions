class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        start=0
        max_len=0

        for end in range(0, len(s)):
            while s[end] in window:
                window.remove(s[start])
                start+=1

            window.add(s[end])
            max_len = max(max_len,end-start+1)

        return max_len
        

        
