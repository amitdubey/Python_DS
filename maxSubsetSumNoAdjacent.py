def maxSubsetSumNoAdjacent(array):
    if len(array)==0:
        return 0
    elif len(array)==1:
        return array[0]
    maxsums =array[:]
    maxsums[1] =max(array[0], array[1])
    for i in range(2,len(array)):
        maxsums[i] =max(maxsums[i-1],maxsums[i-2]+array[i])
    return maxsums[-1]


def main():
    array =[12,14,17,0,25,120,180]
    print(maxSubsetSumNoAdjacent(array))

if __name__ == '__main__':
    main()