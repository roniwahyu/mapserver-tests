# -*- coding: utf-8 -*-

import logging
from hashlib import md5
from tests import TestXML

log = logging.getLogger(__name__)

class TestGetMap(TestXML):
    def test_GetMap(self):
        QUERY = (
            { 'layer': 'postgis-point', 'bbox': '1,1,3,3', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'postgis-point', 'bbox': '1.9,1.9,2.1,2.1', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'postgis-point', 'bbox': '1.99,1.99,2.01,2.01', 'len': 2477, 'md5': 'b8f7974bd616cc3112be222d53b72d7c' },
            { 'layer': 'postgis-point', 'bbox': '1.999,1.999,2.001,2.001', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wms-point', 'bbox': '1,1,3,3', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wms-point', 'bbox': '1.9,1.9,2.1,2.1', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wms-point', 'bbox': '1.99,1.99,2.01,2.01', 'len': 2480, 'md5': 'e71857deedaaebb3cf6f41aa0cfeca7d' },
            { 'layer': 'wms-point', 'bbox': '1.999,1.999,2.001,2.001', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wfs-point', 'bbox': '1,1,3,3', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wfs-point', 'bbox': '1.9,1.9,2.1,2.1', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wfs-point', 'bbox': '1.99,1.99,2.01,2.01', 'len': 2477, 'md5': 'b8f7974bd616cc3112be222d53b72d7c' },
            { 'layer': 'wfs-point', 'bbox': '1.999,1.999,2.001,2.001', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
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
            self.assertEquals(q['len'], len(content))
            self.assertEquals(q['md5'], md5(content).hexdigest())
