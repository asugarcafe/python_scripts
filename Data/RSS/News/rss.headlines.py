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
all_feeds["sltrib"] = "https://www.sltrib.com/arc/outboundfeeds/rss/?outputType=xml"
all_feeds["aljaz"] = "https://www.aljazeera.com/xml/rss/all.xml"
all_feeds["slash."] = "https://rss.slashdot.org/Slashdot/slashdot"
all_feeds["guard.world"] = "https://www.theguardian.com/world/rss"
all_feeds["guard.us"] = "https://www.theguardian.com/us-news/rss"
all_feeds["npr"] = "https://feeds.npr.org/1001/rss.xml"
all_feeds["pbs"] = "https://www.pbs.org/newshour/feeds/rss/headlines"
all_feeds["bbc.us"] = "https://feeds.bbci.co.uk/news/rss.xml?edition=us"
all_feeds["bbc.world"] = "https://feeds.bbci.co.uk/news/rss.xml?edition=int"
all_feeds["nas"] = "https://www.nasa.gov/news-release/feed/"
all_feeds["lemonde"] = "https://www.lemonde.fr/en/rss/une.xml"
all_feeds["lemonde.int"] = "https://www.lemonde.fr/en/international/rss_full.xml"
all_feeds["cnn"] = "http://rss.cnn.com/rss/edition.rss"
all_feeds["dailymail.top"] = "https://www.dailymail.co.uk/news/index.rss"
all_feeds["dailymail.science"] = "https://www.dailymail.co.uk/sciencetech/index.rss"

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