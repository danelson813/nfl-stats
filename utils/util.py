from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup as bs
import sqlite3
import pandas as pd


def get_soup(url):
    ua = UserAgent()
    useragent = ua.random
    headers = {"user-agent": useragent}
    page = requests.get(url, headers=headers)
    soup = bs(page.text, 'html.parser')
    return soup

def create_db(df:  pd.DataFrame, table_name: str) -> None:
    conn = sqlite3.connect('data/NFLStats.db')
    # df = pd.read_csv(path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
