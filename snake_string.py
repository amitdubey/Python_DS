
def snake_string(s:str)->str:
    result=[]
    for i in range(1,len(s),4):
        result.append(s[i])
    for i in range(0,len(s),2):
        result.append(s[i])
    for i in range(3,len(s),4):
        result.append(s[i])
    return ''.join(result)

def snake_string_two(s:str)-> str:
    return s[1::4]+s[::2]+s[3::4]

def main():
    snake='getyourfactright'
    print(snake_string(snake))
    print(snake_string_two(snake))
    

    
if __name__ == '__main__':
    main()
    