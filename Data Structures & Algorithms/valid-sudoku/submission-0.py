class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        flag=True

        def helper(list) -> bool:
            d=defaultdict(bool)
            for i in range(len(list)):
                if list[i]==".":
                    continue
                if d[list[i]]:
                    return False
                d[list[i]]=True
            d.clear()
            return True

        for i in range(9):
            if not helper(board[i]):
                flag=False
                break
            if not helper([board[k][i] for k in range(9)]):
                flag=False
                break
        if flag:
            for i in range(3):
                for j in range(3):
                    if not helper(board[3*i][3*j:3*j+3]+board[3*i+1][3*j:3*j+3]+board[3*i+2][3*j:3*j+3]):
                        flag=False
                        break
                if flag==False:
                    break
        return flag