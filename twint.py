import twint as tw
from contracts import contract
import pandas as pd


@contract()
def twitter(user, word, start_date, finish_date):
    """
    This function for tweet's parsing.
    :param user: Username for searching
    :type user: str
    :param word: Main word for searching
    :type word: str
    :param start_date: Start date of period
    :type start_date: str
    :param finish_date: Finish date of period
    :type finish_date: str
    :return: file csv
    """
    config = tw.Config()
    config.Username = user
    config.Search = word
    config.Since = start_date
    config.Until = finish_date
    config.Store_csv = True
    config.Output = 'tweets.csv'
    tw.run.Search(config)


@contract()
def sub_twitter(users_list, words_list):
    """Function for start of parsing.
    :param users_list: List of users names
    :type users_list: list(str)
    :param words_list: List of main words
    :type words_list: list(str)
    """
    start_date = str(input())
    finish_date = str(input())
    for user in users_list:
        for word in words_list:
            twitter(user, word, start_date, finish_date)


@contract()
def pandas_corrector(file_name):
    """
    Function for analysis of tweets and rewriting a new file.
    :param file_name: Str of file name
    :type file_name: str
    """
    df = pd.read_csv(file_name)
    for param in ['timezone', 'id', 'conversation_id',
              'created_at', 'place', 'mentions',
              'urls', 'photos', 'hashtags',
              'cashtags', 'link', 'retweet',
              'quote_url', 'video', 'user_rt_id',
              'near', 'geo']:
        df.drop([param], axis=1, inplace=True)
    df.to_csv('tweets_new.csv')
    '''tweets = pd.read_csv('tweets_new.csv', parse_dates={'datetime': [1, 2]})
    tweets['datetime'] = tweets['datetime'].dt.floor('min')
    tweets.drop(['Unnamed: 0'], axis=1, inplace=True)
    tweets = tweets.set_index('datetime', append=True).sort_index(level=1)
    tweets.to_csv('new.csv')'''


def main():
    users_list = ['BBCWorld', 'cnnbrk', 'theeconomist',
                  'business', 'reuters', 'washingtonpost',
                  'wsj', 'marketwatch', 'ft']
    words_list = ['oil', 'Iran']
    sub_twitter(users_list, words_list)
    pandas_corrector('name_of_line')


if __name__ == '__main__':
    main()
