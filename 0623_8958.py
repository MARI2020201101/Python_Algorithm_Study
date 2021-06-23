Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #정답 줄의 개수를 입력받는다
#정답을 입력받는다 
#정답을 채점하는 함수에 넣는다
#결과를 출력한다
N=int(input())
list=[""]*N
for i in range(N):
  list[i] = input()
print(list)
#정답을 채점하는 함수
#해당 string을 한개씩 검사. 이전노드가 O였으면->+1
#아니면 그냥 1
# 전체 합계 
def go(n,S):
  cnt=0
  prev=''
  curr=''
  result=[0]*n
  cnts=[0]*1000
  for i in range(len(S)):
    S=S[i]
    print(S)
    for s in S:
      curr=s
      print(curr)
      if prev=='' and curr=='O':
        cnt=1
      if prev=='O' and curr=='O':
        cnt+=1
      if prev=='X' and curr=='O':
        cnt=1
      else:
        cnt=0
      prev=s
      cnts.append(cnt)
    result[i]=sum(cnts)
  return result 

print(go(N,list))