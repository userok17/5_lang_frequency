import os
from collections import Counter
from optparse import OptionParser

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data_file:
        return data_file.read()


def get_most_frequent_words(text):
    words = text.split()
    counts =  Counter(words)
    count_rows = 10
    return counts.most_common(count_rows)

def print_most_frequent_words(counts):
    print('Десять самых популярных слов в этом файле:')
    for key, value in counts:
        print('{:10} {}'.format(key, value))

def parser_command():
    parser = OptionParser()
    parser.add_option('-f', '--filepath', help='Укажите путь до файла',dest='filepath')
    opts, args = parser.parse_args()
    if opts.filepath:
        text = load_data(opts.filepath)
        if text:
            count_words = get_most_frequent_words(text)
            print_most_frequent_words(count_words)
    

if __name__ == '__main__':
    parser_command()
