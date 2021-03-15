from typing import List
def rotate_matrix (square:List[List[int]])->None:
    print('before rotation',square)
    matrix_size= len(square) -1
    for i in range(len(square)//2):
        for j in range(i,matrix_size -i):
            (square[i][j],square[~j][i],square[~i][~j], square[j][~i] )= (square[~j][i],square[~i][~j], square[j][~i],square[i][j])
    return square

def main():
    matrix =[[1,2,3], 
             [3,2,1], 
             [4,5,6]]
    print('after rotation \n',rotate_matrix(matrix))
    

if __name__ == '__main__':
    main()