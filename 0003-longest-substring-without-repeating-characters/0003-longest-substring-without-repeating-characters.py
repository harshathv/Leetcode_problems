class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars=set()
        start=0
        max_length=0
        for end in range(len(s)):
            while s[end] in unique_chars:
                unique_chars.remove(s[start])
                start+=1
            unique_chars.add(s[end])
            max_length=max(max_length,end-start+1)
        return max_length
