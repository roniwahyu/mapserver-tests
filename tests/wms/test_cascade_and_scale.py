# -*- coding: utf-8 -*-

import logging
from hashlib import md5
from tests import TestXML

log = logging.getLogger(__name__)

class TestCascade(TestXML):
    RESULT = u"""<?xml version="1.0" encoding="UTF-8"?>

<msGMLOutput
	 xmlns:gml="http://www.opengis.net/gml"
	 xmlns:xlink="http://www.w3.org/1999/xlink"
	 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<%(layer)s_layer>
	<gml:name>Layer éàè</gml:name>
		<%(layer)s_feature>
			<gml:boundedBy>
				<gml:Box srsName="EPSG:4326">
					<gml:coordinates>2.000000,2.000000 2.000000,2.000000</gml:coordinates>
				</gml:Box>
			</gml:boundedBy>
			<the_geom>
			<gml:Point srsName="EPSG:4326">
			  <gml:coordinates>2.000000,2.000000</gml:coordinates>
			</gml:Point>
			</the_geom>
			<gid>2</gid>
			<int>2</int>
			<real>2.2</real>
			<character>abCéàè2</character>
			<date>2002-10-19 10:23:54</date>
			<boolean>f</boolean>
		</%(layer)s_feature>
	</%(layer)s_layer>
</msGMLOutput>"""
    SHP_RESULT = u"""<?xml version="1.0" encoding="UTF-8"?>

<msGMLOutput
	 xmlns:gml="http://www.opengis.net/gml"
	 xmlns:xlink="http://www.w3.org/1999/xlink"
	 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<%(layer)s_layer>
	<gml:name>Layer éàè</gml:name>
		<%(layer)s_feature>
			<gml:boundedBy>
				<gml:Box srsName="EPSG:4326">
					<gml:coordinates>2.000000,2.000000 2.000000,2.000000</gml:coordinates>
				</gml:Box>
			</gml:boundedBy>
			<the_geom>
			<gml:Point srsName="EPSG:4326">
			  <gml:coordinates>2.000000,2.000000</gml:coordinates>
			</gml:Point>
			</the_geom>
			<INT>2</INT>
			<REAL>2.2</REAL>
			<CHARACTER>abCéàè2</CHARACTER>
			<DATE>2002-10-19 10:23:54</DATE>
			<BOOLEAN>F</BOOLEAN>
		</%(layer)s_feature>
	</%(layer)s_layer>
</msGMLOutput>"""
    NORESULT = u"""<?xml version="1.0" encoding="UTF-8"?>

<msGMLOutput
	 xmlns:gml="http://www.opengis.net/gml"
	 xmlns:xlink="http://www.w3.org/1999/xlink"
	 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
</msGMLOutput>"""

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


    def test_GetFeaturesInfo(self):
        QUERY = (
            { 'layer': 'postgis-point', 'bbox': '1,1,3,3', 'result': self.NORESULT },
            { 'layer': 'postgis-point', 'bbox': '1.9,1.9,2.1,2.1', 'result': self.RESULT % { 'layer': 'postgis-point' } }, # feature present but not visible
            { 'layer': 'postgis-point', 'bbox': '1.99,1.99,2.01,2.01', 'result': self.RESULT % { 'layer': 'postgis-point' } },
            { 'layer': 'postgis-point', 'bbox': '1.999,1.999,2.001,2.001', 'result': self.NORESULT },
            { 'layer': 'shp-point', 'bbox': '1,1,3,3', 'result': self.NORESULT },
            { 'layer': 'shp-point', 'bbox': '1.9,1.9,2.1,2.1', 'result': self.SHP_RESULT % { 'layer': 'shp-point' } }, # feature present but not visible
            { 'layer': 'shp-point', 'bbox': '1.99,1.99,2.01,2.01', 'result': self.SHP_RESULT % { 'layer': 'shp-point' } },
            { 'layer': 'shp-point', 'bbox': '1.999,1.999,2.001,2.001', 'result': self.NORESULT },
            { 'layer': 'wms-point', 'bbox': '1,1,3,3', 'result': self.NORESULT },
            { 'layer': 'wms-point', 'bbox': '1.9,1.9,2.1,2.1', 'result': self.RESULT % { 'layer': 'postgis-point' } }, # feature present but not visible
            { 'layer': 'wms-point', 'bbox': '1.99,1.99,2.01,2.01', 'result': self.RESULT % { 'layer': 'postgis-point' } },
            { 'layer': 'wms-point', 'bbox': '1.999,1.999,2.001,2.001', 'result': self.NORESULT },
            { 'layer': 'wfs-point', 'bbox': '1,1,3,3', 'result': self.NORESULT },
            { 'layer': 'wfs-point', 'bbox': '1.9,1.9,2.1,2.1', 'result': self.RESULT % { 'layer': 'wfs-point' } }, # feature present but not visible
            { 'layer': 'wfs-point', 'bbox': '1.99,1.99,2.01,2.01', 'result': self.RESULT % { 'layer': 'wfs-point' } },
            { 'layer': 'wfs-point', 'bbox': '1.999,1.999,2.001,2.001', 'result': self.NORESULT },
        )
        for q in QUERY:
            content = self._get((
                ('SERVICE', 'WMS'),
                ('VERSION', '1.1.1'),
                ('REQUEST', 'GetFeatureInfo'),
                ('LAYERS', q['layer']),
                ('QUERY_LAYERS', q['layer']),
                ('FORMAT', 'image/png'),
                ('STYLE', ''),
                ('BBOX', q['bbox']),
                ('FEATURE_COUNT', '1'),
                ('HEIGHT', '500'),
                ('WIDTH', '500'),
                ('INFO_FORMAT', 'application/vnd.ogc.gml'),
                ('SRS', 'EPSG:4326'),
                ('X', '250'),
                ('Y', '250')
            ))
            self._assert_result_equals(content, q['result'])
