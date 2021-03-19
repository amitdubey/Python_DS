class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
		let a be the starting number and k be the number of terms
        a + (a + 1) + ... (a + k - 1) = N
        (2a + k - 1) * k / 2 = N
		Since (k + 2a - 1) * k = 2N, k < sqrt(2N)
        On the other hand, the above equation can be turned into ak + k(k-1)/2 
        k(k-1)/2 is basically the sum of 1 to k-1. 
		If we iterate all the way up to sqrt(2N), we could do the sum along the way. 
		As long as (N - sum) can be devided by k, that's one count. 
        '''
        sum_term = 0
        count = 0
        for i in range(int((2 * N) ** 0.5)):
            sum_term += i
            if (N - sum_term) % (i + 1) == 0:
                count += 1
                
        return count
        

def main():
    s =Solution
    print (s.solution(5))

if __name__ == '__main__':
    main()
    