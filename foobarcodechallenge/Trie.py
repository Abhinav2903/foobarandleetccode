class Trie_Node:
    def __init__(self):
        self.endofword=False
        self.children={}
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Trie_Node()
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        nroot=self.root
        for i in word:
            
            # index=ord(i)-ord('a')
            if i not in  nroot.children:
                nroot.children[i]=self.root
            nroot=nroot.children[i]  
        
        nroot.endofword=True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        nroot=self.root
        for j in word:
            
            # index=ord(j)-ord('a')
            if j not in nroot.children:
                return False
            nroot=nroot.children[j]    
        return nroot.endofword


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        nroot=self.root
        for i in prefix:
            # index=ord(i)-ord('a')
            if not nroot.children:
                return False
            nroot=nroot.children[i]
        return True        

obj=Trie()
obj.insert("apqle")
print(obj.search("ap"))
