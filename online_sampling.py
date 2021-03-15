import itertools
from typing import Iterator

import random
def online_random_sample(stream: Iterator[int],k:int):
    running_sample =list(itertools.islice(stream,k))
    num_seen_so_far =k
    
    for x in stream:
        num_seen_so_far +=1
        idx_to_replace =random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            running_sample[idx_to_replace] =x
    return running_sample        


def main():
    stream =[1,2,5,6,7,7,7,754545,45454,4545,12,12,4,6,67]
    k =5
    print(stream,k,'online random sample',online_random_sample(stream,k))
    
if __name__ == '__main__':
    main()
    