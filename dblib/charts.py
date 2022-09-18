"""
Some ideas are taken from the following sources:

See this thread about unique problems with dask and data formatting:
  

"""

import pandas as pd
import dask.dataframe as dd

dtype={'streams': 'float64'}

def pandas_load_charts(location="datasets/charts.csv"):
    """Load the charts dataset into a pandas dataframe

    Assumes the dataset is in the datasets folder in the root of the project
    """
    return pd.read_csv(location)


def pandas_print_charts(location="datasets/charts.csv", record_number=0):
    """Display the charts dataset

    print and returns a single email record from the charts dataset
    """

    df = pd.read_csv(location)
    record = df["title"][record_number]
    print(record)
    return record


def dask_query_charts(location="datasets/charts.csv"):
    """Query the charts dataset

    Assumes the dataset is in the datasets folder in the root of the project
    """

    ddf = dd.read_csv(location, blocksize=None, dtype=dtype, assume_missing=True)
    return ddf
