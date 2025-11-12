import re 


match = re.search(r'portal', 'GeeksforGeeks: A computer science	portal for geeks') 
print(match) 
print(match.group()) 

print('Start Index:', match.start()) 
print('End Index:', match.end()) 

print(re.findall(r'[Gg]eeks', 'GeeksforGeeks: A computer science portal for geeks'))

print('Range',re.search(r'[a-zA-Z]', 'x'))

print(re.search(r'[^a-z]', 'c'))

print(re.search(r'G[^e]', 'Geeks')) 


print('Geeks:', re.search(r'\bGeeks\b', 'Geeks')) 
print('GeeksforGeeks:', re.search(r'\bGeeks\b', 'GeeksforGeeks')) 

print('Color',re.search(r'colou?r', 'color'))  
print('Colour',re.search(r'colou?r', 'colour'))


print('Date{mm-dd-yyyy}:', re.search(r'[\d]{2}-[\d]{2}-[\d]{4}', '18-08-2020')) 

print('Three Digit:', re.search(r'[\d]{3,4}', '189')) 
print('Four Digit:', re.search(r'[\d]{3,4}', '2145')) 


print(re.search(r'[\d]{1,}','5th Floor, A-118, Sector-136, Noida, Uttar Pradesh - 201305'))

print(re.search(r'[\d]+', '5th Floor, A-118, Sector-136, Noida, Uttar Pradesh - 201305'))

grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})', '26-08-2020') 
print(grp) 

grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020') 
print(grp.groups())

grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020') 
print(grp.group(3))

match = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})', 
                  '26-08-2020') 
print(match.group('mm'))

match = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})', 
                  '26-08-2020') 
print(match.groupdict()) 

print(re.search(r'[^a-z]', 'c'))

print(re.search(r'G[^e]', 'Geeks')) 

print('negation:', re.search(r'n[^e]', 'Python')) 
print('lookahead:', re.search(r'n(?!e)', 'Python')) 