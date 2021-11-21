#! python3

import requests
import bs4
import os
import re
import time
from PyQt5.QtCore import QEventLoop, QTimer


class GetWiki:
    """
        Essa classe cria um objeto de busca pela wikipedia
    """
    def __init__(self, search):
        self.search = search.title()
        self.words = '_'.join(self.search.split())
        self.nameArc = self.words+'.txt'
        #self.directory = os.getcwd() + "\\getWiki\\"
        self.url = 'https://pt.wikipedia.org/wiki/'+self.words
        self.listHtml = 'Vazia'

    '''
    def setText(self):
        listTags = self.parseHtml(self.request())['text']
        retRegex = re.compile(r"(([\[])(.)*?([\]]))")
        titulo = self.search+'\n\n'
        listTags.insert(0, titulo)
        for tag in listTags:
            if tag == titulo:
                self.save(titulo)
            else:
                if tag.text == 'Ver também' or tag.text == 'Referências':
                    break
                else:
                    self.save(retRegex.sub("", tag.text).replace('Índice', ''))
        print('Arquivo salvo: ' + self.directory+self.nameArc)

    def request(self):
        r = requests.get(self.url)
        return self.validResp(r)

    def validResp(self, r):
        keysList = list(r.headers.keys())
        if 'Transfer-Encoding' in keysList:
            print('Falha, tentando novamente...')
            time.sleep(10)
            self.request()
        else:
            pos = keysList.index('Content-Length')
            valueList = list(r.headers.values())
            if int(valueList[pos]) > 10000:
                return r
            else:
                return None

    def parseHtml(self, resp):
        html_page = resp.text
        text = bs4.BeautifulSoup(html_page, 'html.parser')

        # exclui todas as tags 'small'
        soup = text.find_all('small')
        for s in soup:
            s.extract()

        # text = text.prettify() somante para uma visualização

        second = text.select("""
            .mw-parser-output > p,
            .mw-parser-output > h2,
            .mw-parser-output > h3,
            .mw-parser-output > blockquote,
            .mw-parser-output > ul > li
        """)

        return {'status': resp.status_code, 'text': second}

    def save(self, li):
        # arch = open(self.directory+self.nameArc, 'w',  encoding="utf-8")
        # arch.write(li+'\n')
        # arch.close()

        with open(self.directory+self.nameArc, 'a',  encoding="utf-8") as f:
            f.write(li+'\n')
        f.close()
    '''

    #@staticmethod
    #def search(busca):
    #    try:
    #        return GetWiki(busca)
    #    except (AttributeError):
    #        print("A página referente a '"+busca+"' ainda não foi criada!")


'''
    def sleep(segundos):
    loop = QEventLoop()
    QTimer.singleShot(segundos*1000, loop.quit)
    loop.exec_()
'''

# GetWiki.search('Anderson Silva')
# GetWiki.search('Charles Darwin')
# GetWiki.search('michael jackson')
# GetWiki.search('supra')
# GetWiki.search('macaco')
