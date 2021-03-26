


def reverse(x: int) -> int:
    res, remain =0 ,abs(x)
    while remain:
        res =res*10+remain%10
        remain//=10
        return -res if x<0 else res
    
        
        
if __name__ == '__main__':
    lst = 1234545
    print(reverse(lst))

