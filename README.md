<h1>Algoritmo de pesquisa no Mercado Livre</h1>
<p>Utilizando das bibliotecas: Requests, BeautifulSoup4, Regex e sqlite3 consegui criar um algoritmo que pesquisa um determinado item no site "Mercado Livre" e implementa em um banco de dados com suas respectivas características. Ao todo, por padrão, serão analisadas 5 paginas do site sobre o item.</p>

<h2>Algoritmo de pesquisa</h2>
<p>No site do <a href="https://www.mercadolivre.com.br/" rel="external" target="_blank">Mercado Livre</a> os parâmetros funcionam da seguinte maneira:</p>
<h3>URL</h3>
<img src="resources/imagens/url.png" alt="url">
<h3>DIV</h3>
<img src="resources/imagens/htmldiv.png" alt="divprincipal">
<p>Todos os recursos que serão disponibilizados de um produto vem dentro dessa <code>div class="ui-search-result__wrapper"</code>
incluindo um caso em especifico de uma tag de "MAIS VENDIDO" como nesse exemplo do pó de café:</p>
<img src="resources/imagens/super.png" alt="super">
<p>Isso é possível identificar dentro do html por causa de uma div específica <code>div class="ui-search-item__highlight-label ui-search-item__highlight-label--best_seller"</code></p>

<h2>Banco de dados</h2>
<p>O banco foi dividido em duas tabelas que vão ficar trocando valores entre si para se reorganizarem, a tabela PRODUTOS e a SORTED_PRODUTOS</p>
<img src="resources/imagens/banco.png" alt="camposTabela">
<p>No final, os itens serão organizados de maneira crescente pelo seu valor, descrescente pela sua qualidade e dando uma prioridade superior para a categoria SUPER, que é justamente se houver a condição de "MAIS VENDIDO"</p>
<h3>Exemplo com o café</h3>
<img src="resources/imagens/resultado.png" alt="resultadoPesquisa">
