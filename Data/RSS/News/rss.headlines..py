# -*- coding: utf-8 -*-
'''
Created on Sun Mar  9 14:22:15 2025

@author: sucrerey
'''
import feedparser
import webbrowser

base_html = "<html><head></head><body>#{body}</body></html>"

def get_article_html(entry):
    article = "<div>"
    #article += "<h4>{}</h4>".format(entry.title)
    article += '<a href="{}">{}</a>'.format(entry.link, entry.title)
    if hasattr(entry,"published"):
        article += '<br/>{}'.format(entry.published)
    if hasattr(entry,"author"):
        article += '<br/>By: {}'.format(entry.author)
    article += "</div><br/>"
    return article

all_feeds = {}
all_feeds["npr.001"] = "https://feeds.npr.org/1001/rss.xml"
all_feeds["pbs.001"] = "https://www.pbs.org/newshour/feeds/rss/headlines"
all_feeds["bbc.us.001"] = "https://feeds.bbci.co.uk/news/rss.xml?edition=us"
all_feeds["bbc.world.001"] = "https://feeds.bbci.co.uk/news/rss.xml?edition=int"
all_feeds["nas.001"] = "https://www.nasa.gov/news-release/feed/"
all_feeds["cnn.001"] = "http://rss.cnn.com/rss/edition.rss"
all_feeds["guard.world.001"] = "https://www.theguardian.com/world/rss"
all_feeds["guard.us.001"] = "https://www.theguardian.com/us-news/rss"
all_feeds["dailymail.001"] = "https://www.dailymail.co.uk/news/index.rss"
all_feeds["dailymail.science.001"] = "https://www.dailymail.co.uk/sciencetech/index.rss"

feed_html = ""

for k,v in enumerate(all_feeds):
    new_feed = feedparser.parse(all_feeds[v])
    feed_html += "<h3>{} : {}</h3>".format(v, new_feed.feed.title)
    feed_html += "<div style='margin-left:20px;'>"
    for entry in new_feed.entries:
        feed_html += get_article_html(entry)
    feed_html += "</div>"

base_html = base_html.replace("#{body}", feed_html)

with open("headlines.html", "w", encoding="utf-8") as text_file:
    text_file.write(base_html)
    webbrowser.open("headlines.html",new=0)