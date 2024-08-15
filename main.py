import feedparser, time

URL = "https://naturecancoding.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 7

new_content = """
<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
"""  # 카드들을 감싸는 div 시작

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        new_content += f"""
        <div style="border: 1px solid #ddd; border-radius: 8px; width: 300px; padding: 16px; margin: 8px; box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);">
            <h3>{feed['title']}</h3>
            <p style="color: #555;">{time.strftime('%Y/%m/%d', feed_date)}</p>
            <a href="{feed['link']}" style="text-decoration: none; color: #1E90FF;">Read More</a>
        </div>
        """  # 개별 카드

new_content += "</div>"  # 카드들을 감싸는 div 종료

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
        # Keep the section before and after the custom section and replace the content in between
        new_lines = lines[:start_index+1] + [new_content + "\n"] + lines[end_index:]
        with open("README.md", "w", encoding="utf-8") as file:
            file.writelines(new_lines)

if __name__ == "__main__":
    update_readme_section(new_content)