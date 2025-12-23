# text warp
import textwrap
def wrap(string, max_width):
    warpped=textwrap.fill(string,max_width)
    return warpped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)