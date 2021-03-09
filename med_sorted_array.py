
class medianofsortedarr(object):
    def findmed(self,arr1, arr2):
        final = sorted(arr1+arr2)
        totlen =len(arr1+arr2)
        left_idx = int(totlen/2 -1)
        right_idx = left_idx+1        
        if (totlen % 2) ==0:
            median = (final[left_idx]+final[right_idx]/2)
            
        else: 
            idx =totlen/2
            median =final[idx]
        return median

def main(): 
    med =medianofsortedarr()
    print("value of median is ", med.findmed([1,2,5,6,7,8],[9,4,3,11]))

if __name__ == '__main__':
    main()
    
            