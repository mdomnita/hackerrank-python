'''Mr. Vincent works in a door mat manufacturing company. 
One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of N and M.

Output Format
Output the design pattern.'''
def generateMat(n):
    n = int(n)
    m = 3*n
    lines = []
    mid = n//2
    for i in range(mid):
        string = '.|.'*(2*i+1)
        line = string.center(m,'-')
        lines.append(line)
    string = 'WELCOME'
    line = string.center(m,'-')
    lines.append(line)
    for i in range(mid,0,-1):
        string = '.|.'*(2*(i-1)+1)
        line = string.center(m,'-')
        lines.append(line)
    return '\n'.join(lines)
        

if __name__ == '__main__':
    n = input().split()[0]
    result = generateMat(n)
    print(result)
