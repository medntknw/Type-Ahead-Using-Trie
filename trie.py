class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.words = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def _get_index(self, char: chr):
        return ord(char) - ord('a')

    def _get_character(self, index: int):
        return chr(index + 97)
    
    def insert_key(self, key: str):
        curr = self.root
        for c in key:
            index = self._get_index(c)
            if not curr.children[index]:
                new_node = TrieNode()
                curr.children[index] = new_node
            curr = curr.children[index]
        curr.words +=1

    def search_key(self, key: str): 
        curr = self.root 
        for c in key:
            index = self._get_index(c)
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.words > 0

    def search_prefix(self, prefix: str):
        curr = self.root
        for c in prefix:
            index = self._get_index(c)
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True
            
    def get_suggestions(self, prefix: str):
        """
        get suggestions of words for existing prefix

        Args:
            prefix (str): search prefix which exists in Trie
        """
        curr = self.root
        suggestions = []
        for c in prefix:
            index = self._get_index(c)
            curr = curr.children[index]

        for i, node in enumerate(curr.children):
            if node:
                char = self._get_character(i)
                self.get_all_words(node, prefix + char, suggestions)
        return suggestions

    def get_all_words(self, node: TrieNode, prefix: str, suggestions: list):
        if node and node.words:
            suggestions.append(prefix)
        for i, n in enumerate(node.children):
            if n:
                char = self._get_character(i)
                self.get_all_words(n, prefix + char, suggestions)
        
    def type_ahead(self, key: str):
        suggestions = []
        if not self.search_prefix(key):
            print('There is no entry related to this prefix')
        else:
            suggestions = self.get_suggestions(key)
            print('%s' % ', '.join(suggestions))

if __name__ == '__main__':
    trie = Trie()
    print('Press 1 for getting suggesstions for a word')
    print('Press 2 for saving the word')
    print('Press 3 to exit')
    while True:
        inp = input('Enter the 1 or 2 or 3:\n')
        print(f'You entered {inp}')
        if int(inp) == 1:
            word = input('Enter the word:\n')
            print(trie.type_ahead(word))
        elif int(inp) == 2:
            word = input('Enter the word:\n')
            trie.insert_key(word)
            print(f'Saved {word} into the Trie!')
        elif int(inp) == 3:
            exit(0)
        else:
            print('Unexpected input! Exiting...')
            exit(1)

            