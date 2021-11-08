import nltk
import string

from replaces import REPLACES


def tokenize_to_words(text):
    return nltk.tokenize.word_tokenize(text, language='russian')


def replace_word(word):
    is_title = word[0].isupper()
    word = word.lower()
    result_word = ''
    for key, value in REPLACES.items():
        if key in word:
            result_word += word.replace(key, value)
            return result_word.title() if is_title else result_word
    return None


if __name__ == '__main__':
    text = """Мама сообщение. Тест. Как классно писать бота в воскресенье вечером"""
    tokens = tokenize_to_words(text)
    print(tokens)
    result = [replace_word(word) for word in tokens if word is not None]
    print(result)
