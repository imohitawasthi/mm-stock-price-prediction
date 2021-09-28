import datetime

RAW_DATA_PATH = './../data/raw/'
PROCESSED_DATA_PATH = './../data/processed/'

FINAL_DATA_PATH = './../data/processed/processed_final_data.csv'
FINAL_DATA_PATH_PICKLE = './../data/processed/processed_final_data.pickle'

FINAL_CORRELATION_PATH = './../data/processed/processed_final_correlation.csv'
FINAL_CORRELATION_PATH_PICKLE = './../data/processed/processed_final_correlation.pickle'

PROCESSED_CORRELATION_PATH = './../data/processed/processed_correlation.csv'
PROCESSED_CORRELATION_PATH_PICKLE = './../data/processed/processed_correlation.pickle'

REGRESSION_MODEL_PATH_PICKLE = './../data/processed/regression.pickle'

LR_VOLUME_INDEPENDENT_VARIABLES = [
    'Turnover'
]

LR_VOLUME_DEPENDENT_VARIABLES = [
    'Timestamp'
]

LR_STOCK_INDEPENDENT_VARIABLES = [
    'Open',
    'Timestamp'
]

LR_STOCK_DEPENDENT_VARIABLES = [
    'Close'
]

PREDICTION_START_DATE = datetime.datetime.now().date()
PREDICTION_DURATION_DAYS = 365

USER_PERSONA = {

}
