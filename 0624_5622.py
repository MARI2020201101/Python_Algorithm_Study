Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #단어를 입력받음
#단어에 해당하는 숫자를 찾음 -> 어떻게 저장하지?
#key 값이 영어이고 value가 숫자?
#해당 숫자가 걸리는 시간을 찾음.해당 숫자에 +2한 리스트?
word=input()
dictionary = {
'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,
'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,
'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,
'Y':9,'Z':9
}
t=0
for w in word:
  num = dictionary[w]
  t+= num+1
print(t)