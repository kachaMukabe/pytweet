from src.ui import create_choice, create_layout
import click
from src.tweet import like, mentions, retweet, retweets, sample, statuses, stream, timeline, tweet, user_info


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        create_layout(tweets=timeline(), mentions=mentions(), user=user_info(), retweets=retweets())
    else:
        pass

@click.command()
@click.argument('status', nargs=-1)
def t(status):
    to_tweet = ' '.join(status)
    tweet(to_tweet)

@click.command()
@click.argument('tweet_id')
def rt(tweet_id):
    retweet(tweet_id)

@click.command()
@click.argument('tweet_id')
def l(tweet_id):
    like(tweet_id)

@click.command()
def st():
    statuses()

@click.command()
def tui():
    create_choice(timeline())
    # click.echo(layout)

cli.add_command(t)
cli.add_command(rt)
cli.add_command(l)
cli.add_command(tui)

if __name__ == "__main__":
    cli()