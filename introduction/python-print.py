if __name__ == '__main__':
    '''Takes in a number n, returns the string 123...n'''
    n = int(input('Enter Number: '))
    
    for num in range(n):
        print(num+1,end='')
        # use the unpack iterator operator on range
        # print(*range(1,n+1),sep="")