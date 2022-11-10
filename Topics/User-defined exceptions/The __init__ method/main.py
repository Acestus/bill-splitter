def check_word(word):
    if '0' in word:
        raise NotWordError(word)
    else:
        print(word)

def error_handling(word):
    try:
        check_word(word)
    except NotWordError as err:
        print(err)