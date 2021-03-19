
from typing import List
class medianofarrays:
 def arraymedian(self,num1:List[int], num2: List[int])-> float:
    num1len =len(num1)
    num2len =len(num2)
    mergedarr =[]
    for i in range(0,num1len):
        mergedarr.append(num1[i])
    for j in range(0 ,num2len):
            mergedarr.append(num2[j])
    mergelen = len(mergedarr)
    rightidx = int(mergelen/2)
    leftidx =rightidx-1
    for k in range(0,mergelen):
        mergedarr.sort()
        if (mergelen//2 ==0):
            return (mergedarr[rightidx]+mergedarr[leftidx])/2
        else:
            return  mergedarr[rightidx]
            

def main():
    num1 =[1,3]
    num2 =[2]
    s=medianofarrays()
    print(s.arraymedian(num1,num2))
        
    
if __name__ == '__main__':
    main()