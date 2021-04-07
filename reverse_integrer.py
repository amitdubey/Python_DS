
def solution(N):
    reverse =0
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        elif enable_print == 1:
            reverse =(reverse*10) +(N%10)
            
        N = int(N // 10)
    return print(reverse)

def main():
    solution(54321)

if __name__ == '__main__':
    main()
    