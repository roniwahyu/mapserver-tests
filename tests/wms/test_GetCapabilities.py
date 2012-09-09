# -*- coding: utf-8 -*-

from tests import TestXML

class TestGetCapabilities(TestXML):
    def test_GetCapabilities(self):
        response, content = self.http.request(self.url + \
            "REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.0.0")
        self._assert_result_equals(content, u"""<?xml version='1.0' encoding="UTF-8" standalone="no" ?>
<!DOCTYPE WMT_MS_Capabilities SYSTEM "http://schemas.opengis.net/wms/1.0.0/capabilities_1_0_0.dtd"
 [
 <!ELEMENT VendorSpecificCapabilities EMPTY>
 ]>  <!-- end of DOCTYPE declaration -->

<WMT_MS_Capabilities version="1.0.0">

PASS...

<Service>
  <Name>GetMap</Name>
  <Title>Tests</Title>
  <OnlineResource>http://example.com/ogc?</OnlineResource>
</Service>

<Capability>
  <Request>
    <Map>
      <Format><GIF /><PNG /><JPEG /><SVG /></Format>
      <DCPType>
        <HTTP>
          <Get onlineResource="http://example.com/ogc?" />
          <Post onlineResource="http://example.com/ogc?" />
        </HTTP>
      </DCPType>
    </Map>
    <Capabilities>
      <Format><WMS_XML /></Format>
      <DCPType>
        <HTTP>
          <Get onlineResource="http://example.com/ogc?" />
          <Post onlineResource="http://example.com/ogc?" />
        </HTTP>
      </DCPType>
    </Capabilities>
    <FeatureInfo>
      <Format><MIME /><GML.1 /></Format>
      <DCPType>
        <HTTP>
          <Get onlineResource="http://example.com/ogc?" />
          <Post onlineResource="http://example.com/ogc?" />
        </HTTP>
      </DCPType>
    </FeatureInfo>
  </Request>
  <Exception>
    <Format><BLANK /><INIMAGE /><WMS_XML /></Format>
  </Exception>
  <VendorSpecificCapabilities />
  <Layer>
    <Name>Tests</Name>
    <Title>Tests</Title>
    <Abstract>Tests</Abstract>
    <SRS>EPSG:4326</SRS>
    <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    <BoundingBox SRS="EPSG:4326"
                minx="-10" miny="-10" maxx="10" maxy="10" />
    <Layer queryable="0">
        <Name>postgis-point-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>postgis-line-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>postgis-polygon-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>postgis-point</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>postgis-line</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>postgis-polygon</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>shp-point-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>shp-line-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>shp-polygon-auto</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>shp-point</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>shp-line</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="0">
        <Name>shp-polygon</Name>
        <Title>Layer</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
  </Layer>
</Capability>
</WMT_MS_Capabilities>""")
