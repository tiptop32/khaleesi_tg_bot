

from replaces import REPLACES


def split_text(msg_text):
    words = msg_text.split()
    return words


def replace_word(word):
    is_title = word[0].isupper()
    _word = word.lower()
    for key, value in REPLACES.items():
        if key in _word:
            result_word = _word.replace(key, value)
            return result_word.title() if is_title else result_word
    return word


def replace_text(msg_text):
    tokens = split_text(msg_text)
    print(tokens)
    replaced_word = [replace_word(word) for word in tokens if word is not None]
    return ' '.join(replaced_word)



if __name__ == '__main__':
    text = """Ну просто пизда хуйня там ещё как было - давали задачи на распределение, все «сложные» в понимании 
    ТЗ отдавали более опытным тестировщикам, потому что там реально надо было «выбивать» требования )))"""
    print(replace_text(text))
