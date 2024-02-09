import pandas as pd
from bs4 import BeautifulSoup as bs

import pyarrow as pa
from utils.util import get_soup, create_db
from utils.logger_module import logger_start
logger = logger_start()
logger.info("Logger has started")

url = "https://www.nfl.com/stats/player-stats/category/passing/2023/post/all/passingyards/desc"

soup = get_soup(url)

rows = soup.select_one('tbody').select('tr')
logger.info(f"There are {len(rows)} rows.")

results = []
for row in rows:
    row_= [td.text.strip() for td in row.findAll('td')]
    result = {
        'player': row_[0],
        'Pass Yds': row_[1],
        'Yds/Att': row_[2],
        'Att': row_[3],
        'Cmp': row_[4],
        'Comp%': row_[5],
        'TD': row_[6],
        'INT': row_[7],
        'Rate': row_[8],
        '1st': row_[9],
        '1st%': row_[10],
        '20+': row_[11],
        '40+': row_[12],
        'Lng': row_[13],
        'Sck': row_[14],
        'SckY': row_[15]
    }
    results.append(result)
df = pd.DataFrame(results)
df.to_csv('data/passing.csv', index=False)
create_db(df, table_name='passing')
