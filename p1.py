# class stacksample : 
#     def __init__(self,limit=10) :
#         self.limit=limit
#         self.array=[]
#     def IsEmpty(self) :
#         return len(self.array)==0
#     def Size(self) :
#         return (len(self.array))
#     def IsFull(self) :
#         return (len(self.array)==self.limit) 
#     def Peek(self)  :
#         if self.IsEmpty() : 
#             return None
#         return self.array[-1]
#     def push(self,data) :
#         if self.IsFull() :
#             self.resize() 
#             raise Exception ("Stack underflow") 
#         self.array.append(data)
#p2
# def factorial(num) : 
#     if num < 0 : 
#         return 0
#     elif num ==0 or num == 1 : return 1
#     else :
#         count =1 
#         while (num>1) : 
#                 count*=num 
#                 num-= 1 
#         return count 
#p3 fibonacci
# fibarray = [0,1]
# def fibonacci(n) :
#     if (n<=0) : 
#         return "inccorect number"
#     elif n<= len(fibarray) : 
#         return fibarray[n-1]
#     else : 
#         temp = fibonacci(n-1)+fibonacci(n-2)
#         fibarray.append(temp)
#         return temp

# def fibnew (n) : 
#     a=0
#     b =1 
#     if (n<=0 ) : 
#         print ("Incorrect input")
#     elif n==1 : 
#         return b 
#     else : 
#         for i in range (2,n) : 
#             c = a +b
#             a =b 
#             b =c 
#         return b 
    
# print all even number 

list1 = [10, 21, 4, 45, 66, 93] 
  
# iterating each number in list 
# for num in list1: 
      
#     # checking condition 
#     if num % 2 == 0: 
#        print(num, end = " ") 
# for num in list1: 
#     if num % 2 != 0 : 
#         print( num,end =" ")
        
# import Tkinter
# top = Tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()


#p4 reverse list 
def reverlist (lst) :  
    newlst = lst[::-1]
    return newlst 


if __name__ == '__main__':
    # newstack =stacksample(5)
    # newstack.push(10)
    # newstack.push(11)
    # newstack.push(16)
    # newstack.push(21)
    # print(newstack.Peek())
    # print(newstack.Size())
   
   #p1
    # num1 =10
    # num2 =20
    # add =num1+num2
    
    # print("sum of {0} and {1} is {2}".format(num1,num2,add))
    #p2 
    
    # num =5 
    # print("factorial of num",num,"is",factorial(num))
    
    #p3
     #print(fibonacci(1))
     #print(fibnew(10))
    
   print( reverlist(list1))