# -*- coding: utf-8 -*-

import logging
import Image
import ImageChops
import ImageStat
from cStringIO import StringIO
from hashlib import md5
from tests import TestXML

log = logging.getLogger(__name__)

class TestGetMap(TestXML):

    MAP_0 = Image.open("tests/wms/GetMap-0.png")
    MAP_1 = Image.open("tests/wms/GetMap-1.png")

    def test_GetMap(self):
        QUERY = (
            { 'layer': 'postgis-point', 'bbox': '1,1,3,3', 'result': self.MAP_0 },
            { 'layer': 'postgis-point', 'bbox': '1.9,1.9,2.1,2.1', 'result': self.MAP_0 },
            { 'layer': 'postgis-point', 'bbox': '1.99,1.99,2.01,2.01', 'result': self.MAP_1 },
            { 'layer': 'postgis-point', 'bbox': '1.999,1.999,2.001,2.001', 'result': self.MAP_0 },
            { 'layer': 'wms-point', 'bbox': '1,1,3,3', 'result': self.MAP_0 },
            { 'layer': 'wms-point', 'bbox': '1.9,1.9,2.1,2.1', 'result': self.MAP_0 },
            { 'layer': 'wms-point', 'bbox': '1.99,1.99,2.01,2.01', 'result': self.MAP_1 },
            { 'layer': 'wms-point', 'bbox': '1.999,1.999,2.001,2.001', 'result': self.MAP_0 },
            { 'layer': 'wfs-point', 'bbox': '1,1,3,3', 'result': self.MAP_0 },
            { 'layer': 'wfs-point', 'bbox': '1.9,1.9,2.1,2.1', 'result': self.MAP_0 },
            { 'layer': 'wfs-point', 'bbox': '1.99,1.99,2.01,2.01', 'result': self.MAP_1 },
            { 'layer': 'wfs-point', 'bbox': '1.999,1.999,2.001,2.001', 'result': self.MAP_0 },
            { 'layer': 'points', 'bbox': '1,1,3,3', 'result': self.MAP_0 },
            { 'layer': 'points', 'bbox': '1.9,1.9,2.1,2.1', 'result': self.MAP_0 },
            { 'layer': 'points', 'bbox': '1.99,1.99,2.01,2.01', 'result': self.MAP_1 },
            { 'layer': 'points', 'bbox': '1.999,1.999,2.001,2.001', 'result': self.MAP_0 },
        )
        results = {}
        for q in QUERY:
            content = self._get((
                ('SERVICE', 'WMS'),
                ('VERSION', '1.1.1'),
                ('REQUEST', 'GetMap'),
                ('TRANSPARENT', 'TRUE'),
                ('LAYERS', q['layer']),
                ('FORMAT', 'image/png'),
                ('STYLE', ''),
                ('BBOX', q['bbox']),
                ('HEIGHT', '500'),
                ('WIDTH', '500'),
                ('SRS', 'EPSG:4326'),
            ))
            self.assertEquals('PNG', content[1:4])
            img = Image.open(StringIO(content))
            self.assertEquals(q['result'].size, img.size)
            diffimg = ImageChops.difference(q['result'], img)
            stats = ImageStat.Stat(diffimg).var
            self.assertTrue(stats[0] + stats[1] + stats[2] < 1, "Wrong image")
