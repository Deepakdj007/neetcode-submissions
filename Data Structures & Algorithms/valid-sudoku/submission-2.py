class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(0,9):
            for c in range(0,9):
                value = board[r][c]

                if value=='.': continue

                if((r,value) in seen
                or (value,c) in seen 
                or (r//3,c//3,value) in seen
                ):
                    return False

                seen.add((r,value))
                seen.add((value,c))
                seen.add((r//3,c//3,value))

        return True