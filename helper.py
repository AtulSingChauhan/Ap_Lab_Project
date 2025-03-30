import pandas as pd

def get_message_count(df):
    return df['user'].value_counts()

def most_common_words(df, n=10):
    words = ' '.join(df['message']).split()
    word_counts = pd.Series(words).value_counts()
    return word_counts.head(n)


