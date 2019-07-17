import re, random
openWordNote = open('wordlist.md', 'r')
practiceLise = []
listNumber = 2
for writeTextToList in openWordNote:
    practiceLise.append(writeTextToList.strip())
  
wordClearList = []
for i in practiceLise:
    if listNumber >= len(practiceLise):
        break
    if listNumber % 2 == 0:
        wordClearList.append(practiceLise[listNumber])
        listNumber = listNumber + 2
    else:
        break
