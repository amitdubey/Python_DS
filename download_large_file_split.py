
from yahoofinancials import YahooFinancials
import pandas as pd
import bisect
import timeit
import statistics
import numpy as np
from functools import reduce
import pandas as pd
from random import sample
from re import split
import os
import glob

number_of_chunks =4
START_DATE = "2019-03-19"
END_DATE = "2021-03-19"
INTERVAL ='daily'
STOCK_NAME ='%5EGSPC'
FOLDER_LOCATION ="/Users/amitdubey/Documents/GitHub/Python_DS"

#download SPY data from yahoo financials
class downloadHistoryStockData(object):
    def downloadfile(self,number_of_chunks,STOCK_NAME,START_DATE,END_DATE,INTERVAL,FOLDER_LOCATION) -> float:    
        assets =[STOCK_NAME]
        yahoo_financials = YahooFinancials(assets)
        data =yahoo_financials.get_historical_price_data(START_DATE,END_DATE,INTERVAL)

        # print(data)
        #get the prices by date
        prices_df = pd.DataFrame({
            a: {x['formatted_date']: x['adjclose'] for x in data[a]['prices']} for a in assets
        })
        #prices_df.head(10)

        #rename the index to column correctly
        prices_df.reset_index(inplace=True)
        prices_df = prices_df.rename(columns = {'index':'date','%5EGSPC':'SPY'})

        #convert the column to float and also round it
        df= prices_df["SPY"].astype('float')
        df=list(prices_df.SPY.values)
        df = [round(num, 1) for num in df]

        # Split the file into the defined no. of chunks
        for i,chunk in enumerate(np.array_split(df, number_of_chunks)):
            chunk =pd.DataFrame(chunk)
            chunk.to_csv('chunk{}.csv'.format(i), index=False)


        os.chdir(FOLDER_LOCATION)
        results = pd.DataFrame([])

        for counter, file in enumerate(glob.glob("chunk*.csv")):
            namedf = pd.read_csv(file,skiprows=0)
            results = results.append(namedf)
        #print(results)

        results.reset_index(drop=True,inplace=True)
        return results
     
def main():
    d =downloadHistoryStockData()
    result =d.downloadfile(number_of_chunks,STOCK_NAME,START_DATE,END_DATE,INTERVAL,FOLDER_LOCATION)
    print(result)
    print(type(result))


if __name__ == '__main__':
    main()
    

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