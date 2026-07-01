# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.

class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        rows = [False] * m
        cols = [False] * n        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True        
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
