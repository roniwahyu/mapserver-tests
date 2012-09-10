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
            { 'layer': 'postgis-point', 'bbox': '1.99,1.99,2.01,2.01', 'len': 1387, 'md5': 'ce9b79ded1ec0828d26dc5c6315c5e62' },
            { 'layer': 'postgis-point', 'bbox': '1.999,1.999,2.001,2.001', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wms-point', 'bbox': '1,1,3,3', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wms-point', 'bbox': '1.9,1.9,2.1,2.1', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wms-point', 'bbox': '1.99,1.99,2.01,2.01', 'len': 1387, 'md5': '93b6d59616ec915ff948501226df363e' },
            { 'layer': 'wms-point', 'bbox': '1.999,1.999,2.001,2.001', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wfs-point', 'bbox': '1,1,3,3', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wfs-point', 'bbox': '1.9,1.9,2.1,2.1', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'wfs-point', 'bbox': '1.99,1.99,2.01,2.01', 'len': 1387, 'md5': 'ce9b79ded1ec0828d26dc5c6315c5e62' },
            { 'layer': 'wfs-point', 'bbox': '1.999,1.999,2.001,2.001', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'points', 'bbox': '1,1,3,3', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'points', 'bbox': '1.9,1.9,2.1,2.1', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
            { 'layer': 'points', 'bbox': '1.99,1.99,2.01,2.01', 'len': 1368, 'md5': 'bb4bd00bf537aec7872ec214bc4fefeb' },
            { 'layer': 'points', 'bbox': '1.999,1.999,2.001,2.001', 'len': 1048, 'md5': '64a17ca946e92cbefd2956b0e9663a12' },
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
