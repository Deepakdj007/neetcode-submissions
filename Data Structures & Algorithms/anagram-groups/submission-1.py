class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencySet = defaultdict(list)

        for string in strs:
            charCount = [0] * 26

            for char in string:
                charCount[ord(char)-ord('a')]+=1

            frequencySet[tuple(charCount)].append(string)

        return list(frequencySet.values())
          