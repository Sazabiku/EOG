from bs4 import BeautifulSoup

with open('Куприн_Вячеслав_Александрович_2.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    root = soup.html

    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)