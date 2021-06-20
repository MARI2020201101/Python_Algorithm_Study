Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
arr = []
for i in range(n):
  arr.append(int(input()))

avg = sum(arr)//len(arr)
arr_=sorted(arr)
mid = arr_[len(arr_)//2+1]
rang = max(arr)-min(arr)
cnt = 0
cnt_list = {}
for a in arr:
  if a in cnt_list:
    cnt_list[a]+=1
  else : cnt_list[a]=1

cnt_list2=list(sorted(cnt_list.items(), key=lambda item: item[1] ,reverse=True))
cnt_list3 = sorted(cnt_list2)
print(*cnt_list2)
print(*cnt_list3)
pk=cnt_list2[0]
print(pk)
#pv=cnt_list2.items()[0]
pk2=cnt_list2[1]
print(pk2)
pv2=cnt_list2.items()[1]

if pv==pv2:
  cnt = pv2
else:
  cnt = pv

print(avg)
print(mid)
print(cnt)
print(rang)

