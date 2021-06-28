Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    
    arr.sort(reverse=True)
 
    
    target = 0;
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
             target = i+1
             break;
             
    
    print(arr[target])