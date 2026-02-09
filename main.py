import re

from SimpleTokenizerV1 import SimpleTokenizerV1


def __main__():

    with open("the_verdict.txt", "r", encoding="utf-8") as f:
      raw_text = f.read()

    preprocessed = re.split(r'([,.?_!"()\']|--|\s)', raw_text)
    #stipe: 공백제거
    preprocessed = [item.strip() for item in preprocessed if item.strip()]

    all_words = sorted(set(preprocessed))

    vocab={token:integer for integer, token in enumerate(all_words)}

    tokenizer = SimpleTokenizerV1(vocab)

    text = """
    It's the last he painted, you know, Mrs. Gisburn said with pardonable pride
    """
    ids = tokenizer.encode(text)
    print(ids)


__main__()