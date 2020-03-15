// udp.h
// author: tari

//--- Constant, define by user
static const char* addr_ip_remote = "192.168.0.56"; //IP address, remotes.
static const int port_udp_remote = 8888; // UDP port, remotes.
//---

#include <WiFi.h>

static WiFiUDP wifiUdp;

void init_udp(int port){
	wifiUdp.begin(port);
  Serial.println("UDP Started.");
}

void send_udp(char content_send){
	wifiUdp.beginPacket(addr_ip_remote, port_udp_remote);
	wifiUdp.write(content_send);
	wifiUdp.endPacket();
}
