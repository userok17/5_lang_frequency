import os
from collections import Counter

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data_file:
        return data_file.read()


def get_most_frequent_words(text):
    words = text.split()
    counts =  Counter(words)
    return counts.most_common(10)


if __name__ == '__main__':
    text = load_data('text.txt')
    count_words = get_most_frequent_words(text)
    for key, value in count_words:
        print('{:10} {}'.format(key, value))
