class medianofarray(object):
    def findmedian(self, ar1, ar2): 
        bigarr =sorted(ar1+ar2)
        length =len(bigarr)
        left_idx = int(length/2-1)
        right_idx= left_idx+1
        if (length%2)==0:
            median =(bigarr[left_idx]+bigarr[right_idx])/2

        else:
            idx = int(length/2)
            median =bigarr[idx]
        return median
    

def main():
    new = medianofarray()
    print("median of aray",new.findmedian([2,3,4,7,9],[25,6,1,8]))

if __name__=='__main__':
    main()
    
