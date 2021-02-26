from src.tweet import like, retweet
import click
from rich import table
from rich import console
from rich.align import Align
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table 
from rich import box
import questionary
from questionary import Choice
from rich.console import Console
from rich.layout import Layout
from rich.text import Text
from rich.theme import Theme
custom_theme = Theme({
    "info" : "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})

def create_layout(tweets=[], mentions=[], user=None, retweets=[]):
    console = Console()
    layout = Layout()

    layout.split(
        Layout(name="PyTweet", size=3),
        Layout(ratio=1, name="main"),
        Layout(size=3, name="footer"),
    )
    table = Table(expand=True, box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column("PyTweet", justify="center")
    layout["PyTweet"].update(table)
    if not user == None:
        layout["footer"].update(create_profile_panel(user))
    # layout["footer"].update(Panel("Coming soon", title="User Info"))

    layout["main"].split(
        Layout(name="side"),
        Layout(name="body", ratio=2),
        direction="horizontal"
    )
    layout["side"].split(Layout(create_mentions(mentions)), Layout(create_retweets_panel(retweets)))
    layout["body"].update(create_timeline_table(tweets))
    console.print(layout)

def create_timeline_table(tweets):
    table = Table.grid(padding=1)
    table.add_column()
    table.add_column(overflow='fold')
    for tweet in tweets:
        user_name = Text(f'@{tweet["user"]["screen_name"]}')
        user_name.stylize("bold magenta")
        text = Text(tweet["text"], overflow='fold')
        table.add_row(user_name, text)
    panel = Panel(table, title="Timeline")
    return panel

def create_mentions(tweets):
    table = Table.grid(padding=1)
    # table.add_column()
    table.add_column(overflow='fold')
    for tweet in tweets:
        # user_name = Text(f'@{tweet["user"]["screen_name"]}')
        # user_name.stylize("bold magenta")
        text = Text(tweet["text"])
        table.add_row(text)
    panel = Panel(table, title="Mentions")
    return panel

def create_retweets_panel(tweets):
    table = Table.grid(padding=1)
    table.add_column()
    table.add_column(overflow='fold')
    for tweet in tweets:
        count = Text(f'{tweet["retweet_count"]}')
        count.stylize("bold magenta")
        text = Text(tweet["text"])
        table.add_row(count,text)
    panel = Panel(table, title="Mentions")
    return panel

def create_profile_panel(profile):
    table = Table.grid(padding=1)
    table.add_column()
    table.add_column()
    table.add_column()
    table.add_row(f"@{profile['screen_name']}", f"Followers: {profile['followers_count']}", f"No Tweets: {profile['statuses_count']}")
    panel = Panel(Align.center(
            table,
            vertical="middle",
        ), title="Me")
    return panel


def create_choice(tweets):
    custom_style_fancy = questionary.Style([
        ("highlighted", "fg:#f44336 bold"),  # style for a token which should appear highlighted
    ])
    console = Console()
    selected = questionary.select("Watch search result", 
    [Choice([('class:highlighted',f"@{tweet['user']['screen_name']}\n"),('class:text',tweet['text'])], value=tweet) for tweet in tweets], style=custom_style_fancy).ask()
    tweet = selected
    table = Table.grid(padding=1)
    table.add_column()
    table.add_column(overflow='fold')
    user_name = Text(f'@{tweet["user"]["screen_name"]}')
    user_name.stylize("bold magenta")
    text = Text(tweet["text"], overflow='fold')
    table.add_row(user_name, text)
    console.print(table)
    answer = Prompt.ask("Like(l)/ Retweet(r)/ Cancel(any)")
    if 'l' in answer:
        like(tweet["id"])
        click.echo("Liked tweet")
    elif 'r' in answer:
        retweet(tweet["id"])
        click.echo("Retweeted")
    else:
        click.echo("Cancelled")
    
    
    