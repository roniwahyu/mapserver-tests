# -*- coding: utf-8 -*-

from wfs import url, TestWFS

class TestMapServerWFS(TestCase):
    def test_describe_feature(self):
        http = httplib2.Http()
        response, content = http.request(self.url +
            "&TYPENAME=postgis-point-auto" +
            "&REQUEST=DescribeFeatureType&SERVICE=WFS&VERSION=1.0.0")
            #service=WFS&version=1.0.0&REQUEST=GetCapabilities
        self.assertEquals(int(response['status']), 200)
        print content
        for t in zip(unicode(content.decode('utf-8')).split('\n'),
            u'''<?xml version='1.0' encoding="UTF-8" ?>
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
<element name="testpoint_unprotected"
type="ms:testpoint_unprotectedType"
substitutionGroup="gml:_Feature" />
<complexType name="testpoint_unprotectedType">
<complexContent>
<extension base="gml:AbstractFeatureType">
<sequence>
<element name="the_geom" type="gml:PointPropertyType" minOccurs="0" maxOccurs="1"/>
<element name="name" type="Character"/>
<element name="city" type="Character"/>
<element name="country" type="Character"/>
<element name="integer" type="Integer"/>
<element name="float" type="Real"/>
</sequence>
</extension>
</complexContent>
</complexType>
</schema>'''.split('\n')):
            self.assertEquals(t[0], t[1])


    GETFEATURE_REQUEST = u"""<?xml version='1.0' encoding="UTF-8" ?>
<wfs:GetFeature xmlns:wfs="http://www.opengis.net/wfs" service="WFS" version="1.1.0" xsi:schemaLocation="http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.1.0/wfs.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" maxFeatures="%(maxfeatures)i">
%(query)s
</wfs:GetFeature>"""
    QUERY = u"""<<wfs:Query typeName="feature:%(feature)s" srsName="EPSG:21781" xmlns:feature="http://mapserver.gis.umn.edu/mapserver">
<ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
<ogc:PropertyIs%(function)s %(arguments)s>
<ogc:PropertyName>%(property)s</ogc:PropertyName>
<ogc:Literal>%(value)s</ogc:Literal>
</ogc:PropertyIs%(function)s>
</ogc:Filter>
</wfs:Query>"""


# Integer|Real|Character|Date|Boolean

