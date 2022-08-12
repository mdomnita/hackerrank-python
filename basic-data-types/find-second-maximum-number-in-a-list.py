'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.'''
if __name__ == '__main__':
    # Find the Runner-Up Score!
    n = int(input())
    arr = map(int, input().split())
    
    # sort the array
    sort = sorted(arr)
    max = sort.pop()
    # if I have more elements equal to the max value I remove all of them
    while sort[-1] == max:
        sort.pop()
    # last element of the sorted list will be the second maximum (I removed all maximums)
    print (sort[-1])
