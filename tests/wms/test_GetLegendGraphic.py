# -*- coding: utf-8 -*-

import logging
import Image
import ImageChops
import ImageStat
from cStringIO import StringIO
from hashlib import md5
from tests import TestXML

log = logging.getLogger(__name__)

class TestGetLegendGraphic(TestXML):

    LEGEND_0 = Image.open("tests/wms/GetLegendGraphic-0.png")
    LEGEND_1 = Image.open("tests/wms/GetLegendGraphic-1.png")
    LEGEND_3 = Image.open("tests/wms/GetLegendGraphic-3.png")

    def test_GetLegendGraphic(self):
        QUERY = (
            { 'layer': 'postgis-point', 'scale': 1000, 'result': self.LEGEND_0 },
            { 'layer': 'postgis-point', 'scale': 10000, 'result': self.LEGEND_1 },
            { 'layer': 'postgis-point', 'scale': 100000, 'result': self.LEGEND_0 },
            { 'layer': 'postgis-point', 'scale': 1000000, 'result': self.LEGEND_0 },
#            { 'layer': 'wms-point', 'scale': 1000, 'result': self.LEGEND_0 }, # issue #4452
            { 'layer': 'wms-point', 'scale': 10000, 'result': self.LEGEND_1 },
#            { 'layer': 'wms-point', 'scale': 100000, 'result': self.LEGEND_0 }, # issue #4452
#            { 'layer': 'wms-point', 'scale': 1000000, 'result': self.LEGEND_0 }, # issue #4452
            { 'layer': 'wfs-point', 'scale': 1000, 'result': self.LEGEND_0 },
            { 'layer': 'wfs-point', 'scale': 10000, 'result': self.LEGEND_1 },
            { 'layer': 'wfs-point', 'scale': 100000, 'result': self.LEGEND_0 },
            { 'layer': 'wfs-point', 'scale': 1000000, 'result': self.LEGEND_0 },
            { 'layer': 'points', 'scale': 1000, 'result': self.LEGEND_0 },
            { 'layer': 'points', 'scale': 10000, 'result': self.LEGEND_3 },
            { 'layer': 'points', 'scale': 100000, 'result': self.LEGEND_0 },
            { 'layer': 'points', 'scale': 1000000, 'result': self.LEGEND_0 },
        )
        results = {}
        for q in QUERY:
            content = self._get((
                ('SERVICE', 'WMS'),
                ('VERSION', '1.1.1'),
                ('REQUEST', 'GetLegendGraphic'),
                ('TRANSPARENT', 'TRUE'),
                ('LAYER', q['layer']),
                ('FORMAT', 'image/png'),
                ('SCALE', q['scale']),
                ('SRS', 'EPSG:4326'),
            ))
            self.assertEquals('PNG', content[1:4])
            img = Image.open(StringIO(content))
            self.assertEquals(q['result'].size, img.size)
            diffimg = ImageChops.difference(q['result'], img)
            stats = ImageStat.Stat(diffimg).var
            self.assertTrue(stats[0] + stats[1] + stats[2] < 1, "Wrong image")
