
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

#download SPY data from yahoo financials
assets =['%5EGSPC']
yahoo_financials = YahooFinancials(assets)
data =yahoo_financials.get_historical_price_data("2019-03-19", "2021-03-19", 'daily')

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
#print(df.dtype)
print(df)
# def splitdataset(datafrm,numsplits):
#     return ([df[i:i+numsplits] for i in range(0,datafrm.shape[0],numsplits)])
# #save the dataframe to CSV if needed
# #prices_df.to_csv('/Users/amitdubey/Documents/GitHub/Python_DS/spy.csv')

# #split the dataframe into 4 equal files
# df1 =pd.DataFrame(splitdataset(prices_df,4))


    ###split file method 2
number_of_chunks =4

for i,chunk in enumerate(np.array_split(df, number_of_chunks)):
    chunk =pd.DataFrame(chunk)
    chunk.to_csv('chunk{}.csv'.format(i), index=False)
# for idx, chunk in enumerate(np.array_split(df, number_of_chunks)):
#     print(chunk)
#     chunk.to_csv(f'/Users/amitdubey/Documents/GitHub/Python_DS/spy_{idx}.csv')

##############Read multiple chunks into one dataframe and pass it for calculations******##############
import os
import glob

path = "/Users/amitdubey/Documents/GitHub/Python_DS" 
os.chdir(path)
results = pd.DataFrame([])

for counter, file in enumerate(glob.glob("chunk*.csv")):
    namedf = pd.read_csv(file,skiprows=0)
    results = results.append(namedf)
#print(results)

results.reset_index(drop=True,inplace=True)

 ##################################*******Median and Average**********##################################       
l = results
print(l)
LIST_RANGE = 10000000000
NUMBERS_OF_TIMES_TO_TEST = 100


def median1():
    return ( statistics.median(l.values))


def median2():
    return (  np.median(l.values))


def median3():
    return pd.Series(map(float,l.values)).median()

def median4():
    data = sorted(l.values)
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return ( (data[i - 1] + data[i]) / 2)

def median5():
    quotient, remainder = divmod(len(l), 2)
    if remainder:
        return sorted(l.values)[quotient]
    return ( sum(sorted(l.values)[quotient - 1:quotient + 1]) / 2)



for func in [median1, median2, median3,median4,median5]:
    print(f"{func.__name__} took: ",  timeit.timeit(stmt=func, number=NUMBERS_OF_TIMES_TO_TEST))


#timing test for mean with different algos




def mean1():
    return statistics.mean(map(float,l.values))
def mean2():
    return ( sum(l.values) / len(l))


def mean3():
    return (  np.mean(l.values))

def mean4():
    return (np.array(l).mean())


def mean5():
    return (  reduce(lambda x, y: x + y / float(len(l)), l.values, 0))

def mean6():
    return ( pd.Series(l.all()).mean())



for func in [mean1, mean2, mean3, mean4, mean5, mean6]:
    print(f"{func.__name__} took: ",  timeit.timeit(stmt=func, number=NUMBERS_OF_TIMES_TO_TEST))


print('****************************************************')
print('Mean is', mean1())
print('Mean is', mean2())
print('Mean is', mean3())
print('Mean is', mean4())
print('Mean is', mean5())

print('****************************************************')
print('Median is', median1())
print('Median is', median2())
print('Median is', median3())
print('Median is', median4())
print('Median is', median5())