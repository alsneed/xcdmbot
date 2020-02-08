import json
import requests
from discord.ext import commands
from keys import keys


YT_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&type=video&q={}&key={}" # NOQA
YT_WATCH_URL = "https://www.youtube.com/watch?v={}"


def yt_search(query):
    results = json.loads(
        requests.get(
            YT_SEARCH_URL.format(query, keys['youtube'])
        ).text
    )

    return results


@commands.command()
async def yt(ctx, *args):
    video_id = yt_search(' '.join(args))['items'][0]['id']['videoId']
    await ctx.send(YT_WATCH_URL.format(video_id))


def setup(bot):
    bot.add_command(yt)
