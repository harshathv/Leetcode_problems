class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_stored={}
        for str in strs:
            sorted_word=" ".join(sorted(str))
            if sorted_word not in strs_stored:
                strs_stored[sorted_word]=[]
            strs_stored[sorted_word].append(str)
        return list(strs_stored.values())
        