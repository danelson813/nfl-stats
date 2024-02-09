import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pyarrow as pa
from utils.util import get_soup, create_db
from utils.logger_module import logger_start
logger = logger_start()
logger.info("Logger has started")


url = "https://www.nfl.com/stats/player-stats/category/rushing/2023/post/all/rushingyards/desc"

soup = get_soup(url)

rows = soup.select_one('tbody').select('tr')
logger.info(f"There are {len(rows)} rows.")

results = []
for row in rows:
    row_= [td.text.strip() for td in row.findAll('td')]
    result = {
        'player': row_[0],
        'Rush Yds': row_[1],
        'Att': row_[2],
        'TD': row_[3],
        '20+': row_[4],
        '40+': row_[5],
        'Lng': row_[6],
        'Rush_1st': row_[7],
        'Rush_1st%': row_[8],
        'Rush_FUM': row_[9]        
    }
    results.append(result)
df = pd.DataFrame(results)
df.to_csv('data/rushing.csv', index=False)
create_db(df, table_name='rushing')


