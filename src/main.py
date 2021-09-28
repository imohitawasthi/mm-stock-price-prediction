"""

### For creating the data
from src.data import fetch_data

### For creating final data
from src.data import make_dataset

### Basic Validation of data fetched and prepared
from src.data import validate_dataset

### Train and Predict Model
from src.models import train, predict

"""

from src.models import predict
from src.features import features


def main():
    # predict('HDFC')
    features()


if __name__ == '__main__':
    main()
