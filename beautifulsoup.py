import requests
import bs4
result = requests.get('https://en.wikipedia.org/wiki/Jonas_Salk')
#type(result)
#result.text
soup = bs4.BeautifulSoup(result.text,'lxml') #lxml para buscar no texto onde estao as classes
site_title = soup.select('title')[0].getText()
print(site_title)
site_paragraphs = soup.select('p')
print(type(site_paragraphs)) #beautiful soup object, not a string, has bs4 methods func
print(type(site_paragraphs[0]))



#find jonas salk table of contents
table_oc = bs4.BeautifulSoup(result.text,'lxml')
item_list = table_oc.select('.toctext')
table_oc.select('.toctext')[1].getText()
for item in table_oc.select('.toctext'):
    print(item.getText())


# request an image from jonas salk
import requests
import bs4
re_quest = requests.get('https://en.wikipedia.org/wiki/Jonas_Salk')
soup_01 = bs4.BeautifulSoup(re_quest.text,'lxml')   #cria objeto beautiful soup com o site.text
download_img = soup_01.select('.thumbimage')[0] #.class thumbimage
type(download_img)
download_img['src']
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Roosevelt_OConnor.jpg/220px-Roosevelt_OConnor.jpg')
image_link.content
f = open('jonasimg.jpg','wb') #wb write binary mode, imagelink.content has binary information of the img
f.write(image_link.content)
f.close()


#pick up every book from https://books.toscrape.com/catalogue/page-1.html that has 2 star rating
#len(all_books) #site showing 1-20 results, we have inside two_star all the books on .product_pod
#example = all_books[0] #example se torna objeto especial TAG 
#'star-rating Two' in str(example) susceptible to errors busca via palavra na string(example)
import requests
import bs4
book_list = []
i = 1
while i <= 50:
    request_url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    request = requests.get(request_url)
    soup = bs4.BeautifulSoup(request.text,'lxml')
    all_books = soup.select('.product_pod')
    for book in all_books:
        if book.select('.star-rating.One') != []:
            book_list.append(book.select('a')[1]['title'])
    i+=1
print(book_list)
print(f'{len(book_list)} books found.')
with open('2-starbooks.txt','w') as f:
    f.write(book_list)

import requests
import bs4
authors = set()
valid_page = True
page_number = 1
while valid_page:
    main_url = requests.get(f'http://quotes.toscrape.com/page/{page_number}/')
    if 'No quotes found!' in main_url.text:
        valid_page = False
    soup = bs4.BeautifulSoup(main_url.text,'lxml')
    for name in soup.select('.author'): #soup.select retorna a lista dos autores
        authors.add(name.text) #iterador.text ja busca e mostra o nome
    page_number+=1 
print(authors) 
print(len(authors)) 

import requests
import bs4
top_tags = []
request_url = requests.get('http://quotes.toscrape.com/')
request_url.text
soup = bs4.BeautifulSoup(request_url.text,'lxml')
for tag in soup.select('.tag-item'):
    print(tag.text)

import requests
import bs4
quotes_list = []
request_url = requests.get('http://quotes.toscrape.com/')
request_url.text
soup = bs4.BeautifulSoup(request_url.text,'lxml')
for quote in soup.select('.text'):
    quotes_list.append(quote.text)
for quote in quotes_list:
    print(quote)