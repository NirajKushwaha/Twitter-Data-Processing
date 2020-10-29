import pandas as pd
import numpy as np
import re
from cltk.tokenize.word import WordTokenizer
from cltk.stop.classical_hindi.stops import STOPS_LIST

data = pd.read_csv("subset100PreProcess.csv")

l = len(data)

tokenizer = WordTokenizer('sanskrit')

for i in range(l):
    dataTemp = data.iloc[i,1]

    for word in STOPS_LIST:
        wordTemp = " " + word + " "
        dataTemp = re.sub(wordTemp , ' ' , dataTemp)

    tokenizedSentenceList = tokenizer.tokenize(dataTemp)

    print(tokenizedSentenceList)



