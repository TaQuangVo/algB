class TrieNode:
    def __init__(self):
        self.nodes = {} 
        self.end_word = False
    def insert(self, word, i):
        if word[i] not in self.nodes: 
            self.nodes[word[i]] = TrieNode()
        if i == len(word) - 1:
            self.nodes[word[i]].end_word = True
            return
        self.nodes[word[i]].insert(word, i+1)
    def contain(self, word, i):
        if word[i] not in self.nodes:
            return false
        if i == len(word) - 1:
            return self.nodes[word[i]].end_word
        return self.nodes[word[i]].contain(word, i+1)


trie = TrieNode()

trie.insert("hello",0)
trie.insert("hello1",0)
trie.insert("word",0)
trie.insert("hell",0)
print(trie.contain("hel",0))
print(trie.contain("hello",0))
print(trie.contain("word",0))
print(trie.contain("w",0))
