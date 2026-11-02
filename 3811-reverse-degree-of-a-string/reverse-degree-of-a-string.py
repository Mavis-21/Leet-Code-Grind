class Solution:
    def reverseDegree(self, s: str) -> int:
        a = []
        l = {}
        p = 0
        k = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        
        for i in range(1, 27):
            a.append(i)
            
        
        a.reverse()
        
        
        for i in range(len(k)):
            l[k[i]] = a[i]
            
        
        for o in range(len(s)):
            u = l[s[o]] * (o + 1)
            p = p + u
            
        return p