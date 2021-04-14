"""find three largest numbers in an array without using sort functions
"""
def findThreeLargestNumbers(array):
    threelarg = [None,None,None]
    for num in array:
        updatelarge(threelarg,num)
    return threelarg

def updatelarge(threelarg,num):
	if threelarg[2] is None or num > threelarg[2]:
		shiftandupdate(threelarg,num,2)
	elif threelarg[1] is None or num > threelarg[1]:
		shiftandupdate(threelarg,num,1)
	elif threelarg[0] is None or num > threelarg[0]:
		shiftandupdate(threelarg,num,0)
def shiftandupdate(array,num,idx):
	for i in range(idx+1):
		if i ==idx:
			array[i] =num
		else:
			array[i]=array[i+1]
   
def main():
    array = [12,0,-1,-500,100,150,154]
    print(findThreeLargestNumbers(array))

if __name__ == '__main__':
    main()