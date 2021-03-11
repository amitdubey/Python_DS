def fibmemoize(n,memo={1:0,2:1}):   
    if n in memo:
        return memo[n]
    else :
        memo[n]= fibmemoize(n-1,memo)+fibmemoize(n-2,memo)
    return memo[n]

def main():
    print(fibmemoize(5))

if __name__ == '__main__':
    main()
    
       
        

