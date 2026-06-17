import re
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(f'[{re.escape(string.punctuation)}]', '', s).replace(" ", '').lower()
        r = ''.join(reversed(s))
        for i in range(len(s)):
            if(s[i] != r[i]):
                return False
        return True