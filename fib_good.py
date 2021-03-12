

# def main():
#     for i in range(1, 15):
#         print("fib({}) is {}".format(i, fib(i)))





# def fib(n): 
#     a,b =1,1 
#     for i in range(1,n): 
#         a,b =b,a+b
#     return a 

def fib(n):  
    a,b =0,1
    while a < n:
        print(a,end='')
        a,b=a,a+b
    
    
    

def main(): 
    print(" value for n =12 is ", fib(12))

if __name__ =='__main__': 
    main()
    
