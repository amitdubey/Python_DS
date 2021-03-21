
from yahoofinancials import YahooFinancials
import pandas as pd
import bisect

import timeit
import statistics
import numpy as np
from functools import reduce
import pandas as pd

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

#save the dataframe to CSV if needed
#prices_df.to_csv('/Users/amitdubey/Documents/GitHub/Python_DS/spy.csv')





LIST_RANGE = 10000000000
NUMBERS_OF_TIMES_TO_TEST = 10000

l = df

def median1():
    return statistics.median(l)


def median2():
    return np.median(l)


def median3():
    return pd.Series(l).median()

def median4():
    data = sorted(l)
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2



for func in [median1, median2, median3,median4]:
    print(f"{func.__name__} took: ",  timeit.timeit(stmt=func, number=NUMBERS_OF_TIMES_TO_TEST))


#timing test for mean with different algos


l = df

def mean1():
    return statistics.mean(l)


def mean2():
    return sum(l) / len(l)


def mean3():
    return np.mean(l)


def mean4():
    return np.array(l).mean()


def mean5():
    return reduce(lambda x, y: x + y / float(len(l)), l, 0)

def mean6():
    return pd.Series(l).mean()



for func in [mean1, mean2, mean3, mean4, mean5, mean6]:
    print(f"{func.__name__} took: ",  timeit.timeit(stmt=func, number=NUMBERS_OF_TIMES_TO_TEST))