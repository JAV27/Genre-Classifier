#This file was used for stripping the brackets [] from the data set 
#No need to run this file again. The new data set is saved in new_data.csv

import pandas as pd

data = pd.read_csv("data.csv", index_col="index")
counter = 0
for index in data.index:
    lyric = data.loc[index, 'Lyric']
    allInd = []

    begIndex = 0
    endIndex = 0
    for i, letter in enumerate(lyric):
        if letter == '[':
            begIndex = i

            for j, let in enumerate(lyric[i:]):
                if let == ']':
                    endIndex = j+i+1
                    allInd = allInd + [(begIndex, endIndex)]
                    begIndex = 0
                    endIndex = 0
                    break
        
    
    for i in allInd:
        lyric = lyric[:i[0]] + lyric[i[1]:]
    
    data.loc[index,'Lyric'] = lyric

    print(index)


data.to_csv("new_data.csv")

