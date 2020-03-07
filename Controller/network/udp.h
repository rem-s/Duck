// udp.h
// author: tari

//--- Constant, define by user
static const char* addr_ip_remote = "***.***.***.**"; //IP address, remotes.
static const int port_udp_remote = 0000; // UDP port, remotes.
//---

void init_udp(int port){
	wifiUdp.begin(port);
}

void send_udp(char content_send){
	wifiUdp.beginPacket(addr_ip_remote, port_udp_remote);
	wifiUdp.write(content_send);
	wifiUdp.endPacket();
}
