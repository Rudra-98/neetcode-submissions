class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0 
        end = len(matrix)-1
        while(start<=end):
            mid_row = (start+end)//2
            found = self.search_in_row(matrix[mid_row],target)
            if found:
                return True
            elif matrix[mid_row][0] > target:
                 end = mid_row - 1
            elif matrix[mid_row][0] < target:
                 start = mid_row + 1
        return found


    def search_in_row(self,matrix_row,target):
        i = 0 
        j = len(matrix_row)-1
        while(i<=j):
            mid = (i+j)//2
            if matrix_row[mid] == target:
                return True
            elif matrix_row[mid] > target:
                 j = mid - 1
            elif matrix_row[mid] < target:
                 i = mid + 1
        return False
        
        
        




            
        


            
        
        