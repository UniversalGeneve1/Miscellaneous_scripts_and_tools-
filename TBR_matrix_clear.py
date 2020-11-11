"""
Given a m * n matrix, if an element is 0, set its entire row and column to 0.

!*! Do it in place !*!

for the exercise, use this matrix:
[[1, 1, 1, 0],
 [1, 1, 1, 0],
 [1, 1, 0, 0],
 [1, 0, 0, 0]]
"""

def mat_print(M):
  for row in M:
    print(row)
  print("------------")

def mat_cleaner(M):
  for r in range(0, len(M)): #row iteration
    for c in range(0, len(M[0])): #column iteration
      if M[r][c] == 0:
          #col iter:
          for ci in range(0, len(M[0])):
            M[r][ci] = 0
            mat_print(M)
          #row iter:
          for ri in range(0, len(M)):
            M[ri][c] = 0
            mat_print(M)

      
test = [[1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0]]

#call:
mat_cleaner(test)
"""
NOTES:
* works, but slow.
* play around with the diagonals maybe? i'll revise in the future.
""""