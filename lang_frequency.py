import os
from collections import Counter
from argparse import ArgumentParser
import re

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data_file:
        return data_file.read()


def get_most_frequent_words(text, rows):
    regex_non_words = re.compile(r'[\d\W]+')
    list_words = regex_non_words.split(text)
    list_words = map(lambda word: word.lower(), list_words) # Все слова в нижний регистр
    counts =  Counter(list_words)
    return counts.most_common(rows)


def main():
    parser = ArgumentParser(description='Чистота слов')
    parser.add_argument('-f', '--filepath', required=True, help='Укажите путь до файла',dest='filepath')
    args = parser.parse_args()

    text = load_data(args.filepath)
    if not text:
        print('Неверно указан путь до текстового файла')
        sys.exit(1)

    rows = 10

    description = '{} самых популярных слов в этом файле:'.format(rows)
    print(description)
    
    count_words = get_most_frequent_words(text, rows)

    for key, value in count_words:
        print('{:10} {}'.format(key, value))

if __name__ == '__main__':
    main()
