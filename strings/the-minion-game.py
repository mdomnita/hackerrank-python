'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.'''
def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            # Kevin gets points for all substring combinations from here to the end
            kevin += len(string)-i
        else:
            # Stuart gets points for all substring combinations from here to the end
            stuart += len(string)-i
    if kevin > stuart:
        print ('Kevin',kevin)
    elif stuart > kevin:
        print('Stuart',stuart)
    else:
        print('Draw')    

if __name__ == '__main__':
    s = input()
    minion_game(s)