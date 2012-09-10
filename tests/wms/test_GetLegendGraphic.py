# -*- coding: utf-8 -*-

import logging
from hashlib import md5
from tests import TestXML

log = logging.getLogger(__name__)

class TestGetLegendGraphic(TestXML):
    def test_GetLegendGraphic(self):
        QUERY = (
            { 'layer': 'postgis-point', 'scale': 1000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'postgis-point', 'scale': 10000, 'len': 431, 'md5': '709d85c7094e3203a7c9538cd8a30cf4' },
            { 'layer': 'postgis-point', 'scale': 100000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'postgis-point', 'scale': 1000000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
#            { 'layer': 'wms-point', 'scale': 1000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' }, TODO assign issue
            { 'layer': 'wms-point', 'scale': 10000, 'len': 431, 'md5': '709d85c7094e3203a7c9538cd8a30cf4' },
#            { 'layer': 'wms-point', 'scale': 100000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' }, TODO assign issue
#            { 'layer': 'wms-point', 'scale': 1000000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' }, TODO assign issue
            { 'layer': 'wfs-point', 'scale': 1000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'wfs-point', 'scale': 10000, 'len': 431, 'md5': '709d85c7094e3203a7c9538cd8a30cf4' },
            { 'layer': 'wfs-point', 'scale': 100000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'wfs-point', 'scale': 1000000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'points', 'scale': 1000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'points', 'scale': 10000, 'len': 548, 'md5': '1e85664a2947b1d917f500554ad3cb55' },
            { 'layer': 'points', 'scale': 100000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
            { 'layer': 'points', 'scale': 1000000, 'len': 75, 'md5': 'b0dc44728d0988e4e8ccca7f5577f386' },
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


