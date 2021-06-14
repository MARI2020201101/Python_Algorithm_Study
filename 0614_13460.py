Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> N,M=map(int,input().split())
box =[[0]*N]
rx,ry=0,0
bx,by=0,0
hx,hy=0,0


for n in range(N):
  for m in range(M):
    if input()=='R':
      rx=n
      ry=m
    if input()=='B':
      bx=n
      by=m
    if input()=='O':
      hx=n
      hx=m
    box[n][m]=input()

move = [[-1,0],[0,1],[1,0],[0,-1]]
cnt=0

for k in range(len(move)):
  rx=n
  ry=m
  rx+=move[k][0]
  ry+=move[k][1]
  bx+=move[k][0]
  by+=move[k][1]
  

  if rx<0 or rx>N-1 or ry<0 or ry>N+1:
    continue

  if box[rx][ry]=="#" or box[rx][ry]=="B":
    continue

  if rx==hx and ry==hy and bx!=hx and by!=hy and cnt<=10:
    print(cnt)
    break

  if cnt>10:
    print(-1)
    break

  cnt+=1

SyntaxError: multiple statements found while compiling a single statement
>>> 