import time
def getMatrixDiagonal(matrix):
    result = ""
    visited = {}
    isUp = True
    i = 0
    j = 0
    visited
    while(not(len(visited.keys()) == len(matrix)*len(matrix))):
        if(isUp):
            while(i>=0 and j<len(matrix)):
                print i,j

                gap = " "
                if(i == 0 and j == 0):
                    gap = ""
                result = '{0}{1}{2}'.format(result,gap,matrix[i][j])
                visited['{0}{1}'.format(i,j)]=True
                gap = " "
                i = i-1
                j = j+1
                if(i<0 and j<len(matrix)):
                    i = 0
                    break
                elif(i>=0 and j>=len(matrix)):
                    j = len(matrix)-1
                    break
                elif(i<0 and j>=len(matrix)):
                    i = 1
                    j = len(matrix)-1
                    break
                    # visited.append(True)

                # print result
        else:
            while(i<len(matrix) and j>=0):
                gap = " "
                result = '{0}{1}{2}'.format(result,gap,matrix[i][j])
                visited['{0}{1}'.format(i,j)]=True
                gap = " "
                i = i+1
                j = j-1
                if(j<0 and i<len(matrix)):
                    j=0
                    break
                elif(j>=0 and i>=len(matrix)):
                    i = len(matrix)-1
                    if(visited.has_key('{0}{1}'.format(i,j))):
                        if(j+2<len(matrix)):
                            j = j+2
                    break
                elif(j<0 and i>len(matrix)):
                    j = 0
                    i = len(matrix)-1
                    break

                    #  visited.append(True)
                # print result
        isUp = not(isUp)
        print result
        time.sleep(1)
        print isUp
    return result
default_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print getMatrixDiagonal(default_matrix)
