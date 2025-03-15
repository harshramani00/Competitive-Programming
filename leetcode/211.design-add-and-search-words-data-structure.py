#
# @lc app=leetcode id=211 lang=python
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TreeNode(object):
    def __init__(self):
        self.child = {}
        self.status = False

class WordDictionary(object):

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TreeNode()
            node = node.child[char]
        node.status = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]  

                if c == ".":
                    for child_node in curr.child.values():
                        if dfs(i + 1, child_node):  
                            return True
                    return False 
                else:
                    if c not in curr.child:
                        return False
                    curr = curr.child[c]

            return curr.status  

        return dfs(0, self.root)

#time complexity: O(N) where N is the length of the word
#space complexity: O(N) where N is the length of the word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

