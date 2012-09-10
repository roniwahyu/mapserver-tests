# -*- coding: utf-8 -*-

import logging
from copy import copy
from tests import TestXML

log = logging.getLogger(__name__)

class TestGetFeature(TestXML):

    RESULT = u"""<?xml version="1.0" encoding="UTF-8"?>

<msGMLOutput
	 xmlns:gml="http://www.opengis.net/gml"
	 xmlns:xlink="http://www.w3.org/1999/xlink"
	 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">%(features)s
</msGMLOutput>
"""

    FEATURE_RESULT = u"""
	<%%(layer)s_layer>
	<gml:name>Layer éàè</gml:name>
		<%%(layer)s_feature>
			<gml:boundedBy>
				<gml:Box srsName="EPSG:4326">
					<gml:coordinates>%(pos)s %(pos)s</gml:coordinates>
				</gml:Box>
			</gml:boundedBy>
			<the_geom>
			<gml:Point srsName="EPSG:4326">
			  <gml:coordinates>%(pos)s</gml:coordinates>
			</gml:Point>
			</the_geom>
			<gid>%(gid)i</gid>
			<int>%(int)i</int>
			<real>%(real)s</real>
			<character>%(character)s</character>
			<date>%(date)i-10-19 10:23:54</date>
			<boolean>%(boolean)s</boolean>
		</%%(layer)s_feature>
	</%%(layer)s_layer>"""
    FEATURE_RESULT_2 = FEATURE_RESULT % {
        'pos': '2.000000,2.000000',
        'gid': 2,
        'int': 2,
        'real': '2.2',
        'character': u'abCéàè2',
        'date': 2002,
        'boolean': 'f',
    }
    FEATURE_RESULT_3 = FEATURE_RESULT % {
        'pos': '3.000000,3.000000',
        'gid': 3,
        'int': 3,
        'real': '3.3',
        'character': u'abCéàè3',
        'date': 2003,
        'boolean': 'f',
    }


    FEATURE_SHP_RESULT = u"""
	<%%(layer)s_layer>
	<gml:name>Layer éàè</gml:name>
		<%%(layer)s_feature>
			<gml:boundedBy>
				<gml:Box srsName="EPSG:4326">
					<gml:coordinates>%(pos)s %(pos)s</gml:coordinates>
				</gml:Box>
			</gml:boundedBy>
			<the_geom>
			<gml:Point srsName="EPSG:4326">
			  <gml:coordinates>%(pos)s</gml:coordinates>
			</gml:Point>
			</the_geom>
			<INT>%(int)i</INT>
			<REAL>%(real)s</REAL>
			<CHARACTER>%(character)s</CHARACTER>
			<DATE>%(date)i-10-19 10:23:54</DATE>
			<BOOLEAN>%(boolean)s</BOOLEAN>
		</%%(layer)s_feature>
	</%%(layer)s_layer>"""
    FEATURE_SHP_RESULT_2 = FEATURE_SHP_RESULT % {
        'pos': '2.000000,2.000000',
        'gid': 2,
        'int': 2,
        'real': '2.2',
        'character': u'abCéàè2',
        'date': 2002,
        'boolean': 'F',
    }
    FEATURE_SHP_RESULT_3 = FEATURE_SHP_RESULT % {
        'pos': '3.000000,3.000000',
        'gid': 3,
        'int': 3,
        'real': '3.3',
        'character': u'abCéàè3',
        'date': 2003,
        'boolean': 'F',
    }

    def test_singleLayer(self):
        REQUETS = (
            ('postgis-point-auto', self.FEATURE_RESULT_2),
            ('postgis-point', self.FEATURE_RESULT_2),
            ('shp-point-auto', self.FEATURE_SHP_RESULT_2),
            ('shp-point', self.FEATURE_SHP_RESULT_2),
        )
        for r in REQUETS:
            log.info(r[0])
            content = self._get((
                ('SERVICE', 'WMS'),
                ('VERSION', '1.1.1'),
                ('REQUEST', 'GetFeatureInfo'),
                ('LAYERS', r[0]),
                ('QUERY_LAYERS', r[0]),
                ('BBOX', '1.99,1.99,2.01,2.01'),
                ('FEATURE_COUNT', '1'),
                ('HEIGHT', '500'),
                ('WIDTH', '500'),
                ('INFO_FORMAT', 'application/vnd.ogc.gml'),
                ('SRS', 'EPSG:4326'),
                ('X', '250'),
                ('Y', '250')
            ))
            self._assert_result_equals(content, self.RESULT % {
                'features':r[1] % { 'layer': r[0] }
            })
            content = self._get((
                ('SERVICE', 'WMS'),
                ('VERSION', '1.1.1'),
                ('REQUEST', 'GetFeatureInfo'),
                ('LAYERS', r[0]),
                ('QUERY_LAYERS', r[0]),
                ('BBOX', '1.99,1.99,2.01,2.01'),
                ('FEATURE_COUNT', '1'),
                ('HEIGHT', '500'),
                ('WIDTH', '500'),
                ('INFO_FORMAT', 'application/vnd.ogc.gml'),
                ('SRS', 'EPSG:4326'),
                ('X', '500'),
                ('Y', '0')
            ))
            self._assert_result_equals(content, self.RESULT % {
                'features': ''
            })

    # With mapserver 6.0.3 when we do a request on two shapefile we reseive an error 500.
    def test_multiple_feature_type(self):
        content = self._get((
            ('SERVICE', 'WMS'),
            ('VERSION', '1.1.1'),
            ('REQUEST', 'GetFeatureInfo'),
            ('LAYERS', 'postgis-point-auto,postgis-point,shp-point-auto,shp-point,wfs-point'),
            ('QUERY_LAYERS', 'postgis-point-auto,postgis-point,shp-point-auto,shp-point,wfs-point'),
            ('BBOX', '1.99,1.99,2.01,2.01'),
            ('FEATURE_COUNT', '10'),
            ('HEIGHT', '500'),
            ('WIDTH', '500'),
            ('INFO_FORMAT', 'application/vnd.ogc.gml'),
            ('SRS', 'EPSG:4326'),
            ('X', '250'),
            ('Y', '250')
        ))
        features = ''
        features += self.FEATURE_RESULT_2 % { 'layer': 'postgis-point-auto' }
        features += self.FEATURE_RESULT_2 % { 'layer': 'postgis-point' }
        features += self.FEATURE_SHP_RESULT_2 % { 'layer': 'shp-point-auto' }
        features += self.FEATURE_SHP_RESULT_2 % { 'layer': 'shp-point' }
