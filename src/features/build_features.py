import pickle
import warnings

import pandas as pd
import numpy as np

from utils.helper import read_data
from src.models import predict

from utils.constants import PROCESSED_CORRELATION_PATH, PROCESSED_CORRELATION_PATH_PICKLE


class BuildFeatures:

    def __init__(self):
        self.data_frame, self.data_correlation = read_data()

    def build_features(self):
        warnings.filterwarnings('ignore')

        updated_data_frame = pd.DataFrame()

        for index, symbol in enumerate(self.data_correlation['Symbol'].unique()):

            data_correlation = self.data_correlation[self.data_correlation['Symbol'] == symbol]

            _, predicted_stock_month, _, _ = predict(symbol, plot=False, duration=31)
            _, predicted_stock_6_months, _, _ = predict(symbol, plot=False, duration=31*6)
            _, predicted_stock_year, _, _ = predict(symbol, plot=False, duration=365)
            _, predicted_stock_3_year, _, _ = predict(symbol, plot=False, duration=365*3)

            data_correlation['PredictedAverage1Month'] = np.mean(predicted_stock_month)
            data_correlation['PredictedAverage6Months'] = np.mean(predicted_stock_6_months)
            data_correlation['PredictedAverage1Year'] = np.mean(predicted_stock_year)
            data_correlation['PredictedAverage3Years'] = np.mean(predicted_stock_3_year)
            data_correlation['PredictedClose1Month'] = predicted_stock_month[-1]
            data_correlation['PredictedClose6Months'] = predicted_stock_6_months[-1]
            data_correlation['PredictedClose1Year'] = predicted_stock_year[-1]
            data_correlation['PredictedClose3Years'] = predicted_stock_3_year[-1]

            updated_data_frame = updated_data_frame.append(data_correlation)

            print("\r Building For ", index + 1, end='')

        # Writing data
        updated_data_frame.to_csv(PROCESSED_CORRELATION_PATH)

        with open(PROCESSED_CORRELATION_PATH_PICKLE, 'wb') as file:
            pickle.dump(updated_data_frame, file)


def features():
    build_features = BuildFeatures()
    build_features.build_features()
