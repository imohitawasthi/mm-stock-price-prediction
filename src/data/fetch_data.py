"""
    Takes almost an entire day to fetch all the data. Also, there are some symbols for which the data can no be fetched
"""

import time
from datetime import date

from nsepy import get_history

from src.data.helpers import SYMBOL_LIST
from utils.constants import RAW_DATA_PATH

DATA_FETCH_FROM_DATE = date(2010, 1, 1)
DATA_FETCH_TO_DATE = date(2021, 9, 4)


def fetch_data():
    total_symbols = len(SYMBOL_LIST)
    index = 0

    for symbol in SYMBOL_LIST:

        try:
            data = get_history(symbol=symbol, start=DATA_FETCH_FROM_DATE, end=DATA_FETCH_TO_DATE)
            data.to_csv(RAW_DATA_PATH + 'data-{symbol}.csv'.format(symbol=symbol.lower()))

        except:
            print('Failed on ', symbol)

        print(
            '\r Total Completion: {completion}, Percentage: {percentage}'.format(
                completion=index,
                percentage=(index / total_symbols) * 100
            ),
            end=''
        )

        # For avoiding any kind of api limits
        time.sleep(1)
        index += 1
