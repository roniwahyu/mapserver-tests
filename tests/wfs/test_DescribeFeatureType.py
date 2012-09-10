# -*- coding: utf-8 -*-

import logging
from tests import TestXML

log = logging.getLogger(__name__)

class TestDescribeFeatureType(TestXML):
    DESCRIBE_FEATURE_TYPE = """<?xml version='1.0' encoding="UTF-8" ?>
<schema
   targetNamespace="http://mapserver.gis.umn.edu/mapserver"
   xmlns:ms="http://mapserver.gis.umn.edu/mapserver"
   xmlns:ogc="http://www.opengis.net/ogc"
   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
   xmlns="http://www.w3.org/2001/XMLSchema"
   xmlns:gml="http://www.opengis.net/gml"
   elementFormDefault="qualified" version="0.1" >

  <import namespace="http://www.opengis.net/gml"
          schemaLocation="http://schemas.opengis.net/gml/2.1.2/feature.xsd" />

  <element name="%(feature)s"
           type="ms:%(feature)sType"
           substitutionGroup="gml:_Feature" />

  <complexType name="%(feature)sType">
    <complexContent>
      <extension base="gml:AbstractFeatureType">
        <sequence>%(elements)s
        </sequence>
      </extension>
    </complexContent>
  </complexType>

</schema>"""

    ELEMENTS = """
          <element name="the_geom" type="gml:%(shape)sPropertyType" minOccurs="0" maxOccurs="1"/>
          <element name="gid" type="Integer"/>
          <element name="int" type="Integer"/>
          <element name="real" type="Real"/>
          <element name="character" type="Character"/>
          <element name="date" type="Date"/>
          <element name="boolean" type="Boolean"/>"""
    ELEMENTS_AUTO = """
          <element name="the_geom" type="gml:%(shape)sPropertyType" minOccurs="0" maxOccurs="1"/>
          <element name="gid" type="Integer"/>
          <element name="int" type="Integer"/>
          <element name="real" type="Real"/>
          <element name="character" type="Character"/>
          <element name="date" type="Date"/>
          <element name="boolean" type="Integer"/>"""
# should be removed ... <element name="boolean" type="Boolean"/>

    ELEMENTS_SHP = """
          <element name="the_geom" type="gml:%(shape)sPropertyType" minOccurs="0" maxOccurs="1"/>
          <element name="INT" type="Integer"/>
          <element name="REAL" type="Real"/>
          <element name="CHARACTER" type="Character"/>
          <element name="DATE" type="Date"/>
          <element name="BOOLEAN" type="Boolean"/>"""
    ELEMENTS_SHP_AUTO = """
          <element name="the_geom" type="gml:%(shape)sPropertyType" minOccurs="0" maxOccurs="1"/>
          <element name="INT" type="Integer"/>
          <element name="REAL" type="Real"/>
          <element name="CHARACTER" type="Character"/>
          <element name="DATE" type="Character"/>
          <element name="BOOLEAN" type="Character"/>"""
# should be removed ... <element name="DATE" type="Date"/>, <element name="boolean" type="Boolean"/>

    LAYERS = [
        ('postgis-point-auto', 'Point', ELEMENTS_AUTO),
        ('postgis-line-auto', 'LineString', ELEMENTS_AUTO),
        ('postgis-polygon-auto', 'Polygon', ELEMENTS_AUTO),
        ('postgis-point', 'Point', ELEMENTS),
        ('postgis-line', 'LineString', ELEMENTS),
        ('postgis-polygon', 'Polygon', ELEMENTS),
        ('shp-point-auto', 'Point', ELEMENTS_SHP_AUTO),
        ('shp-line-auto', 'LineString', ELEMENTS_SHP_AUTO),
        ('shp-polygon-auto', 'Polygon', ELEMENTS_SHP_AUTO),
        ('shp-point', 'Point', ELEMENTS_SHP),
        ('shp-line', 'LineString', ELEMENTS_SHP),
        ('shp-polygon', 'Polygon', ELEMENTS_SHP),
        ('wfs-point', 'Point', ELEMENTS),
    ]

    def test_GetCapabilities(self):
        for l in self.LAYERS:
            log.info("test feature type %s" % l[0])
            url = self.url + \
                "&TYPENAME=%s" % l[0] + \
                "&REQUEST=DescribeFeatureType&SERVICE=WFS&VERSION=1.0.0"
            log.info(url)
            response, content = self.http.request(url)
            self._assert_result_equals(content, self.DESCRIBE_FEATURE_TYPE % {
                'feature': l[0],
                'elements': l[2] % {
                    'shape': l[1]
                }
            })
