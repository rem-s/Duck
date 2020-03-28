<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.2.0">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="24" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="Switch">
<packages>
<package name="PUSH_SW">
<pad name="P1" x="-3.81" y="0" drill="1" shape="long"/>
<pad name="P2" x="-3.81" y="-5.08" drill="1" shape="long"/>
<pad name="P3" x="3.81" y="0" drill="1" shape="long"/>
<pad name="P4" x="3.81" y="-5.08" drill="1" shape="long"/>
<wire x1="-3.81" y1="0" x2="-3.81" y2="-5.08" width="0.127" layer="21"/>
<wire x1="-3.81" y1="-5.08" x2="3.81" y2="-5.08" width="0.127" layer="21"/>
<wire x1="3.81" y1="-5.08" x2="3.81" y2="0" width="0.127" layer="21"/>
<wire x1="3.81" y1="0" x2="-3.81" y2="0" width="0.127" layer="21"/>
<circle x="0" y="-2.54" radius="2.54" width="0.127" layer="21"/>
<circle x="0" y="-2.54" radius="1.27" width="0.127" layer="21"/>
</package>
</packages>
<symbols>
<symbol name="PUSH_SW">
<pin name="P1" x="-5.08" y="0" visible="off" length="short"/>
<pin name="P2" x="-5.08" y="-2.54" visible="off" length="short"/>
<pin name="P3" x="2.54" y="0" visible="off" length="short" rot="R180"/>
<pin name="P4" x="2.54" y="-2.54" visible="off" length="short" rot="R180"/>
<wire x1="-2.54" y1="-2.54" x2="-2.54" y2="0" width="0.254" layer="94"/>
<wire x1="0" y1="0" x2="0" y2="-2.54" width="0.254" layer="94"/>
<wire x1="-2.54" y1="1.016" x2="-1.778" y2="1.016" width="0.254" layer="94"/>
<wire x1="-0.762" y1="1.016" x2="0" y2="1.016" width="0.254" layer="94"/>
<wire x1="-1.778" y1="1.524" x2="-1.778" y2="1.27" width="0.254" layer="94"/>
<wire x1="-1.778" y1="1.27" x2="-1.778" y2="1.016" width="0.254" layer="94"/>
<wire x1="-1.778" y1="1.016" x2="-0.762" y2="1.016" width="0.254" layer="94"/>
<wire x1="-0.762" y1="1.016" x2="-0.762" y2="1.27" width="0.254" layer="94"/>
<wire x1="-0.762" y1="1.27" x2="-0.762" y2="1.524" width="0.254" layer="94"/>
<wire x1="-0.762" y1="1.524" x2="-1.778" y2="1.524" width="0.254" layer="94"/>
<wire x1="-1.778" y1="1.27" x2="-0.762" y2="1.27" width="0.254" layer="94"/>
<wire x1="-0.508" y1="1.27" x2="-0.508" y2="1.524" width="0.254" layer="94"/>
<wire x1="-0.508" y1="1.524" x2="-2.032" y2="1.524" width="0.254" layer="94"/>
<wire x1="-2.032" y1="1.524" x2="-2.032" y2="1.27" width="0.254" layer="94"/>
<wire x1="-0.508" y1="1.27" x2="-2.032" y2="1.27" width="0.254" layer="94"/>
<wire x1="-3.048" y1="1.016" x2="0.508" y2="1.016" width="0.254" layer="94"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="PUSH_SW">
<gates>
<gate name="G$1" symbol="PUSH_SW" x="0" y="0"/>
</gates>
<devices>
<device name="" package="PUSH_SW">
<connects>
<connect gate="G$1" pin="P1" pad="P1"/>
<connect gate="G$1" pin="P2" pad="P2"/>
<connect gate="G$1" pin="P3" pad="P3"/>
<connect gate="G$1" pin="P4" pad="P4"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="ILI9341">
<packages>
<package name="ST7735">
<pad name="CS" x="0" y="-13.97" drill="1" shape="long"/>
<pad name="RST" x="0" y="-11.43" drill="1" shape="long"/>
<pad name="RS" x="0" y="-8.89" drill="1" shape="long"/>
<pad name="SDA" x="0" y="-6.35" drill="1" shape="long"/>
<pad name="CLK" x="0" y="-3.81" drill="1" shape="long"/>
<pad name="NC1" x="0" y="3.81" drill="1" shape="long"/>
<pad name="NC2" x="0" y="1.27" drill="1" shape="long"/>
<pad name="NC3" x="0" y="-1.27" drill="1" shape="long"/>
<pad name="GND1" x="0" y="8.89" drill="1" shape="long"/>
<pad name="GND2" x="0" y="6.35" drill="1" shape="long"/>
<pad name="VCC" x="0" y="11.43" drill="1" shape="long"/>
<wire x1="2.54" y1="12.7" x2="2.54" y2="-15.24" width="0.127" layer="21"/>
<wire x1="2.54" y1="-15.24" x2="-39.37" y2="-15.24" width="0.127" layer="21"/>
<wire x1="-39.37" y1="-15.24" x2="-39.37" y2="12.7" width="0.127" layer="21"/>
<wire x1="-39.37" y1="12.7" x2="2.54" y2="12.7" width="0.127" layer="21"/>
<pad name="SD_CS" x="-38.1" y="-6.35" drill="1" shape="long"/>
<pad name="SD_MOSI" x="-38.1" y="-3.81" drill="1" shape="long"/>
<pad name="SD_SCK" x="-38.1" y="-1.27" drill="1" shape="long"/>
<pad name="SD_MISO" x="-38.1" y="1.27" drill="1" shape="long"/>
<text x="-36.322" y="0.762" size="1.27" layer="21">SD_MISO</text>
<text x="-36.322" y="-1.778" size="1.27" layer="21">SD_SCK</text>
<text x="-36.322" y="-4.318" size="1.27" layer="21">SD_MOSI</text>
<text x="-36.322" y="-6.858" size="1.27" layer="21">SD_CS</text>
<text x="-5.334" y="10.922" size="1.27" layer="21">VCC</text>
<text x="-6.35" y="8.382" size="1.27" layer="21">GND1</text>
<text x="-6.35" y="5.842" size="1.27" layer="21">GND2</text>
<text x="-5.334" y="3.302" size="1.27" layer="21">NC1</text>
<text x="-5.334" y="0.762" size="1.27" layer="21">NC2</text>
<text x="-5.334" y="-1.778" size="1.27" layer="21">NC3</text>
<text x="-5.334" y="-4.318" size="1.27" layer="21">CLK</text>
<text x="-5.334" y="-6.858" size="1.27" layer="21">SDA</text>
<text x="-4.318" y="-9.398" size="1.27" layer="21">RS</text>
<text x="-5.334" y="-11.938" size="1.27" layer="21">RST</text>
<text x="-4.318" y="-14.478" size="1.27" layer="21">CS</text>
<wire x1="-33.782" y1="10.922" x2="-33.782" y2="-14.224" width="0.127" layer="21"/>
<wire x1="-33.782" y1="-14.224" x2="-6.858" y2="-14.224" width="0.127" layer="21"/>
<wire x1="-6.858" y1="-14.224" x2="-6.858" y2="10.922" width="0.127" layer="21"/>
<wire x1="-6.858" y1="10.922" x2="-33.528" y2="10.922" width="0.127" layer="21"/>
<text x="-25.4" y="7.62" size="2.54" layer="21">ST7735</text>
</package>
</packages>
<symbols>
<symbol name="ST7735">
<wire x1="12.7" y1="12.7" x2="-10.16" y2="12.7" width="0.254" layer="94"/>
<wire x1="-10.16" y1="12.7" x2="-10.16" y2="-17.78" width="0.254" layer="94"/>
<wire x1="-10.16" y1="-17.78" x2="12.7" y2="-17.78" width="0.254" layer="94"/>
<wire x1="12.7" y1="-17.78" x2="12.7" y2="12.7" width="0.254" layer="94"/>
<pin name="CS" x="15.24" y="-15.24" visible="pin" length="short" rot="R180"/>
<pin name="RST" x="15.24" y="-12.7" visible="pin" length="short" rot="R180"/>
<pin name="RS" x="15.24" y="-10.16" visible="pin" length="short" rot="R180"/>
<pin name="SDA" x="15.24" y="-7.62" visible="pin" length="short" rot="R180"/>
<pin name="CLK" x="15.24" y="-5.08" visible="pin" length="short" rot="R180"/>
<pin name="NC1" x="15.24" y="2.54" visible="pin" length="short" rot="R180"/>
<pin name="NC2" x="15.24" y="0" visible="pin" length="short" rot="R180"/>
<pin name="NC3" x="15.24" y="-2.54" visible="pin" length="short" rot="R180"/>
<pin name="GND1" x="15.24" y="7.62" visible="pin" length="short" rot="R180"/>
<pin name="VCC" x="15.24" y="10.16" visible="pin" length="short" rot="R180"/>
<text x="-5.08" y="12.7" size="2.54" layer="94">ST7735</text>
<pin name="GND2" x="15.24" y="5.08" visible="pin" length="short" rot="R180"/>
<pin name="SD_SCK" x="-12.7" y="0" visible="pin" length="short"/>
<pin name="SD_MISO" x="-12.7" y="2.54" visible="pin" length="short"/>
<pin name="SD_MOSI" x="-12.7" y="-2.54" visible="pin" length="short"/>
<pin name="SD_CS" x="-12.7" y="-5.08" visible="pin" length="short"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="ST7735">
<gates>
<gate name="G$1" symbol="ST7735" x="-2.54" y="2.54"/>
</gates>
<devices>
<device name="" package="ST7735">
<connects>
<connect gate="G$1" pin="CLK" pad="CLK"/>
<connect gate="G$1" pin="CS" pad="CS"/>
<connect gate="G$1" pin="GND1" pad="GND1"/>
<connect gate="G$1" pin="GND2" pad="GND2"/>
<connect gate="G$1" pin="NC1" pad="NC1"/>
<connect gate="G$1" pin="NC2" pad="NC2"/>
<connect gate="G$1" pin="NC3" pad="NC3"/>
<connect gate="G$1" pin="RS" pad="RS"/>
<connect gate="G$1" pin="RST" pad="RST"/>
<connect gate="G$1" pin="SDA" pad="SDA"/>
<connect gate="G$1" pin="SD_CS" pad="SD_CS"/>
<connect gate="G$1" pin="SD_MISO" pad="SD_MISO"/>
<connect gate="G$1" pin="SD_MOSI" pad="SD_MOSI"/>
<connect gate="G$1" pin="SD_SCK" pad="SD_SCK"/>
<connect gate="G$1" pin="VCC" pad="VCC"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="JOYSTICK">
<packages>
<package name="JOYSTICK">
<pad name="CN21" x="-3.81" y="2.54" drill="1" shape="long"/>
<pad name="CN22" x="-3.81" y="0" drill="1" shape="long"/>
<pad name="CN23" x="-3.81" y="-2.54" drill="1" shape="long"/>
<pad name="CN14" x="8.89" y="-5.08" drill="1" shape="long" rot="R180"/>
<pad name="CN15" x="8.89" y="-7.62" drill="1" shape="long" rot="R180"/>
<pad name="CN16" x="8.89" y="-10.16" drill="1" shape="long"/>
<wire x1="-5.08" y1="3.81" x2="-5.08" y2="-11.43" width="0.127" layer="21"/>
<wire x1="-5.08" y1="-11.43" x2="10.16" y2="-11.43" width="0.127" layer="21"/>
<wire x1="10.16" y1="-11.43" x2="10.16" y2="3.81" width="0.127" layer="21"/>
<wire x1="10.16" y1="3.81" x2="-5.08" y2="3.81" width="0.127" layer="21"/>
<circle x="2.54" y="-3.81" radius="1.79605" width="0.127" layer="21"/>
<circle x="2.54" y="-3.81" radius="3.5921" width="0.127" layer="21"/>
<pad name="CN24" x="-3.81" y="-5.08" drill="1" shape="long"/>
<pad name="CN25" x="-3.81" y="-7.62" drill="1" shape="long"/>
<pad name="CN26" x="-3.81" y="-10.16" drill="1" shape="long"/>
<pad name="CN11" x="8.89" y="2.54" drill="1" shape="long"/>
<pad name="CN12" x="8.89" y="0" drill="1" shape="long"/>
<pad name="CN13" x="8.89" y="-2.54" drill="1" shape="long"/>
<text x="-2.286" y="2.286" size="0.762" layer="21">CN21</text>
<text x="-2.286" y="-0.254" size="0.762" layer="21">CN22</text>
<text x="-2.286" y="-2.794" size="0.762" layer="21">CN23</text>
<text x="-2.286" y="-5.334" size="0.762" layer="21">CN24</text>
<text x="-2.286" y="-7.874" size="0.762" layer="21">CN25</text>
<text x="-2.286" y="-10.414" size="0.762" layer="21">CN25</text>
<text x="5.08" y="2.286" size="0.762" layer="21">CN11</text>
<text x="4.826" y="-0.254" size="0.762" layer="21">CN12</text>
<text x="4.826" y="-2.794" size="0.762" layer="21">CN13</text>
<text x="4.826" y="-5.334" size="0.762" layer="21">CN14</text>
<text x="4.826" y="-7.874" size="0.762" layer="21">CN15</text>
<text x="4.826" y="-10.414" size="0.762" layer="21">CN16</text>
</package>
</packages>
<symbols>
<symbol name="JOYSTICK">
<pin name="CN21" x="-5.08" y="-2.54" visible="pin" length="short"/>
<pin name="CN22" x="-5.08" y="-5.08" visible="pin" length="short"/>
<pin name="CN23" x="-5.08" y="-7.62" visible="pin" length="short"/>
<pin name="CN11" x="25.4" y="-2.54" visible="pin" length="short" rot="R180"/>
<pin name="CN12" x="25.4" y="-5.08" visible="pin" length="short" rot="R180"/>
<pin name="CN13" x="25.4" y="-7.62" visible="pin" length="short" rot="R180"/>
<wire x1="-2.54" y1="0" x2="-2.54" y2="-17.78" width="0.254" layer="94"/>
<wire x1="-2.54" y1="-17.78" x2="22.86" y2="-17.78" width="0.254" layer="94"/>
<wire x1="22.86" y1="-17.78" x2="22.86" y2="0" width="0.254" layer="94"/>
<wire x1="22.86" y1="0" x2="-2.54" y2="0" width="0.254" layer="94"/>
<pin name="CN24" x="-5.08" y="-10.16" visible="pin" length="short"/>
<pin name="CN25" x="-5.08" y="-12.7" visible="pin" length="short"/>
<pin name="CN26" x="-5.08" y="-15.24" visible="pin" length="short"/>
<pin name="CN14" x="25.4" y="-10.16" visible="pin" length="short" rot="R180"/>
<pin name="CN15" x="25.4" y="-12.7" visible="pin" length="short" rot="R180"/>
<pin name="CN16" x="25.4" y="-15.24" visible="pin" length="short" rot="R180"/>
<circle x="10.16" y="-8.89" radius="8.032184375" width="0.127" layer="94"/>
<circle x="10.16" y="-8.89" radius="3.5921" width="0.127" layer="94"/>
<text x="2.54" y="0" size="2.54" layer="94">JOYSTICK</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="JOYSTICK">
<gates>
<gate name="G$1" symbol="JOYSTICK" x="-5.08" y="0"/>
</gates>
<devices>
<device name="" package="JOYSTICK">
<connects>
<connect gate="G$1" pin="CN11" pad="CN11"/>
<connect gate="G$1" pin="CN12" pad="CN12"/>
<connect gate="G$1" pin="CN13" pad="CN13"/>
<connect gate="G$1" pin="CN14" pad="CN14"/>
<connect gate="G$1" pin="CN15" pad="CN15"/>
<connect gate="G$1" pin="CN16" pad="CN16"/>
<connect gate="G$1" pin="CN21" pad="CN21"/>
<connect gate="G$1" pin="CN22" pad="CN22"/>
<connect gate="G$1" pin="CN23" pad="CN23"/>
<connect gate="G$1" pin="CN24" pad="CN24"/>
<connect gate="G$1" pin="CN25" pad="CN25"/>
<connect gate="G$1" pin="CN26" pad="CN26"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="ESP32">
<packages>
<package name="ESP32">
<pad name="3V3" x="0" y="0" drill="1" shape="long"/>
<pad name="EN" x="0" y="-2.54" drill="1" shape="long"/>
<pad name="VP" x="0" y="-5.08" drill="1" shape="long"/>
<pad name="VN" x="0" y="-7.62" drill="1" shape="long"/>
<pad name="34" x="0" y="-10.16" drill="1" shape="long"/>
<pad name="35" x="0" y="-12.7" drill="1" shape="long"/>
<pad name="32" x="0" y="-15.24" drill="1" shape="long"/>
<pad name="33" x="0" y="-17.78" drill="1" shape="long"/>
<pad name="25" x="0" y="-20.32" drill="1" shape="long"/>
<pad name="26" x="0" y="-22.86" drill="1" shape="long"/>
<pad name="27" x="0" y="-25.4" drill="1" shape="long"/>
<pad name="14" x="0" y="-27.94" drill="1" shape="long"/>
<pad name="12" x="0" y="-30.48" drill="1" shape="long"/>
<pad name="GND" x="0" y="-33.02" drill="1" shape="long"/>
<pad name="13" x="0" y="-35.56" drill="1" shape="long"/>
<pad name="D2" x="0" y="-38.1" drill="1" shape="long"/>
<pad name="D3" x="0" y="-40.64" drill="1" shape="long"/>
<pad name="CMD" x="0" y="-43.18" drill="1" shape="long"/>
<pad name="5V" x="0" y="-45.72" drill="1" shape="long"/>
<pad name="GND2" x="25.4" y="0" drill="1" shape="long"/>
<pad name="23" x="25.4" y="-2.54" drill="1" shape="long"/>
<pad name="22" x="25.4" y="-5.08" drill="1" shape="long"/>
<pad name="TX" x="25.4" y="-7.62" drill="1" shape="long"/>
<pad name="RX" x="25.4" y="-10.16" drill="1" shape="long"/>
<pad name="21" x="25.4" y="-12.7" drill="1" shape="long"/>
<pad name="GND3" x="25.4" y="-15.24" drill="1" shape="long"/>
<pad name="19" x="25.4" y="-17.78" drill="1" shape="long"/>
<pad name="18" x="25.4" y="-20.32" drill="1" shape="long"/>
<pad name="5" x="25.4" y="-22.86" drill="1" shape="long"/>
<pad name="17" x="25.4" y="-25.4" drill="1" shape="long"/>
<pad name="16" x="25.4" y="-27.94" drill="1" shape="long"/>
<pad name="4" x="25.4" y="-30.48" drill="1" shape="long"/>
<pad name="0" x="25.4" y="-33.02" drill="1" shape="long"/>
<pad name="2" x="25.4" y="-35.56" drill="1" shape="long"/>
<pad name="15" x="25.4" y="-38.1" drill="1" shape="long"/>
<pad name="D1" x="25.4" y="-40.64" drill="1" shape="long"/>
<pad name="D0" x="25.4" y="-43.18" drill="1" shape="long"/>
<pad name="CLK" x="25.4" y="-45.72" drill="1" shape="long"/>
<wire x1="-2.54" y1="-46.99" x2="27.94" y2="-46.99" width="0.127" layer="21"/>
<wire x1="27.94" y1="-46.99" x2="27.94" y2="1.27" width="0.127" layer="21"/>
<wire x1="27.94" y1="1.27" x2="22.86" y2="1.27" width="0.127" layer="21"/>
<wire x1="22.86" y1="1.27" x2="2.54" y2="1.27" width="0.127" layer="21"/>
<wire x1="2.54" y1="1.27" x2="-2.54" y2="1.27" width="0.127" layer="21"/>
<wire x1="-2.54" y1="1.27" x2="-2.54" y2="-46.99" width="0.127" layer="21"/>
<wire x1="2.54" y1="6.35" x2="2.54" y2="1.27" width="0.127" layer="21"/>
<wire x1="2.54" y1="6.35" x2="22.86" y2="6.35" width="0.127" layer="21"/>
<wire x1="22.86" y1="6.35" x2="22.86" y2="1.27" width="0.127" layer="21"/>
<text x="8.89" y="2.54" size="2.54" layer="21">ANT</text>
<text x="7.62" y="-22.86" size="2.54" layer="21">ESP32</text>
<text x="19.812" y="-0.508" size="1.27" layer="21">GND</text>
<text x="21.844" y="-3.048" size="1.27" layer="21">23</text>
<text x="21.844" y="-5.588" size="1.27" layer="21">22</text>
<text x="21.844" y="-8.128" size="1.27" layer="21">TX</text>
<text x="21.59" y="-10.668" size="1.27" layer="21">RX</text>
<text x="22.098" y="-13.208" size="1.27" layer="21">21</text>
<text x="19.812" y="-15.748" size="1.27" layer="21">GND</text>
<text x="21.844" y="-18.288" size="1.27" layer="21">19</text>
<text x="21.844" y="-20.828" size="1.27" layer="21">18</text>
<text x="22.86" y="-23.368" size="1.27" layer="21">5</text>
<text x="21.844" y="-25.908" size="1.27" layer="21">17</text>
<text x="21.844" y="-28.448" size="1.27" layer="21">16</text>
<text x="22.86" y="-30.988" size="1.27" layer="21">4</text>
<text x="22.86" y="-33.528" size="1.27" layer="21">0</text>
<text x="22.86" y="-36.068" size="1.27" layer="21">2</text>
<text x="21.844" y="-38.608" size="1.27" layer="21">15</text>
<text x="21.59" y="-41.148" size="1.27" layer="21">D1</text>
<text x="21.59" y="-43.688" size="1.27" layer="21">D0</text>
<text x="20.32" y="-46.228" size="1.27" layer="21">CLK</text>
<text x="1.778" y="-46.228" size="1.27" layer="21">5v</text>
<text x="1.778" y="-43.688" size="1.27" layer="21">CMD</text>
<text x="1.778" y="-41.148" size="1.27" layer="21">D3</text>
<text x="1.778" y="-38.608" size="1.27" layer="21">D2</text>
<text x="1.778" y="-36.068" size="1.27" layer="21">13</text>
<text x="1.778" y="-33.528" size="1.27" layer="21">GND</text>
<text x="1.778" y="-30.988" size="1.27" layer="21">12</text>
<text x="1.778" y="-28.448" size="1.27" layer="21">14</text>
<text x="1.778" y="-25.908" size="1.27" layer="21">27</text>
<text x="1.778" y="-23.368" size="1.27" layer="21">26</text>
<text x="1.778" y="-20.828" size="1.27" layer="21">25</text>
<text x="1.778" y="-18.288" size="1.27" layer="21">33</text>
<text x="1.778" y="-15.748" size="1.27" layer="21">32</text>
<text x="1.778" y="-13.208" size="1.27" layer="21">35</text>
<text x="1.778" y="-10.668" size="1.27" layer="21">34</text>
<text x="1.778" y="-8.128" size="1.27" layer="21">VN</text>
<text x="1.778" y="-5.588" size="1.27" layer="21">VP</text>
<text x="1.778" y="-3.048" size="1.27" layer="21">EN</text>
<text x="1.778" y="-0.508" size="1.27" layer="21">3v3</text>
</package>
</packages>
<symbols>
<symbol name="ESP32">
<pin name="3V3" x="-12.7" y="20.32" visible="pin" length="short"/>
<pin name="EN" x="-12.7" y="17.78" visible="pin" length="short"/>
<pin name="VP" x="-12.7" y="15.24" visible="pin" length="short"/>
<pin name="VN" x="-12.7" y="12.7" visible="pin" length="short"/>
<pin name="34" x="-12.7" y="10.16" visible="pin" length="short"/>
<pin name="35" x="-12.7" y="7.62" visible="pin" length="short"/>
<pin name="32" x="-12.7" y="5.08" visible="pin" length="short"/>
<pin name="33" x="-12.7" y="2.54" visible="pin" length="short"/>
<pin name="25" x="-12.7" y="0" visible="pin" length="short"/>
<pin name="26" x="-12.7" y="-2.54" visible="pin" length="short"/>
<pin name="27" x="-12.7" y="-5.08" visible="pin" length="short"/>
<pin name="14" x="-12.7" y="-7.62" visible="pin" length="short"/>
<pin name="12" x="-12.7" y="-10.16" visible="pin" length="short"/>
<pin name="GND" x="-12.7" y="-12.7" visible="pin" length="short"/>
<pin name="13" x="-12.7" y="-15.24" visible="pin" length="short"/>
<pin name="D2" x="-12.7" y="-17.78" visible="pin" length="short"/>
<pin name="D3" x="-12.7" y="-20.32" visible="pin" length="short"/>
<pin name="CMD" x="-12.7" y="-22.86" visible="pin" length="short"/>
<pin name="5V" x="-12.7" y="-25.4" visible="pin" length="short"/>
<pin name="CLK" x="12.7" y="-25.4" visible="pin" length="short" rot="R180"/>
<pin name="D0" x="12.7" y="-22.86" visible="pin" length="short" rot="R180"/>
<pin name="D1" x="12.7" y="-20.32" visible="pin" length="short" rot="R180"/>
<pin name="15" x="12.7" y="-17.78" visible="pin" length="short" rot="R180"/>
<pin name="2" x="12.7" y="-15.24" visible="pin" length="short" rot="R180"/>
<pin name="0" x="12.7" y="-12.7" visible="pin" length="short" rot="R180"/>
<pin name="4" x="12.7" y="-10.16" visible="pin" length="short" rot="R180"/>
<pin name="16" x="12.7" y="-7.62" visible="pin" length="short" rot="R180"/>
<pin name="17" x="12.7" y="-5.08" visible="pin" length="short" rot="R180"/>
<pin name="5" x="12.7" y="-2.54" visible="pin" length="short" rot="R180"/>
<pin name="18" x="12.7" y="0" visible="pin" length="short" rot="R180"/>
<pin name="19" x="12.7" y="2.54" visible="pin" length="short" rot="R180"/>
<pin name="GND3" x="12.7" y="5.08" visible="pin" length="short" rot="R180"/>
<pin name="21" x="12.7" y="7.62" visible="pin" length="short" rot="R180"/>
<pin name="RX" x="12.7" y="10.16" visible="pin" length="short" rot="R180"/>
<pin name="TX" x="12.7" y="12.7" visible="pin" length="short" rot="R180"/>
<pin name="22" x="12.7" y="15.24" visible="pin" length="short" rot="R180"/>
<pin name="23" x="12.7" y="17.78" visible="pin" length="short" rot="R180"/>
<pin name="GND2" x="12.7" y="20.32" visible="pin" length="short" rot="R180"/>
<wire x1="-10.16" y1="22.86" x2="-10.16" y2="-27.94" width="0.254" layer="94"/>
<wire x1="-10.16" y1="-27.94" x2="10.16" y2="-27.94" width="0.254" layer="94"/>
<wire x1="10.16" y1="-27.94" x2="10.16" y2="22.86" width="0.254" layer="94"/>
<wire x1="10.16" y1="22.86" x2="-10.16" y2="22.86" width="0.254" layer="94"/>
<text x="-2.54" y="22.86" size="1.778" layer="97">ANT</text>
<wire x1="-10.16" y1="22.86" x2="-10.16" y2="25.4" width="0.254" layer="94"/>
<wire x1="-10.16" y1="25.4" x2="10.16" y2="25.4" width="0.254" layer="94"/>
<wire x1="10.16" y1="25.4" x2="10.16" y2="22.86" width="0.254" layer="94"/>
<text x="-7.62" y="25.4" size="3.81" layer="94">ESP32</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="ESP32">
<gates>
<gate name="G$1" symbol="ESP32" x="2.54" y="10.16"/>
</gates>
<devices>
<device name="" package="ESP32">
<connects>
<connect gate="G$1" pin="0" pad="0"/>
<connect gate="G$1" pin="12" pad="12"/>
<connect gate="G$1" pin="13" pad="13"/>
<connect gate="G$1" pin="14" pad="14"/>
<connect gate="G$1" pin="15" pad="15"/>
<connect gate="G$1" pin="16" pad="16"/>
<connect gate="G$1" pin="17" pad="17"/>
<connect gate="G$1" pin="18" pad="18"/>
<connect gate="G$1" pin="19" pad="19"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="21" pad="21"/>
<connect gate="G$1" pin="22" pad="22"/>
<connect gate="G$1" pin="23" pad="23"/>
<connect gate="G$1" pin="25" pad="25"/>
<connect gate="G$1" pin="26" pad="26"/>
<connect gate="G$1" pin="27" pad="27"/>
<connect gate="G$1" pin="32" pad="32"/>
<connect gate="G$1" pin="33" pad="33"/>
<connect gate="G$1" pin="34" pad="34"/>
<connect gate="G$1" pin="35" pad="35"/>
<connect gate="G$1" pin="3V3" pad="3V3"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="5V" pad="5V"/>
<connect gate="G$1" pin="CLK" pad="CLK"/>
<connect gate="G$1" pin="CMD" pad="CMD"/>
<connect gate="G$1" pin="D0" pad="D0"/>
<connect gate="G$1" pin="D1" pad="D1"/>
<connect gate="G$1" pin="D2" pad="D2"/>
<connect gate="G$1" pin="D3" pad="D3"/>
<connect gate="G$1" pin="EN" pad="EN"/>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="GND2" pad="GND2"/>
<connect gate="G$1" pin="GND3" pad="GND3"/>
<connect gate="G$1" pin="RX" pad="RX"/>
<connect gate="G$1" pin="TX" pad="TX"/>
<connect gate="G$1" pin="VN" pad="VN"/>
<connect gate="G$1" pin="VP" pad="VP"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply2" urn="urn:adsk.eagle:library:372">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
Please keep in mind, that these devices are necessary for the
automatic wiring of the supply signals.&lt;p&gt;
The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="GND" urn="urn:adsk.eagle:symbol:26990/1" library_version="2">
<wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.254" layer="94"/>
<wire x1="1.27" y1="0" x2="0" y2="-1.27" width="0.254" layer="94"/>
<wire x1="0" y1="-1.27" x2="-1.27" y2="0" width="0.254" layer="94"/>
<text x="-1.905" y="-3.175" size="1.778" layer="96">&gt;VALUE</text>
<pin name="GND" x="0" y="2.54" visible="off" length="short" direction="sup" rot="R270"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="GND" urn="urn:adsk.eagle:component:27037/1" prefix="SUPPLY" library_version="2">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="GND" symbol="GND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply1" urn="urn:adsk.eagle:library:371">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
 GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
 Please keep in mind, that these devices are necessary for the
 automatic wiring of the supply signals.&lt;p&gt;
 The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
 In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
 &lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="+3V3" urn="urn:adsk.eagle:symbol:26950/1" library_version="1">
