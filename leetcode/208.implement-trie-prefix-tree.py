#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        
#time complexity: O(N) where N is the length of the word





# My Approach:

class Trie(object):

    def __init__(self):
        self.dictionary = []
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word not in self.dictionary:
            self.dictionary.append(word)

        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.dictionary:
            return True
        return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        for word in self.dictionary:
            if word.startswith(prefix): 
                return True
        return False
    
    
#time complexity: O(N) where N is the length of the word
# tme complexity of startswith is O(n * m)checking each word in the dictionary

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

