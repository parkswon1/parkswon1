import feedparser, time

URL="https://naturecancoding.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=7

markdown_text = """
[쓰고싶은 내용]
""" # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()