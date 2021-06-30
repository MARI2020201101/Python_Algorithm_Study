Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import textwrap

def wrap(string, max_width):

    if len(string)>0 and max_width > len(string):
      return string
    while max_width <= len(string):
      result = string[:max_width]
      string = string[max_width:]
      print(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)