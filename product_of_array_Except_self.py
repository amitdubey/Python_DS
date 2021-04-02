from typing import List

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
"""
    
def productofarrexceptself(array:List)->None:
    length = len(array)
    
    L,R,ANS =[0]*length,[0]*length,[0]*length
    
    L[0] =1
    
    for i in range(1,length):
        L[i] =array[i-1]*L[i-1]
    R[length-1]=1
    for i in reversed(range(length-1)):
        R[i] =array[i+1]*R[i+1]
    
    for i in range(length):
        ANS[i]=L[i]*R[i]
    return ANS

def main():
    array =[4,5,1,8,2]
    print(productofarrexceptself(array))
    
if __name__ == '__main__':
    main()