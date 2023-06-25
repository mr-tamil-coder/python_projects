import re
import string
frequency={}
fname=input("Enter file name")
document_text=open(fname,'r')
text_string=document_text.read().lower()
match_pattern=re.findall(r'\b[a-z]{3,15}\b',text_string)
for word in match_pattern:
    count=frequency.get(word,0)
    frequency[word]=count+1
    frequency_list=frequency.keys()
maxFrequency=0
for words in frequency_list:
    if(frequency[words]>maxFrequency):
        maxFrequency=frequency[words]
        mostRepeatedWord=words
print("THe repeated word")
print(mostRepeatedWord,maxFrequency)