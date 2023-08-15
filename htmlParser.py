from bs4 import BeautifulSoup

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

def parse_html (filename_input, filename_output):

    with open(filename_input, 'r', encoding='utf-8') as f:

        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')

        root = soup.html
        
        with open (filename_output, 'w', encoding='utf-8') as outf:
            tags =[]
            results=[]
            
            for tag in soup.find_all("div", class_="grid_column_title"):
                tags.append(tag.text)
                
            for result in soup.find_all("div", class_="grid_column_result"):
                results.append(result.text)
                
                
            for key, value in zip(tags, results): 
                outf.write('%s %s\n' % (key, value))
