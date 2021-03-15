import random
def random_sampling(k,a):
    print(a)
    for i in range(k):
        r =random.randint(i,len(a) -1)
        a[i],a[r] =a[r],a[i]
    return a

def main():
    lst=[1,4,5,68,89,55,12,15,19]
    print('random number', random_sampling(3,lst))
    
if __name__ == '__main__':
    main()