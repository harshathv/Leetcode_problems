class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters=set()
        start=0
        max_length=0
        for end in range(len(s)):
            while s[end] in characters:
                characters.remove(s[start])
                start+=1
            characters.add(s[end])
            max_length=max(max_length,end-start+1)
        return max_length
