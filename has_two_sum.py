from typing import List

lst =[1,3,6,9]
t =9
def has_two_sum(A: List[int], t: int) -> bool:

    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  #A[i] + A[j] > t.
            j -= 1
    return False


if __name__ == '__main__':
    print(has_two_sum(lst,t))

