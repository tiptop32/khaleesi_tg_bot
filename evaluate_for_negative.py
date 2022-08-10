

from affinn_ru import AFFINN


def split_text(msg_text):
    return msg_text.split()


def evaluate_word(word):
    _word = word.lower()
    for key, value in AFFINN.items():
        if key in _word:
            return int(float(value))
    return 0


def evaluate_text(msg_text):
    tokens = split_text(msg_text)
    text_rate = 0
    for _word in tokens:
        word_rate = evaluate_word(_word)
        text_rate += word_rate
    return text_rate


if __name__ == '__main__':
    text = """ Вот пример обычного предложение. А ты как хотел бля. Само все что б работало. Или как эх
    Вот пример обычного предложение. А ты как хотел"""
    print(evaluate_text(text))
