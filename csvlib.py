import csv
#UnicodeDecodeError common error, 'charmap' cant decode it
#encoding eh capaz de ler ou nao ler diferentes tipos de caracteres especiais,
# neste caso @ pois no arquivo csv possuem emails, 
#aways take a look on what type of data is on the csv file, like spanish data has special characters etc
#open file
data = open('example.csv',encoding='utf-8') #can read utf-8 characters
# csv.reader
csv_data = csv.reader(data)
#reformat it into a python object list of lists
data_lines = list(csv_data)
data_lines[0:2] # geralmente  data_lines[0] sao os column names
#len(data_lines)



#data_lines[10][3] 
#grab email
all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])
print(len(all_emails))

all_emails = []
i = 1
while i <= len(data_lines[1:]):
    all_emails.append(data_lines[i][3])
    i+=1
#print(all_emails)
print(len(all_emails))


full_names = []
for line in data_lines[1:]:
    full_names.append(line[1]+' '+line[2])
print(full_names)

#creating new csv file
file_to_output = open('to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',') # for TabSV files use delimiter='\t' 
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3','4',],['5','6','7']])
file_to_output.close()
#reading the new created file
open_save = open('to_save_file.csv')
csv_writer_read = csv.reader(open_save)
data_lines02 = list(csv_writer_read)
data_lines02
open_save.close()