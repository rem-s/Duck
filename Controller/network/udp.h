// udp.h
// author: tari

/* usage:
 * init_udp(int port, char* addr)
 *   port: port number, remote hosts.
 *   addr: IP address, remote hosts.
 * send_udp(content_send)
 *   content_send: a character you want to send to the remote host.
 */

#include <WiFi.h>

extern void disp_string(char*);

static int port_udp_remote = 0; // UDP port, remotes.
static char* addr_ip_remote = "0.0.0.0"; //IP address, remotes.

static WiFiUDP wifiUdp;

void init_udp(int port, char* addr) {
char str[50];
  Serial.println("I will initialize service UDP.");
  port_udp_remote = port;
  addr_ip_remote = addr;
  wifiUdp.begin(port_udp_remote);
    disp_string("Remote IP address: ");
    sprintf(str,"%d",addr_ip_remote);
    disp_string(str);
    disp_string("UDP port: ");
    sprintf(str,"%d",port_udp_remote);
    disp_string(str);
  Serial.println("Service UDP started.");
}

void send_udp(int content_send) {
  Serial.println("I will send a character to the client, it is");
  Serial.println("----------");
  Serial.println(content_send);
  Serial.println("----------");
  wifiUdp.beginPacket(addr_ip_remote, port_udp_remote);
  wifiUdp.write(content_send);
  wifiUdp.endPacket();
  Serial.println("I sent that.");
}
