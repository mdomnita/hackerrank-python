'''Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.
 Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. 
Here, 0 <= i <= x;0 <= j <= y;0 <= k <= z. Please use list comprehensions rather than multiple loops, as a learning exercise.'''
if __name__ == '__main__':
    x = int(input('x: '))
    y = int(input('y: '))
    z = int(input('z: '))
    n = int(input('n: '))
    
    #use because ranges are exclusive (end at <val>-1)
    x +=1
    y+=1
    z+=1
    
    #list comprehension variant 1
    # print ([i for i in range(x)])
    #list comprehension with combined loops
    # this is equivalent to nested loops
    # print ([[i,j,k] for i in range(x) for j in range(y) for k in range(z)])
    #list comprehension with combined loops and conditional at the end
    print ([[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i+j+k != n])
