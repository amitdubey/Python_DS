from typing import *
import functools
def roman_to_integer(s:str) ->int:
    T ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    return functools.reduce(lambda val,i : val+(-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]), reversed(range(len(s)-1)), T[s[-1]])

def main():
    roman =('micm')
    print(roman_to_integer(roman.upper()))

if __name__ == '__main__':
    main()
    
    