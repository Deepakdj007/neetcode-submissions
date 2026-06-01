class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_lowercase_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(cleaned_lowercase_text)-1

        while(left<right):
            if cleaned_lowercase_text[left]!=cleaned_lowercase_text[right]: return False
            left+=1
            right-=1

        return True