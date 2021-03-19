class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [""]*numRows
        i = 0
        direct_way = False
        for symbol in s:
            ans[i] = ans[i]+symbol
            if (i == 0) | (i == (numRows-1)):
                direct_way = not direct_way
            if direct_way:
                i += 1
            else:
                i -= 1
        return "".join(ans)


def main():
    s =Solution()
    print(s.convert("PAYPALHASHIREDME",4))

if __name__ == '__main__':
    main()
    