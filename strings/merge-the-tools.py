'''Consider the following:

A string, s, of length s where s=c0c1....cn-1.
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each subtring, t, consists of a contiguous block of k characters in s. 
Then, use each t to create string u such that:

The characters in u are a subsequence of the characters in t.
Any repeat occurrence of a character is removed from the string such that each character in u occurs exactly once. 
In other words, if the character at some index j in t occurs at a previous index <j in t, then 
do not include the character in string u.
Given s and k, print n/k lines where each line i denotes string u
'''
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        word = string[i:i+k]
        chars = ''
        for j in word:
            if not j in chars:
                chars = chars+j
        print(chars)
           

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)