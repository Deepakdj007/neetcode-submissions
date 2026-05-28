class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for string in strs:
            ans.append(str(len(string))+"#"+string)
        print(''.join(ans))
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        i,n = 0, len(s)
        while i<n:
            j = i
            while s[j]!='#':
                j+=1
            size = int(s[i:j])
            j+=1
            ans.append(s[j:j+size])
            i=j+size
        return ans