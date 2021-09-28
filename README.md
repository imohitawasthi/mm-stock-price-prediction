model_stock_predictions
==============================

A Model to predict Stock market behaviour and help in making investment strategies. 

Working
------------

I started with the last 10-years of NSE stock data for 2000 odd companies and fetched it using NSEpy[1]. That allowed me to get all the data in CSV files, and by combining all the CSV files, I created an initial set of raw data. The format which I used to process the data are DataFrame[2], Pickle[3], and CSV. I skipped the data cleaning part, this is not a good practice, but in this case, because the source was reliable and distributed randomly due to its nature, it was okay to ditch the conventional approach.
 
The correlation matrix[4] helped in drawing inferences and making choices towards model parameters. The correlation matrix created using the raw data helped in understanding the internal relations between the DataFrame[5] attributes. One of the correlations was between time and closing price. It gave a clear indication of how the stock has performed over time. A negative correlation suggests that there is an inverse relationship between time[6] and closing price[7].
 
And the other fascinating correlation that helped in choosing the model parameters was between the closing price and opening price(A very high correlation). And by defining time and opening price[8] because independent variables and closing price as a dependent variable, I deliberately overfitted the model. It allowed testing a fascinating way of predicting closing price[9] as the current predicted value will be served as the opening price input to the next prediction. The entire process happens in a loop, where each iteration describes a day and predicts a possible closing price for that particular day.
 
For training, I selected the linear regression model[10], and of course, because of the overfitted model, it did perform well with training data[11] sets. I didn't even test it. But for predictions, I simulated a period through which I recorded the predictions (Average and Last Day Closing Price) against a correlation matrix.
 
It gave me enough information to create a score for each stock price. The higher the score, the higher the chances of success. It naturally means this indicates a good investment. Although there can be outliers and while making final inferences, we can sort them out.
 
For scoring, I used:
 
```
    Score = [Cost Correlation > 70; 1 : 0 ] + [0 < |(Current/Average)| < 2; 1 : 0] + [10 < Change Percentage < 50; 1 : 0] + [10 * ((Predicted Average - Average)/Average)] + [10 * ((Predicted Cost - Cost)/Cost)]
```

> *Interpretation for the above formula [ Condition; If True : If False ]*

References
------------

	1. NSEpy is a library to extract historical and real-time data from NSE’s website. This Library aims to keep the API very simple. (https://nsepy.xyz/) 
	2. pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
	built on top of the Python programming language. (https://pandas.pydata.org/)
	3. Python pickle module is used for serializing and de-serializing a Python object structure
	4. A correlation matrix is a table showing correlation coefficients between variables. Each cell in the table shows the correlation between two variables. A correlation matrix is used to summarize data, as an input into a more advanced analysis, and as a diagnostic for advanced analyses.
	5. Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. (https://www.geeksforgeeks.org/python-pandas-dataframe/)
	6. Time represents a day of stock market.
	7. The price at which trade closed for a stock.
	8. The price at which trade opens for a stock.
	9. The closing price predicted using the modal.
	10. linear regression is a linear approach for modelling the relationship between a scalar response and one or more explanatory variables. The case of one explanatory variable is called simple linear regression; for more than one, the process is called multiple linear regression. (https://en.wikipedia.org/wiki/Linear_regression)
	11. Train/Test is a method to measure the accuracy of your model. It is called Train/Test because you split the data set into two sets: a training set and a testing set. Usually in 20-80 ratio. 


Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

--------

