# -*- coding: utf-8 -*-

import logging
from copy import copy
from wfs import TestWFS

log = logging.getLogger(__name__)

class TestGetFeature(TestWFS):
    GETFEATURE_REQUEST = u"""<?xml version='1.0' encoding="UTF-8" ?>
<wfs:GetFeature xmlns:wfs="http://www.opengis.net/wfs" service="WFS" version="1.1.0" xsi:schemaLocation="http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.1.0/wfs.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" maxFeatures="%(maxfeatures)i">
%(query)s
</wfs:GetFeature>"""
    QUERY = u"""<wfs:Query typeName="feature:%(feature)s" srsName="EPSG:4326" xmlns:feature="http://mapserver.gis.umn.edu/mapserver">
<ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
<ogc:PropertyIs%(function)s %(arguments)s>
<ogc:PropertyName>%(property)s</ogc:PropertyName>
<ogc:Literal>%(value)s</ogc:Literal>
</ogc:PropertyIs%(function)s>
</ogc:Filter>
</wfs:Query>"""
    GEOM_QUERY = u"""<wfs:Query typeName="feature:%(feature)s" srsName="EPSG:4326" xmlns:feature="http://mapserver.gis.umn.edu/mapserver">
<ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
<ogc:Intersects>
<ogc:PropertyName>the_geom</ogc:PropertyName>
<gml:Polygon xmlns:gml="http://www.opengis.net/gml" srsName="EPSG:4326">
<gml:exterior>
<gml:LinearRing>
<gml:posList>%(poslist)s</gml:posList>
</gml:LinearRing>
</gml:exterior>
</gml:Polygon>
</ogc:Intersects>
</ogc:Filter>
</wfs:Query>"""

    RESULT_MISSING = u"""<?xml version='1.0' encoding="UTF-8" ?>
<wfs:FeatureCollection
   xmlns:ms="http://mapserver.gis.umn.edu/mapserver"
   xmlns:gml="http://www.opengis.net/gml"
   xmlns:wfs="http://www.opengis.net/wfs"
   xmlns:ogc="http://www.opengis.net/ogc"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
PASS...
   <gml:boundedBy>
      <gml:Null>missing</gml:Null>
   </gml:boundedBy>
</wfs:FeatureCollection>"""
    RESULT = u"""<?xml version='1.0' encoding="UTF-8" ?>
<wfs:FeatureCollection
   xmlns:ms="http://mapserver.gis.umn.edu/mapserver"
   xmlns:gml="http://www.opengis.net/gml"
   xmlns:wfs="http://www.opengis.net/wfs"
   xmlns:ogc="http://www.opengis.net/ogc"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
PASS...
      <gml:boundedBy>
      	<gml:Envelope srsName="EPSG:4326">
      		<gml:lowerCorner>%(lowerCorner)s</gml:lowerCorner>
      		<gml:upperCorner>%(upperCorner)s</gml:upperCorner>
      	</gml:Envelope>
      </gml:boundedBy>%(features)s
</wfs:FeatureCollection>
"""

    FEATURE_RESULT = u"""
    <gml:featureMember>
      <ms:%%(feature)s gml:id="%%(feature)s.%(gid)i">
        <gml:boundedBy>
        	<gml:Envelope srsName="EPSG:4326">
        		<gml:lowerCorner>%(lowerCorner)s</gml:lowerCorner>
        		<gml:upperCorner>%(upperCorner)s</gml:upperCorner>
        	</gml:Envelope>
        </gml:boundedBy>
        <ms:the_geom>
          <gml:Point srsName="EPSG:4326">
            <gml:pos>%(pos)s</gml:pos>
          </gml:Point>
        </ms:the_geom>
        <ms:gid>%(gid)i</ms:gid>
        <ms:int>%(int)i</ms:int>
        <ms:real>%(real)s</ms:real>
        <ms:character>%(character)s</ms:character>
        <ms:date>%(date)i-10-19 10:23:54</ms:date>
        <ms:boolean>%(boolean)s</ms:boolean>
      </ms:%%(feature)s>
    </gml:featureMember>"""
    FEATURE_RESULT_2 = {
        'lowerCorner': '2.000000 2.000000',
        'upperCorner': '2.000000 2.000000',
        'features': FEATURE_RESULT % {
            'lowerCorner': '2.000000 2.000000',
            'upperCorner': '2.000000 2.000000',
            'pos': '2.000000 2.000000',
            'gid': 2,
            'int': 2,
            'real': '2.2',
            'character': u'abCéàè2',
            'date': 2002,
            'boolean': 'f',
        }
    }
    FEATURE_RESULT_3 = {
        'lowerCorner': '3.000000 3.000000',
        'upperCorner': '3.000000 3.000000',
        'features': FEATURE_RESULT % {
            'lowerCorner': '3.000000 3.000000',
            'upperCorner': '3.000000 3.000000',
            'pos': '3.000000 3.000000',
            'gid': 3,
            'int': 3,
            'real': '3.3',
            'character': u'abCéàè3',
            'date': 2003,
            'boolean': 'f',
        }        
    }


    FEATURE_SHP_RESULT = u"""
    <gml:featureMember>
      <ms:%%(feature)s gml:id="%%(feature)s.%(gid)i">
        <gml:boundedBy>
        	<gml:Envelope srsName="EPSG:4326">
        		<gml:lowerCorner>%(lowerCorner)s</gml:lowerCorner>
        		<gml:upperCorner>%(upperCorner)s</gml:upperCorner>
        	</gml:Envelope>
        </gml:boundedBy>
        <ms:the_geom>
          <gml:Point srsName="EPSG:4326">
            <gml:pos>%(pos)s</gml:pos>
          </gml:Point>
        </ms:the_geom>
        <ms:INT>%(int)i</ms:INT>
        <ms:REAL>%(real)s</ms:REAL>
        <ms:CHARACTER>%(character)s</ms:CHARACTER>
        <ms:DATE>%(date)i-10-19 10:23:54</ms:DATE>
        <ms:BOOLEAN>%(boolean)s</ms:BOOLEAN>
      </ms:%%(feature)s>
    </gml:featureMember>"""
    FEATURE_SHP_RESULT_2 = {
        'lowerCorner': '2.000000 2.000000',
        'upperCorner': '2.000000 2.000000',
        'features': FEATURE_SHP_RESULT % {
            'lowerCorner': '2.000000 2.000000',
            'upperCorner': '2.000000 2.000000',
            'pos': '2.000000 2.000000',
            'gid': 2,
            'int': 2,
            'real': '2.2',
            'character': u'abCéàè2',
            'date': 2002,
            'boolean': 'F',
        }
    }
    FEATURE_SHP_RESULT_3 = {
        'lowerCorner': '3.000000 3.000000',
        'upperCorner': '3.000000 3.000000',
        'features': FEATURE_SHP_RESULT % {
            'lowerCorner': '3.000000 3.000000',
            'upperCorner': '3.000000 3.000000',
            'pos': '3.000000 3.000000',
            'gid': 3,
            'int': 3,
            'real': '3.3',
            'character': u'abCéàè3',
            'date': 2003,
            'boolean': 'F',
        }        
    }

    # With mapserver 6.0.0 when we do a geom filter and a maxFeatures=1 we don't reseive any features.
    def test_max_features(self):
        REQUETS = (
            ('postgis-point-auto', u'int', 2, self.FEATURE_RESULT_2),
            ('postgis-point-auto', u'int', 3, self.FEATURE_RESULT_3),
            ('postgis-point-auto', u'real', '2.2', self.FEATURE_RESULT_2),
            ('postgis-point-auto', u'real', '3.3', self.FEATURE_RESULT_3),
            ('postgis-point-auto', u'character', u'abCéàè2', self.FEATURE_RESULT_2),
            ('postgis-point-auto', u'character', u'abCéàè3', self.FEATURE_RESULT_3),
            ('postgis-point', u'int', 2, self.FEATURE_RESULT_2),
            ('postgis-point', u'int', 3, self.FEATURE_RESULT_3),
            ('postgis-point', u'real', '2.2', self.FEATURE_RESULT_2),
            ('postgis-point', u'real', '3.3', self.FEATURE_RESULT_3),
            ('postgis-point', u'character', u'abCéàè2', self.FEATURE_RESULT_2),
            ('postgis-point', u'character', u'abCéàè3', self.FEATURE_RESULT_3),
            ('shp-point-auto', u'INT', 2, self.FEATURE_SHP_RESULT_2),
            ('shp-point-auto', u'INT', 3, self.FEATURE_SHP_RESULT_3),
            ('shp-point-auto', u'REAL', '2.2', self.FEATURE_SHP_RESULT_2),
            ('shp-point-auto', u'REAL', '3.3', self.FEATURE_SHP_RESULT_3),
            ('shp-point-auto', u'CHARACTER', u'abCéàè2', self.FEATURE_SHP_RESULT_2),
            ('shp-point-auto', u'CHARACTER', u'abCéàè3', self.FEATURE_SHP_RESULT_3),
            ('shp-point', u'INT', 2, self.FEATURE_SHP_RESULT_2),
            ('shp-point', u'INT', 3, self.FEATURE_SHP_RESULT_3),
            ('shp-point', u'REAL', '2.2', self.FEATURE_SHP_RESULT_2),
            ('shp-point', u'REAL', '3.3', self.FEATURE_SHP_RESULT_3),
            ('shp-point', u'CHARACTER', u'abCéàè2', self.FEATURE_SHP_RESULT_2),
            ('shp-point', u'CHARACTER', u'abCéàè3', self.FEATURE_SHP_RESULT_3),
        )
        for r in REQUETS:
            log.info((r[0], r[1], r[2]))
            log.info((r[3]))
            content = self._post(self.GETFEATURE_REQUEST % {
                'maxfeatures': 10,
                'query': self.QUERY % {
                    'feature': r[0],
                    'function': u'EqualTo',
                    'arguments': u'',
                    'property': r[1],
                    'value': r[2],
                }
            })
            p = copy(r[3])
            p['features'] = p['features'] % {'feature': r[0] }
            self._assert_result_equals(content, self.RESULT % p)


        REQUETS = (
            ('postgis-point-auto', u'1.5 1.5 1.5 2.5 2.5 2.5 2.5 1.5 1.5 1.5', self.FEATURE_RESULT_2),
            ('postgis-point-auto', u'2.5 2.5 2.5 3.5 3.5 3.5 3.5 2.5 2.5 2.5', self.FEATURE_RESULT_3),
            ('postgis-point', u'1.5 1.5 1.5 2.5 2.5 2.5 2.5 1.5 1.5 1.5', self.FEATURE_RESULT_2),
            ('postgis-point', u'2.5 2.5 2.5 3.5 3.5 3.5 3.5 2.5 2.5 2.5', self.FEATURE_RESULT_3),
            ('shp-point-auto', u'1.5 1.5 1.5 2.5 2.5 2.5 2.5 1.5 1.5 1.5', self.FEATURE_SHP_RESULT_2),
            ('shp-point-auto', u'2.5 2.5 2.5 3.5 3.5 3.5 3.5 2.5 2.5 2.5', self.FEATURE_SHP_RESULT_3),
            ('shp-point', u'1.5 1.5 1.5 2.5 2.5 2.5 2.5 1.5 1.5 1.5', self.FEATURE_SHP_RESULT_2),
            ('shp-point', u'2.5 2.5 2.5 3.5 3.5 3.5 3.5 2.5 2.5 2.5', self.FEATURE_SHP_RESULT_3),

        )
        for r in REQUETS:
            log.info((r[0], r[1]))
            content = self._post(self.GETFEATURE_REQUEST % {
                'maxfeatures': 1,
                'query': self.GEOM_QUERY % {
                    'feature': r[0],
                    'poslist': r[1],
                }
            })
            p = copy(r[2])
            p['features'] = p['features'] % {'feature': r[0] }
            self._assert_result_equals(content, self.RESULT % p)


    # With mapserver 6.0.0 when we do a case insensitive request on an integer we have an SQL error.
    def test_case_sensitive(self):
        REQUETS = (
            ('postgis-point-auto', None, 'character', u'ABcéàè2', u''),
            ('postgis-point-auto', None, 'character', u'ABcéàè2', u'matchCase="true"'),
            ('postgis-point-auto', self.FEATURE_RESULT_2, 'character', u'ABcéàè2', u'matchCase="false"'),
            ('postgis-point-auto', self.FEATURE_RESULT_2, 'int', 2, u''),
            ('postgis-point-auto', self.FEATURE_RESULT_2, 'int', 2, u'matchCase="true"'),
            ('postgis-point-auto', self.FEATURE_RESULT_2, 'int', 2, u'matchCase="false"'),
            ('postgis-point-auto', self.FEATURE_RESULT_2, 'real', u'2.2', u''),
            ('postgis-point-auto', self.FEATURE_RESULT_2, 'real', u'2.2', u'matchCase="true"'),
            ('postgis-point-auto', self.FEATURE_RESULT_2, 'real', u'2.2', u'matchCase="false"'),
            ('postgis-point', None, 'character', u'ABcéàè2', u''),
            ('postgis-point', None, 'character', u'ABcéàè2', u'matchCase="true"'),
            ('postgis-point', self.FEATURE_RESULT_2, 'character', u'ABcéàè2', u'matchCase="false"'),
            ('postgis-point', self.FEATURE_RESULT_2, 'int', 2, u''),
            ('postgis-point', self.FEATURE_RESULT_2, 'int', 2, u'matchCase="true"'),
            ('postgis-point', self.FEATURE_RESULT_2, 'int', 2, u'matchCase="false"'),
            ('postgis-point', self.FEATURE_RESULT_2, 'real', u'2.2', u''),
            ('postgis-point', self.FEATURE_RESULT_2, 'real', u'2.2', u'matchCase="true"'),
            ('postgis-point', self.FEATURE_RESULT_2, 'real', u'2.2', u'matchCase="false"'),
            ('shp-point-auto', None, 'CHARACTER', u'ABcéàè2', u''),
            ('shp-point-auto', None, 'CHARACTER', u'ABcéàè2', u'matchCase="true"'),
            ('shp-point-auto', self.FEATURE_SHP_RESULT_2, 'CHARACTER', u'ABcéàè2', u'matchCase="false"'),
            ('shp-point-auto', self.FEATURE_SHP_RESULT_2, 'INT', 2, u''),
            ('shp-point-auto', self.FEATURE_SHP_RESULT_2, 'INT', 2, u'matchCase="true"'),
            ('shp-point-auto', self.FEATURE_SHP_RESULT_2, 'INT', 2, u'matchCase="false"'),
            ('shp-point-auto', self.FEATURE_SHP_RESULT_2, 'REAL', u'2.2', u''),
            ('shp-point-auto', self.FEATURE_SHP_RESULT_2, 'REAL', u'2.2', u'matchCase="true"'),
            ('shp-point-auto', self.FEATURE_SHP_RESULT_2, 'REAL', u'2.2', u'matchCase="false"'),
            ('shp-point', None, 'CHARACTER', u'ABcéàè2', u''),
            ('shp-point', None, 'CHARACTER', u'ABcéàè2', u'matchCase="true"'),
            ('shp-point', self.FEATURE_SHP_RESULT_2, 'CHARACTER', u'ABcéàè2', u'matchCase="false"'),
            ('shp-point', self.FEATURE_SHP_RESULT_2, 'INT', 2, u''),
            ('shp-point', self.FEATURE_SHP_RESULT_2, 'INT', 2, u'matchCase="true"'),
            ('shp-point', self.FEATURE_SHP_RESULT_2, 'INT', 2, u'matchCase="false"'),
            ('shp-point', self.FEATURE_SHP_RESULT_2, 'REAL', u'2.2', u''),
            ('shp-point', self.FEATURE_SHP_RESULT_2, 'REAL', u'2.2', u'matchCase="true"'),
            ('shp-point', self.FEATURE_SHP_RESULT_2, 'REAL', u'2.2', u'matchCase="false"'),
        )
        for r in REQUETS:
            log.info((r[0], r[2], r[3], r[4]))
            content = self._post(self.GETFEATURE_REQUEST % {
                'maxfeatures': 10, # should works with 1
                'query': self.QUERY % {
                    'feature': r[0],
                    'function': u'EqualTo',
                    'arguments': r[4],
                    'property': r[2],
                    'value': r[3],
                }
            })
            if r[1]:
                p = copy(r[1])
                p['features'] = p['features'] % {'feature': r[0] }
                self._assert_result_equals(content, self.RESULT % p)
            else:
                self._assert_result_equals(content, self.RESULT_MISSING)


    # With mapserver 6.0.3 when we do a request on two shapefile we reseive an error 500.
    def test_multiple_feature_type(self):
        REQUET = (
            ('postgis-point-auto', self.FEATURE_RESULT_2, 'int', 2),
            ('postgis-point', self.FEATURE_RESULT_2, 'int', 2),
            ('shp-point-auto', self.FEATURE_SHP_RESULT_2, 'INT', 2),
            ('shp-point', self.FEATURE_SHP_RESULT_2, 'INT', 2),
        )
        query = ''
        result = ''
        for r in REQUET:
            log.info((r[0], r[2], r[3]))
            query += self.QUERY % {
                'feature': r[0],
                'function': u'EqualTo',
                'arguments': '',
                'property': r[2],
                'value': r[3],
            }
            result += r[1]['features'] % {'feature': r[0] }
        content = self._post(self.GETFEATURE_REQUEST % {
            'maxfeatures': 10,
            'query': query
        })
        self._assert_result_equals(content, self.RESULT % {
            'lowerCorner': '2.000000 2.000000',
            'upperCorner': '2.000000 2.000000',
            'features': result
        })
