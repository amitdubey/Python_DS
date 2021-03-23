import dask.dataframe as dd
df1 = dd.read_csv('./Users/amitdubey/Documents/GitHub/Python_DS/chunk*.csv')
df1 = df1.repartition(npartitions=4)
df1.to_parquet('./Users/amitdubey/Documents/GitHub/Python_DS/chunkparquet4', write_index=False)



#test code other alternative tried.
#print(df.dtype)
# def splitdataset(datafrm,numsplits):
#     return ([df[i:i+numsplits] for i in range(0,datafrm.shape[0],numsplits)])
# #save the dataframe to CSV if needed
# #prices_df.to_csv('/Users/amitdubey/Documents/GitHub/Python_DS/spy.csv')

# #split the dataframe into 4 equal files
# df1 =pd.DataFrame(splitdataset(prices_df,4))

 # for idx, chunk in enumerate(np.array_split(df, number_of_chunks)):
#     print(chunk)
#     chunk.to_csv(f'/Users/amitdubey/Documents/GitHub/Python_DS/spy_{idx}.csv')