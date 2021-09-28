import pickle
import datetime

from utils.constants import \
    FINAL_DATA_PATH_PICKLE, \
    FINAL_CORRELATION_PATH_PICKLE, \
    PREDICTION_START_DATE, \
    PREDICTION_DURATION_DAYS


def read_data():
    data_frame = open(FINAL_DATA_PATH_PICKLE, "rb")
    data_correlation = open(FINAL_CORRELATION_PATH_PICKLE, "rb")

    data_frame = pickle.load(data_frame)
    data_correlation = pickle.load(data_correlation)

    return data_frame, data_correlation


def test_train_split(data_frame, independent_variables, dependent_variables, fraction=0.98):
    train_frame = data_frame.sample(frac=fraction)
    test_frame = data_frame.drop(train_frame.index)

    train_independent_data = train_frame[independent_variables]
    train_dependent_data = train_frame[dependent_variables]

    test_independent_data = test_frame[independent_variables]
    test_dependent_data = test_frame[dependent_variables]

    return train_independent_data, train_dependent_data, test_independent_data, test_dependent_data


def create_duration(**kwargs):
    return [
        datetime.datetime.strptime(
            datetime.datetime.strftime(
                PREDICTION_START_DATE + datetime.timedelta(days=idx),
                "%Y-%m-%d"
            ),
            "%Y-%m-%d"
        ).timestamp() for idx in range(kwargs['duration'])
    ]
