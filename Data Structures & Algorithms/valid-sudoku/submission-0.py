class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(0,9):
            for c in range(0,9):
                value = board[r][c]

                if value=='.': continue

                if(('row',r,value) in seen
                or ('col',c,value) in seen 
                or (r//3,c//3,value) in seen
                ):
                    return False

                seen.add(('row',r,value))
                seen.add(('col',c,value))
                seen.add((r//3,c//3,value))

        return True