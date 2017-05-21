import math
class Solution:
    # @param A : list of integers
    # @return an integer


    def maxArr(self, A):
        # valueIndexDict = {}
        # for i in range(0,len(A)):
        #     if A[i] in valueIndexDict:
        #         valueIndexDict[A[i]+i] = 0
        #     else:
        #         valueIndexDict[A[i]] =  i

        # SA =  sorted(valueIndexDict)
        # maxFIJ = 0
        # i = 0
        # j = len(SA)-1
        # while i<j:
        #     newI = valueIndexDict[SA[i]]
        #     newJ = valueIndexDict[SA[j]]
        #     fij = math.fabs(SA[i]-SA[j])+math.fabs(newI-newJ)
        #     maxFIJ = max(fij,maxFIJ)

        #     i = i+1
        #     j = j-1
        IPlusV = []
        IMinusV = []
        for i in range(0,len(A)):
            IPlusV.append(A[i]+i)
            IMinusV.append(A[i]-i)
        IPlusV = sorted(IPlusV)
        IMinusV = sorted(IMinusV)
        maxFIJPlus = IPlusV[len(A)-1]-IPlusV[0]
        maxFIJMinus = IMinusV[len(A)-1]-IMinusV[0]
        return int(max(maxFIJPlus,maxFIJMinus))

solution = Solution()
print solution.maxArr([10,8,6,4,10,1,2,2])
