class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m-1
        resi = None
        while l<=r:
            i = l + (r-l)//2
            if matrix[i][0] <= target <= matrix[i][n-1]:
                resi=i
                break
            if matrix[i][0] > target:
                r = i-1
            else:
                l = i+1
        if resi is None:
            return False
        l = 0
        r = n-1
        while l<=r:
            i = l + (r-l)//2
            if matrix[resi][i] == target:
                return True
            if matrix[resi][i] > target:
                r = i-1
            else:
                l = i+1
        return False