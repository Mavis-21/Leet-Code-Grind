class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=s.lower()
        y=''
    
        for i in b:
            if i.isalnum():
                y=y+i

                
            

        if y==y[::-1]:
            return True
        else:
            return False
        