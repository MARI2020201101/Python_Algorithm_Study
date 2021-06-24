Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #한줄 계산하기
# input 학생의 숫자
# list에 저장, avg를 구한다. sum(list)/next
# if 만약에 avg보다 크다면
# largerThanAvg = [] 리스트에 +1 한다.
# sum(largerThanAvg) / len(largerThanAvg) 한후에 소수점 셋째자리까지 출력하기 round 함수.

for i in range(int(input())):
  #n=int(input().split())

  lists=list(map(int,input().split()))
  n=lists[0]
  lists=lists[1:]
  avg = sum(lists)/n
  largerThanAvg=[0]*n

  for i in range(n):
    if lists[i]>avg:
      largerThanAvg[i]=1
  print(round(sum(largerThanAvg)/len(largerThanAvg)*100,3))
