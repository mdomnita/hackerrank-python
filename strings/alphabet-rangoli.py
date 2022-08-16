'''You are given an integer, n. Your task is to print an alphabet rangoli of size n. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

The center of the rangoli has the first alphabet letter a, and the boundary has the nth alphabet letter (in alphabetical order).
'''
def print_rangoli(size):
    # your code goes here
    size = int(size)
    letters = 'abcdefghijklmnopqrstuvwxyz'[:size]
    res = ''
    # letters length + letters in reverse + '-' to join them
    length = (size * 2 - 1) + (size * 2 - 2)
    for l in range(size-1,-1,-1):
        content = [x for x in letters[size+1:l:-1]]
        content += [x for x in letters[l:size]]
        center = '-'.join(content)
        res += '-'*((length - len(center))//2) + center + '-'*((length - len(center))//2) + '\n'
    for l in range(1,size):
        content = [x for x in letters[size+1:l:-1]]
        content += [x for x in letters[l:size]]
        center = '-'.join(content)
        res += '-'*((length - len(center))//2) + center + '-'*((length - len(center))//2)+''     
        res += '\n' if l < size-1 else ''
    print(res)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)