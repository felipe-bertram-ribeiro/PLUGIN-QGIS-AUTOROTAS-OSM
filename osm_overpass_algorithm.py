# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.parse
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsProcessingAlgorithm,
    QgsProcessingParameterEnum,
    QgsProcessingParameterString,
    QgsProcessingParameterExtent,
    QgsProcessingParameterFeatureSink,
    QgsFeature,
    QgsFields,
    QgsField,
    QgsWkbTypes,
    QgsGeometry,
    QgsFeatureSink,
    QgsCoordinateReferenceSystem
)
from PyQt5.QtCore import QVariant

class OSMOverpassAlgorithm(QgsProcessingAlgorithm):
    """Download and filter OSM ways via Overpass API"""

    PARAM_METHOD = 'METHOD'
    PARAM_AREA = 'AREA'
    PARAM_EXTENT = 'EXTENT'
    PARAM_TYPES = 'TYPES'
    PARAM_OUTPUT = 'OUTPUT'

    def tr(self, string):
        return QCoreApplication.translate('Auto Rotas OSM (Overpass)', string)

    def createInstance(self):
        return OSMOverpassAlgorithm()

    def name(self):
        return 'autorotas_overpass'

    def displayName(self):
        return self.tr('Auto Rotas OSM (Overpass)')

    def group(self):
        return self.tr('OSM Tools')

    def groupId(self):
        return 'osm_tools'

    def shortHelpString(self):
        return self.tr('Baixa vias OSM usando Overpass API e filtra por highway.')

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterEnum(
                self.PARAM_METHOD,
                self.tr('Seleção de área'),
                options=[self.tr('Por nome'), self.tr('Por extensão')],
                defaultValue=0
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.PARAM_AREA,
                self.tr('Nome de lugar (ex: Curitiba, Brazil)'),
                defaultValue=''
            )
        )
        self.addParameter(
            QgsProcessingParameterExtent(
                self.PARAM_EXTENT,
                self.tr('Extensão (xmin, ymin, xmax, ymax) se "Por extensão"'),
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.PARAM_TYPES,
                self.tr('Tipos highway OSM (comma-separated)'),
                defaultValue='primary,secondary,tertiary,residential'
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.PARAM_OUTPUT,
                self.tr('Rotas filtradas')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        method = self.parameterAsEnum(parameters, self.PARAM_METHOD, context)
        area = self.parameterAsString(parameters, self.PARAM_AREA, context)
        rect = None
        if method == 1:
            rect = self.parameterAsExtent(parameters, self.PARAM_EXTENT, context)
        types_list = [t.strip() for t in self.parameterAsString(parameters, self.PARAM_TYPES, context).split(',')]

        # Determine bbox
        if method == 0:
            feedback.pushInfo(f'Searching Nominatim for "{area}"')
            nom_url = 'https://nominatim.openstreetmap.org/search?' + urllib.parse.urlencode({'q': area, 'format': 'json'})
            req = urllib.request.Request(nom_url, headers={'User-Agent': 'QGIS AutoRotasOverpass'})
            data = urllib.request.urlopen(req).read()
            results = json.loads(data)
            if not results:
                raise Exception(self.tr('Local não encontrado'))
            bb = results[0]['boundingbox']
            south, north, west, east = map(float, bb)
        else:
            feedback.pushInfo('Using provided extent')
            south, west, north, east = rect.yMinimum(), rect.xMinimum(), rect.yMaximum(), rect.xMaximum()

        # Overpass
        bbox_str = f'({south},{west},{north},{east})'
        query = f'[out:json][timeout:60];way["highway"]{bbox_str};out geom;'
        feedback.pushInfo('Querying Overpass API')
        post_data = urllib.parse.urlencode({'data': query}).encode('utf-8')
        req = urllib.request.Request('https://overpass-api.de/api/interpreter', data=post_data,
                                     headers={'User-Agent': 'QGIS AutoRotasOverpass'})
        response = urllib.request.urlopen(req).read()
        geo = json.loads(response)

        # Prepare sink
        fields = QgsFields()
        fields.append(QgsField('osm_id', QVariant.Int))
        fields.append(QgsField('highway', QVariant.String))
        crs = QgsCoordinateReferenceSystem('EPSG:4326')
        (sink, dest_id) = self.parameterAsSink(
            parameters, self.PARAM_OUTPUT, context,
            fields, QgsWkbTypes.LineString, crs
        )

        # Populate
        for elem in geo.get('elements', []):
            if elem.get('type') != 'way': continue
            tags = elem.get('tags', {})
            hw = tags.get('highway')
            if hw not in types_list: continue
            coords = elem.get('geometry', [])
            pts = [QgsGeometry.fromPointXY(QgsGeometry().fromWkt(f"POINT({pt['lon']} {pt['lat']})").asPoint()) for pt in coords]
            geom = QgsGeometry.fromPolylineXY([p.asPoint() for p in pts])
            feat = QgsFeature(fields)
            feat.setGeometry(geom)
            feat['osm_id'] = elem.get('id')
            feat['highway'] = hw
            sink.addFeature(feat, QgsFeatureSink.FastInsert)

        return {self.PARAM_OUTPUT: dest_id}
