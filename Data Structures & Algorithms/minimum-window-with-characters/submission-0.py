from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ""

        need = Counter(t)
        window = {}

        need_count = len(need)
        have = 0

        res = [-1,-1]
        res_length = math.inf

        l = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)

            if s[r] in need and need[s[r]] == window[s[r]]:
                have+=1

            while need_count == have:
                if (r-l+1)<res_length:
                    res_length = r-l+1
                    res = [l,r]
                    
                window[s[l]]-=1

                if s[l] in need and window[s[l]]<need[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if res_length!=math.inf else ""

        
        
