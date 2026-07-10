class TNode:
    def __init__(self, children, is_word_end):
        self.children = children
        self.is_word_end = is_word_end

# TODO: REWRITE ME !!!!

class WordDictionary:
    def __init__(self):
        self.tree = TNode({}, False)

    def addWord(self, word: str) -> None:
        trie = self.tree
        for (i, ch) in enumerate(word):
            if len(word) - 1 == i:
                is_word_end = True
            else:
                is_word_end = False
            if trie.children.get(ch) is None:
                trie.children[ch] = TNode({}, is_word_end)
            else:
                tr = trie.children[ch]
                if is_word_end:
                    tr[ch].is_word_end = is_word_end
            trie = trie.children[ch]

    def search(self, word: str) -> bool:
        trie = self.tree
        
        def dfs(word, tree):
            if len(word) == 1:
                if word[0] == ".":
                    for item in tree.children.values():
                        if item.is_word_end:
                            return True
                    return False
                else:
                    if tree.children and tree.children.get(word) is not None:
                        return tree.children.get(word).is_word_end
                    else:
                        return False
            if word[0] == ".":
                if tree is not None:
                    return any([dfs(word[1:], item) for item in tree.children.values()])
                else:
                    return False
            else:
                if tree.children and tree.children.get(word[0]):
                    return dfs(word[1:], tree.children.get(word[0]))
                else:
                    return False

            
        for (i, ch) in enumerate(word):
            if ch == '.':
                return dfs(word[i:], trie)
            elif trie.children.get(ch) is None:
                return False
            else:
                if len(word) - 1 == i:
                    return trie.children[ch].is_word_end
                trie = trie.children[ch]

                