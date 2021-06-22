Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #과목 개수를 입력받는다
# 해당 과목 개수 만큼 점수를 입력받는다
# 최댓값을 고른다
# 해당 과목 개수만큼 과목점수를 업데이트 한다
#리스트의 평균을 구한다
n = int(input())
list = list(map(int, input().split()))
#print(list)

maxnum = max(list)
print(maxnum)
for i in range(len(list)):
  
  list[i]=list[i]/maxnum*100
#print(list)

print(sum(list)/len(list))