'''You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.'''
import textwrap

def wrap(string, max_width):
    # result = ''
    # for i in range(0,len(string),max_width):
    #     if i > 0:
    #         result += '\n'
    #     result += string[i:i+max_width]
    # return result
    # the textwrap function does all the work for us
    parts = textwrap.wrap(string,max_width)
    return '\n'.join(parts)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)