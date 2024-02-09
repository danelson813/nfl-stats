import pandas as pd
from utils.util import get_soup, create_db
from utils.logger_module import logger_start
logger = logger_start()
logger.info("Logger has started")


url = "https://www.nfl.com/stats/player-stats/category/receiving/2023/post/all/receivingreceptions/desc"

soup = get_soup(url)

rows = soup.select_one('tbody').select('tr')
logger.info(f"There are {len(rows)} rows.")

results = []
for row in rows:
    row_= [td.text.strip() for td in row.findAll('td')]
    result = {
        'player': row_[0],
        'Rec': row_[1],
        'Yds': row_[2],
        'TD': row_[3],
        '20+': row_[4],
        '40+': row_[5],
        'Lng': row_[6],
        'Rec_1st': row_[7],
        '1st%': row_[8],
        'Rec_FUM': row_[9],
        'Rec_YAC/R': row_[10],
        'Tgts': row_[11]
    }
    results.append(result)
df = pd.DataFrame(results)
df.to_csv('data/receivers.csv', index=False)
create_db(df, table_name='receivers')
