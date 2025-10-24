<h1>Plugin Auto Rotas OSM (Overpass) para QGIS</h1>

<h2>Descrição</h2>
<p>
O <strong>Auto Rotas OSM (Overpass)</strong> é um plugin desenvolvido para o <strong>QGIS</strong> que permite realizar o download de <strong>vias (roads)</strong> do 
<strong>OpenStreetMap (OSM)</strong> utilizando a <strong>Overpass API</strong>. 
Ele possibilita filtrar os resultados com base nos <strong>tipos de rodovias</strong> e definir a área de busca por 
<strong>nome de localidade</strong> (ex.: “Curitiba, Brazil”) ou por <strong>extensão geográfica</strong> 
(coordenadas mínimas e máximas).
</p>

<p>
Após a consulta, os dados são processados e convertidos em uma <strong>camada vetorial de linhas</strong>, permitindo 
<strong>visualização e análise geoespacial</strong> no QGIS.
</p>

<p>
O projeto foi desenvolvido com foco em <strong>eficiência, integração direta com APIs do OSM</strong> e 
<strong>facilidade de uso dentro do ambiente QGIS</strong>.
</p>

<hr>

<h2>O projeto ainda não está concluído e virão novas adições.</h2>

<hr>

<h2>Funcionalidades</h2>
<ul>
  <li><strong>Definir área de pesquisa</strong>
    <ul>
      <li><strong>Por Nome:</strong> Busca a área correspondente usando o serviço <strong>Nominatim</strong> (API de geocodificação do OpenStreetMap).</li>
      <li><strong>Por Extensão:</strong> Define manualmente a área de interesse através das coordenadas <em>xmin, ymin, xmax, ymax</em>.</li>
    </ul>
  </li>

  <li><strong>Filtrar tipos de rodovia (highway)</strong>
    <ul>
      <li>Permite selecionar quais tipos de vias do OSM devem ser baixadas (ex.: <em>primary, secondary, tertiary, residential</em>).</li>
    </ul>
  </li>

  <li><strong>Consulta via Overpass API</strong>
    <ul>
      <li>Realiza requisições à <strong>Overpass API</strong> para obter as vias filtradas dentro da área especificada.</li>
    </ul>
  </li>

  <li><strong>Criação automática de camada no QGIS</strong>
    <ul>
      <li>Gera uma camada vetorial de linhas contendo os atributos:</li>
      <ul>
        <li><strong>ID do OSM</strong></li>
        <li><strong>Tipo de rodovia (highway)</strong></li>
      </ul>
      <li>Os dados são processados automaticamente e adicionados ao painel de camadas do QGIS.</li>
    </ul>
  </li>
</ul>

<hr>

<h2>Parâmetros de Entrada</h2>
<ul>
  <li><strong>Seleção de Área:</strong>
    <ul>
      <li><em>Por Nome:</em> Nome do local (ex.: “Curitiba, Brazil”).</li>
      <li><em>Por Extensão:</em> Coordenadas retangulares (<em>xmin, ymin, xmax, ymax</em>).</li>
    </ul>
  </li>

  <li><strong>Tipos de Rodovia (Highway):</strong>
    <ul>
      <li>Lista de tipos de vias a serem filtradas (ex.: <em>primary, secondary, residential</em>).</li>
    </ul>
  </li>

  <li><strong>Saída:</strong>
    <ul>
      <li>Camada de linhas com as rodovias filtradas exibidas diretamente no QGIS.</li>
    </ul>
  </li>
</ul>

<hr>

<h2>Como Usar</h2>

<h3>Instalação</h3>
<ol>
  <li>Abra o <strong>QGIS</strong>.</li>
  <li>Acesse o <strong>Gerenciador de Plugins</strong>.</li>
  <li>Busque por <strong>Auto Rotas OSM (Overpass)</strong>.</li>
  <li>Clique em <strong>Instalar</strong>.</li>
</ol>

<h3>Execução</h3>
<ol>
  <li>Vá até o <strong>Menu de Processamento</strong> no QGIS.</li>
  <li>Pesquise por <strong>Auto Rotas OSM (Overpass)</strong>.</li>
  <li>Escolha o método de definição da área (por nome ou por extensão).</li>
  <li>Informe os tipos de rodovia que deseja filtrar.</li>
  <li>Execute o algoritmo.</li>
  <li>Visualize a camada resultante diretamente no mapa.</li>
</ol>

<hr>

<h2>Exemplo de Uso</h2>
<ul>
  <li><strong>Área:</strong> “Curitiba, Brazil”</li>
  <li><strong>Tipos de rodovia:</strong> <em>primary, secondary, residential</em></li>
</ul>

<p>
O plugin buscará essas vias na área delimitada e criará uma camada vetorial contendo as rodovias filtradas, prontas para 
visualização e análise no QGIS.
</p>

<hr>

<h2>Tecnologias Utilizadas</h2>
<ul>
  <li><strong>QGIS</strong> (versão 3.22.4 ou superior)</li>
  <li><strong>Python 3</strong></li>
  <li><strong>PyQGIS API</strong></li>
  <li><strong>Overpass API</strong></li>
  <li><strong>Nominatim API (OpenStreetMap)</strong></li>
</ul>

<hr>

<h2>Estrutura do Projeto</h2>
<ul>
  <li><strong>auto_rotas_osm/</strong> – Código-fonte principal do plugin.</li>
  <li><strong>resources/</strong> – Arquivos de interface (ícones, QML, etc).</li>
  <li><strong>metadata.txt</strong> – Informações do plugin para o QGIS.</li>
  <li><strong>__init__.py</strong> – Arquivo de inicialização do plugin.</li>
  <li><strong>main.py</strong> – Arquivo principal com a lógica de execução do algoritmo.</li>
</ul>

<hr>

<p><strong>AUTOR:</strong> FELIPE BERTRAM RIBEIRO<br>
<strong>EMAIL PARA CONTATO:</strong> <a href="mailto:felipebertram3014@gmail.com">felipebertram3014@gmail.com</a></p>
