# -*- coding: utf-8 -*-

from tests import TestXML

class TestGetCapabilities(TestXML):
    def test_GetCapabilities(self):
        content = self._get((
            ('SERVICE', 'WMS'),
            ('VERSION', '1.1.1'),
            ('REQUEST', 'GetCapabilities'),
        ))
        self._assert_result_equals(content, u"""<?xml version='1.0' encoding="UTF-8" standalone="no" ?>
<!DOCTYPE WMT_MS_Capabilities SYSTEM "http://schemas.opengis.net/wms/1.1.1/WMS_MS_Capabilities.dtd"
 [
 <!ELEMENT VendorSpecificCapabilities EMPTY>
 ]>

<WMT_MS_Capabilities version="1.1.1">



<Service>
  <Name>OGC:WMS</Name>
  <Title>Tests</Title>
  <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/>
  <ContactInformation>
  </ContactInformation>
</Service>

<Capability>
  <Request>
    <GetCapabilities>
      <Format>application/vnd.ogc.wms_xml</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Post>
        </HTTP>
      </DCPType>
    </GetCapabilities>
    <GetMap>
      <Format>image/png</Format>
      <Format>image/jpeg</Format>
      <Format>image/gif</Format>
      <Format>image/png; mode=8bit</Format>
      <Format>application/x-pdf</Format>
      <Format>image/svg+xml</Format>
      <Format>image/tiff</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Post>
        </HTTP>
      </DCPType>
    </GetMap>
    <GetFeatureInfo>
      <Format>text/plain</Format>
      <Format>application/vnd.ogc.gml</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Post>
        </HTTP>
      </DCPType>
    </GetFeatureInfo>
    <DescribeLayer>
      <Format>text/xml</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Post>
        </HTTP>
      </DCPType>
    </DescribeLayer>
    <GetLegendGraphic>
      <Format>image/png</Format>
      <Format>image/jpeg</Format>
      <Format>image/gif</Format>
      <Format>image/png; mode=8bit</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Post>
        </HTTP>
      </DCPType>
    </GetLegendGraphic>
    <GetStyles>
      <Format>text/xml</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://example.com/ogc?"/></Post>
        </HTTP>
      </DCPType>
    </GetStyles>
  </Request>
  <Exception>
    <Format>application/vnd.ogc.se_xml</Format>
    <Format>application/vnd.ogc.se_inimage</Format>
    <Format>application/vnd.ogc.se_blank</Format>
  </Exception>
  <VendorSpecificCapabilities />
  <UserDefinedSymbolization SupportSLD="1" UserLayer="0" UserStyle="1" RemoteWFS="0"/>
  <Layer>
    <Name>Tests</Name>
    <Title>Tests</Title>
    <Abstract>Tests</Abstract>
    <SRS>EPSG:4326</SRS>
    <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
    <BoundingBox SRS="EPSG:4326"
                minx="-10" miny="-10" maxx="10" maxy="10" />
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>postgis-point-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>postgis-line-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>postgis-polygon-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>postgis-point</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="65" height="21">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://example.com/ogc?version=1.1.1&amp;service=WMS&amp;request=GetLegendGraphic&amp;layer=postgis-point&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
        <ScaleHint min="2.49451424214819" max="249.451424214819" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>postgis-line</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>postgis-polygon</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>shp-point-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>shp-line-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>shp-polygon-auto</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>shp-point</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="65" height="21">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://example.com/ogc?version=1.1.1&amp;service=WMS&amp;request=GetLegendGraphic&amp;layer=shp-point&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
        <ScaleHint min="2.49451424214819" max="249.451424214819" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>shp-line</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>shp-polygon</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="1">
        <Name>wms-point</Name>
        <Title>WMS client</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>wfs-point</Name>
        <Title>Layer éàè</Title>
        <SRS>EPSG:4326</SRS>
        <LatLonBoundingBox minx="-10" miny="-10" maxx="10" maxy="10" />
        <BoundingBox SRS="EPSG:4326"
                    minx="-10" miny="-10" maxx="10" maxy="10" />
        <ScaleHint min="2.49451424214819" max="249.451424214819" />
    </Layer>
  </Layer>
</Capability>
</WMT_MS_Capabilities>""")
