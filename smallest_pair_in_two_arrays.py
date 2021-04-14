""" find the smallest pair of numbers from two non empty array
"""
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxone =0
    idxtwo =0
    smallest =float("inf")
    current =float("inf")
    smallestpair =[]
    while idxone < len(arrayOne) and idxtwo < len(arrayTwo):
        firstnum = arrayOne[idxone]
        secondnum =arrayTwo[idxtwo]
        if firstnum < secondnum:
            current = secondnum -firstnum
            idxone+=1
        elif secondnum < firstnum:
            current =firstnum -secondnum
            idxtwo +=1
        else:
            return [firstnum,secondnum]
        if smallest > current:
            smallest =current
            smallestpair = [firstnum,secondnum]
    return smallestpair


def main():
    arrayOne =[-1,5,10,20,28,3]
    arrayTwo=[26,134,135,15,17]
    print(smallestDifference(arrayOne,arrayTwo))

if __name__ == '__main__':
    main()
    