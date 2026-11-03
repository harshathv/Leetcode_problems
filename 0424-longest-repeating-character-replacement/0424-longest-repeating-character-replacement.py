class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a={}
        maxlength=0
        maxfrequency=0
        l=0
        for r in range(len(s)):
            a[s[r]]=a.get(s[r],0)+1
            maxfrequency=max(maxfrequency,a[s[r]])
            while (r-l+1)-maxfrequency>k:
                a[s[l]]-=1
                l+=1
            maxlength=max(maxlength,r-l+1)
        return maxlength
        