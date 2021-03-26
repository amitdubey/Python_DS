from typing import List
import has_two_sum

lst =[1,3,4,5,7,9,11,23,12]
t =12

def has_three_sum(A: List[int], t: int) -> bool:

    A.sort()
    # Finds if the sum of two numbers in A equals to t - a.
    return any(has_two_sum(A, t - a) for a in A)


if __name__ == '__main__':
  
   print(has_three_sum(lst,t))