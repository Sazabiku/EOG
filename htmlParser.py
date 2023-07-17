from bs4 import BeautifulSoup
import io


with open('downloads/Куприн_Вячеслав_Александрович_2.html', 'r', encoding='utf-8') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    root = soup.html

    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)
    
    root_childs = [e.name for e in root.descendants if e.name is not None]
    print(root_childs)
    
    #for tag in soup.find_all('div'):
     #   print(f'{tag.text}')
        
    #html_text = soup.find_all('div')
    
    with open ('htmltext.txt', 'w', encoding='utf-8') as txtFile:
        
        for tag in soup.find_all('div'):
            txtFile.write(f'{tag.text}')