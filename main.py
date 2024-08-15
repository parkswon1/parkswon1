import feedparser, time

URL = "https://naturecancoding.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 7

new_content = "### 📝 최신 블로그 포스트\n\n"  # 블로그 포스트 리스트 앞에 제목 추가

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        new_content += f"""<a href="{feed['link']}" style="text-decoration: none; display: block; margin-bottom: 10px;">
    <div style="border: 1px solid #007ACC; border-radius: 5px; padding: 10px; background-color: #f5f5f5;">
        📰 <strong>{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}</strong>
    </div>
</a>\n"""

def update_readme_section(new_content):
    with open("README.md", "r", encoding="utf-8") as file:
        lines = file.readlines()

    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if "<!-- START_CUSTOM_SECTION -->" in line:
            start_index = i
        elif "<!-- END_CUSTOM_SECTION -->" in line:
            end_index = i
            break

    if start_index is not None and end_index is not None:
        new_lines = lines[:start_index+1] + [new_content + "\n"] + lines[end_index:]
        with open("README.md", "w", encoding="utf-8") as file:
            file.writelines(new_lines)

if __name__ == "__main__":
    update_readme_section(new_content)
