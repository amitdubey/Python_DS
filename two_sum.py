

def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)-1) :
        firstsum =array[i]
        for j in range(i+1, len(array)):
            secondsum =array[j]
            if firstsum+secondsum==targetSum:
             return [firstsum,secondsum]
    return []
		
  
def main() :   
      arr =[1,3,5,6,4,2,7]
      targetsum =10
      return print(twoNumberSum(arr,targetsum))


if __name__ == '__main__':     
    main()
    