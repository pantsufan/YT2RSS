# YT2RSS

Convert YouTube channel subscriptions from NewPipe to RSS feeds that can be imported into any RSS reader.

## Quick Start

1. Export your subscriptions from NewPipe
2. Place the `newpipe_subscriptions_*.json` file in the same folder as this script
3. Run: `python script.py`
4. Import `feeds.opml` into your RSS reader

## Requirements

- Python 3
- NewPipe subscription export (JSON format)

## What it does

1. Finds your NewPipe export file automatically
2. Converts YouTube channel URLs to RSS feed URLs
3. Generates a `feeds.opml` file with all your subscriptions

## Example

After running the script, you'll get a `feeds.opml` file like this:

```xml
<outline text="Channel Name" title="Channel Name" type="rss" xmlUrl="https://www.youtube.com/feeds/videos.xml?channel_id=..."/>
```

Import this file into Feedly, Tiny Tiny RSS, or any other RSS reader to follow YouTube channels without YouTube's algorithmic feed.
