from dblib.charts import dask_query_charts

ddf = dask_query_charts()
print("One record from the enron dataset without compute:")
print(ddf["title"][0])
print("One record from the enron dataset with compute:")
print(ddf["title"][0].compute())