def even_off(A:list):
    next_even, next_odd =0,len(A) -1
    while next_even < next_odd: 
        if A[next_even] %2 ==0:
            next_even +=1
        else: 
            A[next_even],A[next_odd] =A[next_odd],A[next_even]
            next_odd -=1
    return A[next_even], A[next_odd]


lst =[1,4,5,67,7,9]
print(even_off(lst))

