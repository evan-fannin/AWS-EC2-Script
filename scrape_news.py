
import requests

from datetime import datetime

from bs4 import BeautifulSoup

import pandas as pd

import boto3

from io import StringIO


def scrape_news():
    r = requests.get('https://www.reuters.com/news/us')
    news = r.text
    time_gathered = datetime.ctime(datetime.now())
    soup = BeautifulSoup(news, 'html.parser')
    brief = soup.find_all("p", class_="FeedItemLede_lede")
    category = soup.find_all("a", class_="FeedItemMeta_channel")
    time_written = soup.find_all("span", class_="FeedItemMeta_date-updated")
    headline = soup.body.find_all("h2", class_="FeedItemHeadline_headline FeedItemHeadline_full")
    for i, entry in enumerate(brief):
        brief[i] = entry.string.replace(u'\xa0', u' ')
    for i, entry in enumerate(category):
        category[i] = entry.string.replace(u'\xa0', u' ')
    for i, entry in enumerate(time_written):
        time_written[i] = entry.string.replace(u'\xa0', u' ')
    for i, entry in enumerate(headline):
        headline[i] = entry.string.replace(u'\xa0', u' ')
    dict = {'category': category, 'time_written': time_written, 'time_gathered': time_gathered, 'headline': headline, 'brief': brief}
    df = pd.DataFrame(dict)
    return df


def save_file_to_s3(filename, df):
    bucket = 'reuters-usnews'
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.client('s3')
    s3_resource.put_object(Bucket=bucket, Key=filename, Body=csv_buffer.getvalue()


df = scrape_news()
filename = "us_news_" + df['time_gathered'][0]
save_file_to_s3(filename, df)
