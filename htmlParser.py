from bs4 import BeautifulSoup
import os, errno
#need to pip install lxml


def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT: 
            raise 


def parse_html (input_file, output_file):

    with open(input_file, 'r', encoding='utf-8') as f:

        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')

        root = soup.html

        print('complete')
        print(root)
        
        with open (output_file, 'a', encoding='utf-8') as outf:
            tags =[]
            results=[]
            
            for tag in root.find_all("div", class_="grid_column_title"):
                tags.append(tag.text)
                
            for result in root.find_all("div", class_="grid_column_result"):
                results.append(result.text)
                
                
            for key, value in zip(tags, results): 
                outf.write('%s %s\n' % (key, value))


def read_txt (input_file):
    with open (input_file, 'r', encoding='utf-8') as f:
        txt_data = f.read()
        output_array = txt_data.split('\n')
    return output_array


if __name__ == '__main__':
    print('Hello')
    parse_html('Антонов Вячеслав Игоревич.html', 'Антонов Вячеслав Игоревич.txt')
    text = []
    text = read_txt('Антонов Вячеслав Игоревич.txt')
    print(text)