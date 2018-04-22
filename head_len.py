import pandas as pd
import read

df = read.load_data()

def most_upvoted_head_len(num_rows):
    df.dropna(inplace=True)
    df['wordcount'] = df['headline'].str.split().map(len)
    return df.groupby('wordcount', as_index=False)['upvotes'].mean().sort_values('upvotes', ascending=False).head(num_rows)

def get_len(headline):
    return len(headline.split(' '))
    
if __name__ == '__main__':
    print(most_upvoted_head_len(10))