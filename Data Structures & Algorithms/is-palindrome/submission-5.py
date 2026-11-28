class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        ind: int = 0
        while ind < len(s)-1:
            if not s[ind].isalnum():
                s = s[:ind] + s[ind+1:]
            else:
                try:
                    s = s[:ind] + s[ind].lower() + s[ind+1:]
                except:
                    pass
                ind += 1
        try:
            s = s[:len(s)-1] + s[len(s)-1].lower()
        except:
            pass
        if not s[len(s)-1].isalnum():
            s = s[:len(s)-1]
        print(s)
        
        lo: int = 0
        hi: int = len(s)-1
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True