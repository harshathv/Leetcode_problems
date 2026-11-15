class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        if len(s)!=len(t):
            return False
        for c in s:
            h[c]=h.get(c,0)+1
        for c in t:
            if c not in h or h[c]==0:
                return False
            h[c]-=1
        return True