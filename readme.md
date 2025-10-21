Plugin Auto Rotas OSM (Overpass) para QGIS

O Auto Rotas OSM (Overpass) é um plugin para o QGIS que permite baixar dados de vias (roads) do OpenStreetMap (OSM) utilizando a Overpass API e filtrá-los com base nos tipos de rodovias. O plugin pode buscar as vias dentro de uma área definida por nome (ex.: "Curitiba, Brazil") ou por uma extensão geográfica (coordenadas mínimas e máximas). O resultado é uma camada de linhas (vias) filtradas que podem ser utilizadas para análise e visualização no QGIS.

Funcionalidade

Selecionar área de pesquisa:
O plugin permite dois métodos para definir a área de interesse:

Por Nome: Você pode fornecer o nome de uma cidade ou local (ex.: "Curitiba, Brazil"), e o plugin irá buscar a área correspondente usando o serviço Nominatim (API de geocodificação do OpenStreetMap).

Por Extensão: Você pode fornecer as coordenadas de uma extensão retangular (xmin, ymin, xmax, ymax) para definir a área a ser consultada.

Filtrar tipos de rodovia:
O plugin permite que você defina quais tipos de rodovias deseja buscar. Você pode especificar uma lista de tipos de rodovias do OpenStreetMap (por exemplo, primary, secondary, tertiary, residential, etc.). O plugin irá buscar apenas essas rodovias dentro da área selecionada.

Consulta via Overpass API:
O plugin consulta a Overpass API para buscar dados de vias (elementos do tipo "way") dentro da área selecionada e com os tipos de rodovia filtrados. Ele utiliza a API de consulta para obter os dados em formato JSON e processá-los.

Criação de camada no QGIS:
Os dados obtidos são processados e convertidos em geometrias de linhas no QGIS. Para cada via (way) encontrada, o plugin cria um objeto de linha (LineString), incluindo o ID do OSM e o tipo de rodovia. Esses dados são então armazenados em uma camada de saída, que pode ser utilizada para visualizações e análises adicionais no QGIS.

Parâmetros de Entrada

Seleção de Área:

Por Nome: Nome do local para pesquisar a área (ex: "Curitiba, Brazil").

Por Extensão: Coordenadas de uma extensão retangular (xmin, ymin, xmax, ymax).

Tipos de Rodovia (Highway): Lista de tipos de rodovias que devem ser filtrados (ex: primary,secondary,tertiary,residential).

Saída: Camada de rodovias filtradas como linhas no QGIS.

Como Usar

Instalação:

Baixe e instale o plugin através do repositório de plugins do QGIS.

Execução:

Abra o QGIS e acesse o Menu de Processamento.

Busque pelo algoritmo Auto Rotas OSM (Overpass).

Selecione o método de busca da área (por nome ou extensão).

Defina os tipos de rodovia a serem filtrados.

Execute o algoritmo e visualize as rodovias filtradas na camada de saída.

Exemplo de Uso

Defina a área como "Curitiba, Brazil".

Filtre rodovias dos tipos primary, secondary e residential.

O plugin buscará essas rodovias na área de Curitiba e criará uma camada com essas vias.