# Twitter v1.1 API examples here: https://repl.it/@aneagoie/TweetTweet


import tweepy


# Twitter tokens/keys
api_key = 'blqdTgkMBqtwGwEs2w4n3HidC'
api_key_secret = 'wYvA9txUuPhRrTMnuEHBNb9MUzGO6qRg09v5VmxYbKWfqlCZ5y'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAK0qigEAAAAAqHtsQjR2jfuuxS15y6L%2FYmi6yVM%3DPslbYRoPdFFnK6jFPTK3HoMP7l6VmbH6v8TlARYB0yxHwukmws'
client_id = 'TVRKc0VnRGxMTWJvbHhjb1ROWGI6MTpjaQ'
client_secret = '0q2UkLnNQPgtPBieR2UuENFsn5Q41PQttIoCTecu6DwRLk5KlK'
access_token = '1584658781178187776-aregf8NBuDBFHScKZXQ6eKSCskoHdA'
access_token_secret = 'tWfbeYETh4CJsZEHtGD5pbjr6dPtlRFimvWDxcokcbSjJ'


def authenticate_user():
    client = tweepy.Client(
        bearer_token = bearer_token,
        consumer_key = api_key,
        consumer_secret = api_key_secret,
        access_token = access_token,
        access_token_secret = access_token_secret
    )

    return client


def verify_account(client):
    while True:
        try:
            handle = input("Which user would you like to follow?")
            user_data = client.get_user(username = handle)
            user_id = user_data[0]['id']
            return user_id

        except TypeError as err:
            print('Not a valid user')


def follow_users_following(client, id):
    following = [follower[0] for follower in tweepy.Paginator(client.get_users_following, id)]

    for follower in following[0]:
        try:
            client.follow_user(follower['id'])
            print(f"You are now following {follower}")
        except tweepy.Forbidden as err:
            print(err.response)


if __name__ == '__main__':
    client = authenticate_user()
    user_id = verify_account(client)
    follow_users_following(client, user_id)
