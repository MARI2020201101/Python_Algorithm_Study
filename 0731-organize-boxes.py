Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def organize(boxes):
  k=len(boxes)-1
  boxes[0]+=1
  boxes[k]-=1
  boxes.sort()
  return boxes



n=int(input())
boxes = list(map(int,input().split()))
m=int(input())

boxes.sort()

for i in range(m):
  boxes=organize(boxes)
print(boxes[n-1]-boxes[0])