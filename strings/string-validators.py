'''You are given a string S.
Your task is to find out if the string  contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.'''
if __name__ == '__main__':
    s = input()
    # check all validators one by one
    found = {
        'alnum':False,
        'alpha':False,
        'digit':False,
        'lower':False,
        'upper':False
    }
    for i in s:
        if i.isalnum():
            found['alnum'] = True
        if i.isalpha():
            found['alpha'] = True
        if i.isdigit():
            found['digit'] = True
        if i.islower():
            found['lower'] = True
        if i.isupper():
            found['upper'] = True
            
    print(found['alnum'])
    print(found['alpha'])
    print(found['digit'])
    print(found['lower'])
    print(found['upper'])
        