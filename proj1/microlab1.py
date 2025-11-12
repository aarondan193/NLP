import sys
import re

number_of_args = len(sys.argv)
theString= ""
date_time_strings = ["tomorrow", "today", "yesterday"]
time_related_prepositions = ["at", "on", "to"]

for i in range(1, number_of_args):
    token = sys.argv[i]
    added = False
    if (i < number_of_args - 1):
        nextToken = sys.argv[i+1]
        #print(i)
        #print(number_of_args)
        #print(token)
        #print(nextToken)


    
    
    for ele in date_time_strings:
        if (ele == token):
            theString = theString + " _" + token
            for time_preposition in time_related_prepositions:
                if (time_preposition == nextToken):
                    theString = theString + token
                    added = True
            if(time_preposition != nextToken and not added):
                theString = theString + "_"
                added = True
    if (not added):
        theString = theString + " " + token
           
                    
print(theString)
        

    #theString = theString + " " + sys.argv[i]

#The assignment is to highlight the time and date mentioned in the SMS. You will "highlight" the data and time by 
# placing data and time between two underscores ('_') if they are part of the same expression, including any time-related 
# preposition between them (e.g., "at", "on"). Make sure you account for the names for the time of the day (afternoon, morning, etc.), 
# days, weeks, months, years, and proximal or relative qualifiers (tomorrow, next day, last week


#for ele in date_time_strings:
#    result = re.search(ele, theString)
#    try:
#        print(ele)
#        theString = re.sub(ele," _" + ele + "_ ",theString)
#        print("here")
#    except:
#        pass


