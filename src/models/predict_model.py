import pickle

import matplotlib.pyplot as plt
import pandas as pd

from utils.constants import REGRESSION_MODEL_PATH_PICKLE, LR_STOCK_INDEPENDENT_VARIABLES
from utils.helper import read_data, create_duration


class PredictModel:

    def __init__(self, stock_name, duration=31):
        model = open(REGRESSION_MODEL_PATH_PICKLE, "rb")
        model = pickle.load(model)
        data_frame, _ = read_data()

        self.model_linear = model['linear'][stock_name]
        self.model_polynomial = model['polynomial'][stock_name]
        self.data_frame = data_frame[data_frame['Symbol'] == stock_name]

        self.model = model
        self.stock_name = stock_name

        self.prediction_duration = create_duration(duration=duration)

        self.prediction_turnover = []
        self.prediction_stocks = []

    def predict_linear(self):

        last_open = self.data_frame['Close'].to_list()[-1]

        stock_time = []
        stock_price = []

        for timestamp in self.prediction_duration:

            try:
                predicted_stock = self.model_linear['model'].predict(
                    pd.DataFrame(
                        {
                            'Open': [last_open],
                            'Timestamp': [timestamp]
                        }
                    )
                )

                last_open = predicted_stock[0][0]

                stock_time.append(timestamp)
                stock_price.append(last_open)

            except:
                last_open = last_open

                stock_time.append(timestamp)
                stock_price.append(last_open)

        return \
            stock_time, \
            stock_price, \
            self.data_frame[LR_STOCK_INDEPENDENT_VARIABLES[1]].to_list(), \
            self.data_frame[LR_STOCK_INDEPENDENT_VARIABLES[0]].to_list()

    def predict_polynomial(self):

        last_open = self.data_frame['Close'].to_list()[-1]

        stock_time = []
        stock_price = []

        for timestamp in self.prediction_duration:
            model_attribute = self.model_polynomial['poly_variables'].fit_transform(pd.DataFrame(
                {
                    'Open': [last_open],
                    'Timestamp': [timestamp]
                }
            ))

            predicted_stock = self.model_polynomial['model'].predict(model_attribute)

            last_open = predicted_stock[0][0]

            stock_time.append(timestamp)
            stock_price.append(last_open)

        return \
            stock_time, \
            stock_price, \
            self.data_frame[LR_STOCK_INDEPENDENT_VARIABLES[1]].to_list(), \
            self.data_frame[LR_STOCK_INDEPENDENT_VARIABLES[0]].to_list()


def predict(model_name, **args):
    predict_model = PredictModel(model_name, args['duration'])
    l_predicted_time, l_predicted_stock, actual_time, actual_stock = predict_model.predict_linear()
    # p_predicted_time, p_predicted_stock, _, _ = predict_model.predict_polynomial()

    # Plot outputs
    if args['plot']:
        plt.plot(actual_time, actual_stock, color='black', linewidth=1)

        plt.plot(l_predicted_time, l_predicted_stock, color='blue', linewidth=1)
        # plt.plot(p_predicted_time, p_predicted_stock, color='gray', linewidth=1)

        plt.xticks()
        plt.yticks()

        plt.show()
    else:
        return l_predicted_time, l_predicted_stock, actual_time, actual_stock
