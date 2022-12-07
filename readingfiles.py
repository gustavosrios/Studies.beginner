'''
file = open('\\x\\xtestando.txt')
file_data = file.read()  	#metodo para variavel para ler o conteudo do arquivo
print(file_data) #ler o conteudo
file.close() 		#metodo para finalizar a leitura e liberar quaisquer gasto computacional da leitura.

---------------------------------------
file_list = []
for i in range(10000):
    file_list.append(open('\\x\\xtestando.txt')) # teste de quantos arquivos posso abrir e colocar dentro da lista, requer poder computacional alto, resultado 8k
    print(i)

file_01 = open('\\x\\creating_new.txt', 'w')
file_01.write('This phrase its inside the creatingnew text file!')
file_01.close()

file_02 = open('\\x\\some_file.txt', 'w')
file_02.write('Hello!! You\'ve read the contents of this file 2!')
file_02.close()
file_02 = open('\\x\\some_file.txt', 'r')
file02_read = file_02.read()
print(f'{file02_read}\nThis is what was written on the file 3!')

with open('\\x\\creating_two.txt', 'w') as f:
    f.write('I can\'t imagine how many things i could do with this, file 4')
with open('\\x\\creating_two.txt', 'r') as t:
    read_file = t.read()
print(f'The content of the file is :\n{read_file}')  #posso printar a variavel fora do with

with open('\\x\\camelot.txt', 'w') as r:
    r.write('We\'re the knights of the round table\nWe dance whenever we\'re able')
with open("\\x\\camelot.txt", 'r') as song:
    print(song.read(2))
    print(song.read(3))
    print(song.read(1))
camelot_lines = []
with open('\\x\\camelot.txt') as k:
    for line in k: #para cada elemento no arquivo
        camelot_lines.append(line.strip()) #coletar o elemento append ate a quebra de linha strip \n
print(camelot_lines)
'''
def create_cast_list(filename):
    with open(filename, 'r') as r: #posso usar input ou quando chamar a funcao ja criara o arquivo com o nome
        cast_list = []
        for i in r:
            cast_list.append(i.split(',')[0]) 
            #lista,iterador devem estar na equacao, split corta o iterado ate a virgula e indexado 0

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt') #chamando a funcao para criar arquivo com esse nome
for actor in cast_list:
    print(actor)