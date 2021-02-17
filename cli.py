import click
from tweet import tweet

@click.command()
@click.argument('status', nargs=-1)
def make_tweet(status):
    to_tweet = ' '.join(status)
    tweet(to_tweet)

if __name__ == "__main__":
    make_tweet()