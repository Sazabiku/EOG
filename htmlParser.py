from bs4 import BeautifulSoup
import io


with open('downloads/Куприн_Вячеслав_Александрович_2.html', 'r', encoding='utf-8') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    root = soup.html
    
    #for tag in soup.find_all('div'):
     #   print(f'{tag.text}')
        
    #html_text = soup.find_all('div')
    
    with open ('htmltext.txt', 'w', encoding='utf-8') as txtFile:
        
        for tag in soup.find_all('div'):
            txtFile.write(f'{tag.text}')