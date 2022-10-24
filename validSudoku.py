class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Verifica as linhas
        for i in board:
            if not self.is_valid(i):
                return False
        
        # Verifica as colunas
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if not self.is_valid(column):
                return False
            
        # Verifica os quadrantes    
        for i in range(3):
            for j in range(3):
                quadrante = []
                for k in range(i*3, i*3+3):
                    for l in range(j*3, j*3+3):
                        quadrante.append(board[k][l])
                if not self.is_valid(quadrante):
                    return False
        return True
         
    def is_valid(self, arr):
        arr = [x for x in arr if x != '.']
        return len(arr) == len(set(arr))
