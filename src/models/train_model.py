# Imports
import pickle

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

from utils.constants import \
    REGRESSION_MODEL_PATH_PICKLE, \
    LR_STOCK_INDEPENDENT_VARIABLES, \
    LR_STOCK_DEPENDENT_VARIABLES
from utils.helper import read_data, test_train_split


class TrainModel:

    def __init__(self):
        self.data_frame, _ = read_data()

        self.model_linear_stock_price = []
        self.model_polynomial_stock_price = []

    def linear_model(self, independent_variable, dependent_variable):
        model = {}

        for index, symbol in enumerate(self.data_frame['Symbol'].unique()):

            try:
                temp_data_frame = self.data_frame[self.data_frame['Symbol'] == symbol]

                train_independent_data, train_dependent_data, test_independent_data, test_dependent_data = test_train_split(
                    temp_data_frame, independent_variable, dependent_variable
                )

                linear_regression = linear_model.LinearRegression()
                linear_regression.fit(train_independent_data, train_dependent_data)

                predicted = linear_regression.predict(test_independent_data)

                model_dict = {
                    'mean_error': mean_squared_error(test_dependent_data, predicted),
                    'r2_score': r2_score(test_dependent_data, predicted),
                    'model': linear_regression
                }

            except:
                model_dict = {
                    'mean_error': 0,
                    'r2_score': 0,
                    'model': None
                }

            model[symbol] = model_dict

            print("\r Model", index + 1, end='')

        return model

    def polynomial_model(self, independent_variable, dependent_variable):
        model = {}

        for index, symbol in enumerate(self.data_frame['Symbol'].unique()):

            try:
                temp_data_frame = self.data_frame[self.data_frame['Symbol'] == symbol]

                train_independent_data, train_dependent_data, test_independent_data, test_dependent_data = test_train_split(
                    temp_data_frame, independent_variable, dependent_variable
                )

                polynomial_regression = Pipeline(
                    [
                        ('poly', PolynomialFeatures(degree=3)),
                        ('linear', linear_model.LinearRegression())
                    ]
                )

                polynomial_regression.fit(train_independent_data, train_dependent_data)

                poly_variables = polynomial_regression.named_steps['poly'].fit_transform(test_independent_data)
                predicted = polynomial_regression.named_steps['linear'].predict(poly_variables)

                model_dict = {
                    'mean_error': mean_squared_error(test_dependent_data, predicted),
                    'r2_score': r2_score(test_dependent_data, predicted),
                    'model': polynomial_regression.named_steps['linear'],
                    'poly_variables': polynomial_regression.named_steps['poly']
                }

            except:

                model_dict = {
                    'mean_error': 0,
                    'r2_score': 0,
                    'model': None,
                    'poly_variables': None
                }

            model[symbol] = model_dict

            print("\r Model", index + 1, end='')

        return model

    def stock_price(self):
        self.model_linear_stock_price = self.linear_model(
            LR_STOCK_INDEPENDENT_VARIABLES,
            LR_STOCK_DEPENDENT_VARIABLES
        )
        self.model_polynomial_stock_price = self.polynomial_model(
            LR_STOCK_INDEPENDENT_VARIABLES,
            LR_STOCK_DEPENDENT_VARIABLES
        )

    def train(self):
        self.stock_price()

        with open(REGRESSION_MODEL_PATH_PICKLE, 'wb') as file:
            pickle.dump(
                {
                    'linear': self.model_linear_stock_price,
                    'polynomial': self.model_polynomial_stock_price
                },
                file
            )


def train():
    train_model = TrainModel()
    train_model.train()
