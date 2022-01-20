class Trie:

    def __init__(self):
        self.children = [None for i in range(26)]
        self.end_of_word = False
        self.word = ''

    def insert(self, str, i=0, reverse=False):
        if len(str) == i:
            if reverse:
                self.word = str[::-1]
            else:
                self.word = str
            self.end_of_word = True
            return
        c = ord(str[i]) - ord('a')
        if self.children[c] is None:
            trie = Trie()
            self.children[c] = trie
        else:
            trie = self.children[c]

        trie.insert(str, i+1, reverse)

    def search(self, str, i=0):
        if len(str) == i:
            if self.end_of_word:
                words = [self.word]
            else:
                words = []
            for child in self.children:
                if child is not None:
                    _words = child._get_words()
                    for word in _words:
                        words.append(word)

            return words
        c = ord(str[i]) - ord('a')
        if 0 <= c < 26 and self.children[c] is not None:
            return self.children[c].search(str, i+1)
        else:
            return []

    def _get_words(self):
        if self.end_of_word:
            words = [self.word]
        else:
            words = []
        for child in self.children:
            if child is not None:
                _words = child._get_words()
                for word in _words:
                    words.append(word)

        return words


def make_from_file(file, reverse=False):
    root = Trie()
    file = open(file)
    words = file.read().splitlines()
    for word in words:
        if reverse:
            root.insert(word[::-1], i=0, reverse=reverse)
        else:
            root.insert(word, reverse)
    del words
    file.close()
    del file

    return root


