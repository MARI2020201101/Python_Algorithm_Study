Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
KeyboardInterrupt
>>> def swap_case(s):
    result = ""
    for ss in s:
        if ss.islower():
            result+=ss.upper()
        else:
            result+=ss.lower()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)