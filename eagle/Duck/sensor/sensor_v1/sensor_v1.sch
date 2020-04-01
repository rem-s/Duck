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
<library name="Sensor">
<packages>
<package name="HCSR04">
<pad name="VCC" x="-3.81" y="0" drill="1" shape="long" rot="R90"/>
<pad name="TRG" x="-1.27" y="0" drill="1" shape="long" rot="R90"/>
<pad name="ECHO" x="1.27" y="0" drill="1" shape="long" rot="R90"/>
<pad name="GND" x="3.81" y="0" drill="1" shape="long" rot="R90"/>
<wire x1="-10.16" y1="-1.27" x2="-3.81" y2="-1.27" width="0.127" layer="21"/>
<wire x1="-3.81" y1="-1.27" x2="3.81" y2="-1.27" width="0.127" layer="21"/>
<wire x1="3.81" y1="-1.27" x2="10.16" y2="-1.27" width="0.127" layer="21"/>
<wire x1="10.16" y1="-1.27" x2="11.43" y2="-1.27" width="0.127" layer="21"/>
<wire x1="11.43" y1="-1.27" x2="11.43" y2="1.27" width="0.127" layer="21"/>
<wire x1="11.43" y1="1.27" x2="-11.43" y2="1.27" width="0.127" layer="21"/>
<wire x1="-11.43" y1="1.27" x2="-11.43" y2="-1.27" width="0.127" layer="21"/>
<wire x1="-11.43" y1="-1.27" x2="-10.16" y2="-1.27" width="0.127" layer="21"/>
<wire x1="-10.16" y1="-1.27" x2="-10.16" y2="-6.35" width="0.127" layer="21"/>
<wire x1="-10.16" y1="-6.35" x2="-3.81" y2="-6.35" width="0.127" layer="21"/>
<wire x1="-3.81" y1="-6.35" x2="-3.81" y2="-1.27" width="0.127" layer="21"/>
<wire x1="3.81" y1="-1.27" x2="3.81" y2="-6.35" width="0.127" layer="21"/>
<wire x1="3.81" y1="-6.35" x2="10.16" y2="-6.35" width="0.127" layer="21"/>
<wire x1="10.16" y1="-6.35" x2="10.16" y2="-1.27" width="0.127" layer="21"/>
</package>
</packages>
<symbols>
<symbol name="HCSR04">
<pin name="VCC" x="-5.08" y="2.54" visible="pin" length="short"/>
<pin name="TRG" x="-5.08" y="0" visible="pin" length="short"/>
<pin name="ECHO" x="-5.08" y="-2.54" visible="pin" length="short"/>
<pin name="GND" x="-5.08" y="-5.08" visible="pin" length="short"/>
<wire x1="-2.54" y1="5.08" x2="-2.54" y2="-7.62" width="0.254" layer="94"/>
<wire x1="-2.54" y1="-7.62" x2="0" y2="-7.62" width="0.254" layer="94"/>
<wire x1="0" y1="-7.62" x2="0" y2="-15.24" width="0.254" layer="94"/>
<wire x1="0" y1="-15.24" x2="7.62" y2="-15.24" width="0.254" layer="94"/>
<wire x1="7.62" y1="-15.24" x2="7.62" y2="12.7" width="0.254" layer="94"/>
<wire x1="7.62" y1="12.7" x2="0" y2="12.7" width="0.254" layer="94"/>
<wire x1="0" y1="12.7" x2="0" y2="5.08" width="0.254" layer="94"/>
<wire x1="0" y1="5.08" x2="-2.54" y2="5.08" width="0.254" layer="94"/>
<circle x="5.08" y="7.62" radius="2.54" width="0.254" layer="94"/>
<circle x="5.08" y="-10.16" radius="2.54" width="0.254" layer="94"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="HCSR04">
<gates>
<gate name="G$1" symbol="HCSR04" x="-2.54" y="0"/>
</gates>
<devices>
<device name="" package="HCSR04">
<connects>
<connect gate="G$1" pin="ECHO" pad="ECHO"/>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="TRG" pad="TRG"/>
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
<symbol name="+5V" urn="urn:adsk.eagle:symbol:26929/1" library_version="1">
<wire x1="1.27" y1="-1.905" x2="0" y2="0" width="0.254" layer="94"/>
<wire x1="0" y1="0" x2="-1.27" y2="-1.905" width="0.254" layer="94"/>
<text x="-2.54" y="-5.08" size="1.778" layer="96" rot="R90">&gt;VALUE</text>
<pin name="+5V" x="0" y="-2.54" visible="off" length="short" direction="sup" rot="R90"/>
</symbol>
</symbols>
<devicesets>
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
<library name="Pinheader">
<packages>
<package name="PIN1X8_254">
<pad name="P$1" x="0" y="0" drill="1.016"/>
<pad name="P$2" x="2.54" y="0" drill="1.016"/>
<pad name="P$3" x="5.08" y="0" drill="1.016"/>
<pad name="P$4" x="7.62" y="0" drill="1.016"/>
<pad name="P$5" x="10.16" y="0" drill="1.016"/>
<pad name="P$6" x="12.7" y="0" drill="1.016"/>
<pad name="P$7" x="15.24" y="0" drill="1.016"/>
<pad name="P$8" x="17.78" y="0" drill="1.016"/>
<wire x1="-0.635" y1="0.635" x2="18.415" y2="0.635" width="0.127" layer="21"/>
<wire x1="18.415" y1="0.635" x2="18.415" y2="-0.635" width="0.127" layer="21"/>
<wire x1="18.415" y1="-0.635" x2="-0.635" y2="-0.635" width="0.127" layer="21"/>
<wire x1="-0.635" y1="-0.635" x2="-0.635" y2="0.635" width="0.127" layer="21"/>
</package>
</packages>
<symbols>
<symbol name="PIN1X8">
<pin name="P1" x="2.54" y="5.08" visible="off" length="middle" rot="R180"/>
<pin name="P2" x="2.54" y="2.54" visible="off" length="middle" rot="R180"/>
<pin name="P3" x="2.54" y="0" visible="off" length="middle" rot="R180"/>
<pin name="P4" x="2.54" y="-2.54" visible="off" length="middle" rot="R180"/>
<pin name="P5" x="2.54" y="-5.08" visible="off" length="middle" rot="R180"/>
<pin name="P6" x="2.54" y="-7.62" visible="off" length="middle" rot="R180"/>
<wire x1="0" y1="7.62" x2="-5.08" y2="7.62" width="0.254" layer="94"/>
<wire x1="-5.08" y1="7.62" x2="-5.08" y2="-15.24" width="0.254" layer="94"/>
<wire x1="-5.08" y1="-15.24" x2="0" y2="-15.24" width="0.254" layer="94"/>
<wire x1="0" y1="-15.24" x2="0" y2="7.62" width="0.254" layer="94"/>
<text x="-6.35" y="7.62" size="1.778" layer="94">PIN1X8</text>
<pin name="P7" x="2.54" y="-10.16" visible="off" length="middle" rot="R180"/>
<pin name="P8" x="2.54" y="-12.7" visible="off" length="middle" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="PIN1X8_254">
<gates>
<gate name="G$1" symbol="PIN1X8" x="0" y="2.54"/>
</gates>
<devices>
<device name="" package="PIN1X8_254">
<connects>
<connect gate="G$1" pin="P1" pad="P$1"/>
<connect gate="G$1" pin="P2" pad="P$2"/>
<connect gate="G$1" pin="P3" pad="P$3"/>
<connect gate="G$1" pin="P4" pad="P$4"/>
<connect gate="G$1" pin="P5" pad="P$5"/>
<connect gate="G$1" pin="P6" pad="P$6"/>
<connect gate="G$1" pin="P7" pad="P$7"/>
<connect gate="G$1" pin="P8" pad="P$8"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="Register">
<packages>
<package name="SMD_REG0805">
<smd name="P1" x="-0.77" y="0" dx="1.27" dy="1" layer="1" rot="R90"/>
<smd name="P2" x="0.801" y="-0.014" dx="1.27" dy="1" layer="1" rot="R90"/>
<wire x1="-1.1" y1="0.65" x2="1.1" y2="0.65" width="0.127" layer="21"/>
<wire x1="1.1" y1="0.65" x2="1.1" y2="-0.65" width="0.127" layer="21"/>
<wire x1="1.1" y1="-0.65" x2="-1.1" y2="-0.65" width="0.127" layer="21"/>
<wire x1="-1.1" y1="-0.65" x2="-1.1" y2="0.65" width="0.127" layer="21"/>
<text x="-1.1" y="0.7" size="0.6096" layer="51">&gt;NAME</text>
</package>
</packages>
<symbols>
<symbol name="REGISTER">
<pin name="P1" x="-5.08" y="0" visible="off" length="short"/>
<pin name="P2" x="5.08" y="0" visible="off" length="short" rot="R180"/>
<wire x1="-2.54" y1="0" x2="-2.286" y2="1.524" width="0.1524" layer="94"/>
<wire x1="-2.286" y1="1.524" x2="-1.778" y2="-1.524" width="0.1524" layer="94"/>
<wire x1="-1.778" y1="-1.524" x2="-1.27" y2="1.524" width="0.1524" layer="94"/>
<wire x1="-1.27" y1="1.524" x2="-0.762" y2="-1.524" width="0.1524" layer="94"/>
<wire x1="-0.762" y1="-1.524" x2="-0.254" y2="1.524" width="0.1524" layer="94"/>
<wire x1="-0.254" y1="1.524" x2="0.254" y2="-1.524" width="0.1524" layer="94"/>
<wire x1="0.254" y1="-1.524" x2="0.762" y2="1.524" width="0.1524" layer="94"/>
<wire x1="0.762" y1="1.524" x2="1.27" y2="-1.524" width="0.1524" layer="94"/>
<wire x1="1.27" y1="-1.524" x2="1.778" y2="1.524" width="0.1524" layer="94"/>
<wire x1="1.778" y1="1.524" x2="2.286" y2="-1.524" width="0.1524" layer="94"/>
<wire x1="2.286" y1="-1.524" x2="2.54" y2="0" width="0.1524" layer="94"/>
<text x="-4.572" y="1.778" size="1.778" layer="95">&gt;NAME</text>
<text x="-4.572" y="-3.429" size="1.778" layer="96">&gt;VALUE</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="SMD_REG0805" uservalue="yes">
<gates>
<gate name="G$1" symbol="REGISTER" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SMD_REG0805">
<connects>
<connect gate="G$1" pin="P1" pad="P1"/>
<connect gate="G$1" pin="P2" pad="P2"/>
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
<part name="U$1" library="Sensor" deviceset="HCSR04" device=""/>
<part name="U$2" library="Sensor" deviceset="HCSR04" device=""/>
<part name="U$3" library="Sensor" deviceset="HCSR04" device=""/>
<part name="P+1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="+5V" device=""/>
<part name="SUPPLY1" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="GND" device=""/>
<part name="U$4" library="Pinheader" deviceset="PIN1X8_254" device=""/>
<part name="P+2" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="+5V" device=""/>
<part name="SUPPLY2" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="GND" device=""/>
<part name="R11" library="Register" deviceset="SMD_REG0805" device="" value="1k"/>
<part name="R12" library="Register" deviceset="SMD_REG0805" device="" value="2k"/>
<part name="SUPPLY3" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="GND" device=""/>
<part name="R21" library="Register" deviceset="SMD_REG0805" device="" value="1k"/>
<part name="R22" library="Register" deviceset="SMD_REG0805" device="" value="2k"/>
<part name="SUPPLY4" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="GND" device=""/>
<part name="R31" library="Register" deviceset="SMD_REG0805" device="" value="1k"/>
<part name="R32" library="Register" deviceset="SMD_REG0805" device="" value="2k"/>
<part name="SUPPLY5" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="GND" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U$1" gate="G$1" x="66.04" y="60.96"/>
<instance part="U$2" gate="G$1" x="66.04" y="30.48"/>
<instance part="U$3" gate="G$1" x="66.04" y="0"/>
<instance part="P+1" gate="1" x="58.42" y="68.58">
<attribute name="VALUE" x="55.88" y="63.5" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="SUPPLY1" gate="GND" x="55.88" y="-10.16">
<attribute name="VALUE" x="53.975" y="-13.335" size="1.778" layer="96"/>
</instance>
<instance part="U$4" gate="G$1" x="10.16" y="63.5"/>
<instance part="P+2" gate="1" x="15.24" y="73.66">
<attribute name="VALUE" x="12.7" y="68.58" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="SUPPLY2" gate="GND" x="15.24" y="45.72">
<attribute name="VALUE" x="13.335" y="42.545" size="1.778" layer="96"/>
</instance>
<instance part="R11" gate="G$1" x="48.26" y="53.34" rot="R90">
<attribute name="NAME" x="46.482" y="48.768" size="1.778" layer="95" rot="R90"/>
<attribute name="VALUE" x="51.689" y="48.768" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="R12" gate="G$1" x="48.26" y="43.18" rot="R90">
<attribute name="NAME" x="46.482" y="38.608" size="1.778" layer="95" rot="R90"/>
<attribute name="VALUE" x="51.689" y="38.608" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="SUPPLY3" gate="GND" x="48.26" y="35.56">
<attribute name="VALUE" x="46.355" y="32.385" size="1.778" layer="96"/>
</instance>
<instance part="R21" gate="G$1" x="48.26" y="22.86" rot="R90">
<attribute name="NAME" x="46.482" y="18.288" size="1.778" layer="95" rot="R90"/>
<attribute name="VALUE" x="51.689" y="18.288" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="R22" gate="G$1" x="48.26" y="12.7" rot="R90">
<attribute name="NAME" x="46.482" y="8.128" size="1.778" layer="95" rot="R90"/>
<attribute name="VALUE" x="51.689" y="8.128" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="SUPPLY4" gate="GND" x="48.26" y="5.08">
<attribute name="VALUE" x="46.355" y="1.905" size="1.778" layer="96"/>
</instance>
<instance part="R31" gate="G$1" x="48.26" y="-7.62" rot="R90">
<attribute name="NAME" x="46.482" y="-12.192" size="1.778" layer="95" rot="R90"/>
<attribute name="VALUE" x="51.689" y="-12.192" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="R32" gate="G$1" x="48.26" y="-17.78" rot="R90">
<attribute name="NAME" x="46.482" y="-22.352" size="1.778" layer="95" rot="R90"/>
<attribute name="VALUE" x="51.689" y="-22.352" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="SUPPLY5" gate="GND" x="48.26" y="-25.4">
<attribute name="VALUE" x="46.355" y="-28.575" size="1.778" layer="96"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="+5V" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="VCC"/>
<wire x1="60.96" y1="63.5" x2="58.42" y2="63.5" width="0.1524" layer="91"/>
<pinref part="P+1" gate="1" pin="+5V"/>
<wire x1="58.42" y1="63.5" x2="58.42" y2="66.04" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="VCC"/>
<wire x1="60.96" y1="33.02" x2="58.42" y2="33.02" width="0.1524" layer="91"/>
<wire x1="58.42" y1="33.02" x2="58.42" y2="63.5" width="0.1524" layer="91"/>
<junction x="58.42" y="63.5"/>
<pinref part="U$3" gate="G$1" pin="VCC"/>
<wire x1="60.96" y1="2.54" x2="58.42" y2="2.54" width="0.1524" layer="91"/>
<wire x1="58.42" y1="2.54" x2="58.42" y2="33.02" width="0.1524" layer="91"/>
<junction x="58.42" y="33.02"/>
</segment>
<segment>
<pinref part="U$4" gate="G$1" pin="P1"/>
<wire x1="12.7" y1="68.58" x2="15.24" y2="68.58" width="0.1524" layer="91"/>
<wire x1="15.24" y1="68.58" x2="15.24" y2="71.12" width="0.1524" layer="91"/>
<pinref part="P+2" gate="1" pin="+5V"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="GND"/>
<wire x1="60.96" y1="-5.08" x2="55.88" y2="-5.08" width="0.1524" layer="91"/>
<pinref part="SUPPLY1" gate="GND" pin="GND"/>
<wire x1="55.88" y1="-5.08" x2="55.88" y2="-7.62" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="GND"/>
<wire x1="60.96" y1="25.4" x2="55.88" y2="25.4" width="0.1524" layer="91"/>
<wire x1="55.88" y1="-5.08" x2="55.88" y2="25.4" width="0.1524" layer="91"/>
<junction x="55.88" y="-5.08"/>
<pinref part="U$1" gate="G$1" pin="GND"/>
<wire x1="60.96" y1="55.88" x2="55.88" y2="55.88" width="0.1524" layer="91"/>
<wire x1="55.88" y1="55.88" x2="55.88" y2="25.4" width="0.1524" layer="91"/>
<junction x="55.88" y="25.4"/>
</segment>
<segment>
<pinref part="U$4" gate="G$1" pin="P8"/>
<wire x1="12.7" y1="50.8" x2="15.24" y2="50.8" width="0.1524" layer="91"/>
<wire x1="15.24" y1="50.8" x2="15.24" y2="48.26" width="0.1524" layer="91"/>
<pinref part="SUPPLY2" gate="GND" pin="GND"/>
</segment>
<segment>
<pinref part="R12" gate="G$1" pin="P1"/>
<pinref part="SUPPLY3" gate="GND" pin="GND"/>
</segment>
<segment>
<pinref part="R22" gate="G$1" pin="P1"/>
<pinref part="SUPPLY4" gate="GND" pin="GND"/>
</segment>
<segment>
<pinref part="R32" gate="G$1" pin="P1"/>
<pinref part="SUPPLY5" gate="GND" pin="GND"/>
</segment>
</net>
<net name="TRG1" class="0">
<segment>
<pinref part="U$4" gate="G$1" pin="P2"/>
<wire x1="12.7" y1="66.04" x2="15.24" y2="66.04" width="0.1524" layer="91"/>
<label x="15.24" y="66.04" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="U$1" gate="G$1" pin="TRG"/>
<wire x1="60.96" y1="60.96" x2="53.34" y2="60.96" width="0.1524" layer="91"/>
<label x="53.34" y="60.96" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
</net>
<net name="ECHO1" class="0">
<segment>
<pinref part="U$4" gate="G$1" pin="P3"/>
<wire x1="12.7" y1="63.5" x2="15.24" y2="63.5" width="0.1524" layer="91"/>
<label x="15.24" y="63.5" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="R11" gate="G$1" pin="P1"/>
<pinref part="R12" gate="G$1" pin="P2"/>
<wire x1="48.26" y1="48.26" x2="45.72" y2="48.26" width="0.1524" layer="91"/>
<junction x="48.26" y="48.26"/>
<label x="45.72" y="48.26" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
</net>
<net name="TRG2" class="0">
<segment>
<pinref part="U$4" gate="G$1" pin="P4"/>
<wire x1="12.7" y1="60.96" x2="15.24" y2="60.96" width="0.1524" layer="91"/>
<label x="15.24" y="60.96" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="U$2" gate="G$1" pin="TRG"/>
<wire x1="60.96" y1="30.48" x2="53.34" y2="30.48" width="0.1524" layer="91"/>
<label x="53.34" y="30.48" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
</net>
<net name="ECHO2" class="0">
<segment>
<pinref part="U$4" gate="G$1" pin="P5"/>
<wire x1="12.7" y1="58.42" x2="15.24" y2="58.42" width="0.1524" layer="91"/>
<label x="15.24" y="58.42" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="R21" gate="G$1" pin="P1"/>
<pinref part="R22" gate="G$1" pin="P2"/>
<wire x1="48.26" y1="17.78" x2="45.72" y2="17.78" width="0.1524" layer="91"/>
<junction x="48.26" y="17.78"/>
<label x="45.72" y="17.78" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
</net>
<net name="TRG3" class="0">
<segment>
<pinref part="U$4" gate="G$1" pin="P6"/>
<wire x1="12.7" y1="55.88" x2="15.24" y2="55.88" width="0.1524" layer="91"/>
<label x="15.24" y="55.88" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="TRG"/>
<wire x1="60.96" y1="0" x2="53.34" y2="0" width="0.1524" layer="91"/>
<label x="53.34" y="0" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
</net>
<net name="ECHO3" class="0">
<segment>
<pinref part="U$4" gate="G$1" pin="P7"/>
<wire x1="12.7" y1="53.34" x2="15.24" y2="53.34" width="0.1524" layer="91"/>
<label x="15.24" y="53.34" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="R31" gate="G$1" pin="P1"/>
<pinref part="R32" gate="G$1" pin="P2"/>
<wire x1="48.26" y1="-12.7" x2="45.72" y2="-12.7" width="0.1524" layer="91"/>
<junction x="48.26" y="-12.7"/>
<label x="45.72" y="-12.7" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="R11" gate="G$1" pin="P2"/>
<pinref part="U$1" gate="G$1" pin="ECHO"/>
<wire x1="48.26" y1="58.42" x2="60.96" y2="58.42" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$1" class="0">
<segment>
<pinref part="R21" gate="G$1" pin="P2"/>
<pinref part="U$2" gate="G$1" pin="ECHO"/>
<wire x1="48.26" y1="27.94" x2="60.96" y2="27.94" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="ECHO"/>
<pinref part="R31" gate="G$1" pin="P2"/>
<wire x1="60.96" y1="-2.54" x2="48.26" y2="-2.54" width="0.1524" layer="91"/>
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