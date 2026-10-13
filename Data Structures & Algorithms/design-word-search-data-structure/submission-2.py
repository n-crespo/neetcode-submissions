class TrieNode:
    def __init__(self):
        self.children = {} # "letter": node
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        # prefixes can be checked very efficiently
        # prefix tree == trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True
        

    def search(self, word: str) -> bool:
        # this is the only difference between this and a trie
        # we basically have a recursive call in here...
        def dfs(j, root):
            current = root

            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]
            return current.endOfWord

        return dfs(0, self.root)