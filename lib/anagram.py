# your code goes here!
class  Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        anagram = []
        for w in words:
            if sorted(self.word) == sorted(w.lower()):
                anagram.append(w)
        return anagram


