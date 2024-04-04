import requests
from bs4 import BeautifulSoup as bs
import re
import maindb

nomeProduto = str(input("Digite o nome do produto: "))

maindb.resetData()

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
link = f"https://lista.mercadolivre.com.br/{nomeProduto.replace(' ', '-')}#D[A:{nomeProduto.replace(' ', '%20')}]"

proximaAbaExiste = True
pagina = 1
produtoAnalisado = 0
avaliacaoEspecial = 0

while proximaAbaExiste:
    request = requests.get(link, headers=header)
    site = bs(request.text, 'html.parser')

    divProduto = site.find_all('div', class_= 'ui-search-result__wrapper') 
    botaoProximoExiste = site.find('li', class_='andes-pagination__button andes-pagination__button--next')

    if botaoProximoExiste!= None and pagina < 5:
        for i in divProduto:
            print(produtoAnalisado)
            avaliacaoSuja = i.find('span', class_='ui-search-reviews__rating-number')
            produtoNomeSujo = i.find('h2', class_='ui-search-item__title')            
            url = i.find('a', class_='ui-search-item__group__element ui-search-link__title-card ui-search-link')
            produtoPrecoSujo = i.find('span', class_='andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript')
            
            nomeFinal = produtoNomeSujo.get_text()

            if produtoPrecoSujo != None:
                precoSeparadoEmListas = re.findall('[0-9]+', produtoPrecoSujo['aria-label'])
                precoFinal = '.'.join(precoSeparadoEmListas)            
            else:
                precoFinal = 'Indisponível'

            if avaliacaoSuja != None:
                if i.find('div', class_='ui-search-item__highlight-label ui-search-item__highlight-label--best_seller') != None:
                    avaliacaoFinal = avaliacaoSuja.get_text()
                    avaliacaoEspecial = 1
                else:
                    avaliacaoFinal = avaliacaoSuja.get_text()
                    avaliacaoEspecial = 0
            else:
                avaliacaoFinal = 0

            maindb.insertData(nomeFinal, precoFinal, avaliacaoFinal, avaliacaoEspecial, url['href'])
            produtoAnalisado += 1
            
        pagina += 1
        linkProximo = botaoProximoExiste.find('a', class_="andes-pagination__link")
        link = linkProximo['href']
    else:
        maindb.sortData()
        print(f'{produtoAnalisado} produtos organizados no banco')
        proximaAbaExiste = False