import pickle
import re
from os import listdir
from os.path import isfile, join

import pandas as pd

from utils.constants import RAW_DATA_PATH, PROCESSED_DATA_PATH


def make_dataset():
    raw_data_file_name = [file_name for file_name in listdir(RAW_DATA_PATH) if isfile(join(RAW_DATA_PATH, file_name))]
    raw_data_file_name = [file_name for file_name in raw_data_file_name if re.search(r'.csv', file_name, re.M)]

    raw_data_files = [pd.read_csv(RAW_DATA_PATH + file_name) for file_name in raw_data_file_name]

    final_data_file = pd.concat(raw_data_files, axis=0, ignore_index=True)

    final_data_file.to_csv(PROCESSED_DATA_PATH + 'final_data.csv')

    with open(PROCESSED_DATA_PATH + 'final_data.pickle', 'wb') as file:
        pickle.dump(final_data_file, file)

    print("Complete")
