# -*- coding: utf-8 -*-

from wfs import TestWFS

class TestGetFeature(TestWFS):
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

    def test_GetCapabilities(self):
        response, content = self.http.request(self.url + \
            "REQUEST=GetCapabilities&SERVICE=WFS&VERSION=1.0.0")
        self._assert_result_equals(content, """<?xml version='1.0' encoding="UTF-8" ?>
<WFS_Capabilities 
   version="1.0.0" 
   updateSequence="0" 
   xmlns="http://www.opengis.net/wfs" 
   xmlns:ogc="http://www.opengis.net/ogc" 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.0.0/WFS-capabilities.xsd">

<!-- MapServer version 6.3-dev OUTPUT=GIF OUTPUT=PNG OUTPUT=JPEG SUPPORTS=PROJ SUPPORTS=GD SUPPORTS=AGG SUPPORTS=FREETYPE SUPPORTS=CAIRO SUPPORTS=ICONV SUPPORTS=FRIBIDI SUPPORTS=WMS_SERVER SUPPORTS=WMS_CLIENT SUPPORTS=WFS_SERVER SUPPORTS=WFS_CLIENT SUPPORTS=WCS_SERVER SUPPORTS=SOS_SERVER SUPPORTS=FASTCGI SUPPORTS=THREADS SUPPORTS=GEOS INPUT=JPEG INPUT=POSTGIS INPUT=OGR INPUT=GDAL INPUT=SHAPEFILE -->

<Service>
  <Name>MapServer WFS</Name>
  <Title>Tests</Title>
  <OnlineResource>http://localhost/mapserv-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&amp;</OnlineResource>
</Service>

<Capability>
  <Request>
    <GetCapabilities>
      <DCPType>
        <HTTP>
          <Get onlineResource="http://localhost/mapserv-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&amp;" />
        </HTTP>
      </DCPType>
      <DCPType>
        <HTTP>
          <Post onlineResource="http://localhost/mapserv-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&amp;" />
        </HTTP>
      </DCPType>
    </GetCapabilities>
    <DescribeFeatureType>
      <SchemaDescriptionLanguage>
        <XMLSCHEMA/>
      </SchemaDescriptionLanguage>
      <DCPType>
        <HTTP>
          <Get onlineResource="http://localhost/mapserv-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&amp;" />
        </HTTP>
      </DCPType>
      <DCPType>
        <HTTP>
          <Post onlineResource="http://localhost/mapserv-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&amp;" />
        </HTTP>
      </DCPType>
    </DescribeFeatureType>
    <GetFeature>
      <ResultFormat>
        <GML2/>
      </ResultFormat>
      <DCPType>
        <HTTP>
          <Get onlineResource="http://localhost/mapserv-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&amp;" />
        </HTTP>
      </DCPType>
      <DCPType>
        <HTTP>
          <Post onlineResource="http://localhost/mapserv-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&amp;" />
        </HTTP>
      </DCPType>
    </GetFeature>
  </Request>
</Capability>

<FeatureTypeList>
  <Operations>
    <Query/>
  </Operations>
    <FeatureType>
        <Name>postgis-point-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>postgis-line-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>postgis-polygon-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>postgis-point</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>postgis-line</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>postgis-polygon</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-point-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-line-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-polygon-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-point</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-line</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-polygon</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
</FeatureTypeList>

<ogc:Filter_Capabilities>
  <ogc:Spatial_Capabilities>
    <ogc:Spatial_Operators>
      <ogc:Equals/>
      <ogc:Disjoint/>
      <ogc:Touches/>
      <ogc:Within/>
      <ogc:Overlaps/>
      <ogc:Crosses/>
      <ogc:Intersect/>
      <ogc:Contains/>
      <ogc:DWithin/>
      <ogc:BBOX/>
    </ogc:Spatial_Operators>
  </ogc:Spatial_Capabilities>
  <ogc:Scalar_Capabilities>
    <ogc:Logical_Operators />
    <ogc:Comparison_Operators>
      <ogc:Simple_Comparisons />
      <ogc:Like />
      <ogc:Between />
    </ogc:Comparison_Operators>
  </ogc:Scalar_Capabilities>
</ogc:Filter_Capabilities>

</WFS_Capabilities>""")
