from operator import truediv


def is_leap(year):
    '''returns a boolean value, True if a year is leap, False otherwise'''
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    # if year % 400 == 0:
    #     return True
    # if year % 100 == 0:
    #     return False
    # if year % 4 == 0:
    #     return True
    # return False
    return False

if __name__ == '__main__':
    year = int(input('Enter year: '))
    print(is_leap(year))