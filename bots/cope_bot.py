import tweepy
import random

def main(tweet_id):
    api = get_authorization()
    tweet = get_tweet(tweet_id, api)
    longest_word = get_longest_word(tweet)
    new_tweet = get_new_tweet(longest_word)
    api.update_status(new_tweet, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)


def get_authorization():
    auth = tweepy.OAuthHandler(COPE_BOT_CONSUMER_KEY, COPE_BOT_CONSUMER_SECRET_KEY)
    auth.set_access_token(COPE_BOT_ACCESS_TOKEN, COPE_BOT_SECRET_ACCESS_TOKEN)
    api = tweepy.API(auth)
    return api


def get_tweet(tweet_id, api):
    return api.lookup_statuses(tweet_id)[0]


def get_longest_word(tweet):
    words = tweet.text.split()
    for word in words:
        if '—' in word:
            words.remove(word)
            split_words = word.split('—')
            for split_word in split_words:
                words.append(split_word)
        if ',' in word:
            words.remove(word)
            words.append(word.rstrip(','))
        if ':' in word:
            words.remove(word)
            words.append(word.rstrip(':'))
        if '.' in word:
            words.remove(word)
            words.append(word.rstrip('.'))
    length = 0
    longest_word = ''
    for word in words:
        if 'https://t.co/' not in word:
            if len(word) > length:
                length = len(word)
                longest_word = word
    return longest_word


def get_new_tweet(longest_word):
    template_tweets = [
        f'I don\'t think "{longest_word}" means what you think it means. Maybe you should put down your phone and pick '
        f'up a dictionary.',
        f'Using big words like "{longest_word}" incorrectly on the internet doesn\'t make you look smart. Try '
        f'developing your mind instead of your social media presence. Just a thought.'
    ]
    new_tweet = random.choice(template_tweets)
    return new_tweet


main()
