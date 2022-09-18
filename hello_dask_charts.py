from dblib.charts import dask_query_charts

ddf = dask_query_charts()
#print("One record from the enron dataset without compute:")
#print(ddf["title"][0])
#print("One record from the enron dataset with compute:")
#print(ddf["title"][0].compute())

#print(ddf["title"][0:10].compute())  

#print(len(ddf['region'].unique()))
#print(ddf[(ddf.title == 'Safari') & (ddf.region == 'Chile')].compute())

#x =ddf[ddf["title"] == "Safari"]["artist"].compute()
#print(x.head(n=1))

def get_artist(title:str):
    x =ddf[ddf["title"] == title]["artist"].compute()
    return x.head(n=1)

#print(get_artist("Safari"))

#def get_artist(name):
   # x = ddf[["title" == name]].compute()
   # artist_name = x["artist"]
  #  return x.head(n=1)

#print(get_artist("Safari"))

#x =ddf[ddf["title"] == title]["artist"].compute()
#return x.head(n=1)


#print(ddf[ddf.chart == top200])
streams = ddf.groupby('region')['streams'].sum().reset_index()
streams['percent_streams'] = streams['streams']/streams['streams'].sum()
streams['region'] = streams.apply(lambda x: x['region'] if x['percent_streams'] >= .01 else 'Other', axis=1, meta=(None, 'object'))
streams = streams.groupby('region')['percent_streams'].sum().reset_index().round(3).sort_values(by='percent_streams')
#print(streams.compute())

def get_country(country:str):
    country_name = streams[streams['region'] == country].compute()
    return country_name.head(n=1)

