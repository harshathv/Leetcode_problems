class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        stored={}
        for strr in strs:
            sorted_word="".join(sorted(strr))
            if sorted_word not in stored:
                stored[sorted_word]=[]
            stored[sorted_word].append(strr)
        return list(stored.values())
