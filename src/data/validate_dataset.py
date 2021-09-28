import pickle

from src.data.helpers import SYMBOL_LIST
from utils.constants import PROCESSED_DATA_PATH


def validate_dataset():
    data_frame = open(PROCESSED_DATA_PATH + 'final_data.pickle', "rb")
    data_frame = pickle.load(data_frame)

    symbol_list = list(data_frame.Symbol.unique())
    symbol_list = [x for x in SYMBOL_LIST if x not in symbol_list]

    print("Data files not available", symbol_list)
