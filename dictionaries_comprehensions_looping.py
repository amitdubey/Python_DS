knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key, value in knights.items():
    print(key, value)
    
#using enumerate function
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


#looping with two or more dictainaries
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
#reversing the dict
for i in reversed(range(1, 10, 2)):
    print(i)
#sorting and remove duplicate using set
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(12)