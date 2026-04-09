class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_map = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in anagrams_map:
                anagrams_map[sorted_word] = []
            anagrams_map[sorted_word].append(word)
        return list(anagrams_map.values())
        