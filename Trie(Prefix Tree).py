class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.chars = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            if c not in p.chars:
                p.chars[c] = TrieNode()
            p = p.chars[c]
        p.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            if c not in p.chars:
                return False
            p = p.chars[c]
        return p.isWord


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            if c not in p.chars:
                return False
            p = p.chars[c]
        return True
