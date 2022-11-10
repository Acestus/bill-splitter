class WordError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_w_letter(word):
    wordLength = len(word)
    for i in range(wordLength):
        if word[i] == 'w':
            raise WordError('Word contains w')
    return word
