class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_size = len(s1)
        s2_size = len(s2)

        if s1_size>s2_size: return False

        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for i in range(s1_size):
            s1_counter[ord(s1[i])-ord('a')] += 1
            s2_counter[ord(s2[i])-ord('a')] += 1
        
        if s1_counter == s2_counter: return True

        left = 0

        for right in range(s1_size,s2_size):
            s2_counter[ord(s2[right])-ord('a')] += 1
            s2_counter[ord(s2[left])-ord('a')] -= 1

            if s1_counter == s2_counter: return True

            left += 1

        return False


            
            