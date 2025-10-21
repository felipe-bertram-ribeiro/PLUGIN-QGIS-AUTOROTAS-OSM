# -*- coding: utf-8 -*-
from qgis.core import QgsProcessingProvider
from .osm_overpass_algorithm import OSMOverpassAlgorithm

class AutoRotasProvider(QgsProcessingProvider):
    def loadAlgorithms(self):
        self.addAlgorithm(OSMOverpassAlgorithm())

    def id(self):
        return 'autorotas_overpass'

    def name(self):
        return self.tr('Auto Rotas OSM (Overpass)')

    def longName(self):
        return self.name()
