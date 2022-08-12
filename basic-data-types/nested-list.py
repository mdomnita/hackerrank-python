
'''Given the names and grades for each student in a class of n students, store them in a nested list 
and print the name(s) of any student(s) having the second lowest grade.'''
if __name__ == '__main__':
    lst = []
    # set of scores ensures each score appears once
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # add all names and scores to a list
        lst.append([name,score])
        scores.add(score)
    
    # find second lowest score
    scoresList = sorted(list(scores))
    secondLowest = scoresList[1]
    namesList = []
    
    # get list of students with second lowest score and sort it
    for score in lst:
        if score[1] == secondLowest:
            namesList.append(score[0])
    
    namesList = sorted(namesList)
    for name in namesList:
        print(name)
        
    
    