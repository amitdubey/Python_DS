def findletterfreq(st,s)-> int:
    count= 0
    dict ={}
    for i in st:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] =1
    return dict
        
    
			

def main():
    array ='missisippi'
    str ='i'
    print(findletterfreq(array,str))

if __name__=='__main__':
    main()
    