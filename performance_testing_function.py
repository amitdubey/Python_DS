import download_large_file_split as dl
import mean_media_class as mc
import statistics
import numpy as np
import pandas as pd
import timeit
from functools import reduce

l=pd.DataFrame(data=None)

"""Return a float

    Time taken in milisecond by list range members for given iterations by a Mean or median  of a numeric array or list
    """


LIST_RANGE = 10000000000
NUMBERS_OF_TIMES_TO_TEST = 100

def main():
    d1 = dl.downloadHistoryStockData()
    result =d1.downloadfile(dl.number_of_chunks, dl.STOCK_NAME, dl.START_DATE, dl.END_DATE, dl.INTERVAL, dl.FOLDER_LOCATION)
    
    m2 =mc.Mean()
    m1 =mc.Median()
    m1.l=result
    m2.l=result
    for func in [m1.median1, m1.median2,m1.median3,m1.median4,m1.median5]:
        print(f"{func.__name__} took: ",  timeit.timeit(stmt=func, number=NUMBERS_OF_TIMES_TO_TEST))

    for func in [m2.mean1, m2.mean2, m2.mean3, m2.mean4, m2.mean5,m2.mean6]:
        print(f"{func.__name__} took: ",  timeit.timeit(stmt=func, number=NUMBERS_OF_TIMES_TO_TEST))
    
    print('****************************************************')
    print('Mean is', m2.mean1())
    print('Mean is', m2.mean2())
    print('Mean is', m2.mean3())
    print('Mean is', m2.mean4())
    print('Mean is', m2.mean5())

    print('****************************************************')
    print('Median is', m1.median1())
    print('Median is', m1.median2())
    print('Median is', m1.median3())
    print('Median is', m1.median4())
    print('Median is', m1.median5())


if __name__ == '__main__':
    main()
   