#        features += self.FEATURE_RESULT_2 % { 'layer': 'postgis-point' }
        features += self.FEATURE_RESULT_2 % { 'layer': 'wfs-point' }
        self._assert_result_equals(content, self.RESULT % {
            'features': features
        })

    def test_group(self):
        content = self._get((
            ('SERVICE', 'WMS'),
            ('VERSION', '1.1.1'),
            ('REQUEST', 'GetFeatureInfo'),
            ('LAYERS', 'points'),
            ('QUERY_LAYERS', 'points'),
            ('BBOX', '1.99,1.99,2.01,2.01'),
            ('FEATURE_COUNT', '10'),
            ('HEIGHT', '500'),
            ('WIDTH', '500'),
            ('INFO_FORMAT', 'application/vnd.ogc.gml'),
            ('SRS', 'EPSG:4326'),
            ('X', '250'),
            ('Y', '250')
        ))
        features = ''
        features += self.FEATURE_RESULT_2 % { 'layer': 'postgis-point-auto' }
        features += self.FEATURE_RESULT_2 % { 'layer': 'postgis-point' }
        features += self.FEATURE_SHP_RESULT_2 % { 'layer': 'shp-point-auto' }
        features += self.FEATURE_SHP_RESULT_2 % { 'layer': 'shp-point' }
        features += self.FEATURE_RESULT_2 % { 'layer': 'wfs-point' }
        self._assert_result_equals(content, self.RESULT % {
            'features': features
        })
