from bs4 import BeautifulSoup

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


with open('downloads/Куприн_Вячеслав_Александрович_2.html', 'r', encoding='utf-8') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    root = soup.html
    
    #for tag in soup.find_all('div'):
     #   print(f'{tag.text}')
        
    #html_text = soup.find_all('div')
    
    with open ('htmltext.txt', 'w', encoding='utf-8') as txtFile:
        
        
        #"class": "grid_column_title"
        
        tags =[]
        results=[]
        
        for tag in soup.find_all("div", class_="grid_column_title"):
            tags.append(tag.text)
            
        for result in soup.find_all("div", class_="grid_column_result"):
            results.append(result.text)
            
            
        for key, value in zip(tags, results): 
            txtFile.write('%s %s\n' % (key, value))
