import sys
import re

#aaron daniels
#COSC524
#microlab 1

#The assignment is to highlight the time and date mentioned in the SMS. You will "highlight" the data and time by 
# placing data and time between two underscores ('_') if they are part of the same expression, including any time-related 
# preposition between them (e.g., "at", "on"). Make sure you account for the names for the time of the day (afternoon, morning, etc.), 
# days, weeks, months, years, and proximal or relative qualifiers (tomorrow, next day, last week

number_of_args = len(sys.argv)
theString= ""
date_time_strings = ["january","february","march","april","may","june","july","august","september","october","november","december","yesterday", "tomorrow", "today", "1","2","3","4","5","6","7","8","9","10","11","12",
                     "afternoon","daytime","dusk","evening","midnight","morning","night","nighttime","noon","sunrise","sunset","monday","tuesday","wednesday","thursday","friday","saturday","sunday","days", "weeks", 
                     "months", "years","o'clock","1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd",
                     "24th","25th","26th","27th","28th""29th","30th","31st"]
time_related_prepositions = ["at", "on", "in"]
lastToken = "_"

list_of_args = sys.argv[1].split()
number_of_args = len(list_of_args)

for i in range(0, number_of_args):
    punc = ""
    token = list_of_args[i]
    if(token[-1] == '.' or token[-1] == '!' or token[-1] == '?' or token[-1] == '.'):
        punc = token[-1]

        token = token[:-1]
    for dts in date_time_strings:
        if (dts == token.lower()):
            token = "_" + token + "_" + punc

    for trp in time_related_prepositions:
        if (trp == token.lower())and(lastToken[-1] == "_"):
            token = "_" + token + "_"

    lastToken = token
    theString = theString + token + " "



theString = re.sub("_ _"," ",theString)

print(theString)
        

 
