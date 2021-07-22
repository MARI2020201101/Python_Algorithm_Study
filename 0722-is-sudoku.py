Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def isSudoku(sudoku,x,y):
  numbers={1,2,3,4,5,6,7,8,9}
  sudokunum=set()
  for i in range(3):
    for j in range(3):
      sudokunum.add(sudoku[x+i][y+j])
  if numbers==sudokunum:
    return True
  else:
    return False

s=[list(map(int,input().split()))for i in range(9)]
result="NO"
for i in range(0,9,3):
  for j in range(0,9,3):
    if isSudoku(s,i,j)==False:
      break
  if i==j==6 and isSudoku(s,6,6)==True:
    result="YES"

print(result)