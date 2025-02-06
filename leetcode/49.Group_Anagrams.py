class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)
        for i in strs:
            sorted_word = ''.join(sorted(i))
            anagram_map[sorted_word].append(i)
        return list( anagram_map.values())
            


        
