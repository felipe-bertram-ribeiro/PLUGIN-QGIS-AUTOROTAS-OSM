AUTOR: FELIPE BERTRAM RIBEIRO
EMAIL PARA CONTATO: felipebertram3014@gmail.com

Plugin Auto Rotas OSM (Overpass) para QGIS
Descrição

O Auto Rotas OSM (Overpass) é um plugin desenvolvido para o QGIS que permite realizar o download de dados de vias (roads) do OpenStreetMap (OSM) por meio da Overpass API, possibilitando o filtro dos resultados com base nos tipos de rodovias.

O plugin oferece duas formas de definir a área de busca:

Por nome de localidade (ex.: “Curitiba, Brazil”);

Por extensão geográfica (coordenadas mínimas e máximas).

Após a consulta, os dados são processados e convertidos em uma camada vetorial de linhas no QGIS, permitindo visualização e análise geoespacial dos tipos de vias desejadas.

O projeto foi desenvolvido com foco em eficiência, integração direta com APIs do OSM e facilidade de uso dentro do ambiente QGIS.

Funcionalidades

Definição da área de busca

Por Nome: Busca a área correspondente usando o serviço Nominatim (API de geocodificação do OpenStreetMap).

Por Extensão: Define manualmente a área de interesse através das coordenadas xmin, ymin, xmax, ymax.

Filtragem de tipos de rodovias (highway):

Permite selecionar quais tipos de vias do OSM devem ser baixadas (ex.: primary, secondary, tertiary, residential).

Consulta via Overpass API:

Realiza requisições à Overpass API para obter as vias filtradas dentro da área especificada.

Criação automática de camada no QGIS:

Gera uma camada vetorial de linhas contendo os atributos:

ID do OSM

Tipo de rodovia (highway)

Os dados são processados automaticamente e adicionados ao painel de camadas do QGIS.

Parâmetros de Entrada

Seleção de Área:

Por Nome: Nome do local (ex.: “Curitiba, Brazil”).

Por Extensão: Coordenadas retangulares (xmin, ymin, xmax, ymax).

Tipos de Rodovia (Highway):

Lista de tipos de vias a serem filtradas (ex.: primary, secondary, residential).

Saída:

Camada de linhas com as rodovias filtradas exibidas diretamente no QGIS.

Como Usar
Instalação

Abra o QGIS.

Acesse o Gerenciador de Plugins.

Busque por Auto Rotas OSM (Overpass).

Clique em Instalar.

Execução

Vá até o Menu de Processamento no QGIS.

Pesquise por Auto Rotas OSM (Overpass).

Escolha o método de definição da área (por nome ou por extensão).

Informe os tipos de rodovia que deseja filtrar.

Execute o algoritmo.

Visualize a camada resultante diretamente no mapa.

Exemplo de Uso

Área: “Curitiba, Brazil”

Tipos de rodovia: primary, secondary, residential

O plugin irá buscar apenas esses tipos de vias dentro da área delimitada de Curitiba e criar uma camada vetorial contendo as respectivas rodovias, prontas para visualização e análise no QGIS.

Tecnologias Utilizadas

QGIS (versão 3.22.4 ou superior)

Python 3

PyQGIS API

Overpass API

Nominatim API (OpenStreetMap)

Estrutura do Projeto

auto_rotas_osm/ – Código-fonte principal do plugin.

resources/ – Arquivos de interface (ícones, QML, etc).

metadata.txt – Informações do plugin para o QGIS.

init.py – Arquivo de inicialização do plugin.

main.py – Arquivo principal com a lógica de execução do algoritmo.

O projeto ainda está em desenvolvimento e poderá receber novas funcionalidades e melhorias de desempenho em versões futuras.
