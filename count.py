from collections import Counter
import pandas as pd
import read

df = read.load_data()

def head_to_list():
    head_string = ''
    headlines = df['headline'].dropna()
    for i, head in enumerate(headlines):
        head_string += head.lower()
        if i != headlines.shape[0] - 1:
            head_string += ' '
    return head_string.split(' ')

def word_counter(num_words):
    words = head_to_list()
    return Counter(words).most_common(num_words)

if __name__ == '__main__':
    print(word_counter(100))