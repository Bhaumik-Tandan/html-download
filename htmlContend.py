from urllib.request import urlopen as u
from bs4 import BeautifulSoup as b
#take input of the url, going to the page reading the page and making beutisoup object
s = b(u(input('Enter the url: ')).read(),'html.parser') 
#opening a file with dynamic name 
f = open(input('Enter the name of the file: ')+".html", "w",encoding="utf-8")
#writing into the file after converting into sting
f.write(str(s))
f.close()