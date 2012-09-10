# -*- coding: utf-8 -*-

from tests import TestXML

class TestGetCapabilities(TestXML):
    def test_GetCapabilities(self):
        content = self._get((
            ('SERVICE', 'WFS'),
            ('VERSION', '1.0.0'),
            ('REQUEST', 'GetCapabilities'),
        ))
        self._assert_result_equals(content, u"""<?xml version='1.0' encoding="UTF-8" ?>
<WFS_Capabilities
   version="1.0.0"
   updateSequence="0"
   xmlns="http://www.opengis.net/wfs"
   xmlns:ogc="http://www.opengis.net/ogc"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.0.0/WFS-capabilities.xsd">

PASS...

<Service>
  <Name>MapServer WFS</Name>
  <Title>Tests</Title>
  <OnlineResource>http://example.com/ogc?</OnlineResource>
</Service>

<Capability>
  <Request>
    <GetCapabilities>
      <DCPType>
        <HTTP>
          <Get onlineResource="http://example.com/ogc?" />
        </HTTP>
      </DCPType>
      <DCPType>
        <HTTP>
          <Post onlineResource="http://example.com/ogc?" />
        </HTTP>
      </DCPType>
    </GetCapabilities>
    <DescribeFeatureType>
      <SchemaDescriptionLanguage>
        <XMLSCHEMA/>
      </SchemaDescriptionLanguage>
      <DCPType>
        <HTTP>
          <Get onlineResource="http://example.com/ogc?" />
        </HTTP>
      </DCPType>
      <DCPType>
        <HTTP>
          <Post onlineResource="http://example.com/ogc?" />
        </HTTP>
      </DCPType>
    </DescribeFeatureType>
    <GetFeature>
      <ResultFormat>
        <GML2/>
      </ResultFormat>
      <DCPType>
        <HTTP>
          <Get onlineResource="http://example.com/ogc?" />
        </HTTP>
      </DCPType>
      <DCPType>
        <HTTP>
          <Post onlineResource="http://example.com/ogc?" />
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
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>postgis-polygon-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>postgis-point</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>postgis-line</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>postgis-polygon</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-point-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-line-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-polygon-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-point</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-line</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>shp-polygon</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLongBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    </FeatureType>
    <FeatureType>
        <Name>wfs-point</Name>
        <Title>Layer éàè</Title>
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
