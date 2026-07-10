class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    # REWRITE ME WITH TRIENODE !!!!!!!!!

    from collections import defaultdict

    def __init__(self):
        self.tree = ({}, False)
        
    def insert(self, word: str):
        trie = self.tree
        for (i, ch) in enumerate(word):
            if len(word) - 1 == i:
                last = True
            else:
                last = False

            if not trie[0].get(ch):
                new = ({}, last)
                trie[0][ch] = new
                trie = new
            else:
                if len(word) - 1 == i:
                    (tr, exists) = trie[0].get(ch)
                    trie[0][ch] = (tr, True)
                trie = trie[0][ch]

    def search(self, word: str) -> bool:
        trie = self.tree
        last_exists = False
        for ch in word:
            if trie[0].get(ch) is None:
                return False
            else:
                tr = trie[0].get(ch)
                last_exists = tr[1]
                trie = tr
        return last_exists

    def startsWith(self, prefix: str) -> bool:
        trie = self.tree
        for ch in prefix:
            if trie[0].get(ch) is None:
                return False
            else:
                trie = trie[0].get(ch)
        return True
        
        