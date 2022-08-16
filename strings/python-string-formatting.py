'''Given an integer, n, print the following values for each integer i from 1 to n:
Decimal
Octal
Hexadecimal (capitalized)
Binary'''

def print_formatted(number):
    # get length of binary (maximum length) needed for formatting 
    bin = "{0:b}".format(number)
    width = len(bin)
    # print in decimal,octal,Hexadecimal and binary base on the same line using the calculated width
    for i in range(number):
        for base in 'doXb':
            print('{0:{width}{base}}'.format(i+1, base=base, width=width), end=' ')
        # add a newline
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)