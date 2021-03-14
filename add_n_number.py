def addnum(num):      
    total =0
    i=0
    while i <=num: 
        total=total+i 
        i+=1
    return total


def main():
    print(addnum(10))


if __name__ == '__main__':
    main()