<wire x1="1.27" y1="-1.905" x2="0" y2="0" width="0.254" layer="94"/>
<wire x1="0" y1="0" x2="-1.27" y2="-1.905" width="0.254" layer="94"/>
<text x="-2.54" y="-5.08" size="1.778" layer="96" rot="R90">&gt;VALUE</text>
<pin name="+3V3" x="0" y="-2.54" visible="off" length="short" direction="sup" rot="R90"/>
</symbol>
<symbol name="+5V" urn="urn:adsk.eagle:symbol:26929/1" library_version="1">
<wire x1="1.27" y1="-1.905" x2="0" y2="0" width="0.254" layer="94"/>
<wire x1="0" y1="0" x2="-1.27" y2="-1.905" width="0.254" layer="94"/>
<text x="-2.54" y="-5.08" size="1.778" layer="96" rot="R90">&gt;VALUE</text>
<pin name="+5V" x="0" y="-2.54" visible="off" length="short" direction="sup" rot="R90"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="+3V3" urn="urn:adsk.eagle:component:26981/1" prefix="+3V3" library_version="1">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="G$1" symbol="+3V3" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="+5V" urn="urn:adsk.eagle:component:26963/1" prefix="P+" library_version="1">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="+5V" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="Sensor">
<packages>
<package name="BMX055">
<pad name="GND" x="-3.81" y="0" drill="1" shape="long"/>
<pad name="VCC" x="3.81" y="0" drill="1" shape="long"/>
<pad name="SDA" x="-3.81" y="-2.54" drill="1" shape="long"/>
<pad name="SCL" x="-3.81" y="-5.08" drill="1" shape="long"/>
<pad name="VCCIO" x="3.81" y="-2.54" drill="1" shape="long"/>
<pad name="3V3" x="3.81" y="-5.08" drill="1" shape="long"/>
<wire x1="-5.08" y1="5.08" x2="-5.08" y2="-10.16" width="0.127" layer="21"/>
<wire x1="-5.08" y1="-10.16" x2="5.08" y2="-10.16" width="0.127" layer="21"/>
<wire x1="5.08" y1="-10.16" x2="5.08" y2="5.08" width="0.127" layer="21"/>
<wire x1="5.08" y1="5.08" x2="-5.08" y2="5.08" width="0.127" layer="21"/>
<wire x1="-1.27" y1="0" x2="-1.27" y2="-5.08" width="0.127" layer="21"/>
<wire x1="-1.27" y1="-5.08" x2="1.27" y2="-5.08" width="0.127" layer="21"/>
<wire x1="1.27" y1="-5.08" x2="1.27" y2="0" width="0.127" layer="21"/>
<wire x1="1.27" y1="0" x2="-1.27" y2="0" width="0.127" layer="21"/>
<text x="-4.826" y="2.032" size="1.778" layer="21">BMX055</text>
</package>
</packages>
<symbols>
<symbol name="BMX055">
<pin name="SDA" x="-5.08" y="0" visible="pin" length="short"/>
<pin name="GND" x="-5.08" y="2.54" visible="pin" length="short"/>
<pin name="SCL" x="-5.08" y="-2.54" visible="pin" length="short"/>
<pin name="3V3" x="17.78" y="-2.54" visible="pin" length="short" rot="R180"/>
<pin name="VCCIO" x="17.78" y="0" visible="pin" length="short" rot="R180"/>
<pin name="VCC" x="17.78" y="2.54" visible="pin" length="short" rot="R180"/>
<wire x1="-2.54" y1="5.08" x2="-2.54" y2="-5.08" width="0.254" layer="94"/>
<wire x1="-2.54" y1="-5.08" x2="15.24" y2="-5.08" width="0.254" layer="94"/>
<wire x1="15.24" y1="-5.08" x2="15.24" y2="5.08" width="0.254" layer="94"/>
<wire x1="15.24" y1="5.08" x2="-2.54" y2="5.08" width="0.254" layer="94"/>
<text x="0" y="5.08" size="2.54" layer="94">BMX055</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="BMX055">
<gates>
<gate name="G$1" symbol="BMX055" x="-5.08" y="0"/>
</gates>
<devices>
<device name="" package="BMX055">
<connects>
<connect gate="G$1" pin="3V3" pad="3V3"/>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="SCL" pad="SCL"/>
<connect gate="G$1" pin="SDA" pad="SDA"/>
<connect gate="G$1" pin="VCC" pad="VCC"/>
<connect gate="G$1" pin="VCCIO" pad="VCCIO"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U$4" library="Switch" deviceset="PUSH_SW" device=""/>
<part name="U$5" library="Switch" deviceset="PUSH_SW" device=""/>
<part name="U$1" library="ILI9341" deviceset="ST7735" device=""/>
<part name="U$2" library="JOYSTICK" deviceset="JOYSTICK" device=""/>
<part name="U$3" library="ESP32" deviceset="ESP32" device=""/>
<part name="SUPPLY1" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="GND" device=""/>
<part name="SUPPLY2" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="GND" device=""/>
<part name="+3V1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="+3V3" device=""/>
<part name="P+1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="+5V" device=""/>
<part name="SUPPLY3" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="GND" device=""/>
<part name="+3V2" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="+3V3" device=""/>
<part name="U$6" library="Sensor" deviceset="BMX055" device=""/>
<part name="SUPPLY5" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="GND" device=""/>
<part name="+3V3" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="+3V3" device=""/>
<part name="+3V4" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="+3V3" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U$4" gate="G$1" x="20.32" y="-22.86"/>
<instance part="U$5" gate="G$1" x="20.32" y="-30.48"/>
<instance part="U$1" gate="G$1" x="22.86" y="27.94"/>
<instance part="U$2" gate="G$1" x="15.24" y="2.54"/>
<instance part="U$3" gate="G$1" x="-30.48" y="25.4"/>
<instance part="SUPPLY1" gate="GND" x="-45.72" y="-5.08">
<attribute name="VALUE" x="-47.625" y="-8.255" size="1.778" layer="96"/>
</instance>
<instance part="SUPPLY2" gate="GND" x="-15.24" y="-5.08">
<attribute name="VALUE" x="-17.145" y="-8.255" size="1.778" layer="96"/>
</instance>
<instance part="+3V1" gate="G$1" x="-48.26" y="50.8">
<attribute name="VALUE" x="-50.8" y="45.72" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="P+1" gate="1" x="-48.26" y="5.08">
<attribute name="VALUE" x="-50.8" y="0" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="SUPPLY3" gate="GND" x="43.18" y="-17.78">
<attribute name="VALUE" x="41.275" y="-20.955" size="1.778" layer="96"/>
</instance>
<instance part="+3V2" gate="G$1" x="45.72" y="43.18">
<attribute name="VALUE" x="43.18" y="38.1" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="U$6" gate="G$1" x="15.24" y="53.34"/>
<instance part="SUPPLY5" gate="GND" x="7.62" y="45.72">
<attribute name="VALUE" x="5.715" y="42.545" size="1.778" layer="96"/>
</instance>
<instance part="+3V3" gate="G$1" x="35.56" y="63.5">
<attribute name="VALUE" x="33.02" y="58.42" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="+3V4" gate="G$1" x="30.48" y="-17.78">
<attribute name="VALUE" x="27.94" y="-22.86" size="1.778" layer="96" rot="R90"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="GND" class="0">
<segment>
<pinref part="SUPPLY1" gate="GND" pin="GND"/>
<wire x1="-45.72" y1="-2.54" x2="-45.72" y2="12.7" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="GND"/>
<wire x1="-45.72" y1="12.7" x2="-43.18" y2="12.7" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="SUPPLY2" gate="GND" pin="GND"/>
<pinref part="U$3" gate="G$1" pin="GND3"/>
<wire x1="-15.24" y1="-2.54" x2="-15.24" y2="30.48" width="0.1524" layer="91"/>
<wire x1="-15.24" y1="30.48" x2="-17.78" y2="30.48" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="GND2"/>
<wire x1="-17.78" y1="45.72" x2="-15.24" y2="45.72" width="0.1524" layer="91"/>
<wire x1="-15.24" y1="45.72" x2="-15.24" y2="30.48" width="0.1524" layer="91"/>
<junction x="-15.24" y="30.48"/>
</segment>
<segment>
<pinref part="SUPPLY3" gate="GND" pin="GND"/>
<wire x1="43.18" y1="-5.08" x2="43.18" y2="-12.7" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="GND1"/>
<wire x1="43.18" y1="-12.7" x2="43.18" y2="-15.24" width="0.1524" layer="91"/>
<wire x1="38.1" y1="35.56" x2="43.18" y2="35.56" width="0.1524" layer="91"/>
<wire x1="43.18" y1="35.56" x2="43.18" y2="33.02" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="GND2"/>
<wire x1="43.18" y1="33.02" x2="43.18" y2="-5.08" width="0.1524" layer="91"/>
<wire x1="38.1" y1="33.02" x2="43.18" y2="33.02" width="0.1524" layer="91"/>
<junction x="43.18" y="33.02"/>
<pinref part="U$2" gate="G$1" pin="CN13"/>
<wire x1="40.64" y1="-5.08" x2="43.18" y2="-5.08" width="0.1524" layer="91"/>
<junction x="43.18" y="-5.08"/>
<pinref part="U$2" gate="G$1" pin="CN16"/>
<wire x1="40.64" y1="-12.7" x2="43.18" y2="-12.7" width="0.1524" layer="91"/>
<junction x="43.18" y="-12.7"/>
</segment>
<segment>
<pinref part="U$6" gate="G$1" pin="GND"/>
<wire x1="10.16" y1="55.88" x2="7.62" y2="55.88" width="0.1524" layer="91"/>
<wire x1="7.62" y1="55.88" x2="7.62" y2="48.26" width="0.1524" layer="91"/>
<pinref part="SUPPLY5" gate="GND" pin="GND"/>
</segment>
</net>
<net name="+3V3" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="3V3"/>
<wire x1="-43.18" y1="45.72" x2="-48.26" y2="45.72" width="0.1524" layer="91"/>
<pinref part="+3V1" gate="G$1" pin="+3V3"/>
<wire x1="-48.26" y1="45.72" x2="-48.26" y2="48.26" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="U$1" gate="G$1" pin="VCC"/>
<pinref part="U$2" gate="G$1" pin="CN14"/>
<wire x1="40.64" y1="-7.62" x2="45.72" y2="-7.62" width="0.1524" layer="91"/>
<wire x1="45.72" y1="-7.62" x2="45.72" y2="0" width="0.1524" layer="91"/>
<wire x1="45.72" y1="0" x2="45.72" y2="38.1" width="0.1524" layer="91"/>
<wire x1="45.72" y1="38.1" x2="38.1" y2="38.1" width="0.1524" layer="91"/>
<pinref part="+3V2" gate="G$1" pin="+3V3"/>
<wire x1="45.72" y1="38.1" x2="45.72" y2="40.64" width="0.1524" layer="91"/>
<junction x="45.72" y="38.1"/>
<pinref part="U$2" gate="G$1" pin="CN11"/>
<wire x1="40.64" y1="0" x2="45.72" y2="0" width="0.1524" layer="91"/>
<junction x="45.72" y="0"/>
</segment>
<segment>
<pinref part="U$6" gate="G$1" pin="3V3"/>
<wire x1="33.02" y1="50.8" x2="35.56" y2="50.8" width="0.1524" layer="91"/>
<wire x1="35.56" y1="50.8" x2="35.56" y2="53.34" width="0.1524" layer="91"/>
<pinref part="+3V3" gate="G$1" pin="+3V3"/>
<pinref part="U$6" gate="G$1" pin="VCCIO"/>
<wire x1="35.56" y1="53.34" x2="35.56" y2="55.88" width="0.1524" layer="91"/>
<wire x1="35.56" y1="55.88" x2="35.56" y2="60.96" width="0.1524" layer="91"/>
<wire x1="33.02" y1="53.34" x2="35.56" y2="53.34" width="0.1524" layer="91"/>
<junction x="35.56" y="53.34"/>
<pinref part="U$6" gate="G$1" pin="VCC"/>
<wire x1="33.02" y1="55.88" x2="35.56" y2="55.88" width="0.1524" layer="91"/>
<junction x="35.56" y="55.88"/>
</segment>
<segment>
<pinref part="U$4" gate="G$1" pin="P3"/>
<wire x1="22.86" y1="-22.86" x2="30.48" y2="-22.86" width="0.1524" layer="91"/>
<pinref part="+3V4" gate="G$1" pin="+3V3"/>
<wire x1="30.48" y1="-22.86" x2="30.48" y2="-20.32" width="0.1524" layer="91"/>
<pinref part="U$5" gate="G$1" pin="P3"/>
<wire x1="22.86" y1="-30.48" x2="30.48" y2="-30.48" width="0.1524" layer="91"/>
<wire x1="30.48" y1="-30.48" x2="30.48" y2="-22.86" width="0.1524" layer="91"/>
<junction x="30.48" y="-22.86"/>
</segment>
</net>
<net name="+5V" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="5V"/>
<wire x1="-43.18" y1="0" x2="-48.26" y2="0" width="0.1524" layer="91"/>
<pinref part="P+1" gate="1" pin="+5V"/>
<wire x1="-48.26" y1="0" x2="-48.26" y2="2.54" width="0.1524" layer="91"/>
</segment>
</net>
<net name="CN12" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="32"/>
<wire x1="-43.18" y1="30.48" x2="-45.72" y2="30.48" width="0.1524" layer="91"/>
<label x="-45.72" y="30.48" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
<segment>
<pinref part="U$2" gate="G$1" pin="CN12"/>
<wire x1="40.64" y1="-2.54" x2="50.8" y2="-2.54" width="0.1524" layer="91"/>
<label x="50.8" y="-2.54" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="CLK" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="CLK"/>
<wire x1="38.1" y1="22.86" x2="50.8" y2="22.86" width="0.1524" layer="91"/>
<label x="50.8" y="22.86" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="18"/>
<wire x1="-17.78" y1="25.4" x2="-12.7" y2="25.4" width="0.1524" layer="91"/>
<label x="-12.7" y="25.4" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="SDA" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="SDA"/>
<wire x1="38.1" y1="20.32" x2="50.8" y2="20.32" width="0.1524" layer="91"/>
<label x="50.8" y="20.32" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="23"/>
<wire x1="-17.78" y1="43.18" x2="-12.7" y2="43.18" width="0.1524" layer="91"/>
<label x="-12.7" y="43.18" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="RS" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="RS"/>
<wire x1="38.1" y1="17.78" x2="50.8" y2="17.78" width="0.1524" layer="91"/>
<label x="50.8" y="17.78" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="2"/>
<wire x1="-17.78" y1="10.16" x2="-12.7" y2="10.16" width="0.1524" layer="91"/>
<label x="-12.7" y="10.16" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="RST" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="RST"/>
<wire x1="38.1" y1="15.24" x2="50.8" y2="15.24" width="0.1524" layer="91"/>
<label x="50.8" y="15.24" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="4"/>
<wire x1="-17.78" y1="15.24" x2="-12.7" y2="15.24" width="0.1524" layer="91"/>
<label x="-12.7" y="15.24" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="CS" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="CS"/>
<wire x1="38.1" y1="12.7" x2="50.8" y2="12.7" width="0.1524" layer="91"/>
<label x="50.8" y="12.7" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="5"/>
<wire x1="-17.78" y1="22.86" x2="-12.7" y2="22.86" width="0.1524" layer="91"/>
<label x="-12.7" y="22.86" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="CN15" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="33"/>
<wire x1="-43.18" y1="27.94" x2="-45.72" y2="27.94" width="0.1524" layer="91"/>
<label x="-45.72" y="27.94" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
<segment>
<pinref part="U$2" gate="G$1" pin="CN15"/>
<wire x1="40.64" y1="-10.16" x2="50.8" y2="-10.16" width="0.1524" layer="91"/>
<label x="50.8" y="-10.16" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="I2C_SDA" class="0">
<segment>
<pinref part="U$6" gate="G$1" pin="SDA"/>
<wire x1="10.16" y1="53.34" x2="5.08" y2="53.34" width="0.1524" layer="91"/>
<label x="5.08" y="53.34" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="21"/>
<wire x1="-17.78" y1="33.02" x2="-12.7" y2="33.02" width="0.1524" layer="91"/>
<label x="-12.7" y="33.02" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="I2C_SCL" class="0">
<segment>
<pinref part="U$6" gate="G$1" pin="SCL"/>
<wire x1="10.16" y1="50.8" x2="5.08" y2="50.8" width="0.1524" layer="91"/>
<label x="5.08" y="50.8" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="22"/>
<wire x1="-17.78" y1="40.64" x2="-12.7" y2="40.64" width="0.1524" layer="91"/>
<label x="-12.7" y="40.64" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="17" class="0">
<segment>
<pinref part="U$5" gate="G$1" pin="P1"/>
<wire x1="15.24" y1="-30.48" x2="12.7" y2="-30.48" width="0.1524" layer="91"/>
<label x="12.7" y="-30.48" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="17"/>
<wire x1="-17.78" y1="20.32" x2="-12.7" y2="20.32" width="0.1524" layer="91"/>
<label x="-12.7" y="20.32" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="16" class="0">
<segment>
<pinref part="U$4" gate="G$1" pin="P1"/>
<wire x1="15.24" y1="-22.86" x2="12.7" y2="-22.86" width="0.1524" layer="91"/>
<label x="12.7" y="-22.86" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="16"/>
<wire x1="-17.78" y1="17.78" x2="-12.7" y2="17.78" width="0.1524" layer="91"/>
<label x="-12.7" y="17.78" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
<compatibility>
<note version="8.2" severity="warning">
Since Version 8.2, EAGLE supports online libraries. The ids
of those online libraries will not be understood (or retained)
with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports URNs for individual library
assets (packages, symbols, and devices). The URNs of those assets
will not be understood (or retained) with this version.
</note>
</compatibility>
</eagle>
