class Solution:
    def findValue(self, lis: list, target: int):
        start=0
        n=len(lis)
        end=n-1
        mid=(end+start)//2
        ans=False
        while(start<=end and start>=0 and end<=n-1):
            mid=(end+start)//2
            if(target<lis[mid]):
                end=mid-1
            elif(target>lis[mid]):
                start=mid+1
            elif(target==lis[mid]):
                ans=True
                break
        return ans

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        start=0
        end=m-1
        ans=False
        while(start<=end and start>=0 and end<=m-1):
            mid=(end+start)//2
            if(target<matrix[mid][0]):
                end=mid-1
            elif(target>matrix[mid][n-1]):
                start=mid+1
            else:
                ans=self.findValue(matrix[mid],target)
                break
        return ans