# -*- coding: utf-8 -*-
"""Plugin initialization for AutoRotasOverpass"""
from qgis.core import QgsApplication
from .provider import AutoRotasProvider

class AutoRotasPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.provider = AutoRotasProvider()

    def initGui(self):
        QgsApplication.processingRegistry().addProvider(self.provider)

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)

def classFactory(iface):
    return AutoRotasPlugin(iface)
