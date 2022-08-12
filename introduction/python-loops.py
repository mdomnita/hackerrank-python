if __name__ == '__main__':
    '''Takes in a number n, returns the square of all numbers i < n'''
    n = int(input('Enter Number: '))
    
    for i in range(n):
        print(i * i)
        # use the power operator
        # print(i ** 2)
        # use the pow function
        # print(pow(i, 2))