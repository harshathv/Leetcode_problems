class Solution:
    def Pal(self,string,left,right):
        while left>0 and right<len(string)-1 and string[left-1]==string[right+1]:
            left-=1
            right+=1
        return left,right,right-left+1
    def longestPalindrome(self, s: str) -> str:
        max_len,l,r=0,0,0
        for ind in  range(len(s)-1):
            l1,r1,max_len1=self.Pal(s,ind,ind)
            if max_len1>max_len:
                max_len=max_len1
                l,r=l1,r1
            if s[ind]==s[ind+1]:
                l2,r2,max_len2=self.Pal(s,ind,ind+1)
                if max_len2>max_len:
                    max_len=max_len2
                    l,r=l2,r2 
        return s[l:r+1]       