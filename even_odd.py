def even_odd(a):
    print('new list is',a)
    next_even, next_odd =0, len(a)-1
    while next_even < next_odd: 
        if a[next_even]% 2==0:
            next_even +=1
        else:
            a[next_odd], a[next_even] =a[next_even],a[next_odd]
            next_odd -=1
            
    return print(next_even,next_odd)

def main():
    lst =[1,2,3,4,4,5,5,5,7,8,9,11,13,14,16]
    even_odd(list(set(lst)))
    
    
    
if __name__ == '__main__':
    main()
    