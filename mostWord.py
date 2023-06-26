import re
import string
frequency={}
fname='data1.txt'
document_text=open(fname,'r')
text_string=document_text.read().lower()
match_pattern=re.findall(r'\b[a-z]{3,15}\b',text_string)
for word in match_pattern:
    count=frequency.get(word,0)
    print(count)
    print(frequency[word])
    frequency[word]=count+1
    frequency_list=frequency.keys()
    ''' 
    frequency = {'apple': 5, 'banana': 2, 'orange': 3}
    dict_keys(['apple', 'banana', 'orange'])

    
    '''
maxFrequency=0
for words in frequency_list:
    if(frequency[words]>maxFrequency):
        maxFrequency=frequency[words]
        mostRepeatedWord=words
print("THe repeated word")
print(mostRepeatedWord,maxFrequency)"""