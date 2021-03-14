def nonConstructibleChange(coins):
    coins.sort()
    currentchangecreated =0
    for coin in coins:
        if coin > currentchangecreated+1:
            return currentchangecreated+1
	
        currentchangecreated += coin
    return currentchangecreated+1


def main(): 
    coins=[5, 7, 1, 1, 2, 3, 22]
    print('current min change or non contructible change is ', nonConstructibleChange(coins))

if __name__ == '__main__':
    main()