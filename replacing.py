

from replaces import REPLACES


def split_text(text):
    words = text.split()
    return words


def replace_word(word):
    is_title = word[0].isupper()
    word = word.lower()
    for key, value in REPLACES.items():
        if key in word:
            result_word = word.replace(key, value)
            return result_word.title() if is_title else result_word
    return word



if __name__ == '__main__':
    text = """Мама прочти сообщение. Помоги сделать работу. 
    Как классно писать бота в воскресенье вечером"""
    tokens = split_text(text)
    print(tokens)
    replaced_word = [replace_word(word) for word in tokens if word is not None]
    result = ' '.join(replaced_word)
    print(result)
