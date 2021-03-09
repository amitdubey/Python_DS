def delete_duplicate(A):
    if not A: return 0
    write_index =1 
    B=[]
    for i in range(1,len(A)) : 
        if A[write_index -1] != A[i] : 
            A[write_index] =A[i]
            B.append(A[i])
            write_index +=1
            
    return B  



print(delete_duplicate([1,1,2,2,3,4,5,5]))