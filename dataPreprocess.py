import pandas as pd
import demoji
import re
from cltk.stop.classical_hindi.stops import STOPS_LIST

data = pd.read_csv("subset100.csv")

l = len(data)

dataPreProcess = pd.DataFrame(columns=["tweetPreProcessed"])

punctuationList = ['…' , ',' , '!' , '?' , '.' , '"' , ':' , "'" , ',' , '’' , '‘' , ':' , '-' , '>' , '<' , '|']

for i in range(l):
    dataTemp = data.iloc[i,1]

    dataTemp = demoji.replace(dataTemp)     #Removing Emoji
    dataTemp = re.sub(r"http\S+" , "" , dataTemp)     #Removing URL
    dataTemp = dataTemp.replace(u'\xa0', u' ')         #Changing \xa0 to space
    dataTemp = dataTemp.replace("\n" , " ")         #Changing "\n" to space
    dataTemp = re.sub(r"pic\S+" , "" , dataTemp)        #Removing Pic Links
    dataTemp = re.sub(r"#\S+" , "" , dataTemp)        #Removing Hastags
    dataTemp = re.sub(r"@\S+" , "" , dataTemp)          #Removing Mentions
    #dataTemp = re.sub(r'[^\w\s]' , '' , dataTemp)      #Removing Punctuation------This removes matras too
    dataTemp = re.sub("["u"A-Z"u"a-z"u"0-9"u"०-९""]+", '', dataTemp)
    
    for char in dataTemp:
        if char in punctuationList:
            dataTemp = dataTemp.replace(char , "")

    for word in STOPS_LIST:
        wordTemp = " " + word + " "
        dataTemp = re.sub(wordTemp , ' ' , dataTemp)
    
    dataPreProcess.loc[i] = str(dataTemp)

#print(dataPreProcess)
dataPreProcess.to_csv("subset100PreProcess.csv")