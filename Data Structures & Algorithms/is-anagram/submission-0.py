class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        charCount = {};

        for i in s:
            charCount[i] = charCount.get(i, 0) + 1
        
        for i in t:
            if i not in charCount: return False

            charCount[i]-=1

            if charCount[i]<0: return False

        return True