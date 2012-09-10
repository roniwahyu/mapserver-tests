# -*- coding: utf-8 -*-

import logging
from hashlib import md5
from tests import TestXML

log = logging.getLogger(__name__)

class TestGetLegendGraphic(TestXML):
    def test_GetLegendGraphic(self):
        QUERY = (
            { 'layer': 'postgis-point', 'scale': 1000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'postgis-point', 'scale': 10000, 'len': 278, 'md5': 'b1668dc07f78e019ca783b3d10a38b80' },
            { 'layer': 'postgis-point', 'scale': 100000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'postgis-point', 'scale': 1000000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
#            { 'layer': 'wms-point', 'scale': 1000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' }, TODO assign issue
            { 'layer': 'wms-point', 'scale': 10000, 'len': 278, 'md5': 'b1668dc07f78e019ca783b3d10a38b80' },
#            { 'layer': 'wms-point', 'scale': 100000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' }, TODO assign issue
#            { 'layer': 'wms-point', 'scale': 1000000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' }, TODO assign issue
            { 'layer': 'wfs-point', 'scale': 1000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'wfs-point', 'scale': 10000, 'len': 278, 'md5': 'b1668dc07f78e019ca783b3d10a38b80' },
            { 'layer': 'wfs-point', 'scale': 100000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'wfs-point', 'scale': 1000000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
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
            self.assertEquals(q['len'], len(content))
            self.assertEquals(q['md5'], md5(content).hexdigest())


