from collections import Counter,defaultdict,namedtuple
mixed_list = [2.44,'a totally randomically list',2,2,5,6,6,6,2.44,
              True,False,True,True,False,True,False,'eeeeddddffgghrrrr']
i = 0
while i < len(mixed_list):
    try: 
        #print(Counter(mixed_list[i]))
        i += 1
        continue
    except:
        i += 1
        continue

sentence = 'Do you mind do you already have do you only have do you please do me a favor'
#print(Counter(sentence.lower().split()))

letters = 'aasddsddssdadssdsderrerererereerddslll'
c = Counter(letters)
list(c)
print(c.most_common())
