import argparse
import re

date_time_strings = ["january","february","march","april","may","june","july","august","september","october","november","december","yesterday", "tomorrow", "today", "1","2","3","4","5","6","7","8","9","10","11","12",
                     "afternoon","daytime","dusk","evening","midnight","morning","night","nighttime","noon","sunrise","sunset","monday","tuesday","wednesday","thursday","friday","saturday","sunday","days", "weeks", 
                     "months", "years","o'clock","next","week","month","year",""]

time_related_prepositions = ["at", "on", "in"]

parser = argparse.ArgumentParser()
parser.add_argument("sentence")

args = parser.parse_args()
inputSent = args.sentence
#matches = re.findall(r"\b[012]\d:\d\d\b",inputSent)
matches = re.findall(r"[012]\d:\d\d",inputSent)
matches = matches + re.findall(r"\d:\d\d",inputSent)

#matches = re.findall(r"\b\d:\d\d\b",inputSent)
#matches = matches + re.findall(r"\b[123]\d?[s][t]\b",inputSent)
#matches = matches + re.findall(r"\b[123]\d?[t][h]\b",inputSent)
#matches = matches + re.findall(r"\b[123]\d?[t][h]\b",inputSent)

for match in matches:
    print(match)
    #inputSent = re.sub(match,"_" + match + "_", inputSent)


for word in inputSent:
    trpMatches = re.findall(r"_ " + word + " _",inputSent)

for match in trpMatches:
    print(trpMatches)
    inputSent = re.sub(trpMatches,"_" + trpMatches + "_", inputSent)

print(inputSent)


#for dts in date_time_strings:
    #searchStr = dts
#    result = re.search(r"\b[012]?\d:\d\d\b",args.sentence)
#    if result:
#        print(